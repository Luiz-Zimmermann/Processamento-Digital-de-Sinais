% Exemplo do calculo da convolução

clear all;close all; clc;

x = [1 1 1 1 1 1];

h =  [1 .5 .25 .125];

y = conv(x,h)

tama = length(x) + length(h) -1;

n = (0:1:tama-1);
stem(n,y)

title('Convol x e h');
xlabel('n');