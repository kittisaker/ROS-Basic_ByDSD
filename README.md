# ROS-Basic : Chapter 2 


## Node && Topic

t1 : Node master
```shell
roscore
```

t2
```shell
rosrun turtlesim turtlesim_node
```

t3
```shell
rosrun turtlesim turtle_teleop_key
```

t4
```shell
rostopic list

rostopic info /turtle1/cmd_vel
```

type: geometry_msgs/Twist

t4
```shell
rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist # tab press

rostopic pub -r 1 /turtle1/cmd_vel geometry_msgs/Twist # tab press

rostopic pub -r 1 /turtle1/cmd_vel geometry_msgs/Twist "linear:
x: 5.0
y: 0.0
z: 0.0
angular:
x: 0.0
y: 0.0
z: 5.0"
```

## Service & Parameter

t1 : Node master
```shell
roscore
```

t2
```shell
rosrun turtlesim turtlesim_node
```

t3
```shell
rosservice list

rosservice call /reset
```

t3
```shell
rosservice info /turtle1/set_pen

rosservice call /turtle1/set_pen "{r: 0, g: 0, b: 0, width: 0, 'off' : 0}"
```

```shell
rosparam list

rosparam get /

rosparam set /turtlesim/background_b 0
rosservice call /clear
```


## Ptyhon OOP

## Pub Node

t1
```shell
roscore
```

Pub-Node.py
```python
#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    pub = rospy.Publisher("chatter",String,queue_size=10)
    rospy.init_node("Talker")
    rate = rospy.Rate(0.5)
    while(not rospy.is_shutdown()):
        pub.publish("hi")
        rate.sleep()
```

t2
```shell
rosrun my_project Pub-Node.py
```

t3
```shell
rqt_graph

rostopic list
rostopic echo /chatter
```

- loginfo()
- rosbag
- logerr
- logwarn

Pub-Node.py
```python
#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    pub = rospy.Publisher("chatter",String,queue_size=10)
    rospy.init_node("Talker")
    rate = rospy.Rate(0.5)
    x = 0
    while(not rospy.is_shutdown()):
        pub.publish(str(x))
        rospy.loginfo(str(x))
        x = x + 1
        rate.sleep()
```

Pub-Node.py
```python
#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    pub = rospy.Publisher("chatter",String,queue_size=10)
    rospy.init_node("Talker")
    rate = rospy.Rate(0.5)
    x = 0
    while(not rospy.is_shutdown()):
        pub.publish(str(x))

        if(x%2 == 0):
            rospy.loginfo(str(x))
        else:
            rospy.logerr(str(x))
        x = x + 1
        rate.sleep()
```

## Sub

Sub-Node.py
```python
#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def run(val):
    rospy.loginfo(val.data)

if __name__ == "__main__":
    sub = rospy.Subscriber("chatter",String,callback=run)
    rospy.init_node("Listener")
    rospy.spin()
```

```shell
rqt_graph
```

## Control Turtlesim

### Position

```shell
rosrun turtlesim turtlesim_node

rostopic echo turtle1/host
```

```shell
rosrun turtlesim turtle_eleop_key
```

### Turtlesim pose1 

t1
```shell
roscore
```

t2
```shell
rosrun turtlesim turtlesim_node
```

t3
```shell
rosrun my_project Pub-Sub-turtle.py
```

```python
#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def run(pose):
    if pose.x > 9.0 or pose.x < 2.0 or pose.y >9.0 or pose.y <2.0:
        cmd = Twist()
        cmd.linear.x = 0.5
        cmd.angular.z = 0.5
        pub.publish(cmd)
    else:
        cmd = Twist()
        cmd.linear.x = 2.0
        cmd.angular.z = 0.0
        pub.publish(cmd)

if __name__ == "__main__":
    rospy.init_node("control")
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist, queue_size=10)
    sub = rospy.Subscriber("/turtle1/pose",Pose,callback=run)
    rospy.spin()
```

---