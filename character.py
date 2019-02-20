
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
    
    def greet(self, someone):
        # if ( ) are used then it needs to have a , after. otherwise it will not run. no () = no ,

        return "Hello, %s, I am %s. I will destroy you." % (someone.name, self.name,)
