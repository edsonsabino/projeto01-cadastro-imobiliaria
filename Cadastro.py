from Aluguel import Aluguel
from Imovel import Imovel
from Pessoa import Pessoa

class Cadastro(Pessoa,Imovel, Aluguel):

    var_pessoa=Pessoa()
    var_imovel=Imovel()
    var_aluguel=Aluguel()
    respota=''

    def __init__(self):

        print("O que voce gostaria de fazer ")
        print ("1 - para cadastrar um novo inquilino")
        print ("2 - para cadastrar um novo proprietario")
        print ("3 - para cadastrar um novo imovek")
        print ("4 - para cadastrar um novo Aluguel")
        try:
            self.resposta=int(input("Sua resposta: "))
        except Exception as e:
            print("erro em Cadastro", str(e))

    if self.resposta in [1,2]:
        self.var_pessoa.cadastra_pessoa()
    elif self.resposta == 3:
        self.var_imovel.cadastra_imovel()
    elif self.resposta == 4:
        self.var_aluguel.cadastra_aluguel()
    else:
        print("Algo deu errado")





    
    
   
    