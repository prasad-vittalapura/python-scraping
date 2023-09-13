# Import the required modules
from selenium import webdriver
from browsermobproxy import Server
from FilterJson import *
import time
import json

from selenium.webdriver.chrome.service import Service

# Main Function
if __name__ == "__main__":

    # Enter the path of bin folder by
    # extracting browsermob-proxy-2.1.4-bin
    apis=["/content","/mppcore/fetchMerchantSpecificInfo"]
    path_to_browsermobproxy = ""

    # Start the server with the path and port 8090
    server = Server(path_to_browsermobproxy
                    + "browsermob-proxy", options={'port': 8091})
    server.start()

    # Create the proxy with following parameter as true
    proxy = server.create_proxy(params={"trustAllServers": "true"})

    # Create the webdriver object and pass the arguments
    options = webdriver.ChromeOptions()

    # Chrome will start in Headless mode
    # options.add_argument('headless')

    # Ignores any certificate errors if there is any
    options.add_argument("--ignore-certificate-errors")

    # Setting up Proxy for chrome
    options.add_argument("--proxy-server={0}".format(proxy.proxy))

    # Startup the chrome webdriver with executable path and
    # the chrome options as parameters.
    service = Service(executable_path='')
    driver = webdriver.Chrome(options, service
                              )

    # Create a new HAR file of the following domain
    # using the proxy.
    proxy.new_har("",options={'captureContent': True})
    driver.get("")
    state=True
    while state:
        if driver.window_handles:
            pass
        else:
            network_logs = proxy.har['log']['entries']
            logData=[]
            for log in network_logs:
                request= log['request']
                api_data={}
                api_data["method"]=request['method'];
                if "postData" in request:
                    api_data["postData"]=request["postData"]
                matches = [string for string in apis if string in request['url']]
                if matches:
                    api_data["url"]=request['url']
                    logData.append(api_data)

            with open("network_request.json", "w", encoding="utf-8") as f:
                f.write(json.dumps(logData))
            state=False
            traverse_json(logData)



