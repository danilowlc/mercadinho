from Models import *

class CategoriaDAO:
    
    @classmethod
    def salvar(cls, categoria):
        with open('./dados/categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')
            
    @classmethod
    def ler(cls):
        with open('./dados/categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()
        
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))
        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))
        
        return cat


class VendaDAO:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('./dados/venda.txt', 'a') as arq:
            arq.writelines(venda.itensVendido.nome + '|' +
                           str(venda.itensVendido.preco) + '|' +
                           venda.itensVendido.categoria + '|' +
                           venda.vendedor + '|' +
                           venda.comprador + '|' +
                           str(venda.quantidadeVendida) + '|' +
                           venda.data)
            arq.writelines('\n')


    @classmethod
    def ler(cls):
        with open('./dados/venda.txt', 'r') as arq:
            cls.venda = arq.readlines()
        
        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))
        
        vendas = []
        for i in cls.venda:
            vendas.append(Venda(
                            Produtos(i[0], i[1], i[2]),
                            i[3], i[4], i[5], i[6]
                            )
                        )
        
        return vendas


class EstoqueDAO:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('./dados/estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + '|' +
                           str(produto.preco) + '|' +
                           produto.categoria + '|' +
                           str(quantidade))
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('./dados/estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()
            
        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
        
        iventario = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                iventario.append(Estoque(
                                    Produtos(i[0], i[1], i[2]),
                                    int(i[3])
                                    )
                                )
        return iventario


class FornecedorDAO:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('./dados/fornecedores.txt', 'a') as arq:
            arq.writelines(fornecedor.nome + '|' +
                           fornecedor.cnpj + '|' +
                           fornecedor.telefone + '|' +
                           fornecedor.categoria)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('./dados/fornecedores.txt', 'r') as arq:
            cls.fornecedor = arq.readlines()
            
        cls.fornecedor = list(map(lambda x: x.replace('\n', ''), cls.fornecedor))
        cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))
        
        fornecedores = []
        for i in cls.fornecedor:
            fornecedores.append(Fornecedor(i[0], i[1], i[2], i[3]))
        
        return fornecedores

class PessoaDAO:
    @classmethod
    def salvar(cls, pessoas: Pessoa):
        with open('./dados/clientes.txt', 'a') as arq:
            arq.writelines(pessoas.nome + '|' +
                           pessoas.cpf, + '|' +
                           pessoas.telefone + '|' +
                           pessoas.email + '|' +
                           pessoas.endereco)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('./dados/clientes.txt', 'r') as arq:
            cls.cliente = arq.readlines()
        
        cls.cliente = list(map(lambda x: x.replace('\n', ''), cls.cliente))
        cls.cliente = list(map(lambda x: x.split('|'), cls.cliente))
        
        clientes = []
        for i in cls.cliente:
            clientes.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
        
        return clientes

class FuncionarioDAO:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('./dados/funcionarios.txt', 'a') as arq:
            arq.writelines(funcionario.nome + '|' +
                           funcionario.cpf, + '|' +
                           funcionario.telefone + '|' +
                           funcionario.email + '|' +
                           funcionario.endereco + '|' +
                           funcionario.clt)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('./dados/funcionarios.txt', 'r') as arq:
            cls.funcionario = arq.readlines()
        
        cls.funcionario = list(map(lambda x: x.replace('\n', ''), cls.funcionario))
        cls.funcionario = list(map(lambda x: x.split('|'), cls.funcionario))
        
        funcionarios = []
        for i in cls.funcionario:
            funcionarios.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))
        
        return funcionarios