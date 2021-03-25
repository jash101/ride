# RIDE: ROS IDE
## RIDE automatically creates the package and boilerplate OOP Python code for nodes as per your needs


### (RIDE is not an IDE, but even ROS isn't an OS, so I guess it's... okay)

## How to use
- clone this
- write pkg.yaml according to the requirements of the package you wish to create
- run ```ride.py```. This runs catkin_create_pkg to create the package and generates boilerplate code for all your nodes
- edit node scripts, mainly subscriber callbacks and spin(), as per your requirements
- that's it!

## Yaml parameters
I've tried to keep the param names self explanatory. Also, you may take a look at sample.yaml.

## What's next
- I wish to create rqt_graph like GUI to intuitively create your node graph and generate pkg and boilerplate code.
 
  **If you or someone you know is experienced or interested in working on this, please contact me!**
- Add functionality for ROS services

  **This is 3AM code. If you have issues, queries, suggestions, let me know :)**
