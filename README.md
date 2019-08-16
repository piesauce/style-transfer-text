# style-transfer-text
Pointer networks for translating between Shakespearean and Modern English

The aim of this project is to explore translation between Shakespearean and Modern English. Sequence to sequence models with 
pointer networks are employed for this purpose.

Data

Data comprises of texts from Shakespearean plays. Thanks to https://github.com/cocoxu/Shakespeare/tree/master/data
The data folder also contains the Shakespeare-English dictionary, which will be leveraged while pre-training embeddings.

The eda folder contains data analyis of the Shakespearan plays, exploring the key characteristics, frequency distribution, and idiosyncracies of the text

The models folder contains a pytorch implementation of seq2seq with a pointer component. Also present is the retrofitting of pre-trained embeddings.

The evaluation folder contains evaluation of style transfer measured through BLEU and PINC metrics

