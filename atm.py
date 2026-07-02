user_information = {
    "name": "chandra",
    "pin": "1432",
    "balance": 10345,
    "mobile_no": "",
    "transaction_his": []
}

print("Please insert your ATM card")

remaining_attempt = 4

while remaining_attempt > 0:
    user_id = input("PIN: ")

    if len(user_id) == 4:
        if user_id == user_information["pin"]:

            print("1. Balance")
            print("2. Withdraw")
            print("3. Change PIN")

            select = int(input("Enter an option: "))

            if select == 1:
                print(f"Your balance is Rs.{user_information['balance']}")

            elif select == 2:
                amount = int(input("Enter your amount: Rs."))

                if amount > 0 and amount <= user_information["balance"]:
                    user_information["balance"] -= amount
                    print("Please collect your cash")
                    print(f"Remaining balance: Rs.{user_information['balance']}")
                else:
                    print("Insufficient balance")

            elif select == 3:
                new_pin = input("Enter new 4-digit PIN: ")

                if len(new_pin) == 4:
                    user_information["pin"] = new_pin
                    print("PIN changed successfully")
                else:
                    print("PIN must be 4 digits")

            break

        else:
            remaining_attempt -= 1

            if remaining_attempt > 0:
                print(f"Invalid PIN. You have {remaining_attempt} attempts left.")
            else:
                print("Card blocked due to multiple incorrect PIN attempts.")

    else:
        print("Please enter a 4-digit PIN.")














        
