class mathematics:

    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def addition(self):
        return self.first_num + self.second_num
    

class Physics(mathematics):

    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def addition(self):
        return self.first_num * self.second_num
    

mathIns = mathematics(2, 3)
print(mathIns.addition())

physicsIns = Physics(2, 3)
print(physicsIns.addition())