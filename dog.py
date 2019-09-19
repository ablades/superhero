class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")


if __name__ == "__main__":
    my_dog = Dog("Rex", "SuperDog")
    print(my_dog)
    print(my_dog.name) 
    print(my_dog.breed)
    my_dog.bark()