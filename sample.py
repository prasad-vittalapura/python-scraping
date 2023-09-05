from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import difflib

# Sample data for training
if __name__ == "__main__":

    categories = {
        "price": ["price", "amount", "amt", "amount1"],
        "token": ["token",
                  "dbuyToken",
                  "transcToken",
                  "SyfToken"],
    }


    def auto_validate_input(input_text, categories):
        for category, category_tokens in categories.items():
            for token in category_tokens:
                if (
                        difflib.SequenceMatcher(None, input_text, token).ratio()
                        >= 0.7  # Adjust the similarity threshold as needed
                ):
                    return category
        return None  # Return None if no category is found


    # Example usage:
    while True:
        test = input("enter")
        input_text = test
        category = auto_validate_input(input_text, categories)
        if category is not None:
            print(f"'{input_text}' is a valid {category}.")
        else:
            print(f"'{input_text}' is not valid for any category.")
