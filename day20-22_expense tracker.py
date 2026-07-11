import os

def load_expenses():
    expenses=[]
    if os.path.exists("expenses.txt"):
        with open("expenses.txt","r") as file:
            for line in file:
                item,price = line.strip().split(",")
                expenses.append((item, float(price)))
    return expenses

def save_expenses(expenses):
    with open("expenses.txt","w") as file:
        for item,price in expenses:
            file.write(f"{item},{price}\n")

def main():
    expenses=load_expenses()
    while True:
        command=input("Commands: add/list/total/delete/quit: ")
        if command=="add":
            item=input("Item:")
            price=float(input("Price:"))
            expenses.append((item, price))
            save_expenses(expenses)
            print("Expense added.")
        elif command=="list":
            if not expenses:
                print("No expenses found.")
            else:
                for index,(item,price) in enumerate(expenses,start=1):
                    print(f"{index}.{item}-${price:.2f}")
        elif command=="total":
            if not expenses:
                print("No expenses found.")
            else:
                total=sum(price for item,price in expenses)
                print(f"Total expenses: ${total:.2f}")
        elif command=="delete":
            delete_name=input("Enter the  name of expense to delete:")
            found=False
            for i,(item,price) in enumerate(expenses):
                if delete_name.lower()==item.lower():
                    del expenses[i]
                    found=True
                    break
            if found:
                save_expenses(expenses)
                print("Expense deleted.")
            else:
                print("Expense not found.")
        elif command=="quit":
            print("Goodbye!")
            break
main()

                






