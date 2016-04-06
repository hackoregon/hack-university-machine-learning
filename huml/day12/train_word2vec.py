from gensim.models import Word2Vec
model = Word2Vec(open('/srv/guten/0/1/1.sent').read().split('\n'), size=100, window=5, min_count=5, workers=2)
model.save('~/src/guten/data/independence.w2v')
model.most_similar(positive=['People', 'we', 'states'])
model = Word2Vec([sent.split() for sent in open('/srv/guten/0/1/1.sent').read().split('\n')], size=100, window=5, min_count=5, workers=2)
model.most_similar(positive=['People', 'we', 'states'])
model.most_similar(positive=['People', 'we', 'people', 'person', 'us'])
model.most_similar(positive=['we', 'people', 'person', 'us'])
google_model = Word2Vec.load('/srv/guten/GoogleNews-vectors-negative300.bin.gz')
