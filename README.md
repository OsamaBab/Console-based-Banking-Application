## The Bank Management Application System
### Project Overview
This bank management system is built using Streamlit and Python programming Language. It enables non-registered users to register memberships accounts, log in to their accounts, and perform different fund transactions’ types such as deposits, withdrawals, and transfers fund across multiple account types. This bank system is designed with a focus on both security and simplicity aspects, ensuring a seamless administrators’ and customers’ experience.
### The System Features
1. #### Users Registration:
    Non-registered users can register their membership with unique customer ids and account types such as Current, Saving, Mortgage, or Business.
2. #### Customers Login:
    Secure login process using customers’ accounts numbers with their associated passwords.
3. #### Account Management:
    The bank customers are able to view their accounts, balances and all transaction histories.
4. #### Transactions:
    1. Customers can select accounts to deposit funds.
    2. Customers can withdraw funds if they have sufficient balances.
    3. Customers can transfer funds between the same accounts’ types while ensuring they have sufficient balances.
5. #### Customers Logout:
    Looged in customers can logout with confirmation of the logout process. 
6. #### Error Handling:
    The system includes comprehensive error messages for both invalid inputs and operations.
7. #### Data Persistence:
    All the bank customers’ data including their accounts and transactions data are loaded, saved and stored in a JSON file.
### The Project Structure
![image](https://github.com/user-attachments/assets/e7d2af1e-926b-4df7-8f18-1e660d01334d)
### Setup Instructions
1. Download the repository to your local machine using this link:  
 https://github.com/OsamaBab/Console-based-Banking-Application/archive/refs/heads/main.zip.  
2. Clone the repository remotely using this command line:   
  git clone https://github.com/OsamaBab/Console-based-Banking-Application.git. 
3. Direct to the directory of the project: cd Console-based-Banking-Application
4. Install the required dependencies: pip install -r requirements.txt.
5. Run the bank application using this command line: streamlit run main.py
### The Usage 
1. Register a new customer: Navigate to the register page to create a new bank account via inputting your name, email, password, and selecting an account type.
2. Login: Enter your account number, and your password to log in to your account.
3. Dashboard: You can view your accounts, account balances and transaction histories.
4. Transactions:
    1. Deposit funds to any of your accounts.
    2. With sufficient balances, withdraw funds from any of your accounts.
    3. With sufficient balances, transfer funds to another account of the same type.
5. Logout: Toggle to logout page and confirm the logging out to exit from the bank services.
### Classes and Methods
#### Bank Class:
Bank class represents the overall banking system info, managing customers, accounts, and the persistence of data.
##### Key Methods:
1. Init method initialises bank objects’ parameters such as bank name, contact, and address.
2. Show bank info method shows banks’ information using the bank class parameters
3. Load customers method loads customers’ data from JSON files.
4. Save customer method saves customers’ data to JSON files.
5. Generate customer id method generates unique customers’ ids for new registered customers.
6. Find customer by account number method retrieves customers based on their accounts’ numbers.
#### Account Class:
Represents a bank account with attributes like balance, account type, customer ID, and associated transaction history.
##### Key Methods
1. Init method initialises accounts objects’ parameters such as account number, balance, account type, customer id, and transaction.
2. Deposit method deposits money into the accounts.
3. Withdraw method withdraws money from accounts if sufficient balance is available.
4. Transfer method transfers money from an account to another account of the same type.
5. Add transaction method records a transaction in the account's history.
6. Get balance method returns accounts’ balances.
7. To dictionary method serialises and converts accounts’ objects into a dictionary compatible format for JSON.
#### Customer Class:
This class represents a bank customer with personal details, associated accounts, and login credentials.
##### Key Methods
1. Init method initialises customers objects’ parameters such as ID, name, email, password, and accounts.
2. Add account method adds new accounts to the customer's account list.
3. To dictionary method serialises and converts accounts’ objects into a dictionary compatible format for JSON file.
### The License
The license for this project is under the MIT License. For more enquires, See the LICENSE file 

