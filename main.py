# dicionário
pessoa ={
    'Nome':'Pri Pedrette',
    'Idade': 36,
    'Profissão': 'Geografa',
}

nova_chave = input('digite o nome do campo: ')
novo_valor = input('Informe o valor do novo campo: ')
pessoa[nova_chave] = novo_valor
pessoa['Empresa'] = input('Empresa:')

# exibe os dados
for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')
