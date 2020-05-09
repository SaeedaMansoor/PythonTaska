import re;
# the double split pattern
#suppose
name='saeeda email iss saeedamansoor21@gmail.com';
w=name.split();
email=w[3];
sp=email.split('@');

slice=sp[1];
print(slice)

# you can do the above thing with the help of the regular expressions like
z=re.findall('@([^ ]*)',name)  # means start searching from @ but dont include it
print(z)

# ESCAPE CHARACTER
#  now if you want to includde the special  character and wants it  to behave normally you will ou the backslash character
#'\$' ettc