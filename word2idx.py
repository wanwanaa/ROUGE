def get_datasets(filename):
    datasets = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            datasets.append(line)
    return datasets


def get_vocab(datasets):
    vocab = set()
    for line in datasets:
        line = line.split()
        for i in line:
            vocab.add(i)
    return vocab


def get_word2idx(vocab):
    vocab = list(vocab)
    word2idx = {}
    for num, v in enumerate(vocab):
        word2idx.get(v)
        word2idx[v] = num
    return word2idx


def sents2idx(datasets, word2idx):
    result = []
    for line in datasets:
        line = line.split()
        r = []
        for c in line:
            r.append(str(word2idx[c]))
        r = ' '.join(r)
        result.append(r)
    return result


if __name__ == '__main__':
    gold_filename = 'gold_summaries.txt'
    hyp_filename = 'summary.txt'
    gold = 'model_summary.txt'
    hyp = 'system_summary.txt'

    # datasets
    gold_datasets = get_datasets(gold_filename)
    hyp_datasets = get_datasets(hyp_filename)
    # vocab
    vocab = get_vocab(gold_datasets)
    vocab2 = get_vocab(hyp_datasets)
    vocab = vocab.union(vocab2)
    # word2idx
    word2idx = get_word2idx(vocab)

    # sentence to index
    gold_result = sents2idx(gold_datasets, word2idx)
    hyp_result = sents2idx(hyp_datasets, word2idx)

    # write result
    with open(gold, 'w', encoding='utf-8') as f:
        f.write('\n'.join(gold_result))
    with open(hyp, 'w', encoding='utf-8') as f:
        f.write('\n'.join(hyp_result))





