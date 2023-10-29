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

