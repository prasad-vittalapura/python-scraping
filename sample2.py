import spacy
import en_core_web_sm

# Sample data for training
if __name__ == "__main__":

    nlp = en_core_web_sm.load()
    training_data = [
        ("price", "static"),
        ("Name", "dynamic"),
        ("cost", "static"),
        ("details", "dynamic"),
    ]


    def word_similarity(word1, word2):
        return nlp(word1).similarity(nlp(word2))


    def predict_category(input_text):
        static_category = "static"
        dynamic_category = "dynamic"
        threshold = 0.5  # You can adjust the threshold as needed

        # Calculate similarity with known keywords
        similarities = {
            static_category: sum(
                word_similarity(input_text, keyword) for keyword, _ in training_data if keyword in input_text),
            dynamic_category: sum(
                word_similarity(input_text, keyword) for keyword, _ in training_data if keyword not in input_text)
        }

        # Determine the category based on similarity
        if similarities[static_category] > similarities[dynamic_category]:
            return static_category
        else:
            return dynamic_category

    # Example usage:
    while True:
        test=input("enter")
        input_text = test
        category = predict_category(input_text)
        print(f"The category of input '{input_text}' is: {category}")