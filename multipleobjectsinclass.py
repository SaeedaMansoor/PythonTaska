# we can have the multiple objects in the class
# each object will have its own cpopy of instance
class PartyAnimal:
    x=0;
    name=""
    def __init__(self,z):
        self.name=z;
        print("i am constructor",self.name);
    def party(self):
        print("i am a function",self.name);
    def __del__(self,z):
        self.name=z;
        print("ii am destrcution",self.name)
a1=PartyAnimal("SAEDA");
a1.party();
s=2;
a2=PartyAnimal("shazia");
a2.party();
print(s)