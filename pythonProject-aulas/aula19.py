pessoas= {'nome':'Gustavo','sexo':'M','idade':22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
pessoas["nome"] = 'leandro'
pessoas['peso'] = 85
del(pessoas['sexo'])
print(pessoas)