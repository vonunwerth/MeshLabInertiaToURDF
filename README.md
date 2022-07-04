# URDF Inertia Calculator
Just run the *main.py* in the same folder of your robot link 3d file, type the filename and the mass and copy the XML output to your URDF. 

### Preperation
You have to install the *pymeshlab* package to run this script.

### Background
You want to calculate the intertial properties for your robots link. In the following this will be done for example for the *Cylinder.dae* file, a simple cylinder 4 metres high and 2 metres in diameter. We assume this Cylinder has a mass of 5kg.

Refering [Wikipedia](https://en.wikipedia.org/wiki/List_of_moments_of_inertia) the inertia tensor for a cylinder can be calculated by:

![](doc/matrix.svg)

which results in ```[7.91667, 7.91667, 2.50000]``` for the diagonal entries with ```h=4, r=1```.

### Usage
Calculating the URDF inertia tag for the *Cylinder.dae* file can be done by typing:

```python3 main.py```

You will be asked to type the filename and the weight of your 3D object. For example, fill *Cylinder.dae* and *5*.

The whole process is based on this tutorial: [Inertial parameters of triangle meshes](https://classic.gazebosim.org/tutorials?tut=inertia&cat=build_robot)

At first the script calculates the center of mass of the object. After that it scales the mesh by a factor of 100 to increase the numerical accuracy. You could manually change that, if you need to scale it more up. Now the convex hull of your object will be calculated. For the hull the geometric properties will be calculated, scaled back down and outputted as URDF XML inertial tag like that (the precision could also be changed in the script):
```
<inertial>
  <origin xyz="0.00000002 -0.00000001 0.00000000"/>
  <mass value="5.00000000"/>
  <inertia ixx="7.90866056" ixy="0.00000006" ixz="0.00000000" iyy="7.90866060" iyz="0.00000000" izz="2.48398783"/>
</inertial>
```
Looks pretty similar to the manually calculated values, doesn't it? ;)

### Licence
The MeshLabInertiaToURDF source is released under the GPLv3 License.

### Copyright
```
MeshLabInertiaToURDF

Maximilian von Unwerth
von-unwerth.de
Copyright(C) 2022
All rights reserved.
```
