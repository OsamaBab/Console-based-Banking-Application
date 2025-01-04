# Import the required files and classes
import streamlit as st
from Classes.bank import Bank

def dashboard_page(bank: Bank):
    """
    This Function handles setting apropriate sesions and represents the dashboard page item 
    such as customer name, accounts list with balances and transactions histories. 
    Args:
        bank (Bank): The bank instance managing all customers and accounts.  
    """
    # Call functionn to display bank info
    bank.show_bank_info() 
    # Set authenticated sesion to False for non-logged in customers
    if not st.session_state.get("authenticated", False):
            # Print a title
            st.title("Dashboard Page") 
            # Display a warrning message
            st.warning("Log in please to access the dashboard.")
            # Redirect to the Login Page
            st.session_state["current_page"] = "Login"  
            # Return nothing 
            return
    # Display Dashboard Page as a title
    st.title("Dashboard")
    # Fetch the logged-in customer's detils
    customer = bank.customers.get(st.session_state["customer_id"])
    # Display welcome with user name message
    st.header(f"Welcome, {customer.cust_name}")
    
    st.subheader("Your Accounts List:")
    # Display accounts grouped by type using for loop # format the display
    for account_type in set(acc.account_type for acc in customer.accounts):
        st.write(f" {account_type.capitalize()} Account:")
        for acc in filter(lambda a: a.account_type == account_type, customer.accounts):
            st.write(
                f"- **Account Number**: {acc.account_number}, "
                f"**Available Balance**: £{acc.get_balance():.2f}"
            )
    # Allow user to select an account for displaying transaction history
    st.subheader("Your Transactions History")
    account_selection = st.selectbox(
        "Select an account to view transactions",
        customer.accounts,
        format_func=lambda acc: f"{acc.account_type.capitalize()} - {acc.account_number}",
    )
    # Show all transaction types history for each selected account if this accont had transactions
    if account_selection.transactions:
        st.write("Transactions History")
        for transaction in reversed(account_selection.transactions):  # Display the new transactions first
            st.write(
                f"**{transaction['time']}** - {transaction['type'].capitalize()}: £{transaction['amount']}"
            )
    else: 
        # Print a message if there is no transaction
        st.write("No transactions available at the moment for this account.")
    
   
        
    