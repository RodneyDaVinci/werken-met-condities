print('########### Circus HotelDeBotel Sollicitatie Circusdirecteur ###########')

# Naam
vnaamanaam = input("Wat is uw voornaam en achternaam?: ")
lichaamsgewicht = int(input("Wat is u lichaamsgewicht? -IN KG-: "))

if lichaamsgewicht >= 90:
    lichaamsgewicht = True
else:
    lichaamsgewicht = False


# Lengte
hoelang = int(input("Wat is u lengte? -IN CM-: "))

if hoelang >= 150:
    hoelang = True
else:
    hoelang = False


# Praktijkervaring dierendressur
dierendressuur = int(input("Hoeveel jaren praktijkervaring heeft u met dierendressur?: "))

if dierendressuur >= 4:
    dierendressuur = True
else:
    dierendressuur = False


# Ervaring acrobatiek
acrobatiek = int(input("Hoeveel jaren ervaring heeft u met acrobatiek?: "))

if acrobatiek >= 3:
    acrobatiek = True
else:
    acrobatiek = False


# Maf 4
basis = input("Heeft u een basisschool diploma? -Ja OF Nee-: ")

# Diploma
mbodiploma = str(input("Heeft u een MBO 4 Diploma? -Ja OF Nee-: "))

if mbodiploma == "Ja":
    mbodiploma = True
else:
    mbodiploma = False


# Maf 3
heftruckbewijs = input("Heeft u een heftruck rijbewijs? -Ja OF Nee-: ")


# Geldig vrachtwagen rijbewijs
vrachtbewijs = str(input("Heeft u een geldig C1, C1E OF CE rijbewijs? -Ja OF Nee-: "))

if vrachtbewijs == "Ja":
    vrachtbewijs = True
else:
    vrachtbewijs = False


# Hoge hoed
hoed = str(input("Heeft u een hoge hoed? -Ja OF Nee-: "))

if hoed == "Ja":
    hoed = True
else:
    hoed = False

# Maf 1
vingers =  input("Hoeveel vingers heeft u op beide handen?: ")

# Certificaat
gevcerti = str(input("Heeft u een certificaat 'Overleven met gevaarlijk personeel'? -Ja OF Nee-: "))

if gevcerti == "Ja":
    gevcerti = True
else:
    gevcerti = False


# Man of vrouw, snor en vrouwenhaar
gender = input("Bent u een man of vrouw? -Man OF Vrouw-: ")

if gender == "Man":
    snor = int(input("Hoe breed is uw snor? -IN CENTIMETERS-: "))
    if snor >= 10:
        snor = True
    else:
        snor = False
else:
    haarvrouw = int(input("Heeft u rood krulhaar? Zo ja, wat is de lengte? -IN CENTIMETERS-: "))
    if haarvrouw >= 20:
        haarvrouw = True
    else:
        haarvrouw = False


# Maf 2
voethaar = input("Heeft u haar op uw voeten?: ")


ervaring = (dierendressuur, acrobatiek)
other = (lichaamsgewicht, hoelang, mbodiploma, vrachtbewijs, hoed, gevcerti, gender)

ervaring = all(ervaring)
other = any(other)

yes = ervaring
no = other

if yes == True:
    ervaringLaatsteString = "voldoende"
elif yes == False:
    ervaringLaatsteString = "onvoldoende"

if no == True:
    otherLaatsteString = "voldoende"
elif no == False:
    otherLaatsteString = "onvoldoende"

#Resultaat
print("Geachte",vnaamanaam,", uw heeft",ervaringLaatsteString,"werkervaring en",otherLaatsteString,"overige ervaring.")
