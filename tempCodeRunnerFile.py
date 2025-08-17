import streamlit as st
import yfinance as yf

st.title("Test Streamlit & yfinance")
data = yf.download("AAPL", period="1mo")
st.write(data)