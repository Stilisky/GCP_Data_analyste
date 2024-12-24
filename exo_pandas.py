import pandas as pd
import random

nom = ["Carlos", "Maxime", "Reina", "Mario", "Gontrand", "Princia", "Violon", "Esperat"]
villes = ["Cotonou", "Parakou", "Bohicon", "Gotouko"]
names = []
city = []
age = []
score = []
for _ in range (100):
    names.append(nom[random.randint(0,7)])
    city.append(villes[random.randint(0,1)])
    age.append(random.randint(20,60))
    score.append(random.randint(0,100))

data = {
    'names': names,
    'cities': city,
    'ages': age,
    'scores': score
}

#Creation de la dataFrame (df)
df = pd.DataFrame(data)

print(df)


#Filtre sur la df
print("Liste dont l'age sup à 40")
filtre = df[df["ages"] > 40]
print(filtre)

#export du df en csv
df.to_csv('out.csv', index=False)

# Creation d'une colonne plus filtre

df["classement"] = df["scores"].apply(lambda x: "Pass" if x > 50 else "Fail")
print(df)
