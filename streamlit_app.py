import streamlit as st
from transformers import pipeline

# Load sentiment analysis model
sentiment_analysis = pipeline("sentiment-analysis")

def main():
    st.title("AI Co-Pilot: Sentiment Analysis")

    # Input text box for user input
    text = st.text_area("Enter text for sentiment analysis:", "")

    if st.button("Analyze"):
        # Perform sentiment analysis
        result = sentiment_analysis(text)
        
        # Display results
        st.write(f"Text: {text}")
        st.write(f"Sentiment: {result[0]['label']}")
        st.write(f"Confidence: {result[0]['score']}")

if __name__ == "__main__":
    main()
