% Exemplo de amostragem
% Amostra um sinal pseudo continuo e apresenta o sinal amostrado
% Walter 1.0
clear all; close all; clc;

% Sinal analogico
Dt = 5*10^-5; t = -5*10^-3:Dt:5*10^-3;

% Plota o sunal analógico
f = 400; xa = cos(2*pi*f*t);

subplot(2,1,1); plot(t*1000,xa);
xlabel('Tempo [ms]'); 
ylabel('xa(t)');
title(['Sinal de Freq = ', num2str(f),'Hz']);
grid on;  hold on;


% Sinal discreto
Fs = 8000; Ts = 1/Fs;
n = -20:1:20; xd = cos(2*pi*n*f/Fs);
N =length(n);


stem(n*Ts*1000,xd, 'r');  hold off;




% Plota o sinal amostrado

subplot(2,1,2); stem(n,xd);
title('Sinal amostrado');
xlabel('Amostras'); 
ylabel('x[n]');
grid on

