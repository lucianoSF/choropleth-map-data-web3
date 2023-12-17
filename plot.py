import plotly.express as px
import plotly as p
import pandas as pd


caminho_arquivo = 'data_extraction.xls'


df = pd.read_excel(caminho_arquivo)

df = df.groupby('País de origem do 1º autor').size().reset_index(name='Valor')

#print(df.sort_values(by=['Valor'], ascending=False))

fig = px.choropleth(
    df,
    locations='País de origem do 1º autor',
    locationmode='country names',
    color='Valor',
    color_continuous_scale='aggrnyl_r',
    projection='natural earth'

)

fig.update_geos(
    showland=True,
    subunitcolor="darkgray",
)


fig.update_layout(
    coloraxis_colorbar=dict(
        title='',
        len=0.70,
        tickfont=dict(size=20) 
    ),
    margin=dict(l=0, r=0, t=0, b=0)
)
p.io.write_image(fig, 'studies_per_country.pdf', format='pdf')
p.io.write_image(fig, 'studies_per_country.png', format='png')

#fig.show()