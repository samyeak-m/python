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

Mountain =['Sagarmatha','Annapurna','Manaslu','Dhaulagiri','Makalu']
print(Mountain)
print(type(Mountain))
print(len(Mountain))

print(Mountain[2:])
print(Mountain[0:3])
print(Mountain[-1])
print(Mountain[-1:-3])
print(Mountain[:])

Mountain.append('Kanchanjunga')
print(Mountain)

Mountain.pop(2)
print(Mountain)

Mountain.sort()
print(Mountain)

Mountain.reverse()
print(Mountain)

Barcelona = ['Messi','Neymar','Suarez']
print(Barcelona)
# Barcelona.pop(1)
PSG=['messi','neymar','mbappe']
print(PSG)

matrix=[Barcelona,PSG]
print(matrix)
print(matrix[1])
print(matrix[0])
print(matrix[1][2])

city=['ktm','pkr','npj','dhr']
dist=['ktm','kaski','banke','unknown']
test=[city,dist]
print(test[1][3])

list1=['one','two','three','four']
print(list1)
print(list1[:])
print(list1[1:])
print(list1[:-2])
print(len(list1))
list1.append('messi')
print(list1)

list1.pop()
print(list1)

list1.sort()
print(list1)

list2=[1,5,3,8,0]
list2.sort()
print(list2)
list2.reverse()
print(list2)

BARCELONA=['messi','Neymar','Suarez','Ter Stegen']
print('messi'in BARCELONA)
print('neymar'not in BARCELONA)
print('Neymar'not in BARCELONA)
print('Torres' not in BARCELONA)
print('Argentina' in BARCELONA)

place=('nepalgunj','pyuthan','bardiya','jomsom')
print(type(place))
print(place)
print(place[0])
print(place.index('pyuthan'))
print(place.count('nepalgunj'))
# place.append('kathmandu')
aayan=('sushant',"aayan","me")
print(type(aayan))
print(len(aayan))
print(aayan[-1])
print(aayan.count('me'))
print(aayan.index('me'))

for x in aayan:
    print(x,end=" ")

if "me" in aayan:
    print('yes')
else:
    print('no')

# while(0):
#     if "me" in aayan:
#         print('yes')
#     else:
#         print('no')