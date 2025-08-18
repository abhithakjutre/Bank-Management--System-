import random

def open_aaccount(fullname,phno,email,adharnumber,first_deposit): 

    if first_deposit<=500 or phno<9999999999 or adharnumber<999999999999:
        account_number = random.choice(3663000000000000,36630999999999999)

        print(f"🎉Welcome! {fullname}, Your Account Opened and Your Current Balance: {first_deposit} 🎉")
        user_detail = f"\nAccount name: {fullname}\nYour Account number: {account_number} Your Phone Number: {phno}\nYour Email i'd: {email}\nYour Adhar Number: {adharnumber}\n Your Current Balance: {first_deposit}"

        print(f" Your Account detail:{user_detail}")

        with open("account_data.txt","a") as file: 
            file.write(f"{account_number}:\n{user_detail}\n")
            print("Thank You 😊")

    
    else: 
        print("⚠ Your Information detail invalid ⚠")

    
def check_balance(account_number): 

    with open("account_data.txt","r") as file: 
        userdata










 

    
    
def main(ammount): 
    pass