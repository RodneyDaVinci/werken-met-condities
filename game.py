# Intro Game Fukushima

print("Na wat research op internet heb jeje zelf bedacht om illegaal de Fukushima exclusion zone te gaan bezoeken")
import time
t = 3.4
time.sleep(t)

print("Je hebt besloten om dit zonder een tourgids te doen omdat je graag zelf alles wilt bekijken.")
import time
t = 3.4
time.sleep(t)

print("Nadat je de exclusion zone hebt betreden kom je erachter dat het wemelt van beveiligers en het leger.")
import time
t = 3.4
time.sleep(t)

print("Op gegeven moment begon het te regenen en te onweren.")
import time
t = 3.4
time.sleep(t)

print("Je zit te twijfelen om toch de exclusion zone weer te verlaten zonder gepakt te worden door de beveiligers of het leger of door te gaan.")
import time
t = 3.4
time.sleep(t)

print ("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀DE REGELS▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
print ("Er worden vragen gesteld die een gevolg hebben op jouw antwoord. Alle vragen moeten met hoofdletter beantwoord worden.")
print ("Je hebt alle tijd om na te denken over de vraag. Er zit dus geen tijd aan vast.")
print ("Verloren? Dan moet je de game opnieuw starten!")
print ("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
import time
t = 7.6
time.sleep(t)

# De game

exclusion = input('Je bent de exclusion zone betreden en je ziet twee beveiligers recht voor je staan. Ga je er proberen zo stil mogelijk langs heen te kruipen of achter de bosjes er stiekem langs glippen? (Kruipen) / (Bosjes) ')
if exclusion == "Bosjes":
    print('Je bent voorbij de beveiligers en je bent rond gaan kijken in de exclusion zone. Je vindt een medkit en een box waar een doods-teken op staat.')
    import time
    t = 5
    time.sleep(t)

    binnenexclusion = input ('Je bent aan het denken welke van de twee voorwerpen je mee wilt nemen want je wilt er maar één meenemen. (Medkit) / (Box) ')
    if binnenexclusion == "Box":
        print('Je hebt de box gekozen met het doods-teken erop! Het doods-teken staat ervoor dat er een wapen in de box zit. Bij deze heb je een wapen ontvangen!')
        import time
        t = 3.4
        time.sleep(t)
    
        print('Je hebt een wapen gevonden en ineens begint het te onweren en te regenen.')
        import time
        t = 3.4
        time.sleep(t)

        print('Vanwege de regen en het ontweer zit je te twijfelen of je de exclusion zone verlaat of toch door blijft onderzoeken.')
        import time
        t = 3.4
        time.sleep(t)

        Box = input('Wat kies je ? (Weggaan) / (Doorgaan) ')
        if Box == "Doorgaan":
           print ('Je besluit toch verder te onderzoeken en je hebt een traforuimte gevonden die stroom leverde voor de inwoners in de exclusion zone.')
           import time
           t = 3.4
           time.sleep(t)

           Onderzoeken = input('Wil je de stroom weer aanzetten door de hendel in de traforuimte naar beneden te drukken? (Ja) / (Nee) ')
           if Onderzoeken == "Ja":
               print('De traforuimte is oud en vervallen en daardoor raakt een van de kabels overhit.')
               import time
               t = 3.4
               time.sleep(t)
               print ('De vlammen komen eruit en je wordt levend verbrand. Helaas een foute keuze!')
           else:
               print('De traforuimte heeft een dodelijke radioactieve straling. Je lichaam smelt weg. Helaas een foute keuze!')

        else: 
            print ('Je wilt weggaan en besluit om terug te keren naar de plek waar je de exclusion zone bent binnen getreden. Je ziet een rare vlek bewegen.')
            import time
            t = 3.4
            time.sleep(t)
            print ('Het is een soldaat en begint op je af te schieten met zijn geweer!')
            import time
            t = 3.4
            time.sleep(t)
            Vuren = input ('Je hebt het wapen die je in het begin hebt gevonden in je rugtas zitten. Je pakt hem uit je rugtas en begint te beslissen of je op zijn hoofd of lichaam schiet. (Hoofd) / (Lichaam) ')
            if Vuren == "Hoofd":
                print ('Je hebt de soldaat doodgeschoten en bent uit de exclusion zone! Gefeliciteerd, je hebt de game gewonnen!')
            else:
                print('De soldaat heeft een kogelvrij vest aan heeft jou alsnog doodgeschoten. Helaas een foute keuze!')
    
    else:
        Medkit = input ('In de medkit zitten wat voedingsupplementen in. Besluit je om een voedingssupplement te nemen? (Ja) / (Nee) ')
        if Medkit == "Ja":
            print ('De medkit is besmet met radioactieve deeltjes. Je keel begint op te zwellen en stikt. Helaas een foute keuze!')
        
        else:
            print ('De hoeveelheid radioactieve straling op de medkit is zo hoog dat bij aanraking alleen al je hele huid wegsmelt. Helaas een foute keuze!')

else:
    Ziekenhuis = input ('Je bent stiekem langs te beveiligers gekropen en je bent binnen de exclusion zone. Er staat een oude ziekenhuis voor je met twee ingangen. Welke ingang neem je? (Ingang1) / (Ingang2) ')
    if Ziekenhuis == "Ingang2":
        print ('Je hebt voor de tweede ingang gekozen en probeert zachtjes het gebouw te betreden. Er staat er een shotgun trap en word je doodgeschoten. Helaas een foute keuze!')

    else:
        print('Je hebt voor de eerste ingang gekozen en probeert zachtjes het gebouw te betreden.')
        import time
        t = 3.4
        time.sleep(t)
        Beveiligingskamer = input ('Je komt een security room tegen waarin een schoonmaker van het ziekenhuis zit. De security room zit opslot. Ga je de deur open maken of dichtlaten? (Openmaken) / (Dichtlaten) ')
        if Beveiligingskamer == "Openmaken":
            print('De schoonmaker is pshychisch ziek en heeft je doodgeslagen met een dweil. Helaas een foute keuze!')
        
        else:
            Kleding = input('Je bent doorgelopen en heb de schoonmaker in de security room gelaten. Je ziet wat operatie kleding liggen met wat operatiemessen erin. Besluit je om het aan te trekken? (Ja) / (Nee) ')
            if Kleding == "Ja":
                print ('Je trekt de operatiekleding aan en neemt de operatiemessen mee.')
                Guards = input('Je ziet een deur die naar de uitgang leidt, maar er staan twee soldaten bij de deur. Besluit je om je operatiekleding aan te houden of uit te trekken? (Aanhouden) / (Uittrekken) ')
                if Guards == "Uittrekken":
                    print ('De soldaten schieten je instant dood. Helaas een foute keuze!')
                
                else:
                    print('Je hebt de operatiekleding aangehouden en bent gewoon langs te soldaten gelopen. Je hebt de game gewonnen, gefeliciteerd!')
            
            else:
                print('Je loopt rustig door zonder de operatiekleding aan te trekken maar neemt wel de operatiemessen mee.')
                RennenVriend = input('Je ziet een deur die naar de uitgang leidt, maar er staan twee soldaten bij de deur. Besluit je om te doen alsof je verdwaalt bent of om op ze af te rennen en ze neer te steken? (Verdwaald) / (Neersteken) ')
                if RennenVriend == "Neersteken":
                    print('Je probeert ze neer te steken maar vanwege de kogelvrije vesten gaat de mes er niet doorheen. Je wordt alsnog doodgeschoten. Helaas een foute keuze!')
                else:
                    print('Je doet alsof je verdwaald bent en legt uit dat je niet meer weet waar je tourgids is. De soldaten geloven het niet en schieten je dood. Helaas een foute keuze!')