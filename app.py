import streamlit as st
import pandas as pd
import pandasai as pai
from pandasai import SmartDataframe

# Load API key from secrets.toml
pai.api_key.set(st.secrets["PANDASAI_API_KEY"])

# Streamlit UI
st.title("📊 PandasAI CSV Query App")
st.write("ℹ️ This app allows you to upload a CSV file and ask questions about the data. It expects a text input and provides text-based responses.")

# File uploader
uploaded_file = st.file_uploader("📂 Upload a CSV file", type=["csv"])

df = None
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)  # Read the uploaded file into a DataFrame
    st.write("### 🔍 Preview of Uploaded Data")
    st.dataframe(df.head())  # Display first few rows
    sdf = pai.DataFrame(df)

    # User input for querying
    user_query = st.text_input("💬 Ask a question based on the data:")
    
    if st.button("🤖 Ask AI"):
        if user_query:
            response = sdf.chat(user_query)  # Get response from PandasAI
            st.write("### 🤖 Response:")
            st.write(response)
