#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.





s=[];
z=[];
l=0;
name=input("enter the name of the file you wana open");
hand=open(name);
for i in hand:

    z=i.split();
    for e in z:

         if e in s:
             continue;
         else:
          s.append(e);

print(sorted(s))


