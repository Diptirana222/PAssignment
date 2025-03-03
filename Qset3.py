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
