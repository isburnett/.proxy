import streamlit as st
import requests

# Your original app content (KEEP THIS)
st.title("WaterMath Streamlit App")

st.header("Main Features")
st.write("Your original app content goes here...")

# Add a divider to separate your main app from the proxy feature
st.markdown("---") 

# Proxy API section (NEW)
st.subheader("API Proxy")

target_url = st.text_input("Enter the URL to fetch data from:")

if st.button("Fetch Data"):
    if target_url:
        try:
            response = requests.get(target_url)
            st.json(response.json())  # Display response as JSON
        except Exception as e:
            st.error(f"Error fetching data: {e}")
