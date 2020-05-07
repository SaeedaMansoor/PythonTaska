print("Hello this is my first code");


s='123'
print(type(s));
sq=int(s);
print(type(sq))
f=str(s);
print(f)
print(type(f));

astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1
print(istr)





hrs=int(input("enter hours"));
rph=float(input("enter rate per hours="));
ex=0;
pay=0;
if hrs >40:
    ex=ex+hrs-40;
    s=(hrs-ex)*rph;

    s2=ex*1.5*rph
    pay=pay+s2+s;


else:
    pay=hrs*rph;
print(pay);




score = float(input("Enter Score: "));
if score>=0.0 and score<=1.0:
    if score >=0.9:
        print("A");
    elif score>=0.8:
        print("B");
    elif score>=0.7:
        print("C");
    elif score>= 0.6:
        print("D");
    elif score < 0.6:
        print("F");

else:
    print("error");