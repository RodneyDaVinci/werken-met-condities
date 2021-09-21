kaasgeel = input('Is de kaas geel')

if kaasgeel == "ja":
    gatenkaas = input("Zitten er gaten in?")

    if gatenkaas == "ja":
        duur = input("Is de kaas belachelijk duur?")

        if duur == "ja":
            print("Emmenthaler")
        else:
                print("Leerdammer")
    else: 
        hard = input('Is de kaas hard als steen?')
        if hard == "ja":
            print("Pammigiano Reggiano")
        else:
            print("Goudse kaas")

else:
    blauw = input('Heeft de kaas blauwe schimmels?')
    if blauw == "ja":
        korst = input("Heeft de kaas een korst?")
        if korst == "ja":
            print("Bleu de Rochbaron")
        else:
            print("Foume d'Ambert")
    else:
        korst2 = input("Heeft de kaas een korst?")
        if korst2 == "ja":
            print("Camembert")
        else:
            print("Mozzarella")
