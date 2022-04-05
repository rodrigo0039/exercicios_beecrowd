renda = float(input())
imposto = float(0)

if renda > 2000:
    imposto =  renda - 2000
    if imposto > 1000:
        imposto = 1000
    total =  imposto * 0.08
    if renda > 3000:
        imposto = (renda - 3000)
        if imposto > 1500:
            imposto = 1500
        total += imposto * 0.18
    if renda > 4500:
        imposto = (renda - 4500)
        total += imposto * 0.28
    print(f"R$ {total:.2f}")
else:
    print("Isento")