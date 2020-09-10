from trimesh import TriMesh
import meshplot as mp
import numpy as np
import os
mp.offline()

mesh = TriMesh.FromOBJ_FileName("../input/bunny_no_holes.obj")

if not(os.path.isdir("plots/")):
	os.mkdir("plots/")

p = mp.plot(mesh.vs, mesh.faces, c=mesh.vs[:,0], return_plot=True, filename='plots/test.html')

if not(os.path.isdir("output/")):
	os.mkdir("output/")

mesh.write_OBJ("output/bunny.obj")
