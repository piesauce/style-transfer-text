import os




def merge_plays(path):
    plays_original_list = []
    plays_modern_list = []
    for dirname, _, filenames in os.walk(path):
        for filename in filenames:
            if 'original' in filename:
                plays_original_list.append(os.path.join(dirname, filename))
            if 'modern' in filename:
                plays_modern_list.append(os.path.join(dirname, filename))
    with open('merged_plays_original.aligned', 'a+') as outfile:
        for fname in plays_original_list:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
    with open('merged_plays_modern.aligned', 'a+') as outfile:
        for fname in plays_modern_list:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
                    
def merge_plays(path):
    play_count = 0
    col_names = ['text', 'playid', 'style']
    df = pd.DataFrame(columns=col_names)
    for dirname, _, filenames in os.walk(path):
        for filename in filenames:
            if 'original' in filename:
                style = 0
            if 'modern' in filename:
                style = 1
            for line in open(os.path.join(dirname, filename)):
                df.loc[len(df)] = [line, play_count, style]
            play_count += 1
    return df
    
def save_df(df):
    df.to_pickle("./plays_df.pkl")
    
def load_df(path):
    return pd.read_pickle(path)
    
