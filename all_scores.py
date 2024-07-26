import streamlit as st
import pandas as pd

def main():
    st.title("📊 All Saved ESG Scores")

    # Check if there are saved scores
    if 'saved_scores' in st.session_state and st.session_state['saved_scores']:
        saved_scores = st.session_state['saved_scores']

        # Convert saved scores to a DataFrame
        df = pd.DataFrame(saved_scores)

        # Display the bar chart
        st.bar_chart(df.set_index('company'))

        # Display the saved scores in a table
        st.write("### Saved ESG Scores")
        st.table(df)
    else:
        st.write("No ESG scores saved yet.")

if __name__ == "__main__":
    main()
