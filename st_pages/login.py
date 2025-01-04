#Import required files
import streamlit as st
from Classes.bank import Bank

def login_page(bank: Bank):
    """
    This function represents the login page to get users' inputs and handle the login perocess
    Args:
        bank (Bank): The bank instance managing all customers and accounts.  
    """
    # Call functionn to display bank info
    bank.show_bank_info() 
    # Set authenticated sesion to False for non-logged in customers
    if st.session_state.get("authenticated", False):
        # Print title
        st.title("Login Page")
        # Print a propriate Warrning message for logged in users if clicked on login page
        st.warning(f"You are already logged in as {st.session_state['customer_id']}.")
        # return nothing and stop here
        return  
    # Print title
    st.title("Login Page")
    # Get user inputs using try and exception to handle any invalid input
    try:
        # Get user accont number 
        account_number = st.text_input("Input Account Number")
        # Get user password
        password = st.text_input("Password",type="password")     
        # Raise an error message with the error details if the user input failed
    except ValueError:
                    st.error("Sorry! Invalid input error.")
    # Create login button
    login_button = st.button("Login")
    # Hadle actions when the button is clicked
    if login_button:
        # Validate user login inputs
        if account_number and password:
            # Check a customer account number and match within the customer accounts dictionary
            for customer in bank.customers.values():
                if ( any(acc.account_number == account_number for acc in customer.accounts)):
                    # Validate user input password
                    if customer.password == password:
                        # Successful login and set session state
                        st.session_state["authenticated"] = True
                        st.session_state["customer_id"] = customer.cust_id
                        # Print welcome message with customer name
                        st.success(f"Welcome, {customer.cust_name}!")
                        # Redirect the user to the dashboard page
                        st.session_state["current_page"] = "Dashboard"
                        return
                    else:
                        # Print an error message if Password is mismatch
                        st.error("Sorry! Invalid input password.")
                        return
            # Print an error message If no customer matched is found
            st.error("Sorry! This accoun is not exsisted. Try another one")
        else:
            # print an error message for missing input fields
            st.error("Fill in all required fields please.")