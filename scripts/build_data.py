from sdg.open_sdg import open_sdg_build

def alter_data(df):
    for col in df.loc[:, df.dtypes == object].columns:
        df[col] = df[col].str.strip()
    return df

open_sdg_build(config='config_data.yml', alter_data=alter_data)
