import streamlit as st
import joblib

# Load the trained model
model = joblib.load("esl_vocab_model.pkl")

# Feature functions
def count_vowels(word):
    vowels = "aeiou"
    return sum(1 for letter in word.lower() if letter in vowels)

def count_syllables(word):
    import re
    groups = re.findall(r'[aeiouy]+', word.lower())
    return max(1, len(groups))

st.title("ESL Vocabulary Difficulty Predictor")
st.write("Enter a word to predict its difficulty level for ESL learners.")

word_input = st.text_input("Enter a word:")

if st.button("Predict"):
    if word_input:
        word_length = len(word_input)
        vowel_count = count_vowels(word_input)
        syllable_count = count_syllables(word_input)

        features = [[word_length, vowel_count, syllable_count]]
        prediction = model.predict(features)[0]

        st.success(f"Predicted difficulty: {prediction}")
    else:
        st.warning("Please enter a word!")