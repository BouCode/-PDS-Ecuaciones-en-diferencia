n=0:80000;

A=[1];
B=[1 0.5];

[x, fs]=audioread('Nota de voz.ogg');

stem(x);
grid;
xlabel('n');
ylabel('x[n]');

y1=0; # y[-1]=0
Ci=[y1];

y=filter(A, B, x, Ci);

figure(2),
stem(n,y,'r');
grid;
xlabel('n');
ylabel('y[n]');