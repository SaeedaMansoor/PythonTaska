# when ever we need to send the data from one python program across the network we dont call it as
# the python data is sent across the netwoork.
# the data sent across the network by agreeing on some format called the wire protocol.
# the one example of wire format is XML
# we agree on an itermediate protocol


#
# It's not internal memory. And the act of going from an internal representation on one computer out to a sort of interchange format is called serialization.


#And so, then the act of taking the data off of the wire and turning it into a new internal data structure, in the new environment, potentially in a very new language, is called de-serialization.


# types of  seterilization are

# 1-----------> XML
# 2-----------> json

# XML is Extensible Markedup lannguage


# Parsing the data in XML
# the ''' triple code means that the string is MULTILINE

import xml.etree.ElementTree as ET;
data='''<person>       
<name>Saeeda</name>
<phone type="int1">
03315236375
</phone>
<email hide="yes>Saeedamansoor21@gmail.com/>
</person>'''

tree=ET.fromstring(data);
# this line means that take the data from data above and return us a nice tree
# now we can say that from the xml data find me the tag name as belo
print('Name:',tree.find('name').text);
print('Phone No:',tree.find('phone').text);
print('ATTR:',tree.find('email').get('hide')); # thisemas that go into the tree and find an attribute called hide from the email