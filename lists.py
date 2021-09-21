#Mainnīgais saraksts jeb lists

#[]

#Mainīgais var saturēt tadus datu tipus
my_list = ['Teksts', 1, 2]
print(my_list)

#Elementu skaits mainigajā

print("Saraksta my_list elementu skaits: ", len(my_list))

#index metode

print(my_list[1])
print(my_list[0:])

#elementa maiņa

my_list[0] = 'Sveiki'
print(my_list)

#Elementu pievienošana 

print(my_list + ["hi"])
my_list = my_list + ["suns"]
print(my_list)

#pop

my_list.pop(0)
print(my_list)