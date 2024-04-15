// Objetivo Geral

Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato. 

// Desafio:

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja moderniar suas
operações e para isso escolheu Python. Para a primeira versão do sistema, devemos implementar apenas 3 
operações: deposito, saque e extrato. 

// Operação de Deposito  

Deve ser permitido depositar valores positivos para a minha conta.
a v1 do projeto trabalha apenas com 1 usuario. Dessa forma, não precisamos nos preocupar em identificar qual é
o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variavel e exibidos na
operação de extrato. 

// Operação de saque:

Deve permitir realizar 3 saques diários com *limite maximo de R$500,00 por saque*. Caso o usuario não tem saldo em
conta, o sistema deve exibir uma mensagem informando que não será possivel sacar o dinheiro por falta de saldo.
Todos os saques devem ser armazenados em uma variavel e exibidos na operação de extrato.

// Operação de extrato:

Essa operação deve listar todos os depositos e saques realizados na conta. No fim da listagem, deve ser exibido o saldo atual da conta.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx 
ex: 1500.45 = R$1500.45