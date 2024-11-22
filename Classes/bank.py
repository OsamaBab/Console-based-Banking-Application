class Bank:
    """
    Discription:
    Represents the overall banking system, managing customers, accounts, 
    and the persistence of data.
    """
    def __init__(myself, bank_name, contact, address):

        """
        Initialise a Bank instance.

        Args:
            bank_name (str): Name of the bank.
            contact (str): Contact information for the bank.
            address (str): the address of the bank
        """
        myself.bank_name = bank_name
        myself.contact = contact
        myself.address = address