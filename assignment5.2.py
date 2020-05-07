a=[];
while True:
    s=input("");
    if s=='done':
        break;
    else:
        try:
            a.append(int(s));
            continue;
        except :
            print('Invalid input')
print('Maximum is ',max(a));
print('Minimum is ',min(a));