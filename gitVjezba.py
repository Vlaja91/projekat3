temperatura = int(input("Unesite temperaturu: "))

if temperatura < 0:
    print("Oprez klizavo")

if temperatura > 0:
    print("Temperatura iznad 0")
    if temperatura > 30:
        print("Uključite klima uredjaj")

