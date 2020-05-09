#import expensesmodel as em

#class Control:
#    '''This class acts as an intermidiary between view and model.'''
#    def __init__(self):
#        # We initiatethis class
#        self.x = em.Model()
#
#    def add(self,name,price):
#        # This method calls the model to add name and price to a dictionary
#        u = self.x.add(name,price)
#        
#    def print(self):
#       # This method returns the dict froom the model
#        return self.x.dict1'''
'''The code was incomplete. It was difficult for me to understand the
Basics of MVC, but after a few readings online I learned what it is
supposed to be. I couldn't understand how to run a program from the
controller that's why my code didn't work.'''

'''This is the controller for the expenses sheet.'''
import expensesmodel as em
import expensesview as ev

class Control:
    '''This class acts as an intermidiary between view and model.'''
    def __init__(self):
        # We initiate this class
        self.x = em.Model()
        self.y = ev.SheetView()

    def add(self,name,price):
        '''This method calls the model to add name and price to a
        dictionary'''
        u = self.x.add(name,price)
        
    def print(self,h):
        '''This method returns the dict from the model'''
        self.x.total()
        # Then it commands the view to print it out
        self.y.printout(h, self.x.total1, self.x.yearly)

    def delete(self, h):
        '''This method deletes the key in the dictionary.'''
        # calls the method in the view to get input
        self.y.delete(h)
        g = self.y.name4
        # then deletes it in the model
        self.x.delete(g)

    def download(self, path):
        '''This method downloads the expenses to a csv file.'''
        self.x.total()
        # We call the method in the model to save info to a file.
        myret = self.x.download(path)
        print(myret)
        q = path
        print(q)
        if myret == 0 and q!= 0:
            self.y.errorm()
            self.y.myrun()
            self.y.download()
            q = self.y.acpath
            self.download(q)

    def run(self):
        '''This method handles the basic running of the program.'''
        self.y.myrun()
        self.y.buttons()
        while self.y.counter != 0:
            # This deals with the addition of expenses
            if self.y.counter == 1:
                try:
                    name = self.y.name2
                    price = self.y.price2
                    self.add(name,price)
                    self.y.myrun()
                    self.y.buttons()
                except:
                    exit()
            # This deals with the printing out
            elif self.y.counter == 2:
                try:
                    self.print(self.x.dict1)
                    self.y.myrun()
                    self.y.buttons()
                except:
                    exit()
            # This deals with the downloading
            elif self.y.counter == 3:
                try:
                    path = self.y.acpath
                    self.download(path)
                    self.y.myrun()
                    self.y.buttons()
                except:
                    exit()
            # This deals with the deleting expenses
            elif self.y.counter == 4:
                try:
                    self.delete(self.x.dict1)
                    self.y.myrun()
                    self.y.buttons()
                except:
                    exit()


if __name__ == '__main__':
    t = Control()
    # We call the run function to run the program
    t.run()
