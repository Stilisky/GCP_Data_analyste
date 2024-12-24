import pandas as pd

data = {
    'name': ['John', 'Paul', 'Anna'],
    'age': [34,23,12],
    'City': ['Casablanca', 'Cotonou', 'Bamako' ]
}

df = pd.DataFrame(data)

print(df)

# Faire un filtre sur la dataFrame
print('---Filtre-------------------------------')
filtre = df[df['age'] > 23]
print(filtre)

#Export en excel
