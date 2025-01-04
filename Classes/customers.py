#from .account import Account

class Customer:
    """
    Discription:
    This class represents a bank customer with personal details, associated accounts, 
    and login credentials.
    """
    def __init__(self, cust_id, cust_name, password=None, email=None, accounts=None):
        """
        Discription:
        this method define the class attributes and initialise a new Customer instance.
        Args:
            cust_id (str): A unique customer identifier.
            cust_name (str): The name of the customer.
            password (str): The password for login.It is empty by default
            email (str): The email address of the customer.It is empty by default
            accounts (list): The list of Accounts that associated to a customer. It is empty by default.
        """
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.password=password
        self.email=email
        self.accounts = accounts if accounts else []

    def add_account(self, account):
        """
        Discription:
        This method adds new accounts to customers account list.
        """
        self.accounts.append(account)

    def to_dictionary(self):
        """
        Discription:
        Return Method to serialise and convert the Customer object into a JSON dictionary compatible format.
        Returns:
            dict: Dictionary representation of the customer, including accounts.
        """
        return {
            #Return
            "cust_id": self.cust_id,
            "cust_name": self.cust_name,
            "password": self.password,
            "email":self.email,
            # Serializsimg accounts
            "accounts": [account.to_dictionary() for account in self.accounts]  
        }

