class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def valor_total(self):
        return self.preco * self.quantidade
    
estoque = []

from produto import Produto
from banco import criar_tabela, inserir_produto, listar_produtos_bd, atualizar_quantidade


def cadastrar_produto():
    nome = input("Nome do produto:")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))
    
    novo_produto = Produto(nome, preco, quantidade)
    inserir_produto(novo_produto)
    print("Produto cadastrado!\n")
        
def listar_produtos():
    produtos = listar_produtos_bd()
    
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.\n")
        return
        
    for produto in produtos:
            alerta = " (ESTOQUE BAIXO!)" if produto.quantidade < 10 else ""
            print(f"{produto.nome} - {produto.quantidade} un. - Valor total: R$ {produto.valor_total():.2f}{alerta}")
    print()
        
def escolher_produto():
    produtos = listar_produtos_bd()
    
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.\n")
        return None
    
    for indice, produto in enumerate(produtos):
        print(f"{indice} - {produto.nome} ({produto.quantidade} un.)")
        
    escolha = input("Escolha o número do produto: ")
    
    if not escolha.isdigit() or int(escolha) not in range(len(produtos)):
        print("Opção inválida.\n")
        return None
    
    return produtos[int(escolha)]

def entrada_estoque():
    produto = escolher_produto()
    
    if produto is None:
        return
    
    quantidade = int(input("Quantidade a adicionar: "))
    produto.registrar_entrada(quantidade)
    atualizar_quantidade(produto.id, produto.quantidade)
    
    print(f"Estoque atualizado! {produto.nome} agora tem {produto.quantidade} un.\n")
    
def saida_estoque():
    produto = escolher_produto()
    
    if produto is None:
        return
    
    quantidade = int(input("Quantidade a retirar: "))
    sucesso = produto.registrar_saida(quantidade)
    
    if not sucesso:
        print("Quantidade insuficiente em estoque.\n")
        return
    
    atualizar_quantidade(produto.id, produto.quantidade)
    print(f"Estoque atualizado! {produto.nome} agora tem {produto.quantidade} un.\n")

def gerar_relatorio():
    produtos = listar_produtos_bd()
    
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.\n")
        return
    
    valor_total_estoque = sum(produto.valor_total() for produto in produtos)
    produtos_baixo_estoque = [produto for produto in produtos if produto.quantidade < 10]
    
    print("=== RELATÓRIO DE ESTOQUE ===")
    print(f"Total de produtos cadastrados: {len(produtos)}")
    print(f"Valor total investido em estoque: R$ {valor_total_estoque:.2f}")
    
    if produtos_baixo_estoque:
        print(f"\nProdutos com estoque baixo ({len(produtos_baixo_estoque)}):")
        for produto in produtos_baixo_estoque:
            print(f"- {produto.nome}: {produto.quantidade} un.")
    else:
        print("\nNenhum produto com estoque baixo.")
    print()

def menu():
    while True:
        print("=== CONTROLE DE ESTOQUE ===")
        print("1 - Cadastrar produto")
        print("2 - Listas produtos")
        print("3 - Registrar entrada")
        print("4 - Registrar saida")
        print("5 - Gerar relatório")
        print("6 - Sair")
            
        opcao = input("Escolha uma opção: ").strip()
            
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            entrada_estoque()
        elif opcao == "4":
            saida_estoque()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "6":
            print("Até mais!")
            break
        else:
            print("Opção inválida.\n")
                
criar_tabela()
menu()