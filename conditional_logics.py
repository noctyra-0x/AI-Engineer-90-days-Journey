name=input("Enter your name: ")
try:
    hour=int(input("Whats the studing goal in hours: "))
    if hour>=3:
        print(f"Thats goof {name} \n You got time for your study. means you are a really  good studeny. Ik you have goals that's why you take time for your studies") 
    else:
        print(f"That's bad to hearing {name} \n that you don't got a time for your studies, Ik that's a little bit bad. But you can do anything if you want furthermore you alos got time for your studies")
except ValueError:
    print(f"Dear {name}, Kindly entered the valid numbers")  