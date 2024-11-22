class Bank:
    """
    Discription:
    Represents the overall banking system, managing customers, accounts, 
    and the persistence of data.
    """
    def __init__(myself, bank_name, phone, address):

        """
        Initialise a Bank instance.

        Args:
            bank_name (str): Name of the bank.
            phone (int): Bank phone number.
            address (str): the address of the bank
        """
        myself.bank_name = bank_name
        myself.phone = phone
        myself.address = address