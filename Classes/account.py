# Import required libraries
import random
import string


class Account:
    """
    Discription:
    Represents a bank account with attributes like balance, account type, customer ID, 
    and associated transaction history.
    """

    def __init__(myself, acc_number=None, balance=0, account_type="savings", cust_id=None, transactions=None):
        
        """
        Discription:
        Initialise a new Account instance from account class.

        Args:
            account_number (str): Account number. Generated if not provided.
            balance (float): Initial balance. Default is 0.
            account_type (str): Type of account (e.g., "savings", "current"). Default is "savings".
            customer_id (str): ID of the customer associated with the account.
            transactions (list): List of transaction.
        """
        myself.acc_number = acc_number or myself.generate_account_number()
        myself.balance = balance
        myself.account_type = account_type
        myself.cust_id = cust_id 
        myself.transactions = transactions if transactions is not None else []

        def generate_account_number(self):
            """
            Generate a random 6-digit account number."""
            """
            Generate a unique account number.

            Returns:
                str: A randomly generated 6-digit account number.
            """
            return ''.join(random.choices(string.digits, k=6))
