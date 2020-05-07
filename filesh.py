
h=open('saeeda.txt','r')
print(h)
z=0;
o=open('saeeda.txt');
count=0;
for i in o:
    print(i)
    count=count+1;
    z=z+len(i);

print("the number of lines are",count)
print("the total words are",z)
words=h.read();
print(len(words))