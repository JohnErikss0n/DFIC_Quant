import threading


class GuildBank(threading.Thread):

    def __init__(self):
        self.balance = 0  # setting balance of initialized bank to 0
        self.account_open = False  # initializing boolean to determine if account is open
        self.lock = threading.Lock()

    def get_balance(self):
        if not self.account_open:  # checking if user has an account open
            raise ValueError("No account open to get balance from!\n")
        return self.balance  # returning the current balance of the guild's bank

    def open_account(self):
        if self.account_open:  # checking if user has an account open
            raise ValueError("Account already open!\n")
        self.account_open = True

    def deposit_gold(self, amount):
        if self.account_open == False or amount < 0:  # checking if user has an account open
            raise ValueError("No account open to deposit to! Or attempting to deposit negative amuont!\n")

        with self.lock:  # locking to ensure that multiple threads can access
            self.balance += amount

    def withdraw_gold(self, amount):
        if self.account_open == False or amount > self.balance or amount < 0:  # checking if user has an account open and that amount is appropriate.
            raise ValueError(
                "No account open to withdraw from! Or attempting to withdraw negative value! Or attempting to withdraw value greater than balance!\n")

        with self.lock:  # locking to ensure multiple threads can access
            self.balance -= amount

    def close(self):
        if not self.account_open:  # checking if user has an account open
            raise ValueError("No account available to close!\n")
        self.account_open = False
        self.balance = 0
