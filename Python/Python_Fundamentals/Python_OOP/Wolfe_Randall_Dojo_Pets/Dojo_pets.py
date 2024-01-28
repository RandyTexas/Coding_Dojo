

class Pet:
    def __init__(self, name, pet_type, tricks, noise):
        self.name = name
        self.pet_type = pet_type
        self.tricks = tricks
        self.noise = noise
        self.health = 100
        self.energy = 50

    def sleep(self):
        # Increases the pet's energy by 25
        self.energy += 25
        return self

    def eat(self):
        # Increases the pet's energy by 5 and health by 10
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        # Increases the pet's health by 5
        self.health += 5
        return self

    def make_noise(self):
        # Prints out the pet's sound
        print(self.noise)


class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        # Walks the ninja's pet, invoking the pet's play() method
        self.pet.play()
        return self

    def feed(self):
        # Feeds the ninja's pet, invoking the pet's eat() method
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}")
            self.pet.eat()
        else:
            print("You need more pet food!")
        return self

    def bathe(self):
        # Cleans the ninja's pet, invoking the pet's make_noise() method
        self.pet.make_noise()
        return self

my_treat =["duck jerky", "dog food", "chiken"]
my_pet_food = ["dog food", "water", my_treat]

rocky = Pet("Rocky", "Dog", ["sit", "down", "hand", "come on"], "bark")
randy = Ninja("Randall","Wolfe",my_treat, my_pet_food, rocky)

randy.feed()

