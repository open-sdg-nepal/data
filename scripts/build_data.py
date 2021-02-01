from sdg.open_sdg import open_sdg_build

def alter_data(df):
    # if 'Source details' in df:
    #   del df['Source details']
    # if 'concept.COMMENT_TS' in df:
    #     del df['concept.COMMENT_TS']
    df = data_frame.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    return df

open_sdg_build(config='config_data.yml', alter_data=alter_data)
