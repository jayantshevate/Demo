


correct_pin = 1234   
balance = 5000       
pin = int(input("Enter your ATM PIN: "))

if pin == correct_pin:
    print("PIN Verified ")
    
    amount = int(input("Enter withdrawal amount: "))
    
    if amount > 0:
        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful!  Please collect your cash.")
            
        else:
            print("Insufficient Balance ")
    else:
        print("Invalid Amount ")
else:
    print("Incorrect PIN ")

 





 





