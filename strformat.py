"""
Módulo de formatação de strings
strformat.py
"""

def frmt_bytes(numero): # dado um número inteiro, converte e formata em Bytes, KB, MG ou GB
    # numformat = " "
    if numero < 1024:
        # numformat = "O tamanho é {}B".format(numero)
        return '%dB' % (numero) # forma mais simples de fazer a linha de cima
    elif numero < (1024 * 1024):
        # numformat = "O tamanho é {}KB".format((numero/1024))
        return '%.1fKB' % (numero / 1024) # forma mais simples de fazer a linha de cima
    elif numero < (1024 * 1024 * 1024):
        # numformat = "O tamanho é {}MB".format((numero/1024/1024))
        return '%.1fMB' % (numero / 1024 / 1024) # forma mais simples de fazer a linha de cima
    else:
        # numformat = "O tamanho é {}GB".format((numero/1024/1024/1024))
        return '%.1fGB' % (numero / 1024 / 1024 / 1024) # forma mais simples de fazer a linha de cima
    # return numformat

def strip_html(txthtml): # retira todo o código html de uma linha de código, devolvendo só o texto
    car = ''
    tam = len(txthtml)
    i = 0
    while i < tam:
        if txthtml[i] == '<':
            while txthtml[i] != '>':
                i += 1
            i += 1
        else:
            car += txthtml[i]
            i +=1
        
    return car.strip() # o método .strip() retira caracteres em branco antes e depois do texto, se houverem

""" inicialização do módulo """
print("Inicializando o módulo strformat") # colocado só pra efeito ilustrativo do exemplo de módulo externo