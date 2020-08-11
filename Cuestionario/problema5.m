# Laboratorio N° 4: Ejercicio 5
# y[n]-5/6y[n-1]+1/6y[n-2]=1/3x[n-1]
N=20;
n=0:N;
omega=pi/4
xn=cos(omega*n)
A=[1 -5/6 1/6];
B=[0 1/3];
dn=[1 zeros(1, (length(n)-1))]; #secuencia de entrada del impulso unitario #secuencia de entrada del impulso unitario
y1=0; y2=0;
ci=[y1 y2];
yn1=filter(B, A, dn, ci);
yn2=filter(B, A, xn, ci);

# Grafico de x[n]
subplot(311);
stem(n, xn,'r'); grid;
xlabel('Tiempo n (Seg)'); ylabel('Amplitud');
title('Entrada cosenoidal: Cos[omega*n]');
# Grafico de h[n]
subplot(312);
stem(n, yn1,'b'); grid;
xlabel('Tiempo n (Seg)'); ylabel('Amplitud');
title('Respuesta impulsional del sistema discreto: h[n]');
# Grafico de y[n]
subplot(313);
stem(n, yn2,'r'); grid;
xlabel('Tiempo n (Seg)'); ylabel('Amplitud');
title('Salida: y[n]');
