class song():
    def __init__(self,lyrics):
        
        self.lyrics=lyrics
        
    def make_sound(self):
        for line in self.lyrics:
            print(line)
            #           print("i like this lyrics soo muchhhh")
    
##rotem= animal("dog","hoooooo","male")
##rotem.make_sound()
##rotem.sound="nininin"
##rotem.make_sound() 

list1=["a","b","c"]
eeee=song(list1)
eeee.make_sound()

