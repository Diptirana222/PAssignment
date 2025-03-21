# Q1
a = int(input("Enter years of service:"))
# a = 8
if a>10:
    bonus = 10000
else:
    if a>5:
        bonus = 5000
    else:
        bonus = 2000
print("The bonus amount is ₹", bonus)

#Q2
m = int(input("Enter your mark brohh:"))
if m > 90:
   grade = 'A'
elif m >= 80 and m <= 90:
    grade = 'B'
elif m >= 70 and m <= 79:
    grade = 'C'
else:
    grade = 'D'
print("mark according your grade is",grade)
   
#Q3
s = int(input("Driving Speed:"))
if s > 80:
    if s > 100:
        msg = "The driver is heavily fined for overspeeding."
    else:
        msg = "Warning: speed is above 80km/h."
elif s>=60 and s<=80:
     msg = "speed is normal."
else:
    if s<40:
        msg = "Warning: Slow driving."
    else:
        msg = "speed is below 60km/h, drive safely."
print(msg)

#Q4
sal = int(input("Enter your salary:"))
if sal>50000:
    note = "you are eligible to apple for a loan."
elif sal>=30000 and sal<=50000:
     score = int(input("scrore de bhai phle:"))
     if score>700:
         note = "your are eligible"
     else:
         note = "you are rejected"
else:
      note = "The loan is denied."
print(note)

#Q5
Original_fare = 200
g = int(input("Enter the age:"))
if g>60:
   ticket = Original_fare * 0.5
elif g >= 18 and g <=60:
   ticket = Original_fare
else:
    if g<5:
       ticket = 0
    else:
        ticket = Original_fare * 0.75
print("The ticket price is ₹",ticket)

#Q6\
