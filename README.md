# tf-idf
[![Build Status](https://travis-ci.org/juliuste/tf-idf.svg?branch=master)](https://travis-ci.org/juliuste/tf-idf) [![Python](https://img.shields.io/badge/python-3.2, 3.3, 3.4, 3.5-blue.svg)](https://www.python.org/)


This script implements the TF-IDF term relevance scoring as described on [Wikipedia's article](http://en.wikipedia.org/wiki/Tf–idf).

Its purpose is to generate the TF-IDF ratings for a collection of documents **in German**. This script will also tokenize the input files to extract words (removes punctuation).

**This script doesn't support Python 2.7 anymore.** For an older, compatible but less-maintained version of this tool check out [this branch](https://github.com/juliuste/tf-idf/tree/0.3).

## Usage
### Build your own script
- Download and import the `tfidf` module

```python
import tfidf
tfidf.analyze(inputFile, resultsPerDocument, preferNouns, showRanking, verbose)
``

Parameter | Type | Description
--------- | ---- | -----------
`inputFile` | String | Path to a file which holds the paths+names of all your documents (in the example shown: `example_data/input.txt`).
`resultsPerDocument` | Integer | *[optional]* Number of highest rated words per document to be output.
`preferNouns` | Boolean | *[optional]* If `true` the algorithm will favour nouns in the generated rankings. Default value: `false`.
`showRanking` | Boolean | *[optional]* If `false` the script will only output sorted lists of words based on their ranking instead of also displaying the ranking score for each word. Default value: `true`.
`verbose` | Boolean | *[optional]* If `true`: Enable console logging. Default value: `false`.

### Use the example script
- Create a file to hold the paths+names of all your documents (in the example shown: `example_data/input.txt`)
- Make sure you have the full paths to the files listed in the file above each on a separate line
- For now, the documents are only collections of text, no HTML, XML, RDF, or any other format
- Simply run the example script file with your input file as a single parameter (or use `-h` for a full list of options), for example:

```python3 example.py example_data/input.txt```

- This script will generate new files, one for each of the input files, with the prefix `tfidf_` which contains terms with corresponding tf-idf score, each on a separate line

This script is based on [Yasser Elsayed](https://github.com/yebrahim/)'s [TF-IDF-Generator](https://github.com/yebrahim/TF-IDF-Generator) module, still in active development and currently in alpha status.

## Contributing

If you found a bug, want to propose a feature or feel the urge to complain about your life, feel free to visit [the issues page](https://github.com/juliuste/tf-idf/issues).