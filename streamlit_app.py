import streamlit as st
import boto3
import os
from dotenv import load_dotenv
import json

st.title("♻️ ESG scorer application")


load_dotenv()

# Initialize a session using Amazon Bedrock
session = boto3.Session(
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY_ID"),
    region_name='us-east-1'
)

bedrock_client = session.client('bedrock-runtime')

st.write(bedrock_client)

with open('Nomura_stocks.json', 'r') as file:
    stock_data = json.load(file)

options = [f"{symbol}: {name}" for symbol, name in stock_data.items()]

selection = st.selectbox(
    "Select an option: ",
    options,
    placeholder="Select an option:",
    index=None
)

# Display selected option
st.write(f"You selected: {selection}")

total_esg_score = 77.121
environment_risk_score = 20.321
governance_risk_score = 25.678
social_risk_score = 31.122

st.write(f"ESG scores for {selection}")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total ESG Risk Score", total_esg_score)

with col2:
    st.metric("Environment Risk Score", environment_risk_score)

with col3:
    st.metric("Governance Risk Score", governance_risk_score)

with col4:
    st.metric("Social Risk Score", social_risk_score)
st.write("\n")
st.title("📰 Upload article")
article_url = st.text_input("Enter article URL:")
