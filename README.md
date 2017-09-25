# SoundexGenerator
The Soundex algorithm is a phonetic algorithm commonly used by libraries and the Census Bureau to represent people's names as they are pronounced in English. It has the advantage that name variations with
minor spelling differences will map to the same representation, as long as they have the same pronunciation in English. 

Here is how the algorithm works:
Step 1: 
Retain the first letter of the name. This may be uppercased or lowercased.

Step 2: 
Remove all non-initial occurrences of the following letters: a, e, h, i, o, u, w, y. 

Step 3: Replace the remaining letters (except the first) with numbers:

* b, f, p, v -> 1
* c, g, j, k, q, s, x, z -> 2
* d, t -> 3
* l -> 4
* m, n -> 5
* r -> 6

The given python code builds a Finite State Transducer to generate soundex for the given input.
