#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
#
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_522423.xml (Sum ends with 76)
# You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

import xml.etree.ElementTree as ET;
import urllib.parse,urllib.request,urllib.error
from bs4 import BeautifulSoup;
url=input('enter the url');
html=urllib.request.urlopen(url).read(); # here read menas that it will read all the data but not in the for loop
soup=BeautifulSoup(html,'html.parser');  # this soup object will ask diff questionns
s=soup('count');
c=0
for i in s:
    z=int(i.get_text());
    c=c+z;
    print(z)
print(c)