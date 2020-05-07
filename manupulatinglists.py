list=[];
list.append('saeeda')
list.append('sana')
print(list)
z='saeeda' in list;
print(z)


# split function

# 1. the first thing about split is that it dpoesnot look for spaces
# the split is done on the basis of the space between thee woords


# you can do double split on the basis of the certain chrataer
list="i am saeeda and my email address is saeedamansoor21@gmail.com"
z=list.split();
print(z)

# using double split or on the basis of crtain thing
email=z[8]
z=email.split('@');
print(z)

r=z.remove('saeedamansoor21')
print(r)

friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends[0])