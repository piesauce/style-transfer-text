import numpy as np
import pandas as pd
import nltk
import preprocessing.utils




train = encoder_inputs, decoder_inputs, decoder_outputs, matching_tokens_arraydef fit_batch(train):

def fit_batch(train):
    batch_cutoff = config.batch_size * (len(train[0]) // config.batch_size)
    encoder_inputs, decoder_inputs, decoder_outputs, matching_tokens_array = train
    encoder_inputs = encoder_inputs[:batch_cutoff]
    decoder_inputs = decoder_inputs[:batch_cutoff]
    decoder_outputs = decoder_outputs[:batch_cutoff]
    matching_tokens_array = matching_tokens_array[:batch_cutoff]
    train = encoder_inputs, decoder_inputs, decoder_outputs, matching_tokens_array
    return train

train_batches = fit_batch(train)  