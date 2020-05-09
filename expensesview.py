#'''This is the view for the expenses sheet.'''
# We import tkinter
#from tkinter import *
#import econtroller

#class SheetView:

#    def __init__(self):
#        '''We create a window with options for the user.'''
#        self.x = econtroller.Control()
#        #self.x = econtroller.Control()
#        self.DEFAULT_F = ('Comicsans', 20)
#        self.window = Tk()
#        title = self.window.title('EXPENSES')
#        # We add the add button
#        self.buttons()
#    def buttons(self):
#        '''This method adds buttons to the window.'''
#        button_add = Button(self.window, text='Add Expense',
#                            font = self.DEFAULT_F,
#                            command =self.add)
#        button_add.pack()
#        # We add the print button
#        button_print = Button(self.window, text='Print monthly or yearly'
#                              ' budget.', font = self.DEFAULT_F,
#                              command =self.printout)
#        button_print.pack()
#        # We add the download button
#        button_down = Button(self.window, text='Download monthly or yearly'
#                             ' budget.', font = self.DEFAULT_F,
#                             command =self.download)
#        button_down.pack()
#        self.window.mainloop()

#    def add(self):
#        '''This function helps add expenses to a list.'''
#        
#        self.root = Tk()
#        label1 = Label(self.root, text='Add name and price of '
#                       'your expense.', font = self.DEFAULT_F)
#        label1.pack()
#        # we create entry to take user input
#        name1 = Entry(self.root, width = 60, font=self.DEFAULT_F)
#        name1.pack()
#        price1 = Entry(self.root, width= 60, font=self.DEFAULT_F)
#        price1.pack()
#        button_work = Button(self.root, text='Submit',
#                             font=self.DEFAULT_F,
#                             command=self.x.add(name1,price1))

#    def printout(self):
#        '''This function helps print stuff.'''
#        self.pwindow = Tk()
#        mydict = self.x.print()
#        for i in mydict.keys():
#            self.createlabels(i)
        

#    def download(self):
#        '''This function helps download stuff.'''
#        pass

#    def createlabels(self, text):
#        '''This function helps create window.'''
#        #label = (self.pwindow, text = text)
        

# x = SheetView()
'''The code was incomplete. It was difficult for me to understand the
Basics of MVC, but after a few readings online I learned what it is
supposed to be. I couldn't understand how to run a program from the
controller that's why my code didn't work.'''


'''This is the view for the expenses sheet.'''
# We import tkinter
from tkinter import *
import os.path

class SheetView:

    def __init__(self):
        #self.x = econtroller.Control()
        self.DEFAULT_F = ('Comicsans', 20)

    def myrun(self):
        '''We create a window with options for the user.'''
        self.window = Tk()
        title = self.window.title('EXPENSES')
        # We add the add button
        #self.buttons()
        
    def buttons(self):
        '''This method adds buttons to the window.'''
        button_add = Button(self.window, text='Add Expense',
                            font = self.DEFAULT_F,
                            command =self.add)
        button_add.pack()
        # We add the delete expense button
        button_delete = Button(self.window, text='Delete Expense',
                               font=self.DEFAULT_F,
                          command=self.deletecue)
        button_delete.pack()
        # We add the print button
        button_print = Button(self.window, text='Print monthly and yearly'
                              ' budget.', font = self.DEFAULT_F,
                              command =self.midstage2)
        button_print.pack()
        # We add the download button
        button_down = Button(self.window, text='Download monthly and yearly'
                             ' budget.', font = self.DEFAULT_F,
                             command =self.download)
        button_down.pack()
        button_q = Button(self.window, text='Quit', font=self.DEFAULT_F,
                          command=self.quitA)
        button_q.pack()
        self.window.mainloop()

    def deletecue(self):
        '''This method is an intermidiary function for deleting
        expenses.'''
        self.counter=4
        self.window.destroy()

    def add(self):
        '''This function helps add expenses to a list.'''
        self.counter = 1
        self.window.destroy()       
        self.root = Tk()
        label1 = Label(self.root, text='Add name and price of '
                       'your expense.', font = self.DEFAULT_F)
        label1.grid(row=1, column= 1)
        label2 = Label(self.root, text='Name of expense',
                       font = self.DEFAULT_F)
        label2.grid(row=2, column=0)
        # We create entry to take user input
        self.name1 = Entry(self.root, width = 40, font=self.DEFAULT_F)
        self.name1.grid(row=2, column=1)
        label3 = Label(self.root, text='Price of expense in $',
                       font = self.DEFAULT_F)
        label3.grid(row=3, column=0)
        self.price1 = Entry(self.root, width= 40, font=self.DEFAULT_F)
        self.price1.grid(row=3, column=1)
        # We create a button for recording entries and proceeding the
        # functioning of the code
        button_work = Button(self.root, text='Submit',
                             font=self.DEFAULT_F,
                             command=self.midstage1)
        button_work.grid(row=4, column =1)
        self.root.mainloop()

    def delete(self, dict1):
        '''This method deletes expenses by taking user input.'''
        self.counter = 4
        # We create a new window
        self.delroot = Tk()
        self.mydict = dict1
        count = 0
        # We print out all available info
        for i in self.mydict.keys():
            count += 1
            self.createlabels(self.delroot,i,count,0)
        count = 0
        for i in self.mydict.values():
            count += 1
            self.createlabels(self.delroot, '$'+str(i),count,1)
        label_mt = self.createlabels(self.delroot, 'Name of expense', count+1,
                                     0)
        # We take user input on the expense to be deleted.
        self.dele = Entry(self.delroot, font=self.DEFAULT_F)
        self.dele.grid(row = count+1, column = 1)
        button_del = Button(self.delroot, text='Submit', font=self.DEFAULT_F,
                            command=self.midstage4)
        button_del.grid(row = count+3, column = 0)
        self.delroot.mainloop()

    def midstage4(self):
        '''This is an intermidiate stage after delete expenses. It deals
        with error handling and processing.'''
        try:
            self.name3 = self.dele.get()
            # We check if user input has any error.
            if self.name3 == '' or self.name3 not in self.mydict.keys():
                raise ValueError
            else:
                self.name4 = self.name3
                self.delroot.destroy()
        except:
            # If there is an error, Error window is opened.
            self.mid1 = Tk()
            label_er = self.createlabels(self.mid1, 'Either the fields are '
                                         'empty or the price input is wrong. '
                                         'Please try again.', 1, 1)
            button_ta = Button(self.mid1, text='Try again',
                               font=self.DEFAULT_F, command=self.mid1.destroy)
            button_ta.grid(row = 3, column = 1)
            self.mid1.mainloop()
    

    def printout(self, dict1, mtotal, ytotal):
        '''This function prints out the expenses with totals to the gui.'''
        '''This function helps print stuff.'''
        self.counter = 2
        self.pwindow = Tk()
        mydict = dict1
        count = 0
        # With this print info to the gui screen
        for i in mydict.keys():
            count += 1
            self.createlabels(self.pwindow,i,count,0)
        count = 0
        for i in mydict.values():
            count += 1
            self.createlabels(self.pwindow, '$'+str(i),count,1)
        # We also print out the totals like monthly and yearly.
        label_mt = self.createlabels(self.pwindow, 'Monthly Total', count+1,
                                     0)
        label_mt1 = self.createlabels(self.pwindow, '$'+str(mtotal), count+1,
                                     1)
        label_yt = self.createlabels(self.pwindow, 'Yearly Total', count+2,
                                     0)
        label_yt1 = self.createlabels(self.pwindow, '$'+str(ytotal), count+2,
                                     1)
        button_mm = Button(self.pwindow, text='Back to main menu',
                           font=self.DEFAULT_F, command=self.runp)
        button_mm.grid(row=count+4, column = 0)
        self.pwindow.mainloop()

    def runp(self):
        '''This is an intermediate method after printout method.'''
        self.pwindow.destroy()
        
        

    def download(self):
        '''This function helps download stuff.'''
        self.counter = 3
        self.window.destroy()
        self.dwindow = Tk()
        # We create a view for the user and then we take inputs.
        labelf = self.createlabels(self.dwindow, 'Name your file', 1, 0)
        labelp = self.createlabels(self.dwindow, 'Enter Path', 2, 0)
        # We take inputs here.
        self.fname = Entry(self.dwindow, font=self.DEFAULT_F, width = 40)
        self.fname.grid(row=1, column=1)
        self.path = Entry(self.dwindow, font=self.DEFAULT_F, width = 40)
        self.path.grid(row=2, column=1)
        sub_button = Button(self.dwindow, text='Submit', font=self.DEFAULT_F,
                            command=self.midstage3)
        sub_button.grid(row=4, column=0)
        q_button = Button(self.dwindow, text='Quit', font=self.DEFAULT_F,
                            command=self.errord)
        q_button.grid(row=4, column=1)
        self.dwindow.mainloop()

    def createlabels(self,window, text, row, column):
        '''This function helps create labels in windows.'''
        label = Label(window, text=text, font=self.DEFAULT_F)
        label.grid(row=row, column=column)
        

    def quitA(self):
        '''This function quits the process altogether, stopping the code.'''
        self.window.destroy()
        self.counter = 0

    def midstage1(self):
        '''This is an intermediate stage after adding expenses. It handles
        eroors and does a checking.'''
        try:
            # We try if the inputs by user are correct. If not, we raise
            # error
            self.name2 = self.name1.get()
            self.price2 = self.price1.get()
            if self.name2 == '' or self.price2 == '':
                raise ValueError
            else:
                self.price2 = float(self.price2)
                self.root.destroy()
        except:
            # This prints out and error message
            self.mid1 = Tk()
            label_er = self.createlabels(self.mid1, 'Either the fields are '
                                         'empty or the price input is wrong. '
                                         'Please try again.', 1, 1)
            button_ta = Button(self.mid1, text='Try again',
                               font=self.DEFAULT_F, command=self.mid1.destroy)
            button_ta.grid(row = 3, column = 1)
            self.mid1.mainloop()

    def midstage2(self):
        '''This is an intermediate function after printing out.'''
        self.window.destroy()
        self.counter = 2


    def midstage3(self):
        '''This is an intermediate function after downloading.'''
        # We save the path and filename to variables and pass them to
        # the controller
        try:
            self.name_file = self.fname.get()
            self.name_path = self.path.get()
            if self.name_file == '' or self.name_path == '':
                raise ValueError
            else:
                self.acpath = os.path.join(self.name_path, self.name_file+'.csv')
                self.dwindow.destroy()
        except:
            self.errorm()

    def errorm(self):
        '''This method deals with printing error meessage.'''
        self.em = Tk()
        # error message is printed
        label_er = self.createlabels(self.em, 'Either the fields are '
                                     'empty or the inputs are wrong. '
                                     'Please try again.', 1, 1)
        button_ta = Button(self.em, text='Try again',
                           font=self.DEFAULT_F, command=self.em.destroy)
        button_ta.grid(row = 3, column = 1)
        self.em.mainloop()

    def errord(self):
        # This is in case there is and error during download.
        self.dwindow.destroy()
        self.acpath = 0
        self.counter=0
        return 1
        
        

