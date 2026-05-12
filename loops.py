multiplier = 5
for  i in range(1,13):
    print(multiplier, "x" , i ,"=", multiplier*i)
    
print("\n")    
counter = 2
while counter <= 10:
    print(counter)
    counter += 3  
   
print("\n")

my_password = "1234"

attempt = 0
while attempt < 3:
    user_paasword= input("Enter your password: ")
    if my_password == user_paasword:
        print("Access Granted!")
        break
    else:
        attempt += 1
        print(f"Wrong password!  Remaining  {3 - attempt} attempt(s)")
    if attempt==3:
        print("Too many password entered.")
        print("Access Blocked")