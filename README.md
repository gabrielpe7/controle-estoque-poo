# Sistema de Controle de Estoque (POO)

Aplicação de linha de comando (CLI) em Python para controle de estoque de produtos, com regras de entrada e saída, alertas de estoque baixo e relatório resumido, desenvolvida como projeto de estudo aplicando Programação Orientada a Objetos.

## Funcionalidades

- Cadastro de produtos (nome, preço e quantidade)
- Registro de entrada e saída de estoque, com validação de quantidade disponível
- Alerta automático de estoque baixo na listagem de produtos
- Relatório com valor total investido em estoque e produtos com estoque baixo
- Persistência de dados em banco de dados SQLite

## Tecnologias utilizadas

- **Python 3** (Programação Orientada a Objetos)
- **SQLite** (via módulo `sqlite3`, nativo do Python)

## Estrutura do projeto

```
controle-estoque-poo/
├── main.py       # menu principal e fluxo do programa
├── produto.py    # classe Produto (atributos e regras de negócio)
└── banco.py      # funções de persistência em SQLite
```

## Sobre o projeto

Este projeto foi construído em etapas, aplicando na prática conceitos de Análise e Desenvolvimento de Sistemas:

1. **Programação Orientada a Objetos** — modelagem da classe `Produto`, com atributos e métodos próprios (cálculo de valor total, entrada e saída de estoque)
2. **Persistência de objetos** — conversão entre objetos Python e registros de banco de dados relacional
3. **Regras de negócio** — validação de estoque disponível antes de uma saída, e alerta automático de estoque baixo
4. **Código organizado em múltiplos arquivos**, cada um com uma responsabilidade clara

## Como executar

Pré-requisito: ter o [Python 3](https://www.python.org/) instalado.

```bash
# Clone o repositório
git clone https://github.com/gabrielpe7/controle-estoque-poo.git

# Entre na pasta do projeto
cd controle-estoque-poo

# Execute o programa
python main.py
```

## Como usar

Ao rodar o programa, um menu é exibido no terminal:

```
=== CONTROLE DE ESTOQUE ===
1 - Cadastrar produto
2 - Listar produtos
3 - Registrar entrada
4 - Registrar saída
5 - Gerar relatório
6 - Sair
```

Basta digitar o número da opção desejada e seguir as instruções na tela.

## Possíveis melhorias futuras

- Categorias de produtos
- Histórico de movimentações (entradas e saídas) com data e hora
- Exportação do relatório em Excel ou PDF
- Interface gráfica

## Autor

Desenvolvido por Gabriel Pereira de Oliveira — estudante de Análise e Desenvolvimento de Sistemas.

[LinkedIn](https://www.linkedin.com/in/gabriel-pereira-de-oliveira-ba1a06316/) · [GitHub](https://github.com/gabrielpe7)
