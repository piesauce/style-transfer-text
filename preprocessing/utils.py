import os
import numpy as np
import pandas as pd
import nltk
from keras.preprocessing.sequence import pad_sequences

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

def load_data(path):
    with open(os.path.join(path,'merged_plays_original2.aligned'), 'r') as orig, open(os.path.join(path, 'merged_plays_modern2.aligned'), 'r') as mod:
        original_text = orig.read()
        modern_text = mod.read()
    return original_text, modern_text

def preprocess(original, modern):
    orig_preprocessed = [line.strip().lower().split(' ') for line in original]
    mod_preprocessed = [line.strip().lower().split(' ') for line in modern]
    return orig_preprocessed, mod_preprocessed
    

def initialize_vocab():
    word_to_idx = {}
    idx_to_word = {}
    num_words = 0
    word_counts = {}
    
    special_entries = ['PAD', 'START', 'END', 'UNK']
    for symbol in special_entries:
        word_to_idx[symbol] = num_words
        idx_to_word[num_words] = symbol
        word_counts[symbol] = 1
        num_words += 1
    return word_to_idx, idx_to_word, num_words, word_counts

def fill_common_vocab(word_to_idx, idx_to_word, num_words, word_counts, original, modern):
    for line in original:
        for word in line:
            if word not in word_to_idx:
                word_to_idx[word] = num_words
                idx_to_word[num_words] = word
                word_counts[word] = 1
                num_words += 1
            else:
                word_counts[word] += 1
    for line in modern:
        for word in line:
            if word not in word_to_idx:
                word_to_idx[word] = num_words
                idx_to_word[num_words] = word
                word_counts[word] = 1
                num_words += 1
            else:
                word_counts[word] += 1
    return word_to_idx, idx_to_word, num_words, word_counts

def truncate_vocab(word_counts, max_vocab_size):
    word_to_idx, idx_to_word, num_words, truncated_word_counts = initialize_vocab()
    truncated_word_counts = sorted(word_counts, key=word_counts.get, reverse=True)[:max_vocab_size]
    for word in truncated_word_counts:
        if word not in ['UNK', 'PAD', 'START', 'END']:
            word_to_idx[word] = num_words
            idx_to_word[num_words] = word
            num_words += 1
    
    return word_to_idx, idx_to_word, num_words, truncated_word_counts

def prepare_sequences(orig, mod, word_to_idx):
    orig_sequences = []
    mod_sequences = []
    for line in orig:
        temp = [word_to_idx['START']]
        for word in line:
            if word not in word_to_idx:
                temp.append(word_to_idx['UNK'])
            else:
                temp.append(word_to_idx[word])
        temp.append(word_to_idx['END'])
        orig_sequences.append(temp)
    for line in mod:
        temp = [word_to_idx['START']]
        for word in line:
            if word not in word_to_idx:
                temp.append(word_to_idx['UNK'])
            else:
                temp.append(word_to_idx[word])
        temp.append(word_to_idx['END'])
        mod_sequences.append(temp)
    return orig_sequences, mod_sequences
    
def pad_seq(orig_sequences, mod_sequences):
    orig_seq_padded = pad_sequences(orig_sequences, maxlen=25, padding='pre', truncating='post')
    mod_seq_padded = pad_sequences(mod_sequences, maxlen=25, padding='post', truncating='post')
    return orig_seq_padded, mod_seq_padded

def toText(text, idx_to_word):
    return [idx_to_word[word] for word in text]

    
