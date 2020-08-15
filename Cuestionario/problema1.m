N = 20;
n = 0:N;
omega = pi/3
xn = cos (omega*n)

A = [1 0.13 0.52 0.3];
B = [0.16 -0.48 0.48 -.016];
dn = [1 zeros(1, (length (n) - 1))];
y1 = 0; y2 = 0; y3 = 0;
ci = [y1 y2 y3];
yn1 = filter (B, A, dn, ci);
yn2 = filter (B, A, dn, ci);

subplot (311);
stem (n, xn, 'r'); grid;
xlabel ('Tiempo n (seg)'); ylabel ('Amplitud');
title ('Entrada cosenoidal: Cos [omega * n]');

subplot (312);
stem (n, yn1, 'b'); grid;
xlabel ('Tiempo n (Seg)'); ylabel ('Amplitud');
title ('Respuesta impulsional del sistema discreto: h[n]');

subplot (313);
stem (n, yn2, 'r'); grid;
xlabel ('Tiempo n (seg)'); ylabel ('Amplitud');
title ('Salida: y[n]');
