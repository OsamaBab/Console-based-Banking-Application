# Import required files
import streamlit as st
from Classes.bank import Bank
from st_pages.login import login_page
from st_pages.dashboard import dashboard_page
from st_pages.register import register_page
from st_pages.deposit import deposit_page
from st_pages.transfer import transfer_page
from st_pages.withdraw import withdraw_page
from st_pages.logout import show_logout

def main():
    """
    The main interface method to enable users to navigate between different pages
    """
    # Initialise session states to control on displaying pages based on each session
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
        st.session_state["customer_id"] = None
        st.session_state["current_page"] = "Login"  # Default to login page
    # Create a bank instance with details
    bank = Bank(
    bank_name=" Osama Bank App",
    contact=" osamabank.ac.uk",
    address=" 123 Great Horton Road, Bradford City"
    )
    
    # create Sidebar Navigation function
    def navigate():
        """
        function uses a radio button to handle page switching and maintains the selected page in st.session_state
        Returns:
        Update the the session of selected page from the list 
        """
        # Print sidbar title
        st.sidebar.title("Navigation")
        # Print sidbar pages names
        pages = ["Login", "Register", "Dashboard", "Transfer","Deposit", "Withdraw","Logout"]
        # List all pages names 
        selected_page = st.sidebar.radio("Go to", pages, index=pages.index(st.session_state["current_page"]))
        # Update current the page seasion
        st.session_state["current_page"] = selected_page  
        # Retrive the selcted page from the pages list
        return selected_page

    # Main Bank App Logic
    page = navigate()
    if page == "Login":
        # Print login page
        login_page(bank)
    elif page == "Register":
        # Print register page
        register_page(bank)
    elif page == "Dashboard":
        # Print dashboard page
        dashboard_page(bank)
    elif page == "Transfer" :
        # Print transfer page
        transfer_page(bank)
    elif page == "Deposit":
        # Print deposit page
        deposit_page(bank)
    elif page == "Withdraw":
        # Print withdraw page
        withdraw_page(bank)
    elif page == "Logout":
        # Print logout page
        show_logout(bank)      
# Run the main method
if __name__ == "__main__":
    main()
