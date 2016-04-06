from gensim.models import Word2Vec
m = Word2Vec.load_word2vec_format('/srv/guten/GoogleNews_word2vec_vectors_negative300', binary=True)
m.most_similar(positive=['we', 'people', 'person', 'us'])
m.most_similar(positive=['we', 'people', 'person', 'us'], negative=['female', 'woman', 'women'])
m.most_similar(positive="A woman king".split())
m.doesnt_match("breakfast cereal dinner lunch")
m.doesnt_match("breakfast cereal dinner lunch".split())
m.vocab
'a' in m.vocab
sentence = "Hello world, I'm a hungry man."
m.most_similar([w for w in sentence.split() if w in m.vocab])
sentence = "because is an extra ripeness even more evident on a line here and tell me I have morals"
m.most_similar("decide")
m.seed_vector("random")
m.seeded_vector("random")
m.most_similar([w for w in sentence.split() if w in m.vocab])
sentence
m['hello']
m['a']
m['king']
