# ROS-Basic : Chapter 3

## Python GUI

```python
#! /usr/bin/env python3

from tkinter import*

window = Tk()
window.geometry("200x200")

B1 = Button(window, text="Ok")
B1.pack()

window.mainloop()
```

```python
#! /usr/bin/env python3

from tkinter import*

window = Tk()
window.geometry("200x200")

B1 = Button(window, text="Ok")
B1.place(x=0, y=0)

B2 = Button(window, text="Ok")
B2.pack()

window.mainloop()
```

## Tk wit 

```python
#! /usr/bin/env python3

from tkinter import*

window = Tk()
window.geometry("200x200")

B1 = Button(window, text="FW")
B1.place(x=80, y=25)

B2 = Button(window, text="LT")
B2.place(x=20, y=90)

B3 = Button(window, text="RT")
B3.place(x=140, y=90)

B4 = Button(window, text="BW")
B4.place(x=80, y=150)

window.mainloop()
```

```python
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
```

```shell
rostopic echo /BOX
```

## Tk with turtle

```python
#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist


frame = Tk()
frame.title("REMOTE")
frame.geometry("200x200")


rospy.init_node("GUI_Remote")
pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)


def fw():
    print("fw")
    cmd = Twist()
    cmd.linear.x = 1.0
    cmd.angular.z=0.0
    pub.publish(cmd)

def bw():
    print("bw")
    cmd = Twist()
    cmd.linear.x = -1.0
    cmd.angular.z=0.0
    pub.publish(cmd)

def lt():
    print("lt")
    cmd = Twist()
    cmd.linear.x = 1.0
    cmd.angular.z= 1.0
    pub.publish(cmd)

def rt():
    print("rt")
    cmd = Twist()
    cmd.linear.x = 1.0
    cmd.angular.z= -1.0
    pub.publish(cmd)


B1 = Button(text = "FW", command=fw)
B1.place(x=73, y=20)

B2 = Button(text = "BW", command=bw)
B2.place(x=73, y=130)

B3 = Button(text = "LT", command=lt)
B3.place(x=20, y=80)

B4 = Button(text = "RT", command=rt)
B4.place(x=128, y=80)

frame.mainloop()
```
