Bank Management Application
Project Overview
This bank management system is built using Streamlit and Python programming Language. It enables non-registered users to register memberships accounts, log in to their accounts, and perform different fund transactions’ types such as deposits, withdrawals, and transfers fund across multiple account types. This bank system is designed with a focus on both security and simplicity aspects, ensuring a seamless administrators’ and customers’ experience.
The System Features.
•	Users Registration: Non-registered users can register their membership with unique customer ids and account types such as Current, Saving, Mortgage, or Business.
•	Customers Login: Secure login process using customers’ accounts numbers with their associated passwords.
•	Account Management: The bank customers are able to view their accounts, balances and all transaction histories.
•	Transactions:
o	Customers can select accounts to deposit funds.
o	Customers can withdraw funds if they have sufficient balances.
o	Customers can transfer funds between the same accounts’ types while ensuring they have sufficient balances.
•	Customers Logout: Confirmed logout process using 
•	Error Handling: The system includes comprehensive error messages for both invalid inputs and operations.
•	Data Persistence: All the bank customers’ data including their accounts and transactions data are loaded, saved and stored in a JSON file.



Project Structure
project Console-based-Banking-Application/
├── home.py		#Entry point of the application
├── class/
│   ├── account.py		# Defines account functionalities
│   ├── bank.py		# Manages customer and account operations
│   ├── customer.py	# Represents customer details
├── st_pages/
│   ├── dashboard.py	# User dashboard
│   ├── deposit.py		# Deposit functionality
│   ├── login.py		# Login functionality
│   ├── logout.py		# Logout functionality
│   ├── register.py		# User registration functionality
│   ├── transfer.py		# Transfer functionality
│   ├── withdraw.py	# Withdrawal functionality
├── data/
│   ├── customers.json	# Persistent storage for customer data
├── README.md		# Documentation
└── requirements.txt         # Python dependencies
Classes and Methods
Bank Class
Bank class represents the overall banking system info, managing customers, accounts, and the persistence of data.
Key Methods
•	Init method initialises bank objects’ parameters such as bank name, contact, and address.
•	Show bank info method shows banks’ information using the bank class parameters
•	Load customers method loads customers’ data from JSON files.
•	Save customer method saves customers’ data to JSON files.
•	Generate customer id method generates unique customers’ ids for new registered customers.
•	Find customer by account number method retrieves customers based on their accounts’ numbers.
Account Class
Represents a bank account with attributes like balance, account type, customer ID, and associated transaction history.
Key Methods
•	Init method initialises accounts objects’ parameters such as account number, balance, account type, customer id, and transaction.
•	Deposit method deposits money into the accounts.
•	Withdraw method withdraws money from accounts if sufficient balance is available.
•	Transfer method transfers money from an account to another account of the same type.
•	Add transaction method records a transaction in the account's history.
•	Get balance method returns accounts’ balances.
•	To dictionary method serialises and converts accounts’ objects into a dictionary compatible format for JSON.
Customer Class
This class represents a bank customer with personal details, associated accounts, and login credentials.
Key Methods
•	Init method initialises customers objects’ parameters such as ID, name, email, password, and accounts.
•	Add account method adds new accounts to the customer's account list.
•	To dictionary method serialises and converts accounts’ objects into a dictionary compatible format for JSON file.
Setup Instructions
1.	Download the repository to your local machine using this link: https://github.com/OsamaBab/Console-based-Banking-Application/archive/refs/heads/main.zip  
2.	Clone the repository remotely using this command line: 
git clone https://github.com/OsamaBab/Console-based-Banking-Application.git 
3.	Direct to the directory of the project: cd Console-based-Banking-Application
4.	Install the required dependencies: pip install -r requirements.txt
5.	Run the bank application using this command line: streamlit run home.py
The usage
1.	Register a new customer: Navigate to the register page to create a new bank account via inputting your name, email, password, and selecting an account type.
2.	Login: Enter your account number, and your password to log in to your account.
3.	Dashboard: You can view your accounts, account balances and transaction histories.
4.	Transactions:
o	Deposit funds to any of your accounts.
o	With sufficient balances, withdraw funds from any of your accounts.
o	With sufficient balances, transfer funds to another account of the same type.
5.	Logout: Toggle to logout page and confirm the logging out to exit from the bank services.
Testing
The bank classes’ instances such as account, bank and customer instances are practically tested and implemented in the test class as well as the bank key functionalities’ use cases such as:
•	Registering a new customer’s functionality
•	Performing operations such as deposits, withdrawals, and transfers.
•	Processes of loading and saving customer data.
*Run the test via navigating to the test page.
Problem Solving and Design Decisions
The below associated design decisions with problem-solving techniques are applied in this banking system:
•	Account Type Matching: For consistency and business logic, the transfer functionality is restricted to the same accounts’ types only.
•	JSON Persistence: For lightweight and simple data storage, Json file is used ensuring the ease of portability.
•	Modular Design: For enhancing maintainability and scalability, functionalities are separated into individual modules.
•	Error Handling: For enhanced and better user experience, comprehensive data checks and descriptive error messages are added.
License
The license for this project is under the MIT License. For more enquires, See the LICENSE file 


