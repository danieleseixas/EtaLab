class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        if '#' in name:
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '@' in name:

            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '!' in name:
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '$' in name:
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '%' in name:
            msg = 'Nome `{}` invalido'.format(name)
            return msg

        if len(number) == 0:

            msg = 'Nome `{}` invalido'.format(number)
            return msg
        if name not in self.entries:
            self.entries[name] = number
        # adicionado um complemento na infomração enviadda ao usuario
        msg = 'Numero adicionado - `{}` '.format(self.entries[name])
        return msg
    # bug1 na linha 17 - palavra Nme esperava Nome
    # bug2 na linha 24 - palavra 'invalio' - trocada por invalido
    # bug4 na linha31  -# bug invalid - esperava invalido
    # bug5 na linha a condição era se o tamanho era 'menor' foi corrigido para 'igual' para atender a condição
    # Refatoração - foi usado uma variável para padronizar os returnos das condições

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """

        if name is None:
            msg = 'Não é permitido nome vazio'
            return msg
        if '#' in name:

            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '@' in name:
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '!' in name:

            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '$' in name:
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '%' in name:

            msg = 'Nome `{}` invalido'.format(name)
            return msg

        for name_pesquisa in self.entries.keys():
            if name_pesquisa == name:
                msg = 'Numero retornado: `{}` '.format(self.entries[name])
                return msg
        msg = 'Nome `{}` não encontado'.format(name)
        return msg

    # bug - linha 56  palavra 'invaldo' - trocada por 'invalido'
    # bug - linha 63 palavra 'Nme' trocada por 'Nome'
    # bug - linha 70 - palavra 'nvalido' trocada por 'invalido'
    # Refatoração linha 73 -inserido uma verificação para consulta um name na lista e retorna o numero
    # Refatoração linha 51 - inserido uma verificação para name vazio
    # Refatoração - foi usado uma variável para padronizar os returnos das condições

    def get_names(self):
        """
        :return: return all names in phonebook
        """
        msg = 'Nomes retornados: `{}` '.format(self.entries.keys())
        return msg
    # Refatoração - foi usado uma variável para padronizar os returnos das condições

    def get_numbers(self):
        """
        :return: return all numbers in phonebook
        """
        msg = 'Nomes retornados: `{}` '.format(self.entries.values())
        return msg

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpo'
        """
        self.entries = {}
        return 'phonebook limpo'
    # Refatoração - trocado a palavra 'limpado' por 'limpo

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():

            if search_name in name:
                result.append({name, number})
        return result

    # Refatoração foi removido o 'not' da função, pois não estava retornando o resultado esperado

    def get_phonebook_sorted(self):
        """
        :return: return phonebook in sorted order
        """
        print(self.entries)
        return dict(sorted(self.entries.items()))
    # refatoração -realizada uma validação para que retornasse o phonebook ordenado

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        return dict(sorted(self.entries.items(), reverse=True))

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        msg = 'Numero deletado - {} '.format(self.entries[name])
        self.entries.pop(name)
        return msg
    # Refatoração - foi usado uma variável para padronizar os returnos das condições
