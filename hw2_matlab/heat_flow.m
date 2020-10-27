clear; close all
[V,F,~]=readOBJ('bunny.obj');
n = size(V,1);

L = laplacian_matrix(V,F);
M = mass_matrix(V,F);
u0 = zeros(n,1);
u0 = rand(n,1);
dt = 3e-5;
u=u0;

nIter = 10;
for i=1:nIter
 options.face_vertex_color = u;
 figure
 plot_mesh(V,F,options)
 colormap summer
 pause;
 %update u here
end
