Descrição do Projeto
Este repositório contém soluções para um conjunto de problemas relacionados à programação. Os exercícios abordam conceitos de sequência de Fibonacci, manipulação de strings, lógica de programação e raciocínio lógico. Os códigos foram implementados em Python, mas podem ser adaptados para outras linguagens conforme a necessidade.

Problemas Resolvidos
1. Sequência de Fibonacci
Escreva um programa que calcula a sequência de Fibonacci a partir de um número informado pelo usuário. O programa deve retornar uma mensagem indicando se o número pertence ou não à sequência. A sequência de Fibonacci se inicia em 0 e 1, e cada próximo valor é a soma dos dois anteriores.

Exemplo de Saída:

mathematica
Copiar código
Informe um número: 8
O número 8 pertence à sequência de Fibonacci.
2. Contagem de Letras
Crie um programa que verifica a existência da letra 'a' (tanto maiúscula quanto minúscula) em uma string fornecida e conta quantas vezes essa letra ocorre.

Exemplo de Saída:

less
Copiar código
Informe uma string: A casa é azul.
A letra 'a' aparece 3 vezes.
3. Cálculo de Soma
Dado o trecho de código abaixo, calcule o valor da variável SOMA ao final do processamento:

c
Copiar código
int INDICE = 12, SOMA = 0, K = 1;
enquanto K < INDICE faça {
    K = K + 1;
    SOMA = SOMA + K;
}
imprimir(SOMA);
Resposta: O valor final de SOMA será 77.

4. Complete a Lógica
Complete os próximos elementos das sequências a seguir:

a) 1, 3, 5, 7, ___ (Resposta: 9)\
b) 2, 4, 8, 16, 32, 64, ____ (Resposta: 128)\
c) 0, 1, 4, 9, 16, 25, 36, ____ (Resposta: 49)\
d) 4, 16, 36, 64, ____ (Resposta: 100)\
e) 1, 1, 2, 3, 5, 8, ____ (Resposta: 13)\
f) 2, 10, 12, 16, 17, 18, 19, ____ (Resposta: 20)
5. Interruptores e Lâmpadas
Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. O objetivo é descobrir qual interruptor controla cada lâmpada em apenas duas idas à sala das lâmpadas.

Solução:

Ligue o primeiro interruptor e deixe-o ligado por alguns minutos.
Desligue-o e vá até a sala das lâmpadas. A lâmpada quente corresponde ao primeiro interruptor.
Volte à sala, ligue o segundo interruptor e vá até a sala novamente. A lâmpada acesa corresponde ao segundo interruptor.
A lâmpada fria será associada ao terceiro interruptor.
Instruções de Uso
Clone este repositório:
bash
Copiar código
git clone https://github.com/seu_usuario/nome_do_repositorio.git
Navegue até o diretório do projeto:
bash
Copiar código
cd nome_do_repositorio
Execute os scripts em Python ou em outra linguagem que desejar utilizar.