#class Model:
#    def __init__(self):
#        self.dict1 = {}
#        pass
#
#    def add(self, name, price):
#        self.dict1[name] = price
'''The code was incomplete. It was difficult for me to understand the
Basics of MVC, but after a few readings online I learned what it is
supposed to be. I couldn't understand how to run a program from the
controller that's why my code didn't work.'''

'''This is the model for the expenses app we are making.'''
class Model:
    '''This class is the brain of the code. It deals with the basic
    functionality of the code.'''
    def __init__(self):
        # We initiate the class
        # we store all the data in the Dictionary
        self.dict1 = {}
        self.total1 = 0
        self.yearly = 0

    def add(self, name, price):
        '''We add elements to a dictionary'''
        self.dict1[name] = price

    def download(self, path):
        '''This helps download dictionary to the file.'''
        try:
            self.path = path
            res = open(self.path, 'w')
            for i,v in self.dict1.items():
                res.write(i+', $'+str(v)+'\n')
            res.write('Total monthly expenses:, $'+str(self.total1)+'\n')
            res.write('Total yearly expenses:, $'+str(self.yearly)+'\n')
            res.close()
            return 1
        except:
            return 0

    def delete(self, key):
        '''We delete elements from dictionary.'''
        del self.dict1[key]

    def total(self):
        '''This method calculates the total and saves it.'''
        self.total1 = sum(self.dict1.values())
        self.yearly = self.total1*12
        
        
            
