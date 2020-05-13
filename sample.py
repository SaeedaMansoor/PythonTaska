import urllib.parse,urllib.request,urllib.error
from bs4 import BeautifulSoup;
url=input('enter the url');
html=urllib.request.urlopen(url).read(); # here read menas that it will read all the data but not in the for loop
soup=BeautifulSoup(html,'html.parser');
s=soup('a');
c=1;
for e in s:

    z=e.get('href',None);
    if c==18:
        break;
    else:
        print(z)

    c=c+1;
print('firt time -------------------------------')
print(z)

#2nd==============================
url=z
html=urllib.request.urlopen(url).read(); # here read menas that it will read all the data but not in the for loop
soup=BeautifulSoup(html,'html.parser');
s=soup('a');
c=1;
for e in s:

    z2=e.get('href',None);
    if c==18:
        break;
    else:
        print(z2)

    c=c+1;
print('2nd time -------------------------------')
print(z2)



#3rd============================================================================================
url=z2;
html=urllib.request.urlopen(url).read(); # here read menas that it will read all the data but not in the for loop
soup=BeautifulSoup(html,'html.parser');
s=soup('a');
c=1;
for e in s:

    z3=e.get('href',None);
    if c==18:
        break;
    else:
        print(z3)

    c=c+1;
print('3rd time -------------------------------')
print(z3)

#4t================================================================================================
url=z3;
html=urllib.request.urlopen(url).read(); # here read menas that it will read all the data but not in the for loop
soup=BeautifulSoup(html,'html.parser');
s=soup('a');
c=1;
for e in s:

    z4=e.get('href',None);
    if c==18:
        break;
    else:
        print(z4)

    c=c+1;
print('4th time -------------------------------')
print(z4)

#5th===================================================================================================
url=z4;
html=urllib.request.urlopen(url).read(); # here read menas that it will read all the data but not in the for loop
soup=BeautifulSoup(html,'html.parser');
s=soup('a');
c=1;
for e in s:

    z5=e.get('href',None);
    if c==18:
        break;
    else:
        print(z5)

    c=c+1;
print('5th time -------------------------------')
print(z5)

#6th==================================================================================================
url=z5;
html=urllib.request.urlopen(url).read(); # here read menas that it will read all the data but not in the for loop
soup=BeautifulSoup(html,'html.parser');
s=soup('a');
c=1;
for e in s:

    z6=e.get('href',None);
    if c==18:
        break;
    else:
        print(z)

    c=c+1;
print('6th time -------------------------------')
print(z6)

#7th=================================================================================================
url=z6;
html=urllib.request.urlopen(url).read(); # here read menas that it will read all the data but not in the for loop
soup=BeautifulSoup(html,'html.parser');
s=soup('a');
c=1;
for e in s:

    z7=e.get('href',None);
    if c==18:
        break;
    else:
        print(z7)

    c=c+1;
print('7th time -------------------------------')
print(z7)

