import pandas as pd
df = pd.read_csv("solicitudes_credito.csv", sep=";", encoding='utf8')
df.drop(['Unnamed: 0'], axis=1,inplace=True)
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df['sexo']=df['sexo'].str.lower()
df['tipo_de_emprendimiento']=df['tipo_de_emprendimiento'].str.lower()
df['idea_negocio']=df['idea_negocio'].str.lower()
df['idea_negocio']=df['idea_negocio'].map(lambda x: x.replace(" ",'_'))
df['idea_negocio']=df['idea_negocio'].map(lambda x: x.replace("-",'_'))
#df['barrio']=df['barrio'].astype(str)

df['barrio']=df['barrio'].map(lambda x: x.replace("-",' '))
df['barrio']=df['barrio'].map(lambda x: x.replace("_",' '))
todos=df.barrio.unique()
df['barrio']=df['barrio'].str.lower()
unicos=df.barrio.unique()
#print(list(set(df.barrio.unique())))
#print(len(list(set(df.barrio.unique()))))
#barrios 234
#print(df.sexo.value_counts().to_list())
#print(df.idea_negocio.unique())
#print(len(df.barrio.unique()))
#print(df.barrio.unique())
cont=0
for i in todos:
    if i in unicos:
        pass
    else:
        cont+=1
        print(i)
print(len(todos))
print(len(unicos))
print(cont)