#question1
a = 100
b = 100
print(id(a))
print(id(b))
#so answer is compare b/w a and b then memory address they are  same and now output is 140719857274888 140719857274888


#task2
x = "hello"
y = "hello"
print(id(x))
print(id(y))
#the addresses are the same and its value 2027230178176 2027230178176


#task3
num1 = 3000
num2 = 3000
print(id(num1))
print(id(num2))
#Python handles memory for large integers in this case. 2711560369424 2711560369424

#4. Task:
Var1 = [1,2,3]
Var2 = [1,2,3]
print(id(Var1))
print(id(Var2))
print(id(Var1)==id(Var2))
#1990967976064
#1990968124032
#False
#because Jab aap do alag-alag variables ko ek hi list assign karte hain, Python unhe alag-alag memory addresses deta hai. Yeh isliye hota hai kyunki lists mutable hote hain, aur Python ensure karta hai ki ek variable ka change dusre variable ko affect na kare. Isliye dono variables ke apne independent objects aur memory addresses hote hain


#5. Task:
x = "hello"
y = "hello"

print(id(x))
print(id(y))
print(id(x) == id(y))
#2273666509840
#2273666509840
#True


#6. Task:
p = 1000
q = 1000
print(id(p))
print(id(q))
print(id(p) == id(q))
#Python chhote integers (-5 se 256) ko intern karta hai aur unka same memory address hota hai. ^^Bade integers (jaise 1000) ka alag memory address hota hai, lekin optimization ke karan kabhi-kabhi same bhi ho sakta hai.


#7. Task:
t1 = (1,2,3,4)
t2 = (1,2,3)
print(id(t1))
print(id(t2))
print(id(t1) == id(t2))
#Tuples immutable hote hain, isliye t1 aur t2 initially same memory address share karte hain. Jab aap t1 ko modify karte hain, ek naya tuple create hota hai, aur t1 ka memory address change ho jata hai, lekin t2 same rehta hai.

#8. Task:
a = 50
b = 50
print(id(a))
print(id(b))
print(a is b)

#9. Task:
str1 = "python"
str2 = "python"
print(id(str1))
print(id(str2))
str1 = "program"
print(id(str1))

#10. Task:
a = 133
b = 133
print(id(a))
print(id(b))
a = 134
print(id(a))

#11. Task:
x = 10
print(type(x))
import sys
print(sys.getsizeof(x),"byte")


#12. Task:
a = 1
b = "hello"
c = [1, 2, 3, 4]
import sys
print(sys.getsizeof(a),"byte")
print(sys.getsizeof(b),"byte")
print(sys.getsizeof(c),"byte")
print(type(a))
print(type(b))
print(type(c))

#13. Task: 
f = 3.14159 
print(type(f))
print(sys.getsizeof(f),"byte")
f = 1.234567890123456789
print(sys.getsizeof(f),"byte")


#14. Task:
list1 = [] 
list2 = [1, 2, 3, 4] 
print(type(list1))
print(type(list2))
print(sys.getsizeof(list1),"byte")
print(sys.getsizeof(list2),"byte")

#15. Task:
a = "Python is awesome!"*1000
print(sys.getsizeof(a),"byte")
print(type(a))
a = "Python is awesome!"
print(type(a))
print(sys.getsizeof(a),"byte")

#Q1:Decimal Number (Base-10)

a=123
print(hex(a))
print(bin(a))
print(oct(a))

#Q2. Binary Number (Base-2)
a=0b1101
# a=int(a)
print((a))

#Q3. Octal Number (Base-8)
a=0o234
print(a)
print(bin(a))

#Q4. Hexadecimal Number (Base-16)
a=0x1A3
print(a)
print(bin(a))

#Q5. Arithmetic with Binary Numbers
a=0b1010
b=0b1101
c=a+b
print(bin(c))

#Q6. Arithmetic with Octal Numbers
a=0o100
b=0o50
c=a-b
print(oct(c))

#Q7. Decimal to Binary Conversion
a=255
print(bin(a))

#Q8. Binary to Hexadecimal Conversion
a=0b111101
print(hex(a))

#Q9. Hexadecimal to Octal Conversion
a=0x7F
print(oct(a))

#Q10. Addition with Hexadecimal Numbers
a=0x2A
b=0x1F
c=a+b
print(hex(c))


#1. int():
a=45.67
print(int(a))
#When you convert a floating-point number to an integer using int(), the decimal part is truncated (i.e., it is removed), and only the integer part is retained. In this example, the decimal part .67 is discarded, and the result is 45.

#2. float():
a=123
print(float(a))


#3. complex():
a=2
b=3
print("Enter the real part:", a)
print("Enter the imaginary part:", b)
print("The complex number is:",complex(a,b))


#4. str():
a=456
print("The number is",str(a))

#5. bool():
a=12
print(bool(a))
a=0
print(bool(a))

#6.int():
a=0x1A
print(int(a))

#7.float():
a="75%"
a=float(a.strip('%'))/100
print(a)

#8.complex():
a=4
b=7
c = complex(a,b)
magnitude = abs(c)
print(c)
print(magnitude)

#9.str():
x=input("")
y=input("")
z = x + y
print("The concatenated result is :",str(z))



