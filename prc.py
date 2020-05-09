a=[];
l=[];
while True:
    i=input("enter a number=");
    try:
        if i=='done':
            break;
        else:
            a.append(int(i));
    except:
        print('invalid number');
large=-1;
small=None;
for i in a:
    smalli=i;
    if large<i:
        large=i;
    if small is  None:
        small=i;
    elif i<small:
        small=i;
print(large,small)

