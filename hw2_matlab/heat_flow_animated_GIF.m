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

frames(nInter) = struct('cdata',[],'colormap',[]);
filename = 'heat_flow.gif';
for i=1:nIter
 options.face_vertex_color = u;
 h = figure
 plot_mesh(V,F,options)
 xlim([-0.0944    0.0608]);
 ylim([0.0333    0.1870]);
 zlim([-0.0617    0.0587]);
 axis tight manual % this ensures that getframe() returns a consistent size
 colormap summer
 frame = getframe(h);
 frames(i) = frame;
 im = frame2im(frame);
 [imind,cm] = rgb2ind(im,256);
 % Write to the GIF File
 if i == 1
    imwrite(imind,cm,filename,'gif', 'Loopcount',inf);
 else
   imwrite(imind,cm,filename,'gif','WriteMode','append');
 end
 close(h);
 %update u here
end
