# tuples? well there are another kind of sequence that are much more like a list they gives us the PAIR VALUES Of dictionarry in the form oflist

# tuples are almost same as lists but the diff is in the syntax
# ;ets see
x=('saeeda','sana','shazia')   # notice that i have used the round brackets

print(x)

# the index starts from 0

# the Tuples and strings both are IMMUTABLE
# but lists can be changed
# MEANS YOU CAN NOT ALTER THE CONTENTS
#FOR eg look below
t=('saeeda','shazia');
# t[0]='princess';
# print(t)  # you wil get an error


# TUPLES ARE MORE EFFICIENT
# since the python doesnot wants to build the structures for tuples to be modified they are more efficient in terms of memory use
# u can also place the tuples on the left hand  side in an assignment statements
# like
(x,y)=('4,2','saeeda,2');  # the first argument will go in to the x and rest to the y
print(x)

# ii have explained in previous file tthat the items() method return the list of values and keys which is basically a TUPLE


# OPERARTORS WITH TUPPLES
# THE THING WHICH WE CAN DO WITH TUPLES IS THAT WE CAN COMPARE THEM
z=(1,2,3)<(2,3,4)
print(z);

d=dict();
d={'money':1,'money':2}
print(d['money'])  # will print the largest one

#  you can also get the sorted order of the dictionary by doing this
d=dict();
d={'money':1,'bag':2,'shoes':3};
s0=sorted(d.items()); # this will sort acorrding to the key values
print(s0);
print(d) # while d will remain unchanhge


# yoou can also sort the tyuples by value by creating a list of the form (v,k);
# so
l=list();
for k,v in d.items():
    l.append((v,k));  # l here is the lost but each of the values in the list is the tuple

print(l)

# now we can sort it

print(sorted(l));
days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])
v=(1,2)
