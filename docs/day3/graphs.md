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

1. [Adjacency Matrix]()
2. [Adjacency List](https://en.wikipedia.org/wiki/Adjacency_list) 
    - [d3 dict of two lists](https://github.com/totalgood/hackor/blob/master/bin/similarity_nlp.py): `"nodes": [], "links": []`
3. [] 

These are easy to implement [in python](http://stackoverflow.com/a/13547260)


## Graph Databases

- [Neo4J](http://neo4j.com/): [Open source](https://github.com/neo4j/neo4j) graph database written in Java
  - Nicole White's demo of [alchemy.js](https://nicolewhite.github.io/2014/07/24/visualize-subset-neo4j-alchemy.html) which adds d3 to Neo4J
  - Huston's [GraphJSON data structure](https://github.com/GraphAlchemist/GraphJSON/blob/gh-pages/examples/data/bacon.json) 
- [NetworkX](https://networkx.github.io/documentation/latest/tutorial/)
  - [python](http://networkx.github.io/documentation/latest/examples/javascript/force.html) to create a force-directed d3 graph ([source code](https://github.com/networkx/networkx/tree/master/examples/javascript))
  - [Pygraphviz plotting tool](http://pygraphviz.github.io/documentation/pygraphviz-1.3rc1/tutorial.html)
Graph Data Structures, Regular Expressions, FSA, NFA, DFA, Data-driven video games vs choose-your-own adventure games/books DIY Chat Bots (twitter or slack)
- [Norvig's pure Python "Graph DB"](http://aima.cs.berkeley.edu/python/search.html)

## d3 Graph Examples

Very little python required to generate the json files, [javascript](https://github.com/hobson/pug/tree/gh-pages/pug/miner/static) does all the work.

- [Word-Word Matrix](http://hobsonlane.com/pug/pug/miner/static/word_cooccurrence_matrix.html)
- [Word-Word Force-Directed Graph](http://hobsonlane.com/pug/pug/miner/static/word_force_graph.html)
- [Document-Document Matrix](http://hobsonlane.com/pug/pug/miner/static/doc_cooccurrence_matrix.html)
- [Document-Document Graph](http://hobsonlane.com/pug/pug/miner/static/doc_force_graph.html)
- [Document-Word-Document Force-Directed Graph](http://hobsonlane.com/pug/pug/miner/static/occurrence_force_graph.html)
- [Hack Oregon Behind the Curtain](http://hobsonlane.com/pug/pug/miner/static/pac_nlp_force_graph.html)
- [Hack Oregon Behind the Curtain, fewer nodes](http://hobsonlane.com/pug/pug/miner/static/pac_nlp_force_graph_smaller.html)