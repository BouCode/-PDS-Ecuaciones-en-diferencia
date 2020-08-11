clear all; close all; clc; clf
n=-10:100;
#y[n]=1.8*cos(pi/16)y[n-1]+0.81y[n-2]=x[n]-1/2*x[n-1];
A=[1 -1.77 0.81];
B=[1 -0.5]; 
fs=1; 
nmax=+100; 
nmin=-10; 
ns=[nmin:1/fs:nmax];
x=1.5*[zeros(1,(abs(nmin)*fs)) ones(1,(abs(nmax)*fs+1))]; 
#figure(1)
subplot(2,1,1); stem(n,x,'r');grid;
xlabel('n');ylabel('x[n]=1.5*u[n]');
y1=0; 
ci=[y1]; 
y=filter(B,A,x); 
subplot(2,1,2);stem(n,y,'b');grid;
xlabel('n');ylabel('y[n]');