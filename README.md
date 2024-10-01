Descrição do Projeto
Este repositório contém soluções para um conjunto de problemas relacionados à programação. Os exercícios abordam conceitos de sequência de Fibonacci, manipulação de strings, lógica de programação e raciocínio lógico. Os códigos foram implementados em Python, mas podem ser adaptados para outras linguagens conforme a necessidade.

Problemas Resolvidos
1. Sequência de Fibonacci
Escreva um programa que calcula a sequência de Fibonacci a partir de um número informado pelo usuário. O programa deve retornar uma mensagem indicando se o número pertence ou não à sequência. A sequência de Fibonacci se inicia em 0 e 1, e cada próximo valor é a soma dos dois anteriores.

Exemplo de Saída:

Informe um número: 8\
O número 8 pertence à sequência de Fibonacci.

2. Contagem de Letras
Crie um programa que verifica a existência da letra 'a' (tanto maiúscula quanto minúscula) em uma string fornecida e conta quantas vezes essa letra ocorre.

Exemplo de Saída:

Informe uma string: A casa é azul.\
A letra 'a' aparece 3 vezes.


3. Cálculo de Soma
Dado o trecho de código abaixo, calcule o valor da variável SOMA ao final do processamento:
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

Resposta: Ligaria o primeiro interruptor, deixaria um tempo ligado e depois desligaria. Iria até a sala e veria qual lâmpada está quente. A lâmpada quente faria referência àquele interruptor.
Depois, voltaria à sala, ligaria mais um interruptor e esperaria. Voltaria e faria o mesmo procedimento, descobrindo qual lâmpada está quente;
assim, a lâmpada quente estaria associada àquele interruptor.No fim, por já ter descoberto dois interruptores, deduziria que o interruptor que não mexi estaria associado à lâmpada que não aqueceu.
Poderia tambem, caso possível, ligar um interruptor, ir à sala verificar a lâmpada acesa e, então, associá-la àquele interruptor. Depois, voltaria,
apagaria o interruptor e ligaria outro, indo à sala para verificar a outra lâmpada acesa, associando-a a esse interruptor. No fim, por já ter descoberto dois interruptores,
deduziria que o interruptor que não mexi estaria associado à lâmpada que não acendeu.

git clone https://github.com/seu_usuario/nome_do_repositorio.git
Navegue até o diretório do projeto:
bash
Copiar código
cd nome_do_repositorio
Execute os scripts em Python ou em outra linguagem que desejar utilizar.
