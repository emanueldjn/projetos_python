# Objetivo Geral

separar as funções existentes de saque, depósito e extrato em funções. 
Criar duas novas funções: Cadastras usuário(cliente); Cadastrar conta bancária

# Desafio

Deixar o codgio mais modularizado, para isso, devemos criar funções para as operações existentes

1- sacar
2- depositar
3- visualizar histórico (extrato)

Além disso, para a versão 2, precisamos criar duas novas funções: 

1- criar usuário(cliente do banco)
2- criar conta corrente(vincular com o usuário)

# função saque 
deve receber argumentos apenas por nome(keyword only)
sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.
sugestão de retorno: saldo e extrato.

# Extrato
deve receber os argumentos por posição e nome (positional only e keyword only).
argumentos posicionais: saldo, argumentos nomeados: extrato

# Novas Funções
2 novas funções: criar usuario, criar conta corrente. 
fique livre para adicionar mais funções.
Ex: listar conta, listar usuario, inativar conta 

# Criar Usuário - cliente 
deve armazenar os usuarios em uma LISTA.
nome, data de nascimento, cpf e endereço. O endereço é uma string com formato: Logradouro - nro - bairro - cidade/sigla estado.
deve ser armazenado somente os números do CPF. 
NÂO PODEMOS CADASTRAR USUÁRIOS COM O MESMO CPF.

# Criar Conta Corrente
Armazenar contas em uma lista. 
Agência, numero de conta e usuário. 
O numero de conta é sequencial, iniciando em 1. 
Numero de agência é fixo: "001".
usuario pode ter mais de uma conta, mas uma conta pertence somente a um usuário.

# Dica
para vincular um usuário a uma conta, filtre a lista de usuário buscando o número do CPF informado para cada usuário da lista.