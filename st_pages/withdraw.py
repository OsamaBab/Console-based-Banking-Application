# Import required files
import streamlit as st
from Classes.bank import Bank

def withdraw_page(bank: Bank):
    # Call functionn to display bank info
    bank.show_bank_info() 
    # Set authenticated sesion to False for non-logged in customers
    if not st.session_state.get("authenticated", False):
            # Print a title
            st.title("Withdrawal Page") 
            # Display a warrning message
            st.warning("Log in please to access the Withdraw page.")
            # Redirect to the Login Page
            st.session_state["current_page"] = "Login"  
            # Return nothing 
            return
    # Print a title
    st.title("Withdraw Page") # Display Withdraw Page as a title
    # Fetch the logged-in customer's detils
    customer = bank.customers.get(st.session_state["customer_id"])
    # Select the account to deposit into
    account_types = [account.account_type for account in customer.accounts]
    selected_acc_type = st.selectbox("Select the account to withdraw from", account_types)
    # Get user inputs using try and exception to handle any invalid input
    try:
        # Get amount to be deposited
        amount = st.number_input("Amount to Deposit", min_value=1.0, step=0.1)       
    except ValueError:
                    # Raise an error message with the error details if the user input failed
                    st.error("Sorry! Invalid input error.")
    # create a register button
    withdraw_btn = st.button("Withdraw") 
    # when clicked on, check customer id exsistance and account type in customer dic
    if withdraw_btn: 
        # Fetch the logged-in customer's detils
        customer = next(c for c in bank.customers.values() if c.cust_id == st.session_state["customer_id"])
        # Find the selected account to deposit the amount
        for account in customer.accounts:
            if account.account_type == selected_acc_type:
                try:
                    # Perform withdrawal process using try and exception to handle any invalid process
                    account.withdraw(amount)
                    # Call the function to save updated data in json file
                    bank.save_customers()
                    # Print success message with withdrawed amount
                    st.success(f"£{amount:.2f} withdrawn successfully!")
                    # Switsh to the dashboard page to prevent multiple withdrawals in a single process
                    st.session_state["current_page"] = "Dashboard"
                # Raise an error message with the error details if the sender fund is insufficient
                except ValueError:
                    st.error("Sorry! Insufficient funds.")
        

    