"""
contacts.py
This program users a person class to keep track of contacts
@author Vigneshwaran

"""


class Person(object):
    """
      This Person class defines a person in terms of a name, phone number and email address
    """
    #Constructor
    def __init__(self,theName,thePhone,theEmail):
        self.name=theName
        self.phone=thePhone
        self.email=theEmail

    #Accesser Methods (getters)
    def getName(self):
        return self.name
    def getPhone(self):
        return self.phone
    def getEmail(self):
        return self.email

    #Mutator Methods (setters)
    def setPhone(self,newPhoneNum):
        self.phone=newPhoneNum
    def setEmail(self,newEmailAdd):
        self.email=newEmailAdd
    def __str__(self):
        return "Person[name="+self.name + \
               ",phone="+self.phone + \
               ",email="+self.email + \
               "]"

class Emp(Person):
    pass