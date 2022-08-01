# TLN-LAB-PART-2: NLP exercises proposed during the TLN course at the University of Turin. More precisely, they concern lexical semantics

### Authors: @PaoloBonicco7

#### @UniTo

---

### ES.1 - Conceptual Similarity

In the first exercise we try to find the conceputal similarity between 2 word, using "WordSim353.csv" file.
The file is organized as follows:

- Word 1, Word 2, Human (mean) --> (an example of a row) love, sex, 6.77

The numeric value correspond to the score of similarity between the 2 word (Word 1 and Word 2), on a scale
between 0 and 10 [0, 10].

In the first part of the excercise we calculate 3 different mesure of similarity and then we evaluate the result
with the following index:

- Spearman correlation coefficient
- Pearson correlation coefficient 

between our results and the result in the csv file

We will take advantage of WordNet and its tree structure for this task.

The 3 different mesure of similarity are:

- Wu and Palmer:
  - cs(s1, s2) = [2 · depth(LCS)] / [depth(s1) + depth(s2)]
    - LCS = lowest common hypernyms
    - depth(x) = WordNet function that returns the depth of the node x in the tree, aka
        the length of the path from the root to the synset x

- Shortest Path:
  - sim_path(s1, s2) = 2 · depthMax - len(s1, s2)
    - depthMax: fixed value in WordNet
  - The value of sim_path is between 0 and 2 * depthMax

- Leakcock & Chodorow:
  - simLC (s1, s2) =  log [len(s1, s2) / 2 · depthMax]
    - To avoid log(0) we add 1 to the numerator and denominator
  - thus the values of simLC(s1,s2) are in the interval [0,log(2*depthMax +1)]

---

