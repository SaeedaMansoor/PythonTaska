# function to add a number
def addi(x,y):

    x=x+x;
    y=y+y;
    print(x);
    print(y);



addi(2,3);

def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)


#hour=int(input("enter the hourly rate"));
#rph=float(input("enter rate per hour"));

def computepay(hour,rph):
    if hour>40:
        ex=hour-40;
        s1=ex*1.5*rph;
        s2=(hour-ex)*rph;
        pay=s1+s2;
        return pay
    else:
        pay=hour*rph;
        return pay

h=int(input("enter hour"));
r=float(input(("enter rate")))
print("Pay ",computepay(h,r))


while True:
    s=int(input([]));
    if 
