import streamlit as st
import requests
import json
import pandas as pd
from dotenv import load_dotenv

# Initialize session state
if 'saved_scores' not in st.session_state:
    st.session_state['saved_scores'] = []

# Function to save current ESG scores
def save_current_scores(selection, esg_scores):
    print("Saving...")
    st.session_state['saved_scores'].append({
        "company": selection,
        "final_esg_risk": esg_scores.get("final_esg_risk", 0),
        "environmental_risk": esg_scores.get("environmental_risk", 0),
        "governance_risk": esg_scores.get("governance_risk", 0),
        "social_risk": esg_scores.get("social_risk", 0)
    })
    print(st.session_state['saved_scores'])

def main():
    st.title("♻️ ESG Scorer Application")

    load_dotenv()

    with open('Nomura_stocks.json', 'r') as file:
        stock_data = json.load(file)

    options = [f"{symbol} {name}" for symbol, name in stock_data.items()]

    selection = st.selectbox(
        "Select an option: ",
        options,
        placeholder="Select an option:",
        index=None
    )

    # Add a button to fetch ESG scores
    if st.button("Get ESG Scores", disabled=not selection):
        # Extract the stock symbol and name

        # Make the request to the Flask API
        response = requests.post(f"http://127.0.0.1:5000/api/esg?stock={selection}")

        if response.status_code == 200:
            data = response.json()
            esg_scores = data.get("esg_scores", {})

            total_esg_risk = esg_scores.get("final_esg_risk", 0)
            environment_risk_score = esg_scores.get("environmental_risk", 0)
            governance_risk_score = esg_scores.get("governance_risk", 0)
            social_risk_score = esg_scores.get("social_risk", 0)

            st.write(f"ESG scores for {selection}")

            # Display the scores in bar graphs using Streamlit's st.bar_chart
            scores = {
                'Risk Type': ['Total ESG Risk', 'Environment Risk', 'Governance Risk', 'Social Risk'],
                'Score': [total_esg_risk, environment_risk_score, governance_risk_score, social_risk_score]
            }

            df = pd.DataFrame(scores)
            st.bar_chart(df.set_index('Risk Type'))

            # Button to save the current ESG scores
            if st.button("Save data"):
                save_current_scores(selection, esg_scores)
                st.success("Data saved successfully!")

            # Display the sources
            st.write("### Sources used for ESG scores:")
            sources = data.get("sources", [])
            for source in sources:
                st.write(f"- [{source}]({source})")
        else:
            st.error("Failed to fetch ESG scores. Please try again later.")

    # Display selected option
    st.write(f"You selected: {selection}")


if __name__ == "__main__":
    main()
