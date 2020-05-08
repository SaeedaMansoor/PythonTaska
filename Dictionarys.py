# dictionary arelike the mini database with no ordered elements
# there are labels of elements in a dictionary
# the example of dictionary is just like a bag with unordered books
o=dict(); # o is an object of dictionary
o['money']=12;
o['price']=14;
o['number']=2;
# here money is the label and 12 is the element
# in short the label of 122 in dictionary is money
print(o);
# to  print something out we write or refer to it with the label assigned to it
# for example
print(o['money'])  # this will print the value
print(o['money']+2)  # this will add 2 to the value


print()
print()
print()
# you can make an empty dictionary by using the CURLY BRACKETS
# the format is
mydictionary={'label1':23,'label2':24}
print(mydictionary)


print()
print()
print()

# the GET method with dictiionary

# the get method is used to find the key and if it doesnot exists it returns back the DEFAULT VALUE like 0
# for example
d=dict();
d={'name':1,'class':23,'bag':26,'color':25};   # make sure you ise the CURLY {} brackets for the insertion
key='bob'
x=d.get('bob',0); # searching for the key bob in the dictionary and if it doesnt exist it will return the default value
print(x)

# now if we serach for the key that exists in the dictionary it will return the value
x=d.get('name',0);
print(x)


# in order to count the words
x=0;
count=dict();
line=input("enter the lines=");
sp=line.split();
for word in sp:
    count[word]=count.get(word,0)+1; # no of times words are present
    x=x+1; # total words
print(count);
print(x)

# let do thiis with the files
x=0;  # to read the words
count2=dict();
hand=open('romeo.txt');
for i in hand:
    sp=i.split();
    for words in sp:

        count2[words]=count2.get(i,0)+1;  # to get the occurence
        x=x+1;
print(count2);
print(x);