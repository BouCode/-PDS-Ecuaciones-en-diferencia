clear;clf;clc;

n1=-10;
n2=100;
n = n1:n2;
N = length(n);

A=[1 -1.8*cos(pi/16) 0.81];
B=[1 0.5];

x=[zeros(1,N-n2-1) 1 zeros(1,N+n1-1)];
#x=[10 ceros,1,0.5,99 ceros]

y=filter(B, A, x)

figure(1),
stem(n,x);grid;
title('Entrada');
xlabel('n');ylabel('x[n]');

figure(2),
stem(n,y);grid;
xlabel('n'); ylabel('y[n]');


