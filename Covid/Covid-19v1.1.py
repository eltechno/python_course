
import pandas as pd
import matplotlib.pyplot as plt

#se crea un dataframe con los datos actualizados del repo github
#https://github.com/datasets/covid-19/tree/master/data

#df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv', parse_dates=['Date'])
#df = pd.read_csv("countries-aggregated.csv", parse_dates=True, index_col="Date")


df = pd.read_csv("https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv", parse_dates=True, index_col="Date")


#se crea una lista de los paises a filtrar
countries=["US", "Honduras", "Chile", "Guatemala", "El Salvador"]

#genera un dataframe con solo la data de los paises filtrados
df = df[df['Country'].isin(countries)]

## SUMA DE LOS CASOS EN TOTAL POR PAIS
#df['Cases'] = df[['Confirmed', "Recovered","Deaths"]].sum(axis=1)
df['Cases'] = df[['Confirmed']].sum(axis=1)
## PIVOT TABLE COLOCANDO EN HORIZONTAL LOS PAISES
df = df.pivot_table(index="Date", columns='Country', values='Cases', fill_value=0)
## COPIANDO EL CONTENIDO DE TABLA US POR UNITED STATES
df["United States"] = df['US']
## ELIMINANDO LA COLUMNA US
df.drop("US", axis=1, inplace= True)

#FILTRO DE SOLO LOS PAISES A COMPARAR
centro_america = df[['Guatemala', 'El Salvador', "Honduras"]]
print(centro_america)


#https://matplotlib.org/api/markers_api.html
#https://matplotlib.org/gallery/lines_bars_and_markers/line_styles_reference.html

#INICIO DE GRAFICA COMPARATIVA
#fig, ax = plt.subplots()
#ax.plot(centro_america["Guatemala"]) #, marker="o", linestyle="--", color="r"
#ax.plot(centro_america["El Salvador"])#, marker="v", linestyle="--"
#ax.plot(centro_america["Honduras"])#, marker="v", linestyle="none"
#ax.set_xlabel("Avance por dias")
#ax.set_ylabel("Casos Activos (total) ")
#ax.set_title("COVID-19 Triangulo Centro Americano")
#plt.show()
##FIN DE GRAFICA COMPARATIVA

fig, ax = plt.subplots()
marzo_abril = centro_america["2020-03-10": "2020-04-22"]
ax.plot(marzo_abril.index, marzo_abril["Guatemala"], color="b")
ax.plot(marzo_abril.index, marzo_abril["El Salvador"], color="g")
ax.plot(marzo_abril.index, marzo_abril["Honduras"], color="r")
ax.set_xlabel("Avance por dias")
ax.set_ylabel("Casos Activos (total) ")
ax.set_title("COVID-19 Triangulo Centro Americano")
#plt.show()

#GRAFICA CON 2 COMPARACIONES DIFERENTE ESCALA MISMO EJE
#ESCALA DE X IDENTICA, ESCALA DE Y DIFERENTE
fig, ax = plt.subplots()
marzo_abril = centro_america["2020-03-22": "2020-04-22"]
ax.plot(marzo_abril.index, marzo_abril["Guatemala"], marker="o", linestyle="--",color="b") ##, linewidth=3)
ax.set_xlabel("Avance por dias")
ax.set_ylabel("Total caso por dia ", color="b")#ESCALAS Y NUMEROS MISMO COLOR QUE GRAFICA
gt_title = ("Guatemala", centro_america["Guatemala"].max())
plt.text(x = marzo_abril.index[-1], y = centro_america["Guatemala"].max(), color = "blue", s = gt_title, weight = 'bold')
#ax.annotate("Guatemala", xy=[pd.Timestamp("2020-04-08"), 100], xytext=[pd.Timestamp("2020-04-22"), 25], arrowprops={})
ax.tick_params("y", colors="blue")
#ax2 = ax.twinx()
ax.plot(marzo_abril.index, marzo_abril["El Salvador"], color="g")
sv_title = ("El Salvador", centro_america["El Salvador"].max())
#ax.set_ylabel("Casos El Salvador ", color="g")
plt.text(x = marzo_abril.index[-1], y = centro_america["El Salvador"].max(), color = "green", s = sv_title, weight = 'bold')
ax.tick_params("y", colors="green") #ESCALAS Y NUMEROS MISMO COLOR QUE GRAFICA
#ax3 = ax.twinx()
ax.plot(marzo_abril.index, marzo_abril["Honduras"], color="r")
hn_title = ("Honduras", centro_america["Honduras"].max())
plt.text(x = marzo_abril.index[-1], y = (centro_america["Honduras"].max()), color = "red", s = hn_title, weight = 'bold')
#ax3.set_ylabel("Casos Honduras ", color="r")
ax.tick_params("y", colors="red") #ESCALAS Y NUMEROS MISMO COLOR QUE GRAFICA
ax.set_title("COVID-19 Triangulo Centro Americano")
plt.show()


#DEFINIENDO UNA FUNCION PARA CREAR LAS GRAFICAS MAS RAPIDO
def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x,y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.tick_params("y", colors=color)


fig, ax = plt.subplots()
#UTILIZANDO LA FUNCION ANTES CREADA PARA GENERAR LAS GRAFICAS
plot_timeseries(ax,marzo_abril.index, marzo_abril["Guatemala"],
                'blue', "Evolucion en dias", "Casos Activos")
ax2 = ax.twinx()

plot_timeseries(ax,marzo_abril.index, marzo_abril["El Salvador"],
                'green', "Evolucion en dias", "Casos Activos")
#plt.show()