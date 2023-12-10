player={'first_name':'lion1','last_name':'messi','age':'35',"height":5.7}
print(player.keys());
print(player.values());
print(player['first_name'])
print(player['last_name'])

player={'first_name':'lion1','last_name':'messi','age':'35',"height":5.7,'associates':['Arg','Braz','Col']}
print(player['associates']);
print(player['associates'][0]);
print(player['associates'][-1]);
print(player['associates'][-2]);

d={}
print(type(d))
d['name']='Samyak'
d['age']=22
print(d)

print(player.keys())
print(player.values())
print(player.items())

test={'key1':{'nestkey':{'subnestkey':'hello'}}}
print(test['key1']['nestkey']['subnestkey'])
print(test['key1']['nestkey'])
print(test['key1'])
print(test.values())
player['award']=235
print(player)

messi={"sushant":"kunwar","ayan":"jindal","aryan":"agarwal"}
print(type(messi))
print(messi["sushant"])
dict2={

    "prabhat":"kc",
    "sushant":"kunwar",
    "aayan":"jindal",
    "players":['messi','suarez','neymar']

}

print(dict2)
print(dict2['players'])
print(dict2['players'][0])

dict={}
print(dict)
print(type(dict))
dict['sushant']='kunwar'
dict['aayan']='jindal'
print(dict)

mydictionary={"hi":{'k xa':{'sushant ?':'thikai xa'}},'howdy':'no response'}
print(mydictionary)

if 'aayan' in mydictionary:
    print('yes')
else:
    print('no')

for x in mydictionary:
    print(x)

set1={'hello','namaste','lhaso'}
print(type(set1))
print(set1)

set2=set(["katmandu","sahara","herdaa","laagxa","rahara"])
print(set2)

# set2.add(["sorry","dhulai","dhulaiko","sahara"])
set2.add("jhuto_bolyaa")
print(set2)

set3={"noobs","always","noobs"}

print(set3)

player={"subash","santosh","karan"}
film={"Karan","Arjun"}
man={"Dipesh","Ram"}

aswell=player.union(film)

print("Union using union() function")
print(aswell)

aswell=player|film

print("Union using | operator")
print(player)
print(aswell)
