# a class is basically a template
#an object at the time of creation is called "CONSTRUCTOR"
# AND object at the time of destruction is called the "DESTRUCTOR"
# the methood inside the class perform somes tasks
# the attributes are basically the data inside the object
class PartyAnimal:
    x=0;
    def __init__(self):   # constructor
        print("i am a constructor");
    def partAnimal(self):  # method
        self.x=self.x+1;
        print("self is",self.x);
    def __del__(self):  #destructor
        print("i am destructor",self.x)

an=PartyAnimal(); # constructor is created
an.partAnimal()
an.partAnimal()
x=23; #destructor 
print(x);