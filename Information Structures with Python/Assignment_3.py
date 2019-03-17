""" Pet is the base class """


class Pet:

    # Create two variables kind and color; assign values
    KIND = 'frog'
    COLOR = 'golden rust'

    def __init__(self, name):
        #  the constructor, initialize the pets name
        self.name = name

    def speak(self):
        if self.KIND == 'canine':
            return self.name + ' says Woof.'
        elif Pet.KIND == 'feline':
            return self.name + ' says Purr.'
        else:
            return NotImplementedError

    def jump(self):
        pass

    def do_tricks(self):

        # Call the speak method and the jump method
        self.speak()
        # Call the jump method
        self.jump()
        # Print the name of the pet and that it is doing tricks
        return self.name + ' is doing tricks.'


class Jumper:
    # This is a mixin class for jump

    def jump(self):
            # Create jump method that prints that a Pet is jumping and the pets name
            return self.name + ' is jumping.'


class Dog(Jumper, Pet):  # You will need to inherit for this to work

    # Change kind to canine
    KIND = 'canine'

    def __str__(self):
        # Print the name and description of dog
        return '\n' + 'I am a dog named ' + self.name + '.'

    def __call__(self, action):
        # self.action = action
        # Rollover action prints the name of the dog and that it is rolling over
        if action == 'rollover':
            return self.name + ' is rolling over.'
        elif action == 'owner':
            return 'Adam is my owner.'
        # Owner action returns the name of the owner


class BigDog(Dog):  # You will need to inherit for this to work

    # Change the color to tan
    COLOR = 'tan'

    def __str__(self):
        # Print the name and description of BigDog
        return '\n' + self.name + ' is a big, strong dog.'

    def speak(self):
        # Print dogs name and what it says
        return self.name + ' says WOOF!'


class SmallDog(Dog):  # You will need to inherit for this to work

    # Change the color to brindle
    COLOR = 'brindle'

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        # Print the name and description of SmallDog
        return '\n' + self.name + ' is a tiny, cute dog.'

    def speak(self):
        # Print dogs name and what it says
        return self.name + ' says yap.'


class Cat(Jumper, Pet):  # You will need to inherit for this to work

    # Change the kind to feline
    KIND = 'feline'

    def __str__(self):
        # Print the name and description of cat
        return '\n' + 'I am a ' + Cat.KIND + ' named ' + self.name + '.'

    def speak(self):
        # Print cats name and what it says
        return self.name + ' says purr.'

    def climb(self):
        # Prints the name of the cat and that it is climbing
        return self.name + ' is climbing the tree.'


class HouseCat(Cat):  # You will need to inherit for this to work
    KIND = 'feline'
    COLOR = 'white'

    def __init__(self, name):
        super().__init__(name)
        # Change the color to white
        Pet.COLOR = 'white'

    def __str__(self):
        # Print the name and description of cat
        return '\n' + self.name + ' is a cat with fluffy, ' + HouseCat.COLOR + ' fur.'

    def speak(self):
        # Print cats name and what it says
        return self.name + ' says meow.'




# ###########################################
#
#
# # EXERCISE YOUR CODE
#
#
# #    1. Instantiate each class(except jumper)
pet = Pet('Taz')
jersey = Dog('Jersey')
benny = BigDog('Benny')
tico = SmallDog('Tico')
tom = Cat('Tom')
walter = HouseCat('Walter')

# #    2. Create a list of the instantiated objects
inst_objects = [pet, jersey, benny, tico, tom, walter]
#
# #    3. Loop through the objects
for item in inst_objects:

    # 4. Print __str__
    print(item)
    # 5. print the kind of pet
    print(item.KIND)

    # print(item('owner'))



    #6. Print the Color of the pet
    print(item.COLOR)

    # 7. Have the pet do tricks
    print(item.do_tricks())
    print(item.speak())
    print(item.jump())

    # 8. if applicable, print rollover action and the owners name
    if item.KIND == 'canine':
        print(item('rollover'))
    else:
        pass

    if item.KIND == 'canine':
        print(item('owner'))
    else:
        pass

# #    9. If applicable, have the pet climb
    if item.KIND == 'feline':
        print(item.climb())
    else:
        pass

# #   10. To separate each pet print underscores
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
