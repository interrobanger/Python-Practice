class Cat:
    def __init__(self, color, age, weight, name, gender):
        self.color = color
        self.age = age
        self.weight = weight
        self.name = name
        self.gender = gender
    def print_info(self):
        if self.gender == 'male':
            print(f'{self.name} is a {self.color} cat. He is {self.age} years old and weighs {self.weight} lbs.')
        else:
            print(f'{self.name} is a {self.color} cat. She is {self.age} years old and weighs {self.weight} lbs.')

Gibson = Cat('black-gray-white-orange', 12, 12, "Gibson", "male")
Kitten = Cat('orange-white',7,15,'Kitten', 'male')
Tele = Cat('gray-white-orange', 11, 11, 'Tele', 'female')

Gibson.print_info()
Tele.print_info()
Kitten.print_info()
