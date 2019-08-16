# style-transfer-text
Pointer networks for translating between Shakespearean and Modern English

The aim of this project is to explore translation between Shakespearean and Modern English. Sequence to sequence models with 
pointer networks are employed for this purpose.

Data
The training data is comprised of text from 14 Shakespearean play along with their translations in modern English. The data is taken from /cocoxu's [repository]( https://github.com/cocoxu/Shakespeare/tree/master/data). The data folder also contains a shakespearean english - modern english dictionary, also taken from [https://github.com/cocoxu/Shakespeare/](https://github.com/cocoxu/Shakespeare/)

The eda folder contains data analyis of the Shakespearan plays, exploring the key characteristics, frequency distribution, and idiosyncracies of the text

The models folder contains a pytorch implementation of seq2seq with a pointer component. Also present is the retrofitting of pre-trained embeddings by leveraging the Shakespearean-Modern English dictionary.

The evaluation folder contains evaluation of style transfer measured through BLEU and PINC metrics

