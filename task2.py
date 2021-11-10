l = ['example', 3, 78]
k = {'school':'teacher', 'food':'apple', 'test_0101':'passed'}
set('lgklkg')
l[1]

g=9
if g == 5:
    print('winner')
elif g == 7:
    print('almost')
elif g == 6:
    print('not yet')
else:
    print('loser')

while h > 3:
    h = h - 1
    if h % 4:
        continue
    result = id(h)
    if result:
        print('break')
        break
else:
    print('very bad')


for t in range(5,10,2):
    print(t)

for w in range(6):
    print(w)

q = 'test'
if 'e' in q:
    print('pass')
else:
    print('not pass')

for text in open(example.txt):
    print(text.strip())

def function(a, b):
    return a+b

print(function(5, 7))

def any_function(*a):
    return a
print(any_function(1, 4, 5, 6))