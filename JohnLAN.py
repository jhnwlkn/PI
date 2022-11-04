#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printName(self):
        print(self.firstname, self.lastname)
    
x = Person('John', 'Lan')
x.printName()
# print(x.firstName)

class Segitiga:
    def __init__(self, tinggi, alas):
        self.t = tinggi
        self.a = alas
    
    def printLuas(self):
        return(self.t*self.a/2)
    
y = Segitiga(7,10)
y.printLuas()

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname,lname)
    
z = Student('JOHN', 'LAN')
z.printName()


# In[ ]:




