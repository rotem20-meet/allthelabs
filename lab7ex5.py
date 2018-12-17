class Person():
   def __init__(self, name, favorite_food ,age,color):
       self.name = name
       self.favorite_food = favorite_food
       self.age = age
       self.color=color

   def define_color(self, color):
       self.color = color

   def print_info(self):
       print("My name is " + self.name + ", I'm " + str(self.age) + " years old.")
       print("My favorite food is " + self.favorite_food + " and my favorite color is " + self.color)


a = Person("Britney", "Pizza", 16,"black")

a.print_info()

b = Person("Jake","kkkk", 15,"red")
b.print_info()

