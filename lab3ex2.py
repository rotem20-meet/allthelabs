class animal():
    def __init__(self,sex,sound,gender,habitat):
        self.sex=sex
        self.sound=sound
        self.gender=gender
        self.habitat=habitat
        
    def make_sound(self):
        print(self.sound+self.sound+self.sound)
    
##rotem= animal("dog","hoooooo","male")
##rotem.make_sound()
##rotem.sound="nininin"
##rotem.make_sound() 


pincky = animal('dinosaur', 'rrrrrrrrrrr', 'male', False)

print(pincky.habitat)

