% Exemplo delay
% walter
clear all; close all; clc;

Fs = 8000;
t1 = 1.0*10^-3; t2 = 1.5*10^-3;

n1 = t1*Fs; n2 = t2*Fs
% Definição dos ganhos 
a0 = .5; a1 = .3; a2 = .2;

tama_delay = n2;
vetor_delay = zeros(tama_delay ,1);

% Definindo a entrada
entrada = zeros(2*tama_delay,1);

entrada(1,1) = 1; % definindo o impulso unitário
tama_loop = length(entrada);
vet_saida = zeros(tama_loop,1);

for j = 1: tama_loop
    input = entrada(j,1);
    
    vetor_delay(1,1) = input;
    
    y = a0* vetor_delay(1,1) + a1 *  vetor_delay(n1,1) + a2 *  vetor_delay(n2,1);
    
    % Desloca o vetor de delay
    for k = 0: tama_delay-2
                vetor_delay(tama_delay-k,1) =  vetor_delay(tama_delay-k-1,1); 
    end   
    
    vet_saida(j,1) = y;
end    

stem(vet_saida)

title('Teste Delay');

