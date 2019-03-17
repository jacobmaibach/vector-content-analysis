### based on script from machinelearningmastery.com

from sklearn.decomposition import PCA
from matplotlib import pyplot

from model_util import Word2Vec
from data_util import load_words,load_pairs
from file_util import OUTPUT_DIR

words_obj = load_words()
model = Word2Vec(words_obj.listed)

### rep

def get_word_rep():
    return model[model.wv.vocab]

def get_sentence_rep(ignore_empty = False):
    out = []
    for sentence in words_obj:
        vectorized = [model[word] for word in sentence if word in model.wv.vocab]
        if(not vectorized):
            if(not ignore_empty):
                out.append(None)
        else:
            avg = sum(vectorized)/len(vectorized)
            out.append(avg)
    return out

def get_word_rep_by_sentence(ignore_empty = False):
    out = []
    for sentence in words_obj:
        vectorized = [model[word] for word in sentence if word in model.wv.vocab]
        if(not vectorized):
            if(not ignore_empty):
                out.append(None)
        else:
            out.append(vectorized)
    return out

## support

def get_sentence_labels(words_obj):
    return [' '.join(sentence) for sentence in words_obj]

def reduce(vals,labels):
    out_vals = []
    out_labels = []
    for x,s in zip(vals,labels):
        if(x is not None):
            out_vals.append(x)
            out_labels.append(s)
    return out_vals,out_labels

def reduce_nested(first,second): # not working - empty output
    first,second = reduce(first,second)
    out_first = []
    out_second = []
    for (x,y) in zip(first,second):
        try:
            new = reduce_nested(x,y)
            if(new[0]):
                out_first.append(new[0])
                out_second.append(new[1])
        except TypeError:
            pass
    return out_first,out_second

### visualize

def pca_visualize(rep,labels=None,n=2):
    if(labels is None):
        labels = list(model.wv.vocab)
    pca = PCA(n_components=n)
    result = pca.fit_transform(rep)
    # create a scatter plot of the projection
    pyplot.scatter(result[:, 0], result[:, 1])
    for i, word in enumerate(labels):
       pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
    pyplot.show()

def pca_visualize_iterative(rep_list,labels_list,n=2):
    pca = PCA(n_components=n)
    for i,(rep,labels) in enumerate(zip(rep_list,labels_list)):
        result = pca.fit_transform(rep)
        pyplot.scatter(result[:, 0], result[:, 1])
        for i, word in enumerate(labels):
            pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
        pyplot.savefig(OUTPUT_DIR + 'sentence_{i}.pdf'.format(i=i))