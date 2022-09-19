import os
import math
import random
import smtplib

# clering terminal
os.system('clear')


try:
    digits = "0123456789"
    OTP = ""
    
    for i in range(6):
        OTP += digits[math.floor(random.random()*10)]
    
    otp = OTP + " is your OTP"
    msg= otp
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("Your Gmail Account", "You app password")
    emailid = input("Enter your email: ")
    server.sendmail('&&&&&&&&&&&',emailid,msg)
    
    a = input("Enter Your OTP >>: ")
    if a == OTP:
        print("Verified")
    else:
        print("Please Check your OTP again")
except:
    print('Error occured somewhere!')
