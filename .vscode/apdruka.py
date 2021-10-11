def pasuti_tkreklus(skaits,apdruka,piegade):

    cena ={"cena":55,"internet-sutījums":1, "foto":2} #dictionaries
    apdrukas_vert = cena[apdruka] * skaits

    cena == 55
    if cena == 55:
        print ("labs pirkums")

    piegade == 0
    if piegade== 0:
        print ("bezmaksas sutījums")

    if cena <50:
        return apdrukas_vert +15

    if cena >50:
        return apdrukas_vert +0 

pasuti_tkreklus(5,"TEKSTS", False)