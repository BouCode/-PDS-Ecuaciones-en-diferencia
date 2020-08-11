clear;clf;clc;
n = 0:100;
A = [1 0 0.5];
B = [1 -2];
M = 1;
f = 2;
Ts = 0.025;
x = M * cos (2 * pi * f * Ts * n) .* [ones ones (1, (length (n) - 1))];
figure (1)
stem (n, x, 'b');
grid;
xlabel ('n');
ylabel ('x[n]');
y1 = 0;
y2 = 0;
ci = [y1 y2];

y = filter (B, A, x, ci);

figure (2)
stem (n, y, 'r');
grid;
xlabel ('n');
ylabel ('y[n]')