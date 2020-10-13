
%Exemplo para plotar a localização dos pólos e zeros
% no plano Z 

% D(Z) = 1 + 1,5Z^-1 + 2Z^-2

clear all; close all; clc;
D = [1, 1.5, 2];

Num = D;
Den = [1, 0, 0];

% Set up vector for zeros
z = roots(Num)

% Set up vector for poles
p = roots(Den)

figure(1);
zplane(z,p);
title('Pole/Zero Plot Example');