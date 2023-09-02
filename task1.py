class Animal():
    def __init__ (self, name, age, breed, color):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

    def __str__(self) -> str:
            return f'{self.name} {self.age} {self.breed} {self.color}'

class Dog(Animal):
    def __init__(self,
                 name: str,
                 age: int,
                 color: str,
                 breed: str,
                 command: str):
        super().__init__(name, age, breed, color)

        self.commnd = command



class Bird(Animal):
    def __init__(self,
                 name: str,
                 age: str,
                 breed: str,
                 color: str,
                 wing_size: float):
        super().__init__(name,age,breed,color)
        self.wing_size = wing_size
        
    def __str__(self) -> str:
        return f'{self.name} {self.age}'
        
class Horse(Animal):
    def __init__(self,
                 name: str,
                 age: str,
                 breed: str,
                 color: str,
                 type: str):
        super().__init__(name,age,breed,color)
        self.type = type


class Farm():
    def __init__(self):
        pass

    def create_animal():
        animal_choice = int(input('Выберите номер животного\n1 - Dog\n2 - Bird\n3 - Horse\n: '))
        if animal_choice == 1:
            animal = Dog('Бобик', 3, "спаниель", "черный", 'умеет подавать голос')
        if animal_choice == 2:
            animal = Bird('Кеша', 35, "попугай", "желтный", 3.5)
        if animal_choice == 3:
            animal = Horse('Ракета', 10, "мустанг", "белый", "скачки")
        if animal_choice <= 0 or animal_choice > 3: 
            print("нет такого животного")
        return animal

if __name__ == "__main__":
    a1 = Farm.create_animal()
    # a1 = create_animal()
    a2 = Farm.create_animal()
    print(a1)
    print(a2)