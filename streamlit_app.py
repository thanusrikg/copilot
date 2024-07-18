import streamlit as st
import requests

# Define the API endpoint URL
API_URL = 'https://jsonplaceholder.typicode.com/posts/1'

# Streamlit app
def main():
    st.title('Simple Streamlit App with API Integration')

    # Fetch data from API
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()

        # Display data
        st.write('Post ID:', data['id'])
        st.write('Title:', data['title'])
        st.write('Body:', data['body'])
    else:
        st.write('Error fetching data from API.')

if __name__ == '__main__':
    main()
