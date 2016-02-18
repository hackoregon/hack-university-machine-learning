# Graphs

[Graph Theory](https://en.wikipedia.org/wiki/Graph_theory) is the study of algorithms, datastructures, and mathematics of graphs (networks of connections).

## Applications

- sociology
  - social connections between people
  - viral and meme "epidemiology"
- biology
  - speciation and evolution
  - symbiosis, ecosystems, interdependence and competition 
- game playing
- path planning
  - google maps
  - traveling salesman problems
  - map coloring problem
- logic
- problem solving
- algebra equation simplification and solving
- communication
  - computer networks, architecture optimization
  - computer virology and epidemiology

## Data Structures

There are [3 fundamental ways](https://en.wikipedia.org/wiki/Graph_(abstract_data_type)) to represent/store a graph:

1. [Adjacency Matrix](https://en.wikipedia.org/wiki/Adjacency_matrix)
  - Straight-forward to implement and do math on, but can be a memory Hog
  - Use `scipy.sparse` to save space
  - [Word-Word Matrix](http://hobsonlane.com/pug/pug/miner/static/word_cooccurrence_matrix.html)
  - [US President Inaugural Speeches](http://hobsonlane.com/pug/pug/miner/static/doc_cooccurrence_matrix.html)
  - [2-layer nested dict in python]([dicts in python](http://stackoverflow.com/a/13547260))
2. [Adjacency List](https://en.wikipedia.org/wiki/Adjacency_list) 
  - [d3 dict of two lists](https://github.com/totalgood/hackor/blob/master/bin/similarity_nlp.py): `"nodes": [], "links": []`
  - [nested dicts in python](http://stackoverflow.com/a/13547260)
3. [Incidence Matrix](https://en.wikipedia.org/wiki/Incidence_matrix) 
  - mainly used for graph math (graph theory)
  - I've never seen them used in an algorithm or data structure


## Databases

Graph databases implement indexes to facilitate traversals. Most have a relational database (like PostGRESQL) under the hood. PostGRESQL can outperform most graph databases at graph search to a depth of about 5 or 6. So if you've only got 6 degrees of separation, you might be able to get away with a conventional DB!


- [Neo4J](http://neo4j.com/): [Open source](https://github.com/neo4j/neo4j) graph database written in Java
  - Nicole White's demo of [alchemy.js](https://nicolewhite.github.io/2014/07/24/visualize-subset-neo4j-alchemy.html) which adds d3 to Neo4J
  - Huston's [GraphJSON data structure](https://github.com/GraphAlchemist/GraphJSON/blob/gh-pages/examples/data/bacon.json) 
- [NetworkX](https://networkx.github.io/documentation/latest/tutorial/)
  - [python](http://networkx.github.io/documentation/latest/examples/javascript/force.html) to create a force-directed d3 graph ([source code](https://github.com/networkx/networkx/tree/master/examples/javascript))
  - [Pygraphviz plotting tool](http://pygraphviz.github.io/documentation/pygraphviz-1.3rc1/tutorial.html)
Graph Data Structures, Regular Expressions, FSA, NFA, DFA, Data-driven video games vs choose-your-own adventure games/books DIY Chat Bots (twitter or slack)
- [iGraph](https://github.com/igraph/python-igraph)
- [Norvig's pure Python "Graph DB"](http://aima.cs.berkeley.edu/python/search.html)

## [Drawing (Layout)](https://en.wikipedia.org/wiki/Graph_drawing)

Graphs have no inherent geometry.
Graph have no inherent number of dimensions.
Graphs can be "embedded" or "flattened" in 2 dimensions for visualization

### Layout Options (e.g. in pyGraphViz)
  - circle
  - star
  - tree 
  - force-directed?

### [Force-Directed Layout](https://en.wikipedia.org/wiki/Force-directed_graph_drawing)

- Difficult to implement
- Usually get a different answer every time
  - Unless your graph has a stable structure!
  - Trusses in 3-D will repeatably reach stable configuration
- Computationally expensive
- d3.js puts that computation on the "client"
- Barnes-Hutt simulation algorithm improves efficiency over exchaustive N^2 approaches
- Great form of unsupervised learning
  - clusters develop "automatically"
  - structure inherent to the graph and not imposed by the algorithm
- Its Natural!

## d3 Graph Examples

Very little python required to generate the json files, [javascript](https://github.com/hobson/pug/tree/gh-pages/pug/miner/static) does all the work.

- [Word-Word Matrix](http://hobsonlane.com/pug/pug/miner/static/word_cooccurrence_matrix.html)
- [Word-Word Force-Directed Graph](http://hobsonlane.com/pug/pug/miner/static/word_force_graph.html)
- [Document-Document Matrix](http://hobsonlane.com/pug/pug/miner/static/doc_cooccurrence_matrix.html)
- [Document-Document Graph](http://hobsonlane.com/pug/pug/miner/static/doc_force_graph.html)
- [Document-Word-Document Force-Directed Graph](http://hobsonlane.com/pug/pug/miner/static/occurrence_force_graph.html)
- [Hack Oregon Behind the Curtain](http://hobsonlane.com/pug/pug/miner/static/pac_nlp_force_graph.html)
- [Hack Oregon Behind the Curtain, fewer nodes](http://hobsonlane.com/pug/pug/miner/static/pac_nlp_force_graph_smaller.html)