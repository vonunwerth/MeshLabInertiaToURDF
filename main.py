import pymeshlab
import numpy as np

ms = pymeshlab.MeshSet()

scale_factor = 100
print('Please put the input file to the same folder as this script and type in the full name of your file.')
file_name = input()
ms.load_new_mesh(file_name)

print('Please type the mass of your object in kg')
mass = float(input())

print('Scaling the mesh')
ms.transform_scale_normalize(axisx=scale_factor, axisy=scale_factor, axisz=scale_factor)

print('Generating the convex hull of the mesh')
ms.convex_hull()  # TODO only if object is not watertight

print('Calculating intertia tensor')
geom = ms.get_geometric_measures()
volume = geom['mesh_volume']
inertia_tensor = geom['inertia_tensor'] / pow(scale_factor, 2) * mass / volume

print('Inertia tensor:')
np.set_printoptions(suppress=True)
print(inertia_tensor)