import pandas as pd

def compare_versions(df):
    df_original = df.loc[df['style'] == 0]
    df_modern = df.loc[df['style'] == 1]
    calc_word_distributions(df_original, df_modern)
    compare_versions_plays(df_original, df_modern)
    
def compare_versions_plays(df_original, df_modern):
    df_original_plays_dic = {k: v for k, v in df_original.groupby('playid')}
    df_modern_plays_dic = {k:v for k,v in df_modern.groupby('playid')}
    analyse_plays(df_original_plays_dic, df_modern_plays_dic)


