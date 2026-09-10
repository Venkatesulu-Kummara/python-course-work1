import logic as lg

if lg.login():
    while True:
        lg.menu()
        choice = input("Enter your choice: ").upper()
        if choice == 'C':
            lg.check_balance()
        elif choice == 'D':
            lg.deposit()
        elif choice == 'W':
            lg.withdraw()
        elif choice == 'T':
            lg.transaction()
        elif choice == 'E':
            print("----------Thank You, visit again----------")
            break
        else:
            print("Invalid choice, please try again.")