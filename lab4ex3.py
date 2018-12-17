class person():
    def __init__(self,name,city,gender,breakfest):
        self.name=name
        self.city=city
        self.gender=gender
        self.breakfest=breakfest
    def breakfest(self,breakfest):
        self.breakfest=breakfest

rotem= person("rotem","shimshit","male","meal")


print(rotem.name)
print(rotem.gender)
print(rotem.breakfest)
           

           
