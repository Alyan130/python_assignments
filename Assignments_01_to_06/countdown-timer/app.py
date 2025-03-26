import time

def countdown(t):
     while t:
       min,sec=divmod(t,60)
       time_display='{:02d}:{:02d}'.format(min,sec)
       print(time_display,end="\r")
       time.sleep(1)
       t-=1
   
     print("Time completed!")

time_input=int(input("Enter countdown time :"))
countdown(time_input)

