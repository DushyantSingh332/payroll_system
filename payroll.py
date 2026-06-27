

FILE_NAME = "employees.txt"

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))
    hra = float(input("Enter HRA: "))
    da = float(input("Enter DA: "))
    tax = float(input("Enter Tax: "))

    net_salary = basic + hra + da - tax

    with open(FILE_NAME, "a") as file:
        file.write(f"{emp_id},{name},{basic},{hra},{da},{tax},{net_salary}\n")

    print(" Employee record added successfully!\n")


def view_employees():
    try:
        with open(FILE_NAME, "r") as file:
            print("\n--- Employee Payroll Records ---")
            for line in file:
                emp_id, name, basic, hra, da, tax, net = line.strip().split(",")
                print(f"""
Employee ID : {emp_id}
Name        : {name}
Basic       : {basic}
HRA         : {hra}
DA          : {da}
Tax         : {tax}
Net Salary  : {net}
----------------------------
""")
    except FileNotFoundError:
        print(" No records found!\n")


def menu():
    while True:
        print("""
======= Employee Payroll System =======
1. Add Employee
2. View Employees
3. Exit
""")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            print("👋 Exiting program. Thank you!")
            break
        else:
            print(" Invalid choice! Try again.\n")


menu()
