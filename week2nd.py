print('Hi Guys!')

a = 10
c = 3
print(a)
print('#########')
print(a + c)
print(a / c)
print(a * c)
print(a // c)
print(a % c)

mylist = list()
mylist2 = []
mylist3 = [1, 2, 3, 4]
mylist4 = ['abc', 3, ['def', 4]]
mylist5 = ['1', 'w', '2', 'e']

mylists = [mylist, mylist2, mylist3, mylist4]

for li in mylists:
    print(li[:2])

mylist.append('plz help me')
print(mylist.pop())
print(mylist)

mylist3.reverse()
print(mylist3)

mylist3.sort()
print(mylist3)

tmp_str = "!".join(mylist5)
print(tmp_str)

print(tmp_str.replace('1', '5'))

mydict = {1: 'hello'}
mydict1 = dict()
mydict2 = {'가': 1, '나': '두번째', '다': [1, 2, 3]}

alldict = [mydict, mydict1, mydict2]

for ad in alldict:
    if ad.get([]) is not None:
        print(ad)

print(mydict2.items())
