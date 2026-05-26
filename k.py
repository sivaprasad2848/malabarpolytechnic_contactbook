class student:
    name=None 
    age=0
    def __init__(self,n,a):
        self.name=n
        self.age=a 
    def display(self):
        print(self.name)
        print(self.age)
    def __del__(self):
        print("This is a simple destructor")