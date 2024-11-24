# Import the required libraries classes and pages
import streamlit as st
from Classes.bank import Bank

def main():
   # st.set_page_config(page_title="Banking App", layout="wide")
    
    # Initialise session states if they don't exist
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
        st.session_state["customer_id"] = None
        st.session_state["current_page"] = "Login"  # Default the app to display login page

    # Create a shared bank object instance details
    bank = Bank(
    bank_name=" Osama Bank App",
    contact=" 10593097@bradfordcollege.ac.uk",
    address=" 123 Great Horton Road, Bradford City"
    )

    