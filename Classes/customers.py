
class Customer:

    """
    Discription:
    A class represents a bank customer details, associated accounts, 
    and login credentials.
    """
    def __init__(myself, cust_id, name, password=None, email=None, cust_accounts=None):
        """
        Discription:
        Initialize a new Customer instance.
        Args:
            cust_id (str): Unique customer identifier for each customer.
            name (str): Full name of the customer.
            password (str): Encrypted password for customer login.
            email (str): Email address of the customer for login.
            cust_accounts ([]): List of associated Account instances for each customer. Default is None or an empty list.
        """
        myself.cust_id = cust_id
        myself.name = name
        myself.password=password
        myself.email=email
        myself.cust_accounts = cust_accounts if cust_accounts else []
