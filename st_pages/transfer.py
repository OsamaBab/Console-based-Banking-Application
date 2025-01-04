# Import required files
import streamlit as st
from Classes.bank import Bank

def transfer_page(bank):

    """
    Display the transfer page for logged-in customers.

        Args:
            bank (Bank): The bank instance managing customers and accounts.

            Returns:  None
    """
   # Call functionn to display bank info
    bank.show_bank_info() 
    # Set authenticated sesion to False for non-logged in customers
    if not st.session_state.get("authenticated", False):
            # Print a title
            st.title("Transfer Page") 
            # Display a warrning message
            st.warning("Log in please to access the Transfer page.")
            # Redirect to the Login Page
            st.session_state["current_page"] = "Login"  
            # Return nothing 
            return
    # Print a title
    st.title("Transfer Page") 
    # Fetch the logged-in customer's detils
    customer = bank.customers.get(st.session_state["customer_id"])
    # Allow the user to select the source account to send from
    source_account_index = st.selectbox(
        "Select Source Account",
        range(len(customer.accounts)),
        format_func=lambda i: f"{customer.accounts[i].account_number} ({customer.accounts[i].account_type} - £{customer.accounts[i].balance:.2f})",
    )
    # Retrieve the sender acount by index
    source_account = customer.accounts[source_account_index]  
    # Get user inputs using try and exception to handle any invalid input
    try:
        # get recipent account number
        recipient_account_number = st.text_input("Recipient Account Number")
        # Get the amount to be transfered
        amount = st.number_input("Amount to Transfer", min_value=0.01, step=0.01)              
        # Raise an error message with the error details if the user input failed
    except ValueError:
                    st.error("Sorry! Invalid user input.")
                    
    # Transfer button with conditions
    if st.button("Transfer"):
        # Get the recipient customer from the bank customer dictionart by calling the function
        recipient_customer = bank.find_customer_by_account_number(recipient_account_number)
        if recipient_customer:
            # Check if the input recipent account number matches exsisted account or return nothing if not exsisted
            recipient_account = next(
                (acc for acc in recipient_customer.accounts if acc.account_number == recipient_account_number),
                None
            )
            if recipient_account:
                try:
                    # Call the function to perform the transfer process
                    source_account.transfer(amount, recipient_account)
                    # Call the function to save updated data in json file
                    bank.save_customers()  
                    st.success(f"£{amount:.2f} transferred successfully to account {recipient_account_number}!")
                    # Switsh to the dashboard page to prevent multiple transfers in a single process
                    st.session_state["current_page"] = "Dashboard"  
                except ValueError as e:
                    # Raise an error message with the error details if the transfer process failed
                    st.error(f"Soory! Transfer is failed: {str(e)}")
            else:
                # Raise an error message if the reciver account dose not match
                st.error("Sorry! This recipient account is NOT found.")
        else:
            # Raise an error message if the reciver is not a customer
            st.error("Sorry! This recipient customer is NOT found.")