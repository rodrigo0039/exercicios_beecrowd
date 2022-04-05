while True:
  try:
    hora, minuto = [int(x) for x in input().split(':')]
    atraso = ((hora * 60) + minuto + 60) - 480
    if atraso <= 0:
      print("Atraso maximo: 0")
    else:
      print(f"Atraso maximo: {atraso}")

  except EOFError:
    break