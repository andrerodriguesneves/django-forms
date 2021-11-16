def origem_destino_iguais(origem, destino, lista_de_erros):
    """   verifica se origem e destino são iguais
    :param origem:
    :param destino:
    :param lista_de_erros:
    :return:
    """
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino não podem ser iguais!'


def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """ Verifica se possui algum caracter numérico

    :param valor_campo:
    :param nome_campo:
    :param lista_de_erros:
    :return:
    """
    if any(char.isdigit() for char in valor_campo):
       lista_de_erros[nome_campo] = 'Não inclua números nesse campo!'