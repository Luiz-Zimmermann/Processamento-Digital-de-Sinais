% Exemplo sistema discreto
% equaçao diferença: y[n] + 0,25y[n-1] + 0,125y[n-2] = x[n]
% walter
clear all; close all; clc;


tama =  10;
% Definindo a entrada
x = zeros(tama,1);
x(1,1) = 1;% definindo o impulso unitário

tama_loop = length(x);
vet_saida = zeros(tama_loop,1);

% Definindo as condições iniciais 
ynm1 = 0;
ynm2 = 0;

for j = 1: tama_loop
    input = x(j,1);
    
   
    
    y = input - 0.25*ynm1 - 0.125*ynm2;
    
    % Desloca o vetor de delay
    ynm2 = ynm1;
    ynm1 = y;
    
    vet_saida(j,1) = y;
end    


% plotando o módulo e a fase
subplot(2,1,1)
stem(x)
title('Entrada x[n]');xlabel('n');
grid on;

subplot(2,1,2)
stem(vet_saida)
title('Saída y[n]');xlabel('n');
grid on;

 vet_saida

