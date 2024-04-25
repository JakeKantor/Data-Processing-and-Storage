class InMemoryDB:
    def __init__(self):
        self.storage = {}
        self.transactionActive = False
        self.transactionStorage = {}
    

    def begin_transaction(self):
        if self.transactionActive:
            raise Exception("Transaction in progress")
        self.transactionActive = True
        self.transactionStorage = self.storage.copy()

    def put(self, key, value):
        if not self.transactionActive:
            raise Exception("No transaction in progress")
        if not isinstance(value, int):
            raise ValueError("Value must be an int")
        self.transactionStorage[key] = value

    def get(self, key):
        if self.transactionActive:
            return self.transactionStorage.get(key)
        return self.storage.get(key)

    def commit(self):
        if not self.transactionActive:
            raise Exception("No transaction to commit")
        self.storage = self.transactionStorage.copy()
        self.transactionActive = False

    def rollback(self):
        if not self.transactionActive:
            raise Exception("No transaction to rollback")
        self.transactionActive = False