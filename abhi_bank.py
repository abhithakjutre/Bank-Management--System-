import os
import json
import random

# class OpenFileOperation:
#     def load_account(self, account_file):
#         if os.path.exists(account_file):
#             with open(account_file, "r", encoding="utf-8") as file:
#                 try:
#                     data = json.load(file)
#                     return data if isinstance(data, dict) else {}
#                 except json.JSONDecodeError:
#                     return {}
#         else:
#             return {}

#     def save_account(self, accounts, account_file):
#         print("DEBUG => saving to file:", account_file)
#         print("DEBUG => data being written:", accounts)
#         dir_path = os.path.dirname(account_file)
#         if dir_path:
#             os.makedirs(dir_path, exist_ok=True)
#         with open(account_file, "w", encoding="utf-8") as file:
#             json.dump(accounts, file, indent=4)


class AccountOperation():
    def __init__(self):
        script_path = os.path.dirname(os.path.abspath(__file__))
        self.account_file = os.path.join(script_path, "account_data.json")

    def load_account(self, account_file):
        if os.path.exists(account_file):
            with open(account_file, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                    return data if isinstance(data, dict) else {}
                except json.JSONDecodeError:
                    return {}
        else:
            return {}

    def save_account(self, accounts, account_file):
        dir_path = os.path.dirname(account_file)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
        with open(account_file, "w", encoding="utf-8") as file:
            json.dump(accounts, file, indent=4)


    def open_account(self):
        fullname = input("\n\nEnter Your Full Name: ").strip()
        phno = input("Enter Your Phone Number (10 digits): ").strip()
        email = input("Enter Your Email: ").strip()

        adharnumber = input("Enter Your Aadhaar Number (12 digits): ").strip()
        try:
            first_deposit = int(input("Enter Your First Deposit minimum 💸500: ").strip())
        except ValueError:
            print("⚠ Invalid amount. Please enter a number. ⚠")
            return

        valid = (
            first_deposit >= 500
            and phno.isdigit() and len(phno) == 10
            and adharnumber.isdigit() and len(adharnumber) == 12
            and "@" in email and "." in email
        )

        if not valid:
            print("⚠ Your information is invalid. Please check and try again. ⚠")
            return

        accounts = self.load_account(self.account_file)

        # generate unique account number
        while True:
            account_number = str(random.randint(3663000000000000, 3663999999999999))
            if account_number not in accounts:
                break

        # ✅ add account
        accounts[account_number] = {
            "fullname": fullname,
            "phno": phno,
            "email": email,
            "adharnumber": adharnumber,
            "balance": first_deposit,
        }

        try:
            self.save_account(accounts, self.account_file)
            print("Your detail saved Successfully ✅")
        except Exception as e:
            print(f"Error saving account: {e}")

        print(f"🎉 Welcome, {fullname}! Your account is opened. Current Balance: {first_deposit} 🎉")

    def check_balance(self, account_number):
        accounts = self.load_account(self.account_file)
        account = accounts.get(str(account_number))
        if account:
            print(f"{account['fullname']} Your Current Balance: {account['balance']}")
        else:
            print("Account Not Found :(")

    def update_user_details(self,account_number,account_file):
        # Update details for an account, with validation and persistence
        user_ac_no = input("Please Enter Your Account Number: ").strip()
        accounts = self.load_account(self.account_file)
        account = accounts.get(str(user_ac_no))

        if not account:
            print("Invalid Account Number :(")
            return

        while True:
            print("\n1. Update Phone No.\n2. Update Name\n3. Update Email\n4. Update Aadhar No.\n5. Go Back")
            choice = input("Enter Your Choice: ").strip()

            if choice == "1":
                new_no = input("Enter New Phone No. (10 digits): ").strip()
                if new_no.isdigit() and len(new_no) == 10:
                    account["phno"] = new_no
                    self.save_account(accounts, self.account_file)
                    print("Phone number updated successfully ✅")
                else:
                    print("Invalid phone number. Try again.")

            elif choice == "2":
                new_name = input("Enter New Full Name: ").strip()
                if new_name:
                    account["fullname"] = new_name
                    self.save_account(accounts, self.account_file)
                    print("Name updated successfully ✅")
                else:
                    print("Name cannot be empty.")

            elif choice == "3":
                new_email = input("Enter New Email: ").strip()
                if "@" in new_email and "." in new_email:
                    account["email"] = new_email
                    self.save_account(accounts, self.account_file)
                    print("Email updated successfully ✅")
                else:
                    print("Invalid email format.")

            elif choice == "4":
                new_aadhar = input("Enter New Aadhar No. (12 digits): ").strip()
                if new_aadhar.isdigit() and len(new_aadhar) == 12:
                    account["adharnumber"] = new_aadhar
                    self.save_account(accounts, self.account_file)
                    print("Aadhar number updated successfully ✅")
                else:
                    print("Invalid Aadhar number.")

            elif choice == "5":
                break
            else:
                print("Invalid choice, try again :(")
    


if __name__ == "__main__":
    operation = AccountOperation()
    print("Welcome to Abhi Bank")
    while True:
        print("1. Open Account\n2. Check Balance\n3. Update Details\n4. Exit")
        choice = input("Enter Your Choice: ")
        if choice == "1":
            operation.open_account()
        elif choice == "2":
            input_account_no = input("Enter Your Account Number: ").strip()
            operation.check_balance(input_account_no)
        elif choice == "3":
            operation.update_user_details(None, None)
        elif choice == "4":
            break
        else:
            print("Invalid Choice")