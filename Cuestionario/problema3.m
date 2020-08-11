clear all;close all;clc;clf;
n=0:63;
# ------------------------------------------------------------
# y[n] + 0y[n-1] + 0.268y[n-2]=0.634x[n] + 0x[n-1]+ 0.634x[n]
# ------------------------------------------------------------
A=[   1    0 +0.268 ];
B=[ 0.634  0 +0.634 ];
# Secuencia de entrada impulso unitario
x=[1 zeros(1,(length(n)-1))];
#
figure(1),
stem(n, x, 'b');grid;
xlabel('n');ylabel('x[n]');
# Condiciones iniciales
y1=0; # y[-1]=0
Ci=[y1];
# Aplicación de la función filter
y=filter(B, A, x);
# Gráfica de la señal de salida
figure(2),
stem(n,y,'r');grid;
xlabel('n'); ylabel('y[n]');
