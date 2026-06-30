import streamlit as st
import tiktoken

# Load tokenizer
encoding = tiktoken.get_encoding("cl100k_base")

# App Title
st.title("🔤 Text to Token Converter")
st.write("Enter text below to convert it into OpenAI tokens using the `cl100k_base` tokenizer.")

# Text input
text = st.text_area("Enter your text:", height=200)

# Convert button
if st.button("Convert to Tokens"):
    if text.strip():
        # Convert text to tokens
        token_ids = encoding.encode(text)

        # Display results
        st.subheader("Token IDs")
        st.write(token_ids)

        st.subheader("Number of Tokens")
        st.success(len(token_ids))
    else:
        st.warning("Please enter some text.")