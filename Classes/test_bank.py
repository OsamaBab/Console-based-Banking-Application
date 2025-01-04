# Import required files
import unittest
from account import Account
from bank import Bank
from customer import Customer

class TestBankSystem(unittest.TestCase):
    """
    This class tesets the Bank Management System key functions to validate theis performance via inheriting TestCase fron unittest 
    """
    
    def setUp(self):
        """
        This function initialises the bank classes' Customer and Account instances
        """
        # Create a mock bank instace from the Bank class
        self.bank = Bank("Halifax Bank", "halifaxbank@co.uk", "2 sst road, Halifax")

        # Create a mock customer's details (customer id, name, email and password)
        self.customer = Customer(
            cust_name="Mohammed Ali",
            email="mohali@gmail.com",
            password="Password1",
            cust_id="CID1111",
        )
        # Add the mocked customer detilas to the bank customers dictionary
        self.bank.customers[self.customer.cust_id] = self.customer
        
        # Create two different mock accounts including details (account number, balance, account type and th same customer id) to the above customer
        # Create mock current account
        self.current_account = Account(
            # account number
            account_number="1000001",
            # Balance
            balance=500.0,
            # Account type
            account_type="Current",
            # Customer id
            cust_id="CID1111"
        )
        # Create mock saving account
        self.saving_account = Account(
            # Account number
            account_number="1000002",
            # Balance
            balance=200.0,
            # Account type
            account_type="Saving",
            # Customer id
            cust_id="CID1111"
        )
        # Add above created mock current account to the customer accounts dictionary
        self.customer.accounts.append(self.current_account)
        # Add above created mock saving account to the customer accounts dictionary
        self.customer.accounts.append(self.saving_account)

    def test_register_new_customer(self):
        """
        This method tests registering new customers 
        """
        # Perform registering a new customer using the mock customers above
        add_new_customer = Customer(
            cust_name="Taha Isa",
            email="tahagmail.com",
            password="Password2",
            cust_id="CID2222",
        )
        # Save the new registered customer to the bank customers dictionary
        self.bank.customers[add_new_customer.cust_id] = add_new_customer
        # Check if the saved customer id in the bank customers dictionary is exsisted
        self.assertIn("CID2222", self.bank.customers)
        # Check if the saved customer name associated to the id in the bank customers dictionary is exsisted
        self.assertEqual(self.bank.customers["CID2222"].cust_name, "Taha Isa")

    def test_deposit_fuction(self):
        """
        This method tests depositing an amount into the current account
        """
        # Perform deposit process into the current account 
        self.current_account.deposit(20.0)
        # Check if the deposited amount 20 is added to the current account based balance 500
        self.assertEqual(self.current_account.balance, 520.0)

    def test_withdraw_function(self):
        """
        This method tests withdrawing an amount from the saving account
        """
        # perform withdrawing process from the saving account
        self.saving_account.withdraw(30.0)
        # Check if the withdrawed amount 30 is diducted from the saving account based balance 200
        self.assertEqual(self.saving_account.balance, 170.0)

    def test_transfer_function(self):
        """
        This method tests transferinging an amount between the same accounts' types
        """
        # Add a Mock account current account to the customer registerd id in the customers dictionary
        reciver_account = Account(
            cust_id="CID2222",
            account_number="1000003",
            balance= 400.0,
            account_type="Current",    
        )
        # Update the customer with the new account
        self.bank.customers["ID2222"] = Customer(
            cust_id="ID2222",
            cust_name="Taha Isa",
            email="taha@gmail.com",
            password="P2222",
            accounts=[reciver_account]
        )
        # Perform the transfer process and transfer 210  
        self.current_account.transfer(210.0, reciver_account)
        # Check if the transfered amount 210 is diducted from the sender account based balance 500
        self.assertEqual(self.current_account.balance, 290.0)
        # Check if the transfered amount 210 is added to the reciver account based balance 400
        self.assertEqual(reciver_account.balance, 610.0)
if __name__ == "__main__":
    # Run the unit test 
    unittest.main()