import streamlit as st
import app
import all_scores

# Dictionary to map pages
PAGES = {
    "Main Page": app,
    "All Saved ESG Scores": all_scores
}

# Set the default page
if 'page' not in st.session_state:
    st.session_state['page'] = 'Main Page'

# Sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Set the page based on selection
st.session_state['page'] = selection

# Load the selected page
page = PAGES[selection]
page.main()
