# Import required files
from Classes.account import Account
from Classes.customer import Customer
from Classes.bank import Bank
#from st_pages import login
import streamlit as st

def register_page(bank: Bank):
    """
    Display the registration page for new users to create an account.
    Args:
        bank (Bank): The bank instance managing all customers and accounts.
    Returns:
        None
    """
    # Call the function to print bank info
    bank.show_bank_info() 
    # Print the title
    st.title("Sign Up Page") # Display Page title
    # Get a user inputs and select account type from a list
    account_type = st.selectbox("Account Type", ("Current", "Saving", "Mortgage", "Business"))
    # Input the deposit amount with minimum £1 deposit using try and exception to handle any invalid input
    try:
        # Get user inputs (name, password and emai)
        cust_name = st.text_input("Name") 
        password = st.text_input("Password",type="password") 
        email = st.text_input("Email")       
    # Raise an error message with the error details if the user inputs failed
    except ValueError:
                    st.error("Sorry! Invalid inputs error.") 
    # create a register button
    register_btn = st.button("Register")
    # when clicked on, check name, passowrd and email in customer dictionary
    if register_btn: 
        if cust_name and password and email and account_type :
            # Check if the customer is already registered 
            exist_customer = None
            for customer in bank.customers.values():
                if customer.cust_name == cust_name and customer.email == email:
                    exist_customer = customer
                    break
            if exist_customer:
                # Check if the entered account type already exists for this customer
                if any(account.account_type == account_type for account in exist_customer.accounts):
                    # Raise an error message 
                    st.error(f"This '{account_type}' account typea lready exists for this customer.")
                else:
                    # Add a new account type of the selected bank type
                    new_account = Account(cust_id = exist_customer.cust_id, account_type=account_type)
                    # Add account details
                    exist_customer.accounts.append(new_account)
                    # Call the function to save the new account to the json file
                    bank.save_customers()
                    st.success(f"The new '{account_type}' account added successfully for {cust_name}.")
                    # Redirect registered customers to login page
                    st.session_state["current_page"] = "Login"  
            else:  # Register a new customer with selected account type             
                # Generate a unique customer ID that to be added to the register information
                cust_id = bank.generate_customer_id()
                # Create a new account with the selected account type
                new_account = Account(cust_id=cust_id, account_type=account_type)
                new_customer = Customer(cust_id, cust_name, password, email, [new_account])
                # Add the new customer to the bank dic and save it
                bank.customers[cust_id] = new_customer
                # Call the function to save the new account to the json file
                bank.save_customers()
                # Print successeful message with name
                st.success(f"The new ccount is created successfully for {cust_name}.") 
                # display baloons as a sign of successful registration
                st.balloons() 
                # Redirect the registered customer to login
                st.session_state["current_page"] = "Login"  
        else:
            # Print an error message
            st.error("Please fill in all fields.") 
