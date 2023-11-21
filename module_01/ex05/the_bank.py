
class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):     #   accept any number of keyword arguments during object initialization
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount



class Bank(object):
    """The bank"""

    def __init__(self):
        self.accounts = []

    def check_corrupt(self, new_account):
        if not isinstance(new_account, Account):
            return False
        if len(vars(new_account)) % 2 == 0:
            return False    #   corrupted
        args = vars(new_account)
        if not all(key in args for key in ("name", "id", "value")):
            return False
        if not isinstance(args['name'], str):
            return False
        if not isinstance(args['id'], int):
            return False
        if not isinstance(args['value'], int) and not isinstance(args['value'], float):
            return False
        for i in args:
            if i.startswith('b') or i.startswith('addr') or i.startswith('zip'):
                return False    #   corrupted

    def add(self, new_account):
        """ 
            Add new_account in the Bank 
                @new_account: Account() new account to append 
                @return True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        if self.check_corrupt(new_account) is False:
            return -1
        
        self.accounts.append(new_account)
        return True

    def transfer(self, origin, dest, amount):
        """
            Perform the fund transfer 
                @origin: str(name) of the first account
                @dest: str(name) of the destination account
                @amount: float(amount) amount to transfer
                @return True if success, False if an error occured
        """
        # find origin obj and dest ob
        if origin == dest:
            return True
        origin_acc = None
        dest_acc = None
        for acc in self.accounts:
            if acc.name == origin:
                origin_acc = acc
            elif acc.name == dest:
                dest_acc = acc
        if origin_acc is None or dest_acc is None:
            return False
        if amount < 0 or amount > origin_acc.value:
            return False
        origin_acc.value -= amount
        dest_acc.value += amount
        
    def fix_account(self, name):    #   does not work
        """ 
            fix account associated to name if corrupted
            @name: str(name) of the account
            @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False
        found_acc = None
        for acc in self.accounts:
            if acc.name == name:
                found_acc = acc
                if not check_corrupt(found_acc):
                    return False
                break
        if found_acc is not None: 
            found_acc.name = name
        return True


# def main():
#     bank = Bank()
#     bank.add(Account("gui", value=100))
#     bank.add(Account("lala", value=100))
#     bank.transfer("gui", "lala", 15)

# if __name__== "__main__":
#     main()