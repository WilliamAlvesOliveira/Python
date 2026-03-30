lar = float(input('Qual é a largura da parede: '))
alt = float(input('Qual é a altura da parede: '))
área = lar*alt
print('Sua parede tem a dimensão de {}x{}, e sua área é de {}m²'.format(lar,alt,área))
tinta = área/2
print('para pintar essa parede você vai precisar de {} latas de tinta'.format(tinta))