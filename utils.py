import pandas as pd
def create_data_frame():
    df = pd.read_excel('data/MDIP_2024.xlsx', header=(0))
    return df

def preprocess_data():
    df = create_data_frame()
    df = df.dropna()

    # delete column because of nonsense values
    df = df.drop('NATUREZA_APURADA', axis=1)
    # change to uppercase all 'object' type data
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.upper()
    # delete nonsense data
    df = df[df['SEXO_PESSOA'] != 'REGISTRADO NA PF']
    df = df[df['COR_PELE'] != 'REGISTRADO NA PF']
    df = df[df['COR_PELE'] != 'POLICIA FEDERAL']
    df = df[df['DATAHORA_REGISTRO_BO'] != 'CRIME MILITAR']
    df = df[df['DATAHORA_REGISTRO_BO'] != 'REGISTRADO NA PF']
    # work on column consistency
    for line in df['DATAHORA_REGISTRO_BO']:
        df['DATAHORA_REGISTRO_BO'] = df['DATAHORA_REGISTRO_BO'].str.replace('00:00:00', '')
    # rename column
    df.rename(columns={'DATAHORA_REGISTRO_BO': 'DATA_RESGISTRO_BO'}, inplace=True)

    # convert 'LATITUDE' and 'LONGITUDE' columns type
    df['LATITUDE'] = pd.to_numeric(df['LATITUDE'], errors='coerce')
    df['LONGITUDE'] = pd.to_numeric(df['LONGITUDE'], errors='coerce')
    # delete lines where 'LATITUDE' and 'LONGITUDE' are NAN or zero
    df = df.dropna(subset=['LATITUDE', 'LONGITUDE'])
    df = df[(df['LATITUDE'] != 0) | (df['LONGITUDE'] != 0)]

    # change column type treating errors
    df['IDADE_PESSOA'] = pd.to_numeric(df['IDADE_PESSOA'], errors='coerce')
    # delete lines where convertion failed (NaN)
    df_idade_valida = df.dropna(subset=['IDADE_PESSOA']).copy()

    # change column type
    df['DATA_FATO'] = pd.to_datetime(df['DATA_FATO'])
    # create new column
    df['ANO_MES'] = df['DATA_FATO'].dt.to_period('M')

    return df, df_idade_valida