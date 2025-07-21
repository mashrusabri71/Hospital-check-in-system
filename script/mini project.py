# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 14:24:29 2020

@author: mashr
"""
from time import sleep 
from engi1020.arduino import *

touch = digital_read(4)
servo = digital_read(5)
button = digital_read(2)
temp = analog_read(0)
x = 1 #determines seat number for covid parients
y= 0 ##determines seat number for non covid parients


data_forDoc = {} #patient datavfor doctors



def patient():
   
        global x
        global y
        print("Wellcome to the hospital")
        print("Answer the questions with y/n where applicable")
        name = str(input("What is your name: "))
        q1=str(input("Have you come into close contact (within 6 feet) with someone who has a laboratory confirmed COVID – 19 diagnosis in the past 14 days?:  "))
    
        fever = str(input("Do you have any of the following:  fever or chills, cough, shortness of breath or difficulty breathing, body aches, headache, new loss of taste or smell, sore throat? "))
    
    
    
        covid= str(input("Answer honestly! Do you have covid? "))
    
        prob = str(input("Why are you here today " ))
    
    
        update_data ={name:["Fever:"+fever, "problem:"+prob, "Covid: "+ covid]}
    
        data_forDoc.update(update_data)
    #print(data_forDoc)
        if covid=="y":#If the user is honest
            lcd_rgb(255, 0,0)
            lcd_print("GO to red zone seat no: " +str(seat_cov+2))
            print("GO to red zone seat no: " +str(seat_cov+2))
            print(" You have covid")
    
        elif q1 == 'y' and fever =='y': #The user might not have tested for covid hence the symptoms my indicate they have covid
            x+=2
            print("You are a suspect of covid")
        
            lcd_rgb(255, 0,0)
            lcd_print("GO to red zone seat no: " +str(x))
            print("GO to red zone seat no: " +str(x))
        else:
             y +=2
             lcd_rgb(0, 0,255)
             lcd_print("GO to blue zone seat no: "+ str(y))
             print("GO to Blue zone seat no: "+ str(y))
             
        
        
        
        
        

def doctor():
    
       
        
    print("Doctor Identified")
    print()
    print()
    print("Hello Doc   here are your patients and their record:")
    print()
    print(data_forDoc)
        
def start():
    if  touch==1 or button==1:
        
        
        lcd_rgb(255, 255, 0)
        lcd_print("Hello <3s")
        print("sanitizer sprayed")
        servo_move(5, 180)
        servo_move(5, 0)
        print("Hello")


        
    
def main():
    total =0
    while True:
        print("Hold button or touch sesnor to start")
        
        sleep(2)
        start()
        print("IF DOCTOR Hold TOUCH SENSOR or IF PATIENT Hold BUTTON")
        sleep(5)
        if touch==1:
            doctor()
        elif button==1:
            patient()
            total+=1
        
        print("Total number of people  inside the hospital today: ", total )
        
        
        
       
           
        print("Tanks for comming....")
        end = input("Enter q to exit and anything else to continue for new patient/ doctor entry: ")
        if end=='q':
            print("Program Shutting down..")
            break
        else:
            print()

main()



    