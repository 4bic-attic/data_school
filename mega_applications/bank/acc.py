class Account(object):
    """Description for Account class."""
    def __init__(self,filepath):
        with open(filepath, 'r') as file:
            self.balance = int(file.read())
            

account=Account("balance.txt")
