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
            #bug - Nme esperava Nome
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '!' in name:
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '$' in name:
            #bug - invalio - esperava invalido
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '%' in name:
            msg = 'Nome `{}` invalido'.format(name)
            return msg
#a função usando len não está atendendo a verificação esperada
        if len(number) == 0:
            # bug invalid - esperava invalido
            msg = 'Nome `{}` invalido'.format(number)
            return msg
        if name not in self.entries:
            self.entries[name] = number
        #adicionado um complemento na infomração enviadda ao usuario
        msg = 'Numero adicionado - `{}` '.format(self.entries[name])
        return msg

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        # inserido uma verificação para name vazio
        if name is None:
            msg = 'Não é permitido nome vazio'
            return msg
        if '#' in name:
            # bug invaldo - esperava invalido
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '@' in name:
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '!' in name:
            # bug Nme - esperava Nome
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '$' in name:
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '%' in name:
            # bug nvalido - esperava invalido
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        # inserido uma verificação para consulta um name na lista e retorna o numero
        for name_pesquisa in self.entries.keys():
            if name_pesquisa == name:
                msg = 'Numero retornado: `{}` '.format(self.entries[name])
                return msg
        msg = 'Nome `{}` não encontado'.format(name)
        return msg

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        msg = 'Nomes retornados: `{}` '.format(self.entries.keys())
        return msg

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        msg = 'Nomes retornados: `{}` '.format(self.entries.values())
        return msg


    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            #Foi removido o 'not' da função, pois não estava retornando o resultado esperado
            if search_name in name:
                result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        #Foi feito uma validação para que retornasse o phonebook ordenado
        print(self.entries)
        return dict(sorted(self.entries.items()))

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




