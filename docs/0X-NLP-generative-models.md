# Generative Models

## Computational Discourse

Dialogue bots can be built using both statistical language models and grammar-based models.

### Statistical Models

- Markhov Chain Monte Carlo (MCMC)
- Canvolutioanl Neural Networks (CNNs)
- Recurrent Neural Networks (RNNs)
- Logistic Regression

### Grammar-Based Models

Many different "grammar-based" tools can be combined in a computational discourse engine. Most of these algorithms can be implemented in a Finite Space Automata (deep, complicated regular expressions). See _Speech_and_Language_Processing_ by Jurafsky and Martin for more details.

- Automatic Coherence Assignment
- Segmentation
- Reference Resolution
- Pronomial Anaphora Resolution
- Anaphora Resolution Algorithms
  - Hobbs Algorithm
  - Centering Algorithm
  - Log-Linear Model

## MQA - Multilingual Question and Answer Engine

The Learning Machines 101 Podcast provided a [nice summary](http://www.learningmachines101.com/lm101-045-how-to-build-deep-learning-machine-answering-questions-about-images/) of a paper from China scientists who demonstrated a system for answering questions about images.

There are 3 components to a machine learning system used to answer natural language questions about images. Imagine a picture of a dinner table, and a judge asking the machine, through a chat interface, "What kind of vegetable is on the plate in the image."

- Question Natural Language -> Semantic Representation
  - RNN 
  - generate features based on sequences of words
  - predict the next word in the sequence based on the previous words
  - this produces a compressed representation
  - use the features ass
- Image -> Semantic Representation 
  - Pretrained Google Image CNN
  - Extracts features (edges, corners, "roughness", "flow")
  - computes semantic content of the image based on the
- Answer generation from the two semantic 
  - Same RNN as in the Question processing step
  - Run the semantic represenations of the image and question backwards through the RNN?

## References

[2008-Aceves-Perez: Answer Fusion...](https://ccc.inaoep.mx/~villasen/articulos/AnswerFusionInMultilingualQA-TSD07.pdf)
[2015 Gau at arXiv: Multilingual QA](http://arxiv.org/pdf/1505.05612v1.pdf) 
[2015 Gau at NiPs: mQA](http://papers.nips.cc/paper/5641-are-you-talking-to-a-machine-dataset-and-methods-for-multilingual-image-question.pdf)
[2015 Gau mQA data](http://face.baidu.com/nips/FM-IQA.tar.gz)