# Import The required files and classes 
import json
import random
import os
import streamlit as st
from Classes.customer import Customer
from Classes.account import Account

class Bank:
    """
    Discription:
    Represents the overall banking system, managing customers, accounts, 
    and the persistence of data.
    """
    def __init__(self, bank_name, contact, address):
        """
        Initialize a Bank instance.

        Args:
            bank_name (str): Name of the bank.
            contact (str): Contact information for the bank.
            address (str): the address of the bank
        """
        self.bank_name = bank_name
        self.contact = contact
        self.address = address
        self.customers = {}
        self.load_customers()

    def show_bank_info(self):
        """
        Method to show the bank information using the bank class parameters
        Reurns:
        bank information as strings
        """
        # Print these info in the sidebar of the page   
        st.sidebar.markdown("Bradford College" )
        st.sidebar.text(f"Bank Name: {self.bank_name}")
        st.sidebar.text(f"Email: {self.contact}")
        st.sidebar.text(f"Address: {self.address}")

    def load_customers(self):
        """
        Load customer data from a JSON file.

            Returns:
                None
        """
        file_path = "data/customers.json"
        if os.path.exists(file_path):
            # Load the JSON file data and open it as read option
            with open("data/customers.json", "r") as file: 
                # Use try and except to handle any error 
                try:
                    data = json.load(file)
                    for cust_id, customer_info in data.items():
                        # Validate all essential fields
                        if "cust_id" in customer_info and "accounts" in customer_info:
                            # Parse all accounts into Account objects
                            accounts = [
                                Account(**acc) for acc in customer_info.get("accounts", [])
                            ]
                            # Create a new customer object
                            customer = Customer(
                                cust_id=customer_info["cust_id"],
                                cust_name=customer_info["cust_name"],
                                password=customer_info["password"],
                                email=customer_info["email"],
                                accounts=accounts
                            )
                            # Add the new object to customers dictionary
                            self.customers[customer_info["cust_id"]] = customer
                # Raise an error message withe the erorr details
                except json.JSONDecodeError as e:
                    print(f"Sorry! Error decoding json file: {e}")

    def save_customers(self):
        """
        Function to save customer data to a JSON file.
            Args:
                file_path (str): Path to the JSON file.
                customers (dict): Dictionary of customer objects.
        """
        # Defind the json file path using try and except error handller 
        file_path = "data/customers.json"
        try:
            # use with open to write the data
            with open(file_path, "w") as file:
                # Serialise customer objects into dictionaries
                json_data = {
                    cust_id: customer.to_dict()
                    for cust_id, customer in self.customers.items()
                }
                # Save the customer data to json file
                json.dump(json_data, file, indent=4)
        # Raise an error appropriate message and return the error details
        except Exception as e:
            print(f"Error saving in customers.json: {e}")

    def generate_customer_id(self):
        """
        Function to generate a unique customer id for a new registered customer.
        Returns:
            str: generated randomly  customer id start with CID.
        """
        # while loop to generate customer id if id is not exsist in customer dic
        while True:
            cust_id = f"CID{random.randint(1000, 9999)}"
            if cust_id not in self.customers:
                # Return the generated id value
                return cust_id
            
    def find_customer_by_account_number(self, account_number):
        """
        Function to find customers using their account number.
            parameters:
                account number = (str) account number to be passed to the function
            Returns: 
                    return the customer if the entered account is exsist
                    return non for customer values
        """
        # Filter the customer dictionary file and mathch the passed account number if it is exsisted.
        for customer in self.customers.values():
            for account in customer.accounts:
                if account.account_number == account_number:
                    # Return the customer who's holding this account
                    return customer
        # Return None if account number is not exsist
        return None
    
    

        

