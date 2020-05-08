# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
#
d2=dict();
d=dict();
bigcout=None;
bigw=None;
name=input("enter the name of the file you wanna oopen=");
hand=open(name);
for line in hand:
    z=line.split();
    for word in z:
        if word.startswith('From:'):
            slice=z[1];
            #d={slice};
            d[slice]=d.get(slice,0)+1;  # adding into dictionaries
#print(d)
for word,count in d.items():

    if bigcout is None or count>bigcout:
        bigw=word;
        bigcout=count;


print(bigw,bigcout);
