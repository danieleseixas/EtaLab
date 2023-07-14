from src.phonebook import Phonebook

phonebook = Phonebook()


print("#Primeiro teste- adicionando Saude")

name_1 = 'Saude'
number_1 = '110'

phonebook = Phonebook()
resultado = phonebook.add(name_1, number_1)

print(resultado)

print("#Segundo teste - tentando adicionar #")
name_1 = '#'
number_1 = '120'

phonebook = Phonebook()
resultado = phonebook.add(name_1, number_1)

print(resultado)

print("#Terceiro teste -  adicionar @")
name_1 = '@'
number_1 = '120'

phonebook = Phonebook()
resultado = phonebook.add(name_1, number_1)

print(resultado)

print("#Quarto teste -  adicionar !")
name_1 = '!'
number_1 = '120'

phonebook = Phonebook()
resultado = phonebook.add(name_1, number_1)

print(resultado)

print("#Quinto teste -  adicionar $")
name_1 = '$'
number_1 = '120'

phonebook = Phonebook()
resultado = phonebook.add(name_1, number_1)

print(resultado)

print("#Sexto teste -  adicionar %")
name_1 = '%'
number_1 = '120'

phonebook = Phonebook()
resultado = phonebook.add(name_1, number_1)

print(resultado)

# usando o len verificar posteriormente

print("#Setimo teste - Adicionando um numero menor que 0")
name_1 = 'a'
number_1 = []

phonebook = Phonebook()
resultado = phonebook.add(name_1, number_1)

print(resultado)


print("#Oitavo teste - pesquisando por #")
name_1 = '# '
number_1 = '345'

phonebook = Phonebook()
resultado = phonebook.lookup(name_1)
print(name_1)
print(resultado)

print("#Nono teste - pesquisando por @")
name_1 = '@ '
number_1 = '345'

phonebook = Phonebook()
resultado = phonebook.lookup(name_1)
print(name_1)
print(resultado)

print("#Decimo teste - pesquisando por !")
name_1 = '! '
number_1 = '345'

phonebook = Phonebook()
resultado = phonebook.lookup(name_1)
print(name_1)
print(resultado)

print("#Decimo primeiro teste - pesquisando por $")
name_1 = '$'
number_1 = '345'

phonebook = Phonebook()
resultado = phonebook.lookup(name_1)
print(name_1)
print(resultado)

print("#Decimo segundo teste - pesquisando por %")
name_1 = '% '
number_1 = '345'

phonebook = Phonebook()
resultado = phonebook.lookup(name_1)

print(resultado)

print("#Decimo terceiro teste - pesquisando por Silva")
name_5 = 'Silva'
number_5 = '4990'
name_6 = 'Ferreira'
number_6 = '451'

resultado = phonebook.add(name_5, number_5)
resultado = phonebook.add(name_6, number_6)
resultado_consulta5 = phonebook.lookup(name_5)
print(resultado_consulta5)

print("#Decimo quarto teste - pesquisando por nome vazio")
name_1 = None
number_1 = '400'

resultado_consulta = phonebook.lookup(name_1)
print(resultado_consulta)

print("#Decimo quinto teste - pesquisando por nome inexiste na lista")
name_1 = 'Gal'
number_1 = '400'

resultado_consulta = phonebook.lookup(name_1)
print(resultado_consulta)

print("#Decimo sexto teste - exibir todos nomes ")

resultado_consulta = phonebook.get_names()
print(resultado_consulta)

print("#Decimo setimo teste - exibir todos numeros ")

resultado_consulta = phonebook.get_numbers()
print(resultado_consulta)

print("#Decimo oitavo teste - limpar todo phonebook ")

resultado_consulta = phonebook.clear()
print(resultado_consulta)

print("#Decimo nono teste - pesquisar por um nome que está na dicionário e retornar uma lista com nome e numero ")

name = 'JOANA'
number = '3567'
name1 = 'GAL'
number1 = '99'
name2 = 'JOANA SILVA'
number2 = '3988'
search_name = 'JOANA'

resultado = phonebook.add(name, number)
resultado = phonebook.add(name1, number1)
resultado = phonebook.add(name2, number2)
resultado_consulta = phonebook.search(search_name)
print(resultado_consulta)

print("#Vigesimo teste - Ordenar o phonebook ")

name = 'JOANA'
number = '3567'
name1 = 'GAL'
number1 = '99'
name2 = 'KAIO'
number2 = '876'

resultado = phonebook.add(name, number)
resultado = phonebook.add(name1, number1)
resultado = phonebook.add(name2, number2)
resultado_ordenacao = phonebook.get_phonebook_sorted()
print(resultado_ordenacao)


print("#Vigesimo primeiro teste - Reverse o phonebook ")

name = 'JOANA'
number = '3567'
name1 = 'GAL'
number1 = '99'
name2 = 'KAIO'
number2 = '876'

resultado = phonebook.add(name, number)
resultado = phonebook.add(name1, number1)
resultado = phonebook.add(name2, number2)
resultado_ordenacao = phonebook.get_phonebook_reverse()
print(resultado_ordenacao)

print("#Vigesimo segundo teste - deletar numero ")

name = 'JOANA'
number = '3567'
name1 = 'GAL'
number1 = '99'
name2 = 'KAIO'
number2 = '876'

resultado = phonebook.add(name, number)
resultado = phonebook.add(name1, number1)
resultado = phonebook.add(name2, number2)
resultado_deletado = phonebook.delete(name1)
print(resultado_deletado)
