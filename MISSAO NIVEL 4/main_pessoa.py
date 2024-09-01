from pessoa import Pessoa

# Instanciando o objeto da classe Pessoa
pessoa1 = Pessoa("João", "2000-01-01", "000.111.222-33", "15975388-1", False)

# Obtendo os atributos do objeto
attrs = vars(pessoa1)

# Imprimindo os atributos do objeto
print('Instância da classe Pessoa:')
print(', '.join("%s: %s" % item for item in attrs.items()))

# Alterando os valores usando os setters
try:
    pessoa1.nome = "Ana"
    pessoa1.data_nascimento = "1995-05-05"
    pessoa1.cpf = "1234567890"  # CPF com menos de 14 caracteres
    pessoa1.rg = "98765432-1"
    pessoa1.status = True
except ValueError as e:
    print(f"\nErro ao definir CPF: {e}")

# Imprimindo os atributos após as alterações
attrs = vars(pessoa1)
print('\nAtributos após as alterações:')
print(', '.join("%s: %s" % item for item in attrs.items()))
