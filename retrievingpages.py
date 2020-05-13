# all the things we have done in the previous task in socket etc
# all the things we have done while dealing wid the socket can be reducd to few lines by using few lines an imporrting the ibarary called
#  urllib
import urllib.parse,urllib.request,urllib.error;
mysocke=urllib.request.urlopen('http://data.pr4e.org/romeo.txt');
for line in mysocke:
    print(line.decode().strip());  # now it will skip the headers and will simply print the data

# you can also count the words in a file using this code
count=dict();
for l in  mysocke:
    w=l.decode().split();
    for e in w:
        count[e]=count.get(e,0)+1
print(count)