# Natural Language Processing

## Natural vs machine language

- French vs. C
- Heiroglyphics vs. semaphores
- Morse Code?
- TCP/IP? 
- SQL?
- Python?

## Natural Language

- anything that can't be deterministically "compiled"
- compilation produces a machine-readable file
- database
- .exe file

## Formal Language

- finite set of "generative" rules
- you see something similar in software "help" files
- finite set of valid statements
- must be gramatically correct to be "accepted"
- Regular Expressions

## Two Approaches

- Grammar-based
- Statistical

## Grammar

- Grammar is hard for human
- Easy for a computer
- A lot like running a compilable language
- Rules are "made to be broken" by humans
- Software and algorithms are lengthy/complicated

## Stemmer Example

- Finding the root of a word is hard...
- ... for a machine
- Marting Porter has made a [career of it](http://tartarus.org/~martin/PorterStemmer/)
- His first stemmer was built [in 1979](http://tartarus.org/~martin/PorterStemmer/def.txt)
- Teaching a machine the rules to find the "root"
- A ["simplified" porter stemmer in python](../../huml/day4/porter.py)

## Statistical

- Statistical is easy for human
- Algorithms are count and sort and linear algebra
- Hard for a computer
    - Lots of RAM to remember all the words
    - Lots of CPU to multiply huge matrices

## Lots of Data

- Hyper-dimensional
    - Words are each unique "dimensions" with meaning
    - Google vocabulary is > 2M "words"
    - order of words affects meaning
- Google document memory
    - [30 Trillion pages](http://www.statisticbrain.com/total-number-of-pages-indexed-by-google/)
    - 100 Petabyte index
    - 1M servers 

## PCA + CNN = Magic!

- Deep Learning = PCA and many-layered Convolutional Neural Networks 
- No "hard-coding" required
- [Word2Vec](http://rare-technologies.com/word2vec-tutorial/) is uncannily good at "human" IQ tests
- PCA = LSA = LSI = SVD
    - Principal Component Analysis
    - Latent Semantic Analysis
    - Latent Semantic Indexing
    - Singular Value Decomposition

## Advanced Techniques

- [Kernel method](https://en.wikipedia.org/wiki/Kernel_method) for [information retrieval](http://www.jmlr.org/papers/volume2/lodhi02a/lodhi02a.pdf) document search/matching
- [LETOR](http://research.microsoft.com/en-us/um/beijing/projects/letor/) -- "Learning to Rank" search results
