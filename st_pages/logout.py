# Import required files
import streamlit as st
from Classes.bank import Bank

def show_logout(bank: Bank):
    """
    Discription:
    The Bank object is passed to page function to display the bank information in the sidebar.
    """
    # Call functionn to display bank info
    bank.show_bank_info() 
    # Set authenticated sesion to False for non-logged in customers
    if not st.session_state.get("authenticated", False):
            # Print a title
            st.title("Logout Page") 
            # Display a warrning message
            st.warning("Sorry! You are not logged in to log out. login first please.")
            # Redirect to the Login Page
            st.session_state["current_page"] = "Login"  
            # Return nothing 
            return
    # Print title
    st.title("Log Out")
    # Get the customer id sesion and match it with the logged in customers
    customer = bank.customers.get(st.session_state["customer_id"])
    if not customer:
        # Print an error message
        st.error("You need to log in first.")
        # Return nothing
        return
    # Create authenticated logout button
    confirme_logout = st.checkbox("Confirm Logout")
    # Perform logout process
    if confirme_logout:
        # Create logout button
        if st.button("Log Out"):
            # Reset and clear all session states
            st.session_state["authenticated"] = False
            st.session_state["customer_id"] = None
            # Redirect to login page
            st.session_state["current_page"] = "Login"
            # Print a success message
            st.success("You have been logged out. Redirecting to Login page...")


