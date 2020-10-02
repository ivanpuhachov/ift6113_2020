import meshplot as mp
import numpy as np
import os
from trimesh import TriMesh

mp.offline()

inputfile = "../input/horse-1.obj"

mesh = TriMesh.FromOBJ_FileName(inputfile)

eigenvectors = np.random.rand(*mesh.vs.shape)

if not(os.path.isdir("plots/")):
	os.mkdir("plots/")

p = mp.plot(mesh.vs, mesh.faces, c=eigenvectors[:,0], return_plot=True, filename='plots/test.html')

