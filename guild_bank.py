import threading

class GuildBank(threading.Thread):

    def __init__(self):
        self.balance = 0 #setting balance of initialized bank to 0
        self.account_open = False
        self.lock = threading.Lock()

    def get_balance(self):
        if self.account_open == False: #checking if user has an account open
            raise ValueError("No account open to get balance from!")
        return self.balance #returning the current balance of the guild's bank

    def open_account(self):
        if self.account_open == True: #checking if user has an account open
            raise ValueError("Account already open!")
        self.account_open = True

    def deposit_gold(self, amount):
        if self.account_open == False or amount<0: #checking if user has an account open
            raise ValueError("No account open to deposit to! Or attempting to deposit negative amuont!")

        with self.lock:
            self.balance += amount
        #print("Deposited ",amount,"to your account.")

    def withdraw_gold(self, amount):
        if self.account_open == False or amount>self.balance or amount<0: #checking if user has an account open
            raise ValueError("No account open to withdraw from! Or attempting to withdraw negative value! Or attempting to withdraw value greater than balance!")
        with self.lock:
            self.balance-=amount
        #print("Deposited ",amount,"to your account.")


    def close(self):
        if self.account_open == False: #checking if user has an account open
            raise ValueError("No account available to close!")
        self.account_open = False
        self.balance = 0

class Thread(threading.Thread):
    def __init__(self, t, *args):
        threading.Thread.__init__(self, target=t, args=args)
        self.start()