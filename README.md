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
#! /usr/bin/env python3
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


## ROS with Arduino nano

### Install Arudino IDE


### Install Driver in Ubuntu

```shell
mkdir CH340_Soruce
cd CH340_Soruce/
git clone http://github.com/juliagoda/CH341SER.git

cd CH341SER/
make clean
make

sudo make load
sudo rmmod ch341
lsmod | grep ch34
dmesg
```

### Install library on Arduino
```
rosserial
```

### Upload code Arduino and Blink LED

```Cpp
#include <ros.h>
#include <std_msgs/Int16.h>
 
ros::NodeHandle  nh;
 
void control_LED( const std_msgs::Int16 & cmd_msg){
  int value = cmd_msg.data; 
  digitalWrite(13, value);  
}

ros::Subscriber<std_msgs::Int16> sub("Topic_LED_13", control_LED);
 
void setup(){
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
}
 
void loop(){
  nh.spinOnce();
  delay(1);
}
```

```shell
sudo apt-get install ros-noetic-rosserial-arduino
```

```shell
rosrun rosserial_python serial_node.py /dev/ttyUSB0
```


```python
#!/usr/bin/env python3
from tkinter import*
import rospy
from std_msgs.msg import Int16

frame=Tk()
frame.geometry("200x200")

rospy.init_node('GUI_LED_Control')
rate = rospy.Rate(10) 
rate.sleep()
pub1 = rospy.Publisher('Topic_LED_13', Int16, queue_size=10)
   
def talker(val):
    cmd_value = Int16(val)
    rospy.loginfo(cmd_value)
    pub1.publish(cmd_value)
    
B1= Button(frame,text = "ON",command= lambda: talker(1))
B1.pack()
B2= Button(frame,text = "OFF",command= lambda: talker(0))
B2.pack()

frame.mainloop()
```

```shell
rosrun my_project scale-test.py 
```


### Upload code Arduino and Servo mortor

```python
#! /usr/bin/env python3
from tkinter import*

window = Tk()

S1 = Scale(window)
S1.pack()

window.mainloop()
```

```cpp
#include <Servo.h> 
#include <ros.h>
#include <std_msgs/Int16.h>
 
ros::NodeHandle  nh;
 
Servo servo_9;
Servo servo_10;

void s_9( const std_msgs::Int16& cmd_msg){
  servo_9.write(cmd_msg.data); 
}
 
void s_10( const std_msgs::Int16& cmd_msg){
  servo_10.write(cmd_msg.data); 
}
 
ros::Subscriber<std_msgs::Int16> sub_1("Topic_servo_9", s_9);
ros::Subscriber<std_msgs::Int16> sub_2("Topic_servo_10", s_10);

void setup(){
  servo_9.attach(9); 
  servo_10.attach(10); 
  nh.initNode();
  nh.subscribe(sub_1);
  nh.subscribe(sub_2);
}
 
void loop(){
  nh.spinOnce();
  delay(1);
}
```

```shell
rosrun
```

```shell
rosrun rosserial_python serial_node.py /dev/ttyUSB0
```

```python
#!/usr/bin/env python3
from tkinter import*
import rospy
from std_msgs.msg import Int16

frame=Tk()
frame.geometry("200x200")

S1_value = 0
S2_value = 0

rospy.init_node('GUI')
pub1 = rospy.Publisher('Topic_servo_9', Int16, queue_size=10)
pub2 = rospy.Publisher('Topic_servo_10', Int16, queue_size=10)
rate = rospy.Rate(100)
rate.sleep()

def talker(val):
    global S1_value
    global S2_value

    S1_value = Int16(S1.get())
    S2_value = Int16(S2.get())
    
    pub1.publish(S1_value)
    pub2.publish(S2_value)

S1= Scale(frame, from_=0, to=180, label= "SV-9", command=talker)
S1.place(x=5, y=10)
S1.set(90)

S2= Scale(frame, from_=0, to=180, label= "SV-10", command=talker)
S2.place(x=100, y=10)
S2.set(90)

frame.mainloop()
```

```shell
rosrun my_project scale-test.py 
```

##