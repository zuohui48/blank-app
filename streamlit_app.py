import streamlit as st
import boto3
import os
from dotenv import load_dotenv
import json

st.title("Aquila BEESGA 😎😎😎🦅🦅")

load_dotenv()

# Initialize a session using Amazon Bedrock
session = boto3.Session(
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY_ID"),
    region_name='us-east-1'
)

bedrock_client = session.client('bedrock-runtime')

#st.write(bedrock_client)

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


def llm_invoke(body_dict):
    # Convert the dictionary to a JSON string
    body_json = json.dumps(body_dict)

    # Define the kwargs with the formatted body
    kwargs = {
        "modelId": "meta.llama3-70b-instruct-v1:0",
        "contentType": "application/json",
        "accept": "application/json",
        "body": body_json
    }
    return bedrock_client.invoke_model(**kwargs)

def get_llm_output(symbol):
  # llama_init()
  # prompt "generate score for symbol"
  # json output


  pass



def upload_article(article):
  #upload to s3
  pass
