print("Welcome to Length Conversion :) ")
#print("We have different scenarios... ")

while True:  
    a=user_input=input("Which unit do you want to convert? ").lower()
    b=converted_input=input("In which unit do you want to convert? ").lower()

    if a=="km" and b=="m":
       value=float(input("Enter your Value: "))
       c=int(value*1000)   
       print(c,b)
    elif a=="m" and b=="km":
       value=float(input("Enter your Value: "))
       c=float(value/1000)   
       print(c,b)
    elif a=="m" and b=="Cm":
       value=float(input("Enter your Value: "))
       c=float(value*100)   
       print(c,b)
    elif a=="cm" and b=="m":
      value=float(input("Enter your Value: "))
      c=float(value/100)   
      print(c,b)   
    elif a=="feet" and b=="inch":
      value=float(input("Enter your Value: "))
      c=float(value*12)   
      print(c,b)
    elif a=="inch" and b=="feet":
      value=float(input("Enter your Value: "))
      c=float(value/12)   
      print(c,b)
    elif a=="mile" and b=="km":
      value=float(input("Enter your Value: "))
      c=float(value*1.609)   
      print(c,b)
    elif a=="km" and b=="mile":
      value=float(input("Enter your Value: "))
      c=float(value/1.609)   
      print(c,b)
    else:
       break  