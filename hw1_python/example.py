from trimesh import TriMesh
import meshplot as mp
import numpy as np
import os
import argparse
mp.offline()

parser = argparse.ArgumentParser(description="Run subdivision")
parser.add_argument("--input", "-i", default="../input/cube.obj", help="path to input .obj")
parser.add_argument("-n", default=3, type=int, help="number of iterations to perform")
args = parser.parse_args()

inputfile = args.input
number_of_iterations = args.n

mesh = TriMesh.FromOBJ_FileName(inputfile)

if not(os.path.isdir("plots/")):
	os.mkdir("plots/")

p = mp.plot(mesh.vs, mesh.faces, c=mesh.vs[:,0], return_plot=True, filename='plots/test.html')

if not(os.path.isdir("output/")):
	os.mkdir("output/")

mesh.write_OBJ("output/test_output.obj")
