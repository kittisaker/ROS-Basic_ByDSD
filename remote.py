#! /usr/bin/env python3

from tkinter import*
import rospy
from std_msgs.msg import Int16

rospy.init_node("REMOTE")
pub = rospy.Publisher("BOX", Int16, queue_size=10)

def send():
    pub.publish(999)

window = Tk()
window.geometry("200x200")

B1 = Button(window, text="FW", command = send)
B1.place(x=80, y=25)

B2 = Button(window, text="LT")
B2.place(x=20, y=90)

B3 = Button(window, text="RT")
B3.place(x=140, y=90)

B4 = Button(window, text="BW")
B4.place(x=80, y=150)

window.mainloop()