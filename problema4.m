clear; clc; clf; 
n = 0:1:50;

h1 = abs (((1/2).^ (n/2)) .* (cos (pi * n/2) - 2* ((2) .^ 0.5) .* sin (pi * n/2)));
S1 = sum (h1)
fig (1)
stem (n, h1)
h2 = abs (((0.88).^ (n)) .* (cos (pi * n/16) + (8.17)*(sin (pi*n/2))));
S2 = sum (h2)
fig (2) 
stem (n, h2)