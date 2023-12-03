print("hello")
first_name="Samyak"
last_name="Maharjan"
print(first_name)
print(last_name)
print(first_name,last_name)
print(first_name+last_name)

x = str(3) #'3'
y = int(3) #3
z = float(3) #3.0

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

text1 = "How are you?"
text2 = 4
text3 = float(text2)
print(text2)
print(text3)
print(type(text1))
print(str(text2))

print(complex(text2))

# text4 = "Hello World" + text2
# print(text4)

text5 = "Hello World {}"
print(text5.format(text2))

text6 = "Hello World " + str(text2)
print(text6)

text7 = "Hello World {1} {0}"
print(text7.format(text3, text6))

age=int (input("Enter your age: "))
name=str(input("Enter your name: "))

print(type(age))

output="Your name is {0} and your age is {1}."
print(output.format(name,age))

a="a"
print(name.count(a))