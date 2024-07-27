# arm_task
 taprobane arm task(sub)

1. the arm cad file converted into a urdf file using sw2urdf tool in solidworks.
2. the urdf file converted into a ros2 supported urdf file.
3. generated the moveit config files using the moveit setup assistant.
4. rewritten demo2.launch.py file as a properly working alternative for demo.launch.py

after running the demo2.launch.py and getting the rviz2 arm,
1. arm would not be able to move or rotate in every direction at the start.
2. change the "goal state" of the motion planning to "rest" position.
3. now you can use the markers to drag the arm around!

i am planning to do the "control arm using keyboard" and the "brick wall construct" tasks using rviz2
