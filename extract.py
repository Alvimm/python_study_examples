class Extract:
    def __init__(self):
        self.transactions = []

    def extracts(self, account_number):
        print(f'Extract: {account_number}\n')
        for p in self.transactions:
            print(f'{p[0]:15s} {p[1]:10.2f} {p[2]:10s} {p[3]}')
