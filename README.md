# tf-idf
[![Build Status](https://travis-ci.org/juliuste/tf-idf.svg?branch=master)](https://travis-ci.org/juliuste/tf-idf) [![Python](https://img.shields.io/badge/python-2.7, 3.3, 3.5-blue.svg)](https://www.python.org/)


This script implements the TF-IDF term relevance scoring as described on [Wikipedia's article](http://en.wikipedia.org/wiki/Tf–idf).

Its purpose is to generate the TF-IDF ratings for a collection of documents **in German**. This script will also tokenize the input files to extract words (removes punctuation).

## Usage
- Create a file to hold the paths+names of all your documents (in the example shown: `examples/input.txt`)
- Make sure you have the full paths to the files listed in the file above each on a separate line
- For now, the documents are only collections of text, no HTML, XML, RDF, or any other format
- Simply run this script file with your input file as a single parameter, for example:

```python tfidf.py examples/input.txt```

- This script will generate new files, one for each of the input files, with the prefix `tfidf_` which contains terms with corresponding tf-idf score, each on a separate line

This script is based on [Yasser Elsayed](https://github.com/yebrahim/)'s [TF-IDF-Generator](https://github.com/yebrahim/TF-IDF-Generator) module, still in active development and currently in alpha status.

## Contributing

If you found a bug, want to propose a feature or feel the urge to complain about your slightly below-average life, feel free to visit [the issues page](https://github.com/juliuste/tf-idf/issues).