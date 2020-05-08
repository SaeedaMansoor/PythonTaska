# you can also convert the dictionary nto a list and can retrieve only keys from the dictionary


# tto convert the dictionary to a lsit
# lets make a dictionary first
d=dict();
d={'key1':1,'key2':2,'key3':3};    #make sure you use the CURLY BRACKETS IN CASE OF DICTIONARIES
# CONVERSION
lis=list(d);
print(lis);   # this will only fetch the keys notthe values because in this case the keys will be ttreated as the strings


# now in order to get only keys from the dictionary without converting iit to the string we do as below
z=d.keys();
print(z);

# now in order to get only the values we do
print(d.values());


# theere is an another method which gives us the KEY VALUES PAIRs WHICH IS item
# you will notice that we will get the list in return
# so
print(d.items()); # the square bracket in the output indicates the list
# the output of above is the 3 item list in which the each item is called TUPLE
