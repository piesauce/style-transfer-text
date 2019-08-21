import os
import numpy as np
import pandas as pd
import nltk

# def merge_plays(path):
    # plays_original_list = []
    # plays_modern_list = []
    # for dirname, _, filenames in os.walk(path):
        # for filename in filenames:
            # if 'original' in filename:
                # plays_original_list.append(os.path.join(dirname, filename))
            # if 'modern' in filename:
                # plays_modern_list.append(os.path.join(dirname, filename))
    # with open('merged_plays_original.aligned', 'a+') as outfile:
        # for fname in plays_original_list:
            # with open(fname) as infile:
                # for line in infile:
                    # outfile.write(line)
    # with open('merged_plays_modern.aligned', 'a+') as outfile:
        # for fname in plays_modern_list:
            # with open(fname) as infile:
                # for line in infile:
                    # outfile.write(line)
                    
# def create_dataframe(path):
    # play_count = 0
    # col_names = ['text', 'playid', 'style']
    # df = pd.DataFrame(columns=col_names)
    # for dirname, _, filenames in os.walk(path):
        # for filename in filenames:
            # if 'original' in filename:
                # style = 0
            # if 'modern' in filename:
                # style = 1
            # for line in open(os.path.join(dirname, filename)):
                # df.loc[len(df)] = [line, play_count, style]
            # play_count += 1
    # return df
    
# def save_df(df):
    # df.to_pickle("./plays_df.pkl")
    
# def load_df(path):
    # return pd.read_pickle(path)
    
# def to_lower_df(df):
    # df['text'] = df['text'].str.lower()
    # return df

# def sent_tokenize_df(df, tokenizer):
    # df['text'] = df['text'].apply(tokenizer.tokenize)
    # return df
    
# def read_data(path):
    # for filename in os.listdir(path):
        # if 'original' in filename:
            # with open(os.path.join(path, filename), "r") as f:
                # original_data = f.read()
        # if 'modern' in filename:
            # with open(os.path.join(path, filename), 'r') as f:
                # modern_data = f.read()
    # return original_data, modern_data

# def prepare_text(original, modern):
    # original, modern = original.lower(), modern.lower()
    # tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
    # original_tokenized = tokenizer.tokenize(original)
    # modern_tokenized = tokenizer.tokenize(modern)
    # return original_tokenized, modern_tokenized
    
def merge_plays(path):
    plays_original_list = []
    plays_modern_list = []
    name_plays = []
    file_list = sorted(os.listdir(path))
    for filename in file_list:
        if 'original' in filename:
            plays_original_list.append(os.path.join(path, filename))
        if 'modern' in filename:
            plays_modern_list.append(os.path.join(path, filename))
    len_original_plays, len_modern_plays = get_len_plays(plays_original_list, plays_modern_list)
    with open('merged_plays_original1.aligned', 'a+') as outfile_orig, open('merged_plays_modern1.aligned', 'a+') as outfile_mod:
        for name_o, name_m, len_o, len_m in zip(plays_original_list, plays_modern_list, len_original_plays, len_modern_plays):
            if len_o == len_m:
                name_play = get_name_play(name_o)
                name_plays.append(name_play)
                with open(name_o, 'r') as a, open(name_o, 'r') as b:
                    orig_text, mod_text = a.read(), b.read()
                    for line in orig_text:
                        outfile_orig.write(line)
                    for line in mod_text:
                        outfile_mod.write(line)
    return len_original_plays, len_modern_plays, name_plays


def get_len_plays(plays_original_list, plays_modern_list):
    len_original_plays, len_modern_plays = [], []
    for name_o, name_m in zip(plays_original_list, plays_modern_list):
            with open(name_o, 'r') as a, open(name_o, 'r') as b:
                orig_text, mod_text = a.read(), b.read()
                if len(orig_text) == len(mod_text):
                    len_original_plays.append(len(orig_text)), len_modern_plays.append(len(mod_text))
    
    return len_original_plays, len_modern_plays

def get_name_play(filename):
    filename = filename.rsplit('/',1)[1]
    index = filename.find('_ori')
    return filename[:index]

    
