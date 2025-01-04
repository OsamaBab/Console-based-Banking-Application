# Import Required files
import streamlit as st
from Classes.bank import Bank

def deposit_page(bank: Bank):
    """
    Display the deposit page for the customer to deposit money into a selected account.
        Args:
        bank (Bank): The bank instance managing all customers and accounts.   
    """
    # Call functionn to display bank info
    bank.show_bank_info() 
    # Set authenticated sesion to False for non-logged in customers
    if not st.session_state.get("authenticated", False):
            # Print a title
            st.title("Deposit Page") 
            # Display a warrning message
            st.warning("Log in please to access the deposit page.")
            # Redirect to the Login Page
            st.session_state["current_page"] = "Login"  
            # Return nothing 
            return
    # Display a title
    st.title("Deposit Page") 
    # Fetch the logged-in customer's detils
    customer = bank.customers.get(st.session_state["customer_id"])
    # Select the account to deposit into
    account_types = [account.account_type for account in customer.accounts]
    selected_acc_type = st.selectbox("Select Account to deposit", account_types)
    # Get user inputs using try and exception to handle any invalid input
    try:
        # Get amount to be deposited
        amount = st.number_input("Amount to Deposit", min_value=1.0, step=0.1)       
        # Raise an error message with the error details if the user input failed
    except ValueError:
                    st.error("Sorry! Invalid input error.")
    # create a deposit button to handle the process
    deposit_btn = st.button("Submit")
    if deposit_btn:
        #check if the customer logged in then process
        #customer = next(c for c in bank.customers.values() if c.cust_id == st.session_state["customer_id"])
        # Find the selected account and deposit the amount
        for account in customer.accounts:
            if account.account_type == selected_acc_type:
                try:
                    # Call the function to perform deposit process using try and exception to handle any invalid process
                    account.deposit(amount)
                    # Call the function to save updated data in json file
                    bank.save_customers()
                    st.success(f"£{amount:.2f} deposited successfully!") # display success deposit message
                    # Switsh to the dashboard page to prevent multiple deposits on a single process
                    st.session_state["current_page"] = "Dashboard"
                # Raise an error message with the error details if the user input failed
                except ValueError:
                    st.error("Sorry! Invalid input error.")
            
                
    