# Import the required libraries classes and pages
import streamlit as st
from Classes.bank import Bank
from pages.login import login_page
from pages.dashboard import dashboard_page
from pages.register import register_page
from pages.deposit import deposit_page
from pages.transfer import transfer_page
from pages.withdraw import withdraw_page
from pages.logout import show_logout

def main():
   # st.set_page_config(page_title="Banking App", layout="wide")
    
    # Initialise session states if they don't exist
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
        st.session_state["customer_id"] = None
        st.session_state["current_page"] = "Login"  # Default the app to display login page

    # Create a shared bank object instance details
    bank = Bank(
    bank_name=" Osama Bank App",
    contact=" 10593097@bradfordcollege.ac.uk",
    address=" 123 Great Horton Road, Bradford City"
    )

# create Sidebar Navigation function
    def navigate():
        """
        function uses a radio button to handle page switching and maintains the selected page in st.session_state
        Returns:
        Update the the session of selected page from the list 

        """
        st.sidebar.title("Navigation")
        pages = ["Login", "Register", "Dashboard", "Transfer","Deposit", "Withdraw", "Logout"]
        selected_page = st.sidebar.radio("Go to", pages, index=pages.index(st.session_state["current_page"]))
        st.session_state["current_page"] = selected_page  # Update current page seasion
        return selected_page

    # Main Bank App Logic
    page = navigate() # Assign navigate function 
    # If any page is selected, direct to its page
    if page == "Login": 
        login_page(bank) # redirect to login page
    elif page == "Register":
        register_page(bank) # redirect to register page
    elif page == "Dashboard":
        dashboard_page(bank) # # redirect to dashboard page
    elif page == "Transfer" :
        transfer_page(bank) # redirect to transfer page
    elif page == "Deposit":
        deposit_page(bank) # redirect to deposit page
    elif page == "Withdraw":
        withdraw_page(bank) # redirect to withdraw page
    elif page == "Logout":
        show_logout(bank) # redirect to logout page
        
# Call main page as an entry point to the app
if __name__ == "__main__":
    main()

    