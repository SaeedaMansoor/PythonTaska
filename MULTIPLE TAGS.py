import xml.etree.ElementTree as ET;
data= '''
<person>
    <users>
        <user x="2">
            <id>201</id>
            <name>Saeeda</name>
        </user>
        <user x="7">
            <id>102</id>
            <name>Shazia</name>
        </user>
    </users>
 </persons>''';
tree=ET.fromstring(data);
# this line means that take the data from data above and return us a nice tree
l=tree.findall('users/user'); # this mean find all the tag of user under the tag USERS
for t in l:
    print('ID:',t.find('id').text);
    print('Name:',t.find('name').text);