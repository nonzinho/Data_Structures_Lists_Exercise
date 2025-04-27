#Let us say your expense for every month are listed below,
#January - 2200
#February - 2350
#March - 2600
#April - 2130
#May - 2190

#Create a list to store these monthly expenses and using that find out,
#1. In Feb, how many dollars you spent extra compare to January?
#2. Find out your total expense in first quarter (first three months) of the year.
#3. Find out if you spent exactly 2000 dollars in any month
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this

expenses = [2200, 2350, 2600, 2130, 2190]

def compare_expenses(month1, month2):
    return month2 - month1

print("Compare expenses between January and February:")
print(f"February - January = {compare_expenses(expenses[0], expenses[1])}")


def find_total_expense_in_quarter(expenses):
    return sum(expenses[:3])

print(f"Total expense in first quarter: {find_total_expense_in_quarter(expenses[:3])} ")

def check_expense(expenses, amount):
    for expense in expenses:
        if expense == amount:
            return 'Yes'
    return 'No'

print(f'Did you spend exactly 2000 dollars in any month? {check_expense(expenses, 2000)}')

def add_expense(expenses, new_expense):
    expenses.append(new_expense)
    return expenses

print(f"Adding June expense: {add_expense(expenses, 1980)}")

def correct_expense(expenses, month, refund):
    expenses[month] += refund
    return expenses

print(f"Correcting April expense: {correct_expense(expenses, 3, 200)}")

print(f"Final expenses: {expenses}")

#Done, yay!
#The code is complete and all the tasks are done.