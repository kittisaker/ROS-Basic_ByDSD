# ROS-Basic : Chapter 1 

## Set Enviroment on Ubuntu


## Ubuntu install of ROS Noetic
[ROS Noetic Ninjemys install](https://wiki.ros.org/noetic/Installation/Ubuntu)

## Create a ROS Workspace

```shell
mkdir catkin_ws
cd catkin_ws
mkdir src

catkin_make
```

```shell
gedit ~/.bashrc
```

```bash
# In .bashrc At the end line add and save file : 
source ~/catkin_ws/devel/setup.bash
```

## Creating a ROS Package

### Creating a catkin Package
```shell
cd /catkin_ws/src

catkin_create_pkg my_project rospy
# roscpp
```

### Building a catkin workspace and sourcing the setup file
```shell
cd catkin_ws
catkin_make
cd --
```

### Using python with rospy

```shell
# Terminal : 1
roscore
```

```shell
# Terminal : 2
cd ~/catkin_ws/src/my_project/src
touch test.py
```

test.py
```python
#! /usr/bin/env python3
print("Hello World")
```

```shell
# Terminal : 3
rqt_graph
```

```shell
# Terminal : 3
rosrun my_project test.py
# Error
```

```shell
# Terminal : 3
cd catkin_ws/src/my_project/src
chmod +x test.py
```

test.py
```shell
#!/usr/bin/env python3
rosrun my_project test.py
```

```shell
# Terminal : 3
rosrun my_project test.py
# hello World
```

---