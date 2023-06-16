import random

colours = ["black", "white", "silver", "golden", "light brown", "dark brown"]
hair_length = ["short", "medium length", "long", "curly"]
character = [
    "friendly",
    "grumpy",
    "loyal",
    "evil",
    "cuddly",
    "curious",
    "silly",
    "clever",
    "funny",
]


class Pet:
    def __init__(self, species, name):
        self.name = name
        self.species = species
        self.character = random.choice(character)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        assert 3 <= len(new_name) <= 30, "Name must be between 3 and 30 letters long."
        self._name = new_name

    @classmethod
    def create_pet(cls, choice, name):
        return cls(choice, name)

    def speak(self):
        if self.name.lower() == "fox":
            print(f"'What does the fox say?'")
        else:
            print(f"'What does the {self.breed} say?'")

    def pet_pet(self):
        print(f"You pet {self.name}. They make a happy noise.")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.species}, {self.name})"

    def __str__(self):
        return f"{self.name}, a {self.character} {self.breed}"


class Dog(Pet):
    dogs = [
        "mutt",
        "setter",
        "mastiff",
        "collie",
        "grayhound",
        "terrier",
        "bloodhound",
        "lapdog",
    ]

    def __init__(self, species, name):
        super().__init__(species, name)
        self.breed = random.choice(Dog.dogs)
        self.fur = random.choice(hair_length)
        self.colour = random.choice(colours)
        self.adoption_message = f"Congratulation! {self.name} is a {self.character} {self.breed} with {self.fur}, {self.colour} coloured fur."

    def speak(self):
        print("Bark!")


class Cat(Pet):
    def __init__(self, species, name):
        super().__init__(species, name)
        self.fur = random.choice(hair_length)
        self.colour = random.choice(colours)
        self.adoption_message = f"Congratulation! {self.name} is a {self.character} {self.species} with {self.fur}, {self.colour} coloured fur."

    def speak(self):
        print("Meow!")

    def __str__(self):
        return f"{self.name}, a {self.character} cat"


class Rodent(Pet):
    rodents = ["rat", "mouse", "bunny", "hamster", "guinea pig"]

    def __init__(self, species, name):
        super().__init__(species, name)
        self.breed = random.choice(Rodent.rodents)
        self.colour = random.choice(colours)
        self.adoption_message = f"Congratulation! {self.name} is a {self.colour} coloured {self.character} {self.breed}."

    def speak(self):
        print("Squeek!")


class Reptile(Pet):
    reptiles = ["snake", "tortoise", "iguana", "gecko"]

    def __init__(self, species, name):
        super().__init__(species, name)
        self.breed = random.choice(Reptile.reptiles)
        self.adoption_message = (
            f"Congratulation! {self.name} is a {self.character} {self.breed}."
        )


class Exotic(Pet):
    exotics = ["frog", "fish", "ferret", "tarantula"]

    def __init__(self, species, name):
        super().__init__(species, name)
        self.breed = random.choice(Exotic.exotics)
        self.colour = random.choice(colours)
        self.adoption_message = f"Congratulation! {self.name} is a {self.colour} coloured {self.character} {self.breed}."


class Bird(Pet):
    birds = ["parrot", "budgie", "cockatiel", "macaw", "canary"]

    def __init__(self, species, name):
        super().__init__(species, name)
        self.breed = random.choice(Bird.birds)
        self.adoption_message = f"Congratulation! {self.name} is a colourful, {self.character} {self.breed}."

    def speak(self):
        print("SQUAAAK!")
