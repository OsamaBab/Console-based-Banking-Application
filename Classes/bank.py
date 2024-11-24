# Import required libraries and files
import streamlit as st

class Bank:
    """
    Discription:
    Represents the overall banking system, managing customers, accounts, 
    and the persistence of data.
        Attributes:
            bank_name (str): Name of the bank.
            phone (int): Bank phone number.
            address (str): the address of the bank
    """
    def __init__(myself, bank_name, phone, address):

        """
        Initialise a Bank instance.  
        """
        myself.bank_name = bank_name
        myself.phone = phone
        myself.address = address

    def show_bank_info(self):
        """
        Functon to show the bank information using the bank class object parameters
            Reurns:
            bank information as strings in sidebar using Streamlit
        """
        st.sidebar.markdown("Bradford College" ) 
        st.sidebar.text(f"Bank Name: {self.bank_name}")
        st.sidebar.text(f"Email: {self.contact}")
        st.sidebar.text(f"Address: {self.address}")