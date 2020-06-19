
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

from matplotlib.dates import DateFormatter
import matplotlib.ticker as ticker

#se crea un dataframe con los datos actualizados del repo github
#https://github.com/datasets/covid-19/tree/master/data

#df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv', parse_dates=['Date'])
df = pd.read_csv('countries-aggregated.csv', parse_dates=['Date'])
#poblacion total por pais ha 2018
#https://data.worldbank.org/indicator/SP.POP.TOTL
population = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_936048.csv")

#se crea una lista de los paises a filtrar
countries=["US", "Honduras", "Chile", "Guatemala", "El Salvador"]
pop_countries=["United States","Mexico", "China", "Guatemala", "El Salvador"]

#genera un dataframe con solo la data de los paises filtrados
df = df[df['Country'].isin(countries)]
#se crea una nueva columna con la sumatoria de los casos por paises
#axis = 1 hace la suma horizontal de los valores encontrados

## FILTRADO POR FECHA
start_date = "2020-03-10"
end_date = "2020-04-22"
after_start_date = df["Date"] >= start_date
data = df.loc[after_start_date]
## FILTRADO POR FECHA

## SUMA DE LOS CASOS EN TOTAL POR PAIS
data['Cases'] = data[['Confirmed', "Recovered","Deaths"]].sum(axis=1)
## PIVOT TABLE COLOCANDO EN HORIZONTAL LOS PAISES
data = data.pivot_table(index="Date", columns='Country', values='Cases', fill_value=0)
## COPIANDO EL CONTENIDO DE TABLA US POR UNITED STATES
data["United States"] = data['US']
## ELIMINANDO LA COLUMNA US
data.drop("US", axis=1, inplace= True)

#FILTRO DE SOLO LOS PAISES A COMPARAR
centro_america = data[['Guatemala', 'El Salvador', "Honduras"]]
print(centro_america)


#https://matplotlib.org/api/markers_api.html
#https://matplotlib.org/gallery/lines_bars_and_markers/line_styles_reference.html

#INICIO DE GRAFICA COMPARATIVA
fig, ax = plt.subplots()
ax.plot(centro_america["Guatemala"]) #, marker="o", linestyle="--", color="r"
ax.plot(centro_america["El Salvador"])#, marker="v", linestyle="--"
ax.plot(centro_america["Honduras"])#, marker="v", linestyle="none"
ax.set_xlabel("Avance por dias")
ax.set_ylabel("Casos Activos (total) ")
ax.set_title("COVID-19 Triangulo Centro Americano")
plt.show()
##FIN DE GRAFICA COMPARATIVA

fig, ax = plt.subplots(2,2)
ax[0,0].plot(centro_america["El Salvador"], linestyle="--")
ax[0,1].plot(centro_america["Honduras"], linestyle="--")
plt.show()



#genera un dataframe con solo la data de los paises filtrados
population = population[population['Country Name'].isin(pop_countries)]
#separa solo 2 columnas y ordenamos por nombre de pais
population = population[['Country Name', '2018']].sort_values(by=["Country Name"])
#Reset index
population = population.reset_index(drop=True)
print(population)
#population dataframe contiene los habitantes por pais

#[print(key, value) for key, value in population.items()]
#print(population["Country Name"][0],":",population["2018"][0])
#[print(population["Country Name"][i],":",population["2018"][i]) for i in range(len(pop_countries))]



#definimos lista de colores para cuando exista una grafica
#list_colors = ['#045275', '#089099', '#7CCBA2','#FCDE9C', '#DC3977', '#7C1D6F']

#create a dictionary with the data from the last dataframe
#dicts={}
#for i in range (len(pop_countries)):
#    dicts[population["Country Name"][i]] = population["2018"][i]

#reemplezamos la variable population for el diccionario antes creado
#population = dicts
#print(dicts)




#creamos el diccionario de colores que corresponden a cada pais
#colors={}
#for i in range (len(pop_countries)):
#    colors[population["Country Name"][i]] = list_colors[i]

#kind="area"
#plot = centro_america.plot( stacked=False,figsize=(8,4), linewidth=3)
#plot.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
#plot.grid(color='#d4d4d4')
#plot.set_xlabel('Fecha')
#plot.set_ylabel('# de Casos')
#plt.title('Covid 19 dia por dia')
#plt.show(block=True)











#centro_america.plot(kind="area", stacked=False)
#plt.plot(centro_america)
#plt.show()





#print(population["Country Name"][0])
#for pais in countries:
#    print(population[population["Country Name"] == pais])
#se cambia el anterior indice por Date
#covid = df.reset_index('Date')
#se estable Date como index del dataframe
#covid.set_index(['Date'], inplace=True)


'''
#create a copy from covid dataset
percapita = df.copy()

#generaremos calculo de casos por cada 100,000 personas
for country in list(percapita.columns):
    percapita[country] = (percapita[country]/ population[country]) * 100000

plt.style.use('fivethirtyeight')
# Section 7 - Creating the Visualization
plot = percapita.plot(figsize=(8,4), color=list(colors.values()), linewidth=5, legend=False)
plot.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plot.grid(color='#d4d4d4')
plot.set_xlabel('Date')
plot.set_ylabel('# of Cases')
# Section 8 - Assigning Colour
for country in list(colors.keys()):
    plot.text(x = percapita.index[-1], y = percapita[country].max(), color = colors[country], s = country, weight = 'bold')
# Section 9 - Adding Labels
plot.text(x = percapita.index[1], y = int(percapita.max().max())+45000, s = "COVID-19 Cases by Country", fontsize = 23, weight = 'bold', alpha = .75)
plot.text(x = percapita.index[1], y = int(percapita.max().max())+15000, s = "For the USA, China, Germany, France, United Kingdom, and Canada\nIncludes Current Cases, Recoveries, and Deaths", fontsize = 16, alpha = .75)
plot.text(x = percapita.index[1], y = -100000,s = 'datagy.io                      Source: https://github.com/datasets/covid-19/blob/master/data/countries-aggregated.csv', fontsize = 10)
plt.show()
'''