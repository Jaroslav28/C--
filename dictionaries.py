#Mainīgais bibliotēka

#{}, katrai vērtībai ir sava atslēga 

pirmais = {'atsl1':'vert1', 'atsl2':'vert2'}
print(pirmais)

print(pirmais['atsl1'])

otrais = {'atsl1':[1,2,3], 'atsl2':'Teksts', 'atsl3':5}

print(otrais['atsl1'],otrais['atsl3'])

trešais = {'Macību priekšmeti':{'Matemātika':5, "Latviešu valoda":[6,8,5], "Programmēšana":4}}

print(trešais["Macību priekšmeti"]["Latviešu valoda"][2])

#Tukšas bibliotēkas izveide

pirmais = {}
pirmais['koks'] = 'bērzs'
pirmais['ūdenstilpe'] = 'upe'
