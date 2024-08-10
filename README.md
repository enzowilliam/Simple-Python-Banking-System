Simple Python Banking System
Este projeto é parte do desafio do curso de Formação Python Developer da Digital Innovation One (DIO). O sistema é uma aplicação simples de banco desenvolvida em Python, onde os usuários podem realizar operações básicas como depósitos, saques e visualização de extrato.

Funcionalidades
Depósito: Permite ao usuário adicionar fundos à sua conta bancária.
Saque: Permite ao usuário retirar fundos de sua conta, com limitações diárias e de valor.
Extrato: Exibe todas as transações realizadas (depósitos e saques) e o saldo atual da conta.
Sair: Finaliza a execução do sistema.

Requisitos
Python 3.6 ou superior

Como executar
1. Clone o repositório ou copie o código para sua máquina local.
  git clone https://github.com/enzowilliam/Simple-Python-Banking-System.git

2. Navegue até o diretório do projeto.
  cd simple-python-banking-system

3. Execute o arquivo Python.
  python3 banking_system.py



Após iniciar o sistema, você verá o seguinte menu:

[d] = Depositar
[s] = Sacar
[e] = Extrato
[q] = Sair

Depósito: Pressione d para depositar. Você será solicitado a inserir o valor a ser depositado.
Saque: Pressione s para sacar. O sistema solicitará o valor a ser sacado e verificará o saldo disponível, o limite de saques diários e o limite de valor para saques.
Extrato: Pressione e para visualizar o extrato de todas as transações realizadas e o saldo atual.
Sair: Pressione q para encerrar o programa.

Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
