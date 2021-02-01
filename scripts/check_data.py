from sdg.open_sdg import open_sdg_check

def alter_data(df):
    # if 'Source details' in df:
    #   del df['Source details']
    # if 'concept.COMMENT_TS' in df:
    #     del df['concept.COMMENT_TS']
    df = data_frame.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    return df

# Validate the indicators.
validation_successful = open_sdg_check(config='config_data.yml')

# If everything was valid, perform the build.
if not validation_successful:
    raise Exception('There were validation errors. See output above.')
