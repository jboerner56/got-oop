# not real tests
from character import Character
# characters can be instantiated with name and avatar
arya = Character("Arya Stark", "arya.png")
jon = Character("Jon Snow", "jon.pgn")

print(arya.name, arya.avatar)
print(jon.name, jon.avatar)

# after adding 2 items to inventory, inventory length should = 2
arya.inventory.append('sword')
arya.inventory.append('mask')

print(len(arya.inventory))

# arya should have a 'greet' method
# when i call with arya.greet(jon) it should return "hello, jon snow, i am arya stark, i will destroy you."
print(arya.greet(jon))