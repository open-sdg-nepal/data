from sdg.open_sdg import open_sdg_build

def alter_data(df):
    df['COMMENT_OBS'] = df['COMMENT_OBS'].str.strip()
    df['SOURCE_DETAIL'] = df['SOURCE_DETAIL'].str.strip()
    if not df['COMMENT_OBS']:
        print("df['COMMENT_OBS'] does not exist")
    return df

open_sdg_build(config='config_data.yml', alter_data=alter_data)
