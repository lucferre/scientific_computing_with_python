class Category:
    
    def __init__(self, category):
        self.ledger = []
        self.category = category.capitalize()
        
    def __str__(self):
        string = """"""
        # Add title
        while len(string) < 30:
            if len(string) == int((30-len(self.category))/2):
                string += self.category.capitalize()
            else:
                string += '*'
        string += '\n'
        # Add items
        for item in self.ledger:
            desc = item['description'][:23]
            while len(desc) < 23:
                desc += ' '
            # Create amount string (right side of line)
            # right aligned, max 7 char, 2 decimal places
            amount = list("{:.2f}".format(item['amount'])[:7])
            while len(amount) < 7:
                amount.insert(0, ' ')
            string += desc + ''.join(amount) + '\n'
        # Add total
        string += 'Total: {:.2f}'.format(self.get_balance())
        return string
        
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        
    def get_balance(self):
        return sum([x['amount'] for x in self.ledger])
    
    def check_funds(self, amount):
        enough_funds = False
        if amount <= self.get_balance():
            enough_funds = True
        return enough_funds
        
    def withdraw(self, amount, description=''):
        withdrawn = False
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            withdrawn = True
        return withdrawn
    
    def transfer(self, amount, recipient):
        transferred = False
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {recipient.category}')
            recipient.deposit(amount, f'Transfer from {self.category}')
            transferred = True
        return transferred



def create_spend_chart(categories):
    string = """Percentage spent by category\n"""
    # Create list with percentages from 100 to 0 at 10 intervals
    graph_pcts = [str(x) for x in range(100, -1, -10)]
    
    # Create list with amounts of withdrawals for category
    categ_names = [] # list of the category names passed into the function
    expenses = []
    for i, category in enumerate(categories):
        # Add an integer to next index in expenses list
        expenses.append(0)
        categ_names.append(category.category)
        for dict in category.ledger:
            if dict['amount'] < 0:
                # Add expense amount to new integer in list
                expenses[i] += dict['amount']
    
    # Create list with the percentages to draw in the graph
    expenses_pct = [str(int(expense/sum(expenses)*10)*10) for expense in expenses]
    
    # Have we started drawing the bar for each of the categories?
    bar_started = [False for i in range(4)]
    
    # If so, where have we started?
    first_started_at = 0
    
    # For each line in the graph (string)
    for pct in graph_pcts:
        # Add leading space(s), percentage, and pipe to graph
        if len(pct) == 2:
            string += ' '
        elif len(pct) == 1:
            string += '  '
        string += pct + '| '
        
        # Should we start drawing the bar?
        if pct in expenses_pct:
            bar_started[expenses_pct.index(pct)] = True
        
        # Draw the bars    
        for i in range(len(categ_names)):
            if bar_started[i]:
                string += 'o  '
            else:
                string += ' '*3
        string += '\n'
    # Add horizontal bar of '-'
    string += ' '*4 + '-' + '---'*bar_started.count(True) + '\n'
    # Add categories names arranged vertically
    no_of_lines = max([len(categ) for categ in categ_names]) # the length of longest name
    for n in range(no_of_lines):
        # Add line leading spaces
        string += ' '*5
        for categ in categ_names:
            if n < len(categ):
                string += categ[n] + ' '*2
            else:
                string += ' '*3
            if categ == categ_names[-1]:
                string += '\n'
        
    return string[:-1]
