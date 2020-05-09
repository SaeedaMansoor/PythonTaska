import re

# A regular expression as the name shows....are written in formal language that can be nterpreted by the
# regular expression processor.
# in case of rehular expressions instead of programming with lines with program or paly with the CHARACTERS
# before using the regular expressions you must import the library called th 'import re'

hand = open('mbox-short.txt');
for line in hand:
    if re.search('^F.+?:',line):
        z=re.findall('\S+@\S+',line);  #\s means non-blck character
        print(z)
# the double split pattern
#suppose
name='saeeda email iss saeedamansoor21@gmail.com';
w=name.split();
email=w[1];
print(email)




txt = "The rain in The TSpain"
x = re.search("^T", txt)
print(x)
for line in hand:
    line.rsplit();
    if re.search('^F',line):  #to check that whther the line begins from the F
        print(line)
print('********************************************')
# #to check that whteher the line starts with F and followed by many characters and:
# for line in hand:
#     line.rsplit();
#     if re.search('^F.*:',line):
#         print(line)

# iin order to find orextract the dasta we do
l="the 2 is 1 qaned 32";
x=re.findall('[0-9]+',l);  #here [0-9] means search for one or more digits
print(x)
z=re.findall('[t]+',l)  # this will find that is there any upper case viwels in the line
print(z)

print()
print()
print()
# the repeat characters + and * push outward in both dirextions to match the largest possible thing
m='From: using the: character';
y=re.findall('^F.+:',m)
print(y) # this will print the largest possible ting

print()
print()
print()
# in order to do the non-greedy matching we do
y=re.findall('^F.+?:',m)   # the ? here means non-greedy
print(y)

