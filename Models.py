from datetime import datetime

class Categoria:
    def __init__(self, categoria) -> None:
        self.categoria = categoria
        
class Produtos:
    def __init__(self, nome, preco, categoria) -> None:
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        
class Estoque:
    def __init__(self, produto: Produtos, quantidade) -> None:
        self.produto = produto
        self.quantidade = quantidade

class Venda:
    def __init__(self, itensVendido: Produtos, vendedor, comprador, quantidadeVendida, data = datetime.now().strftime("%d/%m/%Y")) -> None:
        self.itensVendido = itensVendido
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidadeVendida = quantidadeVendida
        self.data = data

class Fornecedor:
    def __init__(self, nome, cnpj, telefone, categoria) -> None:
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria

class Pessoa:
    def __init__(self, nome, cpf, telefone, email, endereco) -> None:
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        
class Funcionario(Pessoa):
    def __init__(self, nome, cpf, telefone, email, endereco, clt) -> None:
        super().__init__(nome, cpf, telefone, email, endereco)
        self.clt = clt
        
