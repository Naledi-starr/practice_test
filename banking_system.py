
# Function to deposit money into an account
def deposit(account: dict, amount: float) -> None:
    if amount > 0:
        account['balance'] += amount

# Function to withdraw money from an account
def withdraw(account: dict, amount: float) -> None:

    if amount <= account['balance'] and amount > 0:
        account['balance'] -= amount

    # else:
    #     return "Insufficient Funds"
        

# Function to transfer money between two accounts
def transfer(from_account: dict, to_account: dict, amount: float) -> None:
    if amount > 0 and from_account['balance'] >= amount:
        from_account['balance'] -= amount
        to_account['balance'] += amount

# Function to add a new account to the system
def add_account(accounts: dict, owner: str, initial_balance: float) -> None:
    if owner not in accounts and initial_balance >= 0:
        accounts[owner] = {'balance':initial_balance}

# Function to find an account by owner's name
def find_account(accounts: dict, owner: str) -> dict:
    # if accounts[owner] in accounts:
    return accounts.get(owner)
        

# Function to display all accounts in the system
def display_all_accounts(accounts: dict) -> str:
    return '\n'.join([f"{owner}: {account['balance']}" for owner, account in accounts.items()])
