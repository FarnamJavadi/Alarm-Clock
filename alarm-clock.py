from tkinter import *
import datetime
import time
from playsound import playsound

root =Tk()
root.geometry("400x200")

def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        time.sleep(1)
        print(current_time, set_alarm_time)
        if current_time == set_alarm_time:
            print("Time to Wake Up!")
            playsound('alarm.wav')
            break

Label(root, text="Alarm Clock", font=('hevetica', 20, 'bold'), fg='Blue').place(x=120, y=10)
Label(root, text="Set The Time", font=('hevetica', 15, 'bold'), fg='black').place(x=130, y=50)

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04',
         '05', '06', '07', '08', '09',
         '10', '11', '12', '13', '14',
         '15', '16', '17', '18', '19',
         '20', '21', '22', '23', '24')
hour.set(hours[0])

hrs = OptionMenu(root, hour, *hours)
hrs.place(x=90, y=100)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04',
           '05', '06', '07', '08', '09',
           '10', '11', '12', '13', '14',
           '15', '16', '17', '18', '19',
           '20', '21', '22', '23', '24',
           '25', '26', '27', '27', '28',
           '29', '30', '31', '32', '33',
           '34', '35', '36', '37', '38',
           '39', '40', '41', '42', '43',
           '44', '45', '46', '47', '48',
           '49', '50', '50', '51', '52',
           '53', '54', '55', '56', '57',
           '58', '59', '60')

mins = OptionMenu(root, minute, *minutes)
mins.place(x=180, y=100)

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04',
           '05', '06', '07', '08', '09',
           '10', '11', '12', '13', '14',
           '15', '16', '17', '18', '19',
           '20', '21', '22', '23', '24',
           '25', '26', '27', '27', '28',
           '29', '30', '31', '32', '33',
           '34', '35', '36', '37', '38',
           '39', '40', '41', '42', '43',
           '44', '45', '46', '47', '48',
           '49', '50', '50', '51', '52',
           '53', '54', '55', '56', '57',
           '58', '59', '60')

second.set(seconds[0])

secs = OptionMenu(root, second, *seconds)
secs.place(x=270, y=100)

Button(root, text="Set the Alarm", font=('helvetica', 15), fg="red", command=alarm).place(x=120, y=150)

root.mainloop()
