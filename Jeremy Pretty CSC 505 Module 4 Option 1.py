# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 08:20:37 2021

@author: jpret
"""
# Creating the Lead class.. This is the head of driving to accomplish
class Lead:
    def DriveToAccomplish(self):
            print("You have the Drive to Accomplish any tasks! \n")
 
# Creating the Concrete Builder Class
class Concrete_Builder:
    def TechnicalExpertise(self):
            print("You have the Technical Expertise for being a software engineer! \n")
 
# Creating the Interface Builder Class 
class Interface_Builder:
    def Communication(self):
            print("You have great communication! \n")

# Creating the Product Class
class Product(Concrete_Builder):
    def Software_Developer(self):
            Lead.DriveToAccomplish(self)
            Concrete_Builder.TechnicalExpertise(self)
            Interface_Builder.Communication(self)
 
# Creating the instances of the classes
r1 = Lead()
r2 = Concrete_Builder()
r3 = Interface_Builder()
r4 = Product()

# Main Menu! 
def MainMenu():
    while True:
            print("Please pick from one of the following menu items!")    
            print("Press 1 to learn about the Lead and what is needed!")
            print("Press 2 to learn about the Concrete Builder!")
            print("Press 3 to learn about the Interface Builder!")
            print("Press 4 to see how it all works!")
            print("Press 5 to leave the program")
            
            #selection variable
            selection = int(input("Enter Choice: "))
            if selection == 1:
                r1.DriveToAccomplish()
            elif selection == 2:
                r2.TechnicalExpertise()
            elif selection == 3:
                r3.Communication()
            elif selection == 4:
                r4.Software_Developer()
            elif selection == 5:
                print("Thank you for using this program, have a great day!")
                break
            else: 
                print("Invalid choice, please select correct option!")
                
MainMenu()