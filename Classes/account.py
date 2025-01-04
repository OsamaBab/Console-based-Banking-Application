# Import the reaquired files, classes and metods 
import random
import string
from datetime import datetime

class Account:
    """
    Discription:
    Represents a bank account with attributes like balance, account type, customer ID, 
    and associated transaction history.
    """

    def __init__(self, account_number=None, balance=0, account_type="savings",cust_id = None,  transactions=None):      
        """
        Discription:
        This method Initialising new accounts objects instances parameters.

        Args:
            account_number (str): Account number. Generated if not provided.
            balance (float): Initial balance. Default is 0.
            account_type (str): Type of account (e.g., "savings", "current"). Default is "savings".
            cust_id (str): ID of the customer associated with the account.
            transactions (list): List of transaction dictionaries. Default is empty.
        """
        self.account_number = account_number or self.generate_account_number()
        self.balance = balance
        self.account_type = account_type
        self.cust_id = cust_id 
        self.transactions = transactions if transactions is not None else []

    def generate_account_number(self):
        """
        Discription:
        Function to Generate a random 7-digit as an account number
            Returns:
                str: A randomly generated 7-digit account number.
        """
        return ''.join(random.choices(string.digits, k=7))
    
    def deposit(self, amount):
        """
        Discription:
        A function to deposit money into the account and record the deposit transaction details
            Attributes:
            amount: (float) The amount to be deposited
        """
        # Add the deposited amount to the balance
        self.balance += amount
        # Record the deposit transaction in the account history
        self.add_transaction(amount, "deposit")

    def withdraw(self, amount):
        """
        Discription:
        A function to withdraw money from an account and record the withdraw transaction details
            Attributes:
            amount: (float) The amount to be withdrawn
        """
        # Check if the account has sufficient balance
        if self.balance >= amount:
            # Deduct the amount from the account balance
            self.balance -= amount
            # Record the withdrawal transaction in the account history
            self.add_transaction(amount, "withdraw")
       
    def transfer(self, amount, recipient_account):
        """
        Discription:
        A function to transfer money between accounts of the same type and record the transactions details
            Args:
                amount (float): The amount to transfer.
                reciver_account (number): The recipient's account.

             Raises:
                ValueError: If the accounts are not in Similar type or if the balance is insufficient.
        """
        # Check if the accounts match 
        if self.account_type != recipient_account.account_type:
            raise ValueError("Transfers are allowed between similar account types only.")
        # Check the sender balance
        # Check if the sender's account has sufficient balance
        if self.balance >= amount:
            # Deduct the amount from the sender's account balance
            self.balance -= amount
            # Record the transaction in the sender's account history
            self.add_transaction(amount, f"transfer to {recipient_account.account_number}")
            # Add the amount to the recipient's account balance
            recipient_account.balance += amount
            # Record the transaction in the recipient's account history
            recipient_account.add_transaction(amount, f"transfer from {self.account_number}")
        else:
            # Raise an error if the sender has insufficient balance
            raise ValueError("Sorr!! You do NOT have sufficient balance")

    def add_transaction(self, amount, transaction_type):
        """
        Add a transaction to the user's history.
        
        Args:
            amount (float): Transaction amount.
            transaction_type (str): Type of transaction (e.g., "deposit", "withdraw", "transfer").
        """
        transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append({
            "time": transaction_time,
            "type": transaction_type,
            "amount": amount
        })

    def get_balance(self):
        """
        Return the account balance.
        """
        return self.balance

    def to_dictionary(self):
        """
        Convert the Account object into a dictionary format for JSON serialization.
            Returns:
                dict: Dictionary representation of the account.
        """
        return {
            "account_number": self.account_number,
            "balance": self.balance,
            "account_type": self.account_type,
            "cust_id": self.cust_id,
            "transactions": self.transactions
        }
