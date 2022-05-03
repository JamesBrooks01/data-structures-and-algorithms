from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.cat_Q = Queue()
        self.dog_Q = Queue()

    def enqueue(self, animal):
        if animal.type == "Dog":
            self.dog_Q.enqueue(animal)

        if animal.type == "Cat":
            self.cat_Q.enqueue(animal)

    def dequeue(self, animal):
        if animal == "dog":
            return self.dog_Q.dequeue()

        elif animal == "cat":
            return self.cat_Q.dequeue()

        else:
            return None


class Dog:
    def __init__(self):
        self.type = "Dog"


class Cat:
    def __init__(self):
        self.type = "Cat"
