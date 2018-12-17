class Bear():
    def __init__(self, name):
        self.name=name

    def say_hi(self):
        print("Hi! Im a bear. My name is " + self.name)
my_bear = Bear("Danny")
my_bear.say_hi()


