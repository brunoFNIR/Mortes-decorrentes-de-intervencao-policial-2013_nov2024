import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

# import 'utils' file functions
from utils import create_data_frame, preprocess_data

# SreamLit initial configs
st.set_page_config(layout='wide')


@st.cache_data
def get_preprocessed_data():
    return preprocess_data()


df, df_idade_valida = get_preprocessed_data()

# dashboard title and description
st.title("Análise de Mortes Decorrente de Ação Policial no Estado de São Paulo")
st.markdown("<h2>Este dashboard apresenta insights sobre as ocorrências de mortes decorrentes de ação policial no estado de São Paulo, de 2013 a Novembro de 2024.</h2>", unsafe_allow_html=True)


# some categorical variables data distribution visualization
st.header("Visualização das Distribuições das seguintes variáveis")
st.markdown("<h2>Distribuição por Corporação:</h2>", unsafe_allow_html=True)

fig1, ax1 = plt.subplots(figsize=(8, 5))
ax1 = sns.countplot(data=df, y='COORPORAÇÃO', order=df['COORPORAÇÃO'].value_counts().index, palette='viridis', ax=ax1)
plt.title('Distribuição de Ocorrências por Corporação')
plt.xlabel('Número de Ocorrências')
plt.ylabel('Corporação')
# add correspondent values on the bars
for p in ax1.patches:
    width = p.get_width()
    ax1.text(width + 5, p.get_y() + p.get_height()/2.,
             '{:1.0f}'.format(width),
             ha='left', va='center')
st.pyplot(fig1)

st.markdown("<h2>Distribuição por Situação:</h2>", unsafe_allow_html=True)

fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2 = sns.countplot(data=df, y='SITUAÇÃO', order=df['SITUAÇÃO'].value_counts().index, palette='viridis', ax=ax2)
plt.title('Distribuição de Ocorrências por Situação')
plt.xlabel('Número de Ocorrências')
plt.ylabel('Situação')
# add correspondent values on the bars
for p in ax2.patches:
    width = p.get_width()
    ax2.text(width + 5, p.get_y() + p.get_height()/2.,
             '{:1.0f}'.format(width),
             ha='left', va='center')
st.pyplot(fig2)


st.markdown("<h2>Distribuição por Sexo:</h2>", unsafe_allow_html=True)

fig3, ax3 = plt.subplots(figsize=(8, 5))
ax3 = sns.countplot(data=df, y='SEXO_PESSOA', order=df['SEXO_PESSOA'].value_counts().index, palette='viridis', ax=ax3)
plt.title('Distribuição de Ocorrências por Sexo da Pessoa')
plt.xlabel('Número de Ocorrências')
plt.ylabel('Sexo da Pessoa')
# add correspondent values on the bars
for p in ax3.patches:
    width = p.get_width()
    ax3.text(width + 5, p.get_y() + p.get_height()/2.,
             '{:1.0f}'.format(width),
             ha='left', va='center')
st.pyplot(fig3)


st.markdown("<h2>Distribuição por Cor de Pele:</h2>", unsafe_allow_html=True)

fig4, ax4 = plt.subplots(figsize=(8, 5))
ax4 = sns.countplot(data=df, y='COR_PELE', order=df['COR_PELE'].value_counts().index, palette='viridis', ax=ax4)
plt.title('Distribuição de Ocorrências por Cor de Pele')
plt.xlabel('Número de Ocorrências')
plt.ylabel('Cor de Pele')
# add correspondent values on the bars
for p in ax4.patches:
    width = p.get_width()
    ax4.text(width + 5, p.get_y() + p.get_height()/2.,
             '{:1.0f}'.format(width),
             ha='left', va='center')
st.pyplot(fig4)


st.markdown("<h2>Distribuição por Idade:</h2>", unsafe_allow_html=True)

fig5, ax5 = plt.subplots(figsize=(10, 6))
sns.histplot(data=df_idade_valida, x='IDADE_PESSOA', bins=30, kde=True, color='skyblue', ax=ax5)
plt.title('Distribuição da Idade das Pessoas nas Ocorrências')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.grid(axis='y', alpha=0.75)
st.pyplot(fig5)


st.header("Análise Temporal")
st.markdown("<h2>Número de ocorrências ao longo do tempo:</h2>", unsafe_allow_html=True)

ocorrencias_por_mes = df['ANO_MES'].value_counts().sort_index()
# data visualization (temporal series)
fig6, ax6 = plt.subplots(figsize=(15, 7))
ocorrencias_por_mes.plot(kind='line', marker='o', ax=ax6)
plt.title('Número de Ocorrências ao Longo do Tempo (Mensal)')
plt.xlabel('Mês/Ano')
plt.ylabel('Número de Ocorrências')
plt.grid(True)
st.pyplot(fig6)


st.header("Análise Geográfica")
st.markdown("<h2>Distribuição Geográfica das Ocorrências:</h2>", unsafe_allow_html=True)

fig7, ax7 = plt.subplots(figsize=(10, 8))
ax7.scatter(df['LONGITUDE'], df['LATITUDE'], alpha=0.5, s=5) # s -> dot size
plt.title('Distribuição Geográfica das Ocorrências')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
st.pyplot(fig7)


st.header("Dados Relacionados as 5 Cidades com Maior Número de Ocorrências")
st.markdown("<h2>Número de Mortes:</h2>", unsafe_allow_html=True)

#top 5 cities names list
top_5_municipios = df['MUNICIPIO_ELABORACAO'].value_counts().head(5).index.tolist()
#top 5 cities respective values list
valores = df['MUNICIPIO_ELABORACAO'].value_counts().head(5).tolist()

numero_de_mortes_por_localidade = dict(zip(top_5_municipios, valores))
df_numero_de_mortes_por_localidade = pd.DataFrame(list(numero_de_mortes_por_localidade.items()), columns=['MUNICIPIO', 'NUMERO_DE_MORTES'])

fig8, ax8 = plt.subplots(figsize=(12, 7))
sns.barplot(x='MUNICIPIO',
            y='NUMERO_DE_MORTES',
            data=df_numero_de_mortes_por_localidade,
            palette='viridis', ax=ax8)
plt.title('Número de Mortes por Município (Top 5)')
plt.xlabel('Município')
plt.ylabel('Número de Mortes')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig8)

# processes data (esta parte está fora de uma função, ok para o app.py se for para uso único)
df_mortes_por_municipio_mes = df.groupby(['MUNICIPIO_ELABORACAO', 'ANO_MES']).size().reset_index(name='NUMERO_DE_MORTES')

# convert 'ANO_MES' back to timestamp for the plot
df_mortes_por_municipio_mes['ANO_MES'] = df_mortes_por_municipio_mes['ANO_MES'].dt.to_timestamp()


# get top 5 cities (based on total number of deaths)
top_municipios_geral = df['MUNICIPIO_ELABORACAO'].value_counts().head(5).index.tolist()

# dataframe  filter (gets just the top 5)
df_top_5_mortes_temporal = df_mortes_por_municipio_mes[df_mortes_por_municipio_mes['MUNICIPIO_ELABORACAO'].isin(top_municipios_geral)].copy()


# data visualization (Média Móvel)
st.markdown("<h2>Média Móvel:</h2>", unsafe_allow_html=True)

df_top_5_mortes_temporal = df_top_5_mortes_temporal.sort_values(by=['MUNICIPIO_ELABORACAO', 'ANO_MES'])

# top 5 cities rolling mean (3 months)
df_top_5_mortes_temporal['NUMERO_DE_MORTES_MEDIA_MOVEL'] = df_top_5_mortes_temporal.groupby('MUNICIPIO_ELABORACAO')['NUMERO_DE_MORTES'].transform(lambda x: x.rolling(window=3, min_periods=1).mean())

# sns.relplot cria sua própria figura, acessamos ela via 'g.fig'
g_media_movel = sns.relplot(
    data=df_top_5_mortes_temporal,
    x='ANO_MES',
    y='NUMERO_DE_MORTES_MEDIA_MOVEL',
    col='MUNICIPIO_ELABORACAO',
    col_wrap=2,
    kind='line',
    height=4, aspect=1.5,
    linewidth=2.5,
    color='steelblue',
    facet_kws={'sharey': False} # dinamic Y axis
)

g_media_movel.set_axis_labels("Ano/Mês", "Média Móvel de Ocorrências de Mortes (3 meses)")
g_media_movel.set_titles("Município: {col_name}")

for ax in g_media_movel.axes.flat:
    ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m'))
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    ax.grid(True, linestyle='--', alpha=0.6)

g_media_movel.fig.suptitle('Média Móvel de Mortes (Ocorrências) por Ação Policial por Município', fontsize=16, fontweight='bold', y=1.03)
plt.tight_layout(rect=[0, 0, 1, 0.98])
st.pyplot(g_media_movel.fig)


st.markdown("<h2>Número de Mortes (Linha de Tendência):</h2>", unsafe_allow_html=True)

# convert column 'ANO_MES', avoiding plot errors
df_top_5_mortes_temporal['ANO_MES_ORDINAL'] = df_top_5_mortes_temporal['ANO_MES'].apply(mdates.date2num)

g_tendencia = sns.relplot(
    data=df_top_5_mortes_temporal,
    x='ANO_MES',
    y='NUMERO_DE_MORTES',
    col='MUNICIPIO_ELABORACAO',
    col_wrap=2,
    kind='line',
    height=4, aspect=1.5,
    marker='o',
    linewidth=1,
    color='steelblue',
    facet_kws={'sharey': False} # dinamic Y axis
)

# add tendency line (linear regression)
g_tendencia.map_dataframe(sns.regplot,
                x='ANO_MES_ORDINAL',
                y='NUMERO_DE_MORTES',
                ci=None,
                scatter=False,
                color='red',
                line_kws={'linestyle': '--', 'linewidth': 2})

g_tendencia.set_axis_labels("Ano/Mês", "Número de Ocorrências de Mortes")
g_tendencia.set_titles("Município: {col_name}")

for ax in g_tendencia.axes.flat:
    ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m'))
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    ax.grid(True, linestyle='--', alpha=0.6)

g_tendencia.fig.suptitle('Número de Mortes (Ocorrências) por Ação Policial por Município com Linha de Tendência', fontsize=16, fontweight='bold', y=1.03)
plt.tight_layout(rect=[0, 0, 1, 0.98])
st.pyplot(g_tendencia.fig)


st.markdown("<h2>---</h2>", unsafe_allow_html=True)
st.markdown("Para rodar este aplicativo Streamlit localmente, navegue até o diretório raiz do projeto no terminal e execute:", unsafe_allow_html=True)
st.code("streamlit run app.py")
st.markdown("Para mais informações sobre o projeto, visite o [repositório GitHub](https://github.com/brunoFNIR/Mortes-decorrentes-de-intervencao-policial-2013_nov2024).", unsafe_allow_html=True)