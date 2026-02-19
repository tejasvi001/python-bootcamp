from animal import Animal

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("I am swimming")