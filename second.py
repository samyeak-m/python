x=7
y=9
z=11

print(x<y or x>z)
print(x<y or x<z)
print(x<y and x>z)
print(x<y and x<z)
print(x>y and x<z)
print(x<y and x>z)
print(not(x<y and x>z))

z=x+y
print(z)
print(x+y)
# print(x,y)

d = x/y
print(d)
print(x/y)

m =x*y
print(m)
print(x*y)

s = x-y
print(s)
print(x-y)

r = x%y
print(r)
print(x%y)

p = x**y
print(p)
print(x**y)

f = x//y
print(f)
print(x//y)

a=input("enter a character:")
c=len(a)
print(c)
if c%2==0:
    print("the character",a,"has even number of letters")
else:
    print("the character",a,"has odd number of letters")

vowel = input("enter a character:").lower()
if vowel=="a" or vowel=="a" or vowel=="e" or vowel=="i" or vowel=="o" or vowel=="u":
    print("the character",vowel,"is a vowel")
else:
    print("the character",vowel,"is not a vowel")

