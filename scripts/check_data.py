from sdg.open_sdg import open_sdg_check

def alter_data(df):
    df['COMMENT_OBS'] = df['COMMENT_OBS'].str.strip()
    df['SOURCE_DETAIL'] = df['SOURCE_DETAIL'].str.strip()
    if not df['COMMENT_OBS']:
        print("df['COMMENT_OBS'] does not exist")
    return df

# Validate the indicators.
validation_successful = open_sdg_check(config='config_data.yml', alter_data=alter_data)

# If everything was valid, perform the build.
if not validation_successful:
    raise Exception('There were validation errors. See output above.')
