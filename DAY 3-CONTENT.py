

s.add()
s.update()
s.discard()
s.remove()- throws eroor if ele is not present


//
s={1,2,2,4,9,6,2}
len(s)
5
s.add(90)
s
{1, 2, 4, 6, 9, 90}
s.update([99,90])
s
{1, 2, 99, 4, 6, 9, 90}
s.discard(1)
s
{2, 99, 4, 6, 9, 90}
s.discard(10)
s
{2, 99, 4, 6, 9, 90}
s.remove(10)
//

s1|s2 
s1.union(s2)

s1$s2
s1.intersection(s2)

s1-s2
s1.difference(s2)

//
s1={1,2,3}
s2={1,4,5,6}
s1|s2
{1, 2, 3, 4, 5, 6}
s1&s2
{1}
s1-s2
{2, 3}
s2-s1
{4, 5, 6}
//

superset
// 
s1.issuperset(s2)
False
//

symmetric-
s1={1,2,3,4,5,10}
s2={4,1,9,2,10}
s1^s2
{3, 5, 9}
print(s1.symmetric_difference(s2))
{3, 5, 9}



TUPLE
ordered
()
count and index operations

//
t=(4,3,4,9.6,"ice cream")
type(t)
<class 'tuple'>
t.count(4)
2
t.index(4)
0
t.index(9.6)
3
//

DICTIONARY
key and value occur in pairs
key is unique

//
type(d)
<class 'dict'>
d.keys()
dict_keys([1, 2])
d.values()
dict_values(['one', 'two'])
d.items()
dict_items([(1, 'one'), (2, 'two')])


d={'a':'dog','b':'cat'}
d.keys()
dict_keys(['a', 'b'])
d.values()
dict_values(['dog', 'cat'])
d.get('a')
'dog'

operations

d.items()
d.update()
d.pop()
d.popitem()-removes the last added value
d.setdefault(key:value)


