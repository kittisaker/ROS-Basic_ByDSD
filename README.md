# ROS-Basic : Chapter 4

## P

```shell
roscore
```

```shell
rosrun rosserial_python serial_node.py /dev/ttyUSB0
```

```python
#! /usr/bin/env python3
import rospy
from std_msgs.msg import Int16
import time

pub = rospy.Publisher("/Topic_servo_9", Int16, queue_size=10)
rospy.init_node("servo_control")
rospy.loginfo("Start Node --- servo_control")
rate = rospy.Rate(10)

position = 90

while(not rospy.is_shutdown()):
    rate.sleep()
    while(position <= 180):
        pub.publish(position)
        position = position+1
        time.sleep(0.01)
    while(position >= 90):
        pub.publish(position)
        position = position-1
        time.sleep(0.01)
```

```shell
rosrun my_project smooth-control.py
```

## 

```py
#! /usr/bin/env python3
import rospy
from std_msgs.msg import Int16
import time

pub = rospy.Publisher("/Topic_servo_9", Int16, queue_size=10)
rospy.init_node("servo_control")
rospy.loginfo("Start Node --- servo_control")
rate = rospy.Rate(10)

position = 90
pub.publish(position)
time.sleep(1)

def cmd(goal):
    global position
    while(not rospy.is_shutdown()):
        rate.sleep()
        while(position < goal.data):
            position = position+1
            pub.publish(position)
            rospy.loginfo(str(position))
            time.sleep(0.01)
        while(position > goal.data):
            position = position+1
            pub.publish(position)
            rospy.loginfo(str(position))
            time.sleep(0.01)

sub = rospy.Subscriber("cmd", Int16, callback=cmd)
rospy.spin()
```

## 

```cpp
#include <Servo.h> 
#include <ros.h>
#include <std_msgs/Int16.h>
 
ros::NodeHandle  nh;
 
Servo servo_9;
Servo servo_10;
Servo servo_11;
Servo servo_12;

void s_9( const std_msgs::Int16& cmd_msg){
  servo_9.write(cmd_msg.data); 
}
 
void s_10( const std_msgs::Int16& cmd_msg){
  servo_10.write(cmd_msg.data); 
}

void s_11( const std_msgs::Int16& cmd_msg){
  servo_11.write(cmd_msg.data); 
}

void s_12( const std_msgs::Int16& cmd_msg){
  servo_12.write(cmd_msg.data); 
}
 
ros::Subscriber<std_msgs::Int16> sub_1("Topic_servo_9", s_9);
ros::Subscriber<std_msgs::Int16> sub_2("Topic_servo_10", s_10);
ros::Subscriber<std_msgs::Int16> sub_3("Topic_servo_11", s_11);
ros::Subscriber<std_msgs::Int16> sub_4("Topic_servo_12", s_12);

void setup(){
  servo_9.attach(9); 
  servo_10.attach(10);
  servo_11.attach(11);
  servo_12.attach(12);
  nh.initNode();
  nh.subscribe(sub_1);
  nh.subscribe(sub_2);
  nh.subscribe(sub_3);
  nh.subscribe(sub_4);
}
 
void loop(){
  nh.spinOnce();
  delay(1);
}
```

```python
#! /usr/bin/env python3
import rospy
from std_msgs.msg import Int16
import time

pub1 = rospy.Publisher("/Topic_servo_9", Int16, queue_size=10)
pub2 = rospy.Publisher("/Topic_servo_10", Int16, queue_size=10)
pub3 = rospy.Publisher("/Topic_servo_11", Int16, queue_size=10)
pub4 = rospy.Publisher("/Topic_servo_12", Int16, queue_size=10)
rospy.init_node("servo_control")
rospy.loginfo("Start Node --- servo_control")
rate = rospy.Rate(10)

position1 = 90
position2 = 90
position3 = 90
position4 = 90
pub1.publish(position1)
pub2.publish(position2)
pub3.publish(position3)
pub4.publish(position4)
time.sleep(1)

def cmd(goal):
    global position1
    global position2
    global position3
    global position4
    
    while(not rospy.is_shutdown()):
        rate.sleep()
        while(position1 < goal.data):
            position1 = position1+1
            pub1.publish(position1)
            rospy.loginfo(str(position1))
            time.sleep(0.01)
        while(position1 > goal.data):
            position1 = position1+1
            pub1.publish(position1)
            rospy.loginfo(str(position1))
            time.sleep(0.01)

        while(position2 < goal.data):
            position2 = position2+1
            pub2.publish(position2)
            rospy.loginfo(str(position2))
            time.sleep(0.01)
        while(position2 > goal.data):
            position2 = position2+1
            pub2.publish(position2)
            rospy.loginfo(str(position2))
            time.sleep(0.01)

        while(position3 < goal.data):
            position3 = position3+1
            pub3.publish(position3)
            rospy.loginfo(str(position3))
            time.sleep(0.01)
        while(position3 > goal.data):
            position3 = position3+1
            pub3.publish(position3)
            rospy.loginfo(str(position3))
            time.sleep(0.01)

        while(position4 < goal.data):
            position4 = position4+1
            pub4.publish(position4)
            rospy.loginfo(str(position4))
            time.sleep(0.01)
        while(position4 > goal.data):
            position4 = position4+1
            pub4.publish(position4)
            rospy.loginfo(str(position4))
            time.sleep(0.01)

sub = rospy.Subscriber("cmd", Int16, callback=cmd)
rospy.spin()
```

```python
#!/usr/bin/env python3
from tkinter import*
import rospy
from std_msgs.msg import Int16

frame=Tk()
frame.geometry("400x200")

S1_value = 0
S2_value = 0
S3_value = 0
S4_value = 0

rospy.init_node('GUI')
pub1 = rospy.Publisher('Topic_servo_9', Int16, queue_size=10)
pub2 = rospy.Publisher('Topic_servo_10', Int16, queue_size=10)
pub3 = rospy.Publisher('Topic_servo_11', Int16, queue_size=10)
pub4 = rospy.Publisher('Topic_servo_12', Int16, queue_size=10)
rate = rospy.Rate(100)
rate.sleep()

def talker(val):
    global S1_value
    global S2_value
    global S3_value
    global S4_value

    S1_value = Int16(S1.get())
    S2_value = Int16(S2.get())
    S3_value = Int16(S3.get())
    S4_value = Int16(S4.get())
    
    pub1.publish(S1_value)
    pub2.publish(S2_value)
    pub3.publish(S3_value)
    pub4.publish(S4_value)

S1= Scale(frame, from_=0, to=180, label= "SV-9", command=talker)
S1.place(x=5, y=10)
S1.set(90)

S2= Scale(frame, from_=0, to=180, label= "SV-10", command=talker)
S2.place(x=100, y=10)
S2.set(90)

S3= Scale(frame, from_=0, to=180, label= "SV-11", command=talker)
S3.place(x=195, y=10)
S3.set(90)

S4= Scale(frame, from_=0, to=180, label= "SV-12", command=talker)
S4.place(x=290, y=10)
S4.set(90)

frame.mainloop()
```

---