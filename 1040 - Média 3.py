n1, n2, n3, n4 = [float(x) for x in input().split(' ')]
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print(f'Media: {media:.1f}')
if media >= 7:
    print('Aluno aprovado.')
elif media >= 5 and media <= 6.9:
    print('Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    media = (media + exame) / 2
    if media >= 5:
        print(f'Aluno aprovado.\nMedia final: {media:.1f}')
    else:
        print('Aluno reprovado.')
else:
    print('Aluno reprovado.')