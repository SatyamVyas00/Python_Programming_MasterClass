import datetime
import pytz


class Account:
    """ Simple Account class with Balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = []
        print("Account Created for " + self._name)
        self._transaction_list.append((Account._current_time(), self.__balance))

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Balance deposited {}".format(amount))
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Amount Withdrawn {}".format(amount))
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("Insufficient Balance in Account to Withdraw")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transaction(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                trans_type = "deposited"
            else:
                trans_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {}".format(amount, trans_type, date, date.astimezone()))


if __name__ == "__main__":
    Satyam = Account("Satyam", 0)
    Satyam.show_balance()
    Satyam.withdraw(500)
    Satyam.deposit(1000)
    Satyam.withdraw(500)
    Satyam.withdraw(2000)

    Satyam.show_transaction()

    account2 = Account("account2", 800)
    account2.deposit(100)
    account2.withdraw(200)
    account2.__balance = 200
    account2.show_transaction()
    account2.show_balance()
    print(account2.__dict__)