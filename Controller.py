from Models import *
from DAO import *
from datetime import datetime

class CategoriaController:
    def cadastraCategoria(self, novaCategoria):
        isCategoria = False
        categorias = CategoriaDAO.ler()
        for categoria in categorias:
            if categoria.categoria == novaCategoria:
                isCategoria = True

        if not isCategoria:
            CategoriaDAO.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso')
        else:
            print('Categoria já existe')

    def removerCategoria(self, categoriaRemover):
        categorias = CategoriaDAO.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, categorias))

        if len(cat) <= 0:
            print('A categoria não existe')
        else:
            for i in range(len(categorias)):
                if categorias[i].categoria == categoriaRemover:
                    del categorias[i]
                    break
            
            print('Categoria remova com sucesso')

            with open('./dados/categoria.txt', 'w') as arq:
                for i in categorias:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')
        
        estoque = EstoqueDAO.ler()
        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, 'Sem Categoria'), x.quantidade) 
                           if(x.produto.categoria == categoriaRemover) else (x), estoque))
        with open('./dados/estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + '|' +
                                str(i.produto.preco) + '|' +
                                i.produto.categoria + '|' +
                                str(i.quantidade))
                arq.writelines('\n')
    
    def alterarCategoria(self, categoriaAtual, categoriaNova):
        x = CategoriaDAO.ler()
        
        cat = list(filter(lambda x: x.categoria == categoriaAtual, x))
        
        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaNova, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaNova) if(x.categoria == categoriaAtual) else(x), x))
                print('Alteração realizada com sucesso')
                
                estoque = EstoqueDAO.ler()
                estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, categoriaNova), x.quantidade) 
                                if(x.produto.categoria == categoriaAtual) else (x), estoque))
                
                with open('./dados/estoque.txt', 'w') as arq:
                    for i in estoque:
                        arq.writelines(i.produto.nome + '|' +
                                        str(i.produto.preco) + '|' +
                                        i.produto.categoria + '|' +
                                        str(i.quantidade))
                        arq.writelines('\n')
                        
            else: print('A categoria já existe')
        else:
            print('A categoria não existe')
        
        with open('./dados/categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def show(self):
        categorias = CategoriaDAO.ler()
        if len(categorias) == 0:
            print("Nao existe categoria cadastrada")
        else:
            for categoria in categorias:
                print(f'Categoria: {categoria.categoria}')

class EstoqueController:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = EstoqueDAO.ler()
        y = CategoriaDAO.ler()
        h = list(filter(lambda x: x.categoria == categoria, y))
        estoque = list(filter(lambda x: x.produto.nome == nome, x))
        if len(h) > 0:
            if len(estoque) == 0:
                produto = Produtos(nome, preco, categoria)
                EstoqueDAO.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso')
            else:
                print('Produto já existe no estoque')
        else:
            print('Categoria inexistente')
    
    
    def removeProduto(self, nome):
        x = EstoqueDAO.ler()
        estoque = list(filter(lambda x: x.produto.nome == nome, x))
        if len(estoque) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i] 
                    break
            print('Produto removido com sucesso')
        else:
            print('O produto não existe')
            
        with open('./dados/estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + '|' +
                                str(i.produto.preco) + '|' +
                                i.produto.categoria + '|' +
                                str(i.quantidade))
                arq.writelines('\n')
    
    def alterarProduto(self, nomeAtual, nomeNovo, precoNovo, categoriaNovo, quantidadeNovo):
        x = EstoqueDAO.ler()
        y = CategoriaDAO.ler()
        h = list(filter(lambda x: x.categoria == categoriaNovo, y))
        
        if len(h) > 0:
            estoque = list(filter(lambda x: x.produto.nome == nomeAtual, x))
            if len(estoque) > 0:
                estoque = list(filter(lambda x: x.produto.nome == nomeNovo, x))
                if len(estoque) == 0:
                    x  = list(map(lambda x: Estoque(Produtos(nomeNovo, precoNovo, categoriaNovo), quantidadeNovo) if (x.produto.nome == nomeAtual) else(x), x))
                    print('Produto alterado com sucesso')
                else:
                    print('Produto já cadastrado')
            else:
                print('O produto não existe')
            
            with open('./dados/estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + '|' +
                                str(i.produto.preco) + '|' +
                                i.produto.categoria + '|' +
                                str(i.quantidade))
                    arq.writelines('\n')
        else:
            print('A categoria não existe')
    
    
    def show(self):
        estoques = EstoqueDAO.ler()
        if len(estoques) == 0:
            print("Estoque vazio")
        else:
            print('=========Produtos=========')
            for estoque in estoques:
                print(f'Nome: {estoque.produto.nome}\n'
                      f'Preço: {estoque.produto.preco}\n'
                      f'Categoria: {estoque.produto.categoria}\n'
                      f'Qtd: {estoque.quantidade}')
                print(26*'-')

class VendaController:
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        
        x = EstoqueDAO.ler()
        temp = []
        existe = False
        quantidade = False
        
        for i in x:
            if not existe:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if i.quantidade >= quantidadeVendida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)
                        
                        vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)
                        valorCompra = int(quantidadeVendida) * int(i.produto.preco)

                        VendaDAO.salvar(vendido)
            temp.append(Estoque(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade))
            
        arq = open('./dados/estoque.txt', 'w')
        arq.write('')

        for i in temp:
            with open('./dados/estoque.txt', 'a') as arq:
                arq.writelines(i.produto.nome + '|' + 
                            str(i.produto.preco) + '|' + 
                            i.produto.categoria + '|' + 
                            str(i.quantidade)
                            )
                arq.writelines('\n')

        if not existe:
            print('O produto não existe')
            return None
        elif not quantidade:
            print('Não tem quantidade suficiente')
            return None
        else:
            print('Venda realizada com sucesso')
            return valorCompra
            
    def relatorioProdutos(self):
        vendas = VendaDAO.ler()
        produtos = []
        for i in vendas:
            nome = i.itensVendido.nome
            quantidade = i.quantidadeVendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(quantidade) + int(x['quantidade'])} if (x['produto'] == nome) else(x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': int(quantidade)})
            
        ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)
            
        print('Esses são os produtos mais vendidos')
        a = 1
        for i in ordenado:
            print(f'==========Produto [{a}]==========')
            print(f"Produto: {i['produto']}\n"
                  f"Quantidade: {i['quantidade']}\n")
            a += 1
    
    def relatorioPeriodo(self, dataInicial, dataFinal):
        vendas = VendaDAO.ler()
        dataInicial1 = datetime.strptime(dataInicial, '%d/%m/%Y')
        dataFinal1 = datetime.strptime(dataFinal, '%d/%m/%Y')
        
        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicial1 and datetime.strptime(x.data, '%d/%m/%Y') <= dataFinal1, vendas))

        cont = 1
        total = 0
        for i in vendasSelecionadas:
            print(f"==========Venda [{cont}]==========")
            print(f"Nome: {i.itensVendido.nome}\n"
                  f"Categoria: {i.itensVendido.categoria}\n"
                  f"Data: {i.data}\n"
                  f"Quantidade: {i.quantidadeVendida}\n"
                  f"Preço: {i.itensVendido.preco}\n"
                  f"Total: {int(i.itensVendido.preco) * int(i.quantidadeVendida)}\n"
                  f"Cliente: {i.comprador}\n"
                  f"Vendedor: {i.vendedor}\n")
            total += int(i.itensVendido.preco) * int(i.quantidadeVendida)
            cont += 1
        print(f"Total vendido: {total}")

class FornecedorController:
    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        x = FornecedorDAO.ler()
        listaCNPJ = list(filter(lambda x: x.cnpj == cnpj, x))
        listaTelefone = list(filter(lambda x: x.telefone == telefone, x))
        
        if len(listaCNPJ) > 0:
            print('O CNPJ já existe')
        elif len(listaTelefone) > 0:
            print('O telefone já existe')
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                print("Fornecedor Cadastrado com sucesso")
                FornecedorDAO.salvar(Fornecedor(nome, cnpj, telefone, categoria))
            else:
                print('Digite um CNPJ ou telefone válido')
    
    def alterarFornecedor(self, nomeAtual, nomeNovo, cnpjNovo, telefoneNovo, categoriaNovo):
        x = FornecedorDAO.ler()
        
        est = list(filter(lambda x: x.nome == nomeAtual, x))
        if len(est) > 0:
            est = list(filter(lambda x: x.cnpj == cnpjNovo, x))
            if len(est) == 0:
                x = list(map(lambda x: Fornecedor(nomeNovo, cnpjNovo, telefoneNovo, categoriaNovo) if(x.nome == nomeAtual) else(x), x))
            else:
                print('CNPJ já existe')
        else: 
            print('O fornecedor não existe')
        
        with open('./dados/fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' +
                           i.cnpj + '|' +
                           i.telefone + '|' +
                           i.categoria)
                arq.writelines('\n')
            print("Fornecedor alterado com sucesso")
    
    def removerFornecedor(self, nome):
        x = FornecedorDAO.ler()
        est = list(filter(lambda x: x.nome == nome, x))
        
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print('O Fornecedor não existe')
            return None

        with open('./dados/fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' +
                           i.cnpj + '|' +
                           i.telefone + '|' +
                           i.categoria)
                arq.writelines('\n')
            print('Fornecedor excluido com sucesso')
    
    def show(self):
        fornecedores = FornecedorDAO.ler()
        if len(fornecedores) == 0:
            print("Nao existe esse fornecedor cadastrado")
        else:
            print('==========Fornecedores==========')
            for fornecedor in fornecedores:
                print(f'Fornecedor: {fornecedor.nome}\n'
                      f'Telefone: {fornecedor.telefone}\n'
                      f'CNPJ: {fornecedor.cnpj}\n'
                      f'Categoria: {fornecedor.categoria}')
                print('===============================')

class ClienteController:
    def cadastraCliente(self, nome, cpf, telefone, email, endereco):
        x = PessoaDAO.ler()
        
        listaCPF = list(filter(lambda x: x.cpf == cpf, x))
        
        if len(listaCPF) > 0:
            print('O CPF já existe')
        else:
            if len(cpf) == 11 and len(telefone) <= 11 and len(telefone) >= 10:
                PessoaDAO.salvar(Pessoa(nome, cpf, telefone, email, endereco))
                print("Cliente Cadastrado com sucesso")
            else:
                print('Digite um CPF ou telefone válido')

    def alterarCliente(self, nomeAtual, nomeNovo, cpfNovo, telefoneNovo, emailNovo, enderecoNovo):
        x = PessoaDAO.ler()
        est = list(filter(lambda x: x.nome == nomeAtual, x))
        
        if len(est) > 0:
            x = list(map(lambda x: Pessoa(nomeNovo, cpfNovo, telefoneNovo, emailNovo, enderecoNovo) if (x.nome == nomeAtual) else(x), x))
        else:
            print('O cliente não existe')
        
        with open('./dados/clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' +
                           i.cpf, + '|' +
                           i.telefone + '|' +
                           i.email + '|' +
                           i.endereco)
                arq.writelines('\n')
            print('Cliente alterado com sucesso')
    
    def removerCliente(self, nome):
        x = PessoaDAO.ler()
        est = list(filter(lambda x: x.nome == nome, x))
        
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print('O Cliente não existe')
            return None
        
        with open('./dados/clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' +
                           i.cpf, + '|' +
                           i.telefone + '|' +
                           i.email + '|' +
                           i.endereco)
                arq.writelines('\n')
            print('Cliente excluido com sucesso')
    
    def show(self):
        clientes = PessoaDAO.ler()
        if len(clientes) == 0:
            print('Cliente não cadastrado')
        else:
            print('==========Clientes==========')
            for cliente in clientes:
                print(f'Cliente: {cliente.nome}\n'
                      f'CPF: {cliente.cpf}\n'
                      f'Telefone: {cliente.telefone}\n'
                      f'E-mail: {cliente.email}\n'
                      f'Endereço: {cliente.endereco}')
                print('===============================')

class FuncionarioController:
    def cadastrarFuncionario(self, nome, cpf, telefone, email, endereco, clt):
        x = FuncionarioDAO.ler()
        
        listaCPF = list(filter(lambda x: x.cpf == cpf, x))
        listaCLT = list(filter(lambda x: x.clt == clt. x))
        
        if len(listaCPF) > 0:
            print('CPF já existe')
        elif len(listaCLT) > 0:
            print('CLT já existe')
        else:
            if len(cpf) == 11 and len(telefone) <= 11 and len(telefone) >= 10:
                FuncionarioDAO.salvar(nome, cpf, telefone, email, endereco, clt)
                print('Funcionario cadastrado com sucesso')
            else:
                print('Digite um CPF ou Telefone valido')
        
    def alterarFuncionario(self, nomeAtual, nomeNovo, cpfNovo, telefoneNovo, emailNovo, enderecoNovo, cltNovo):
        x = FuncionarioDAO.ler()
        est = list(filter(lambda x: x.nome == nomeAtual, x))
        
        if len(est) > 0:
            x = list(map(lambda x: Funcionario(nomeNovo, cpfNovo, telefoneNovo, emailNovo, enderecoNovo, cltNovo) if (x.nome == nomeAtual) else(x), x))
        else: 
            print('Funcionario não existe')
        
        with open('./dados/funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' +
                           i.cpf, + '|' +
                           i.telefone + '|' +
                           i.email + '|' +
                           i.endereco + '|' +
                           i.clt)
                arq.writelines('\n')
            print('Funcionario alterado com sucesso')
    
    def removerFuncionario(self, nome):
        x = FuncionarioDAO.ler()
        est = list(filter(lambda x: x.nome == nome, x))
        
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print('Funcionario não existe')
            return None
        
        with open('./dados/funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' +
                           i.cpf, + '|' +
                           i.telefone + '|' +
                           i.email + '|' +
                           i.endereco + '|' +
                           i.clt)
                arq.writelines('\n')
            print('Funcionario excluido com sucesso')
    
    def show(self):
        funcionarios = FuncionarioDAO.ler()
        
        if len(funcionarios) == 0:
            print('Nenhum funcionario cadastrado')
        else:
            print('==========Funcionarios==========')
            for funcionario in funcionarios:
                print(f'Funcionario: {funcionario.nome}\n'
                      f'CPF: {funcionario.cpf}\n'
                      f'Telefone: {funcionario.telefone}\n'
                      f'E-mail: {funcionario.email}\n'
                      f'Endereço: {funcionario.endereco}\n'
                      f'CLT: {funcionario.clt}\n')
                print('===============================')
                
