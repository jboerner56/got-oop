
# name
# avatar: 'profile picture'
# inventory

class Character():
    # called dunder init(double underscore followed by init followed by double underscore), this method is the constructor
    def __init__(self, new_name, new_avatar):
        # "self" is the customary way to refer to the instance being built
        # in some other languages, they use "this"
        self.name = new_name
        self.avatar = new_avatar
        self.inventory = []
    
    # someone=None is a default arguement
    # none is equivalent to 'null' in other languages
    def greet(self, someone=None):
        # if ( ) are used then it needs to have a , after. otherwise it will not run. no () = no ,
        # if there is a value for 'someone'
        # when we assume that 'someone' has a .name property
        # this is an Object Oriented Programming principle 'polymorphism.
        # in python, its called "Duck Typing"
        if someone:
            return "Hello, %s, I am %s. I will destroy you." % (someone.name, self.name,)
        else:
            return "Hello, I am %s. I will destroy you" % (self.name)

# Hero is a kind of Character
# Hero is a subclass of Character
# Hero inherits from Character
# Charater is the superclass of Hero
class Hero(Character):
    pass

# creates monster class
class Monster(Character):
    def greet(self, someone=None):
        if someone:
            return "Hello, %s I am %s. You may want to run away" % (someone.name, self.name,)    