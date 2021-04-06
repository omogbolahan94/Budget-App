
class Budget:
    """
    Create a Budget class that can instantiate objects based on different
    budget categories(class instances) like food, clothing, and entertainment.
    These objects should allow for:
    1.  Depositing funds to each of the categories
    2.  Withdrawing funds from each category
    3.  Computing category balances
    4.  Transferring balance amounts between categories
    """
    def __init__(self):
        self.amount = 200

    def deposit(self, deposit_amount):
        """
        Deposit money to budget
        :param deposit_amount:
        :return: None
        """
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        """
        Withdraw money from budget
        :param withdraw_amount:
        :return: None
        """
        self.amount -= withdraw_amount

    def balance(self):
        """
        To check budget balance
        :return: None
        """
        return f"${self.amount}"

    def transfer(self, category_budget, amount):
        """
        Transfer money from this this category to the category_budget
        class composition is a way of instantiating instant method parameter with another class object
        :param: category_budget, amount:
        :return: None
        """
        self.amount -= amount
        category_budget.amount += amount


print("\n")
print("==" * 5, "Food Budget", "==" * 5)
food = Budget()
food.deposit(100)
food.withdraw(50)
print(f"Food balance after depositing $100 and Withdrawing $50 is: {food.balance()}")

print("\n")
print("==" * 5, "Clothing Budget", "==" * 5)
clothing = Budget()
food.transfer(clothing, 100)
print(f"Clothing balance after receiving $100 from food budget balance: {clothing.balance()}")
print(f"Food budget balance after transferring $100 to clothing budget balance: {food.balance()}")
print("\n")
print("==" * 5, "Entertainment Budget", "==" * 5)
entertainment = Budget()
print(f"Entertainment budget balance is untouched and it is: {entertainment.balance()}")