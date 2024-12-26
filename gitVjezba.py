temperatura = int(input("Unesite temperaturu: "))
test_temperatura = -1 
temperatura = test_temperatura
poruka = ""
if temperatura < 0:
    poruka = "Oprez klizavo"

if temperatura > 0:
    poruka = "Temperatura iznad 0"
    if temperatura > 30:
        poruka = "Uključite klima uredjaj"

ocekivana_poruka = "Oprez klizavo"
if poruka == ocekivana_poruka:
    print("Case - ispod nule - test prosao")