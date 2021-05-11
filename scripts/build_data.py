from sdg.open_sdg import open_sdg_build

def alter_meta(meta):
    if data.empty == False:
        meta['reporting_status']='complete'
    return meta

open_sdg_build(config='config_data.yml', alter_meta=alter_meta)
