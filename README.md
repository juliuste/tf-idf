# tf-idf

This script implements the TF-IDF term relevance scoring as described on [Wikipedia's article](http://en.wikipedia.org/wiki/Tf–idf).

Its purpose is to generate the TF-IDF ratings for a collection of documents **in German**. This script will also tokenize the input files to extract words (removes punctuation).

## Usage
- Create a file to hold the paths+names of all your documents (in the example shown: `input.txt`)
- Make sure you have the full paths to the files listed in the file above each on a separate line
- For now, the documents are only collections of text, no HTML, XML, RDF, or any other format
- Simply run this script file with your input file as a single parameter, for example:
```python tfidf.py input.txt```
- This script will generate new files, one for each of the input files, with the prefix `tfidf_` which contains terms with corresponding tf-idf score, each on a separate line

This script is a fork from [Yasser Elsayed](https://github.com/yebrahim/)'s [TF-IDF-Generator](https://github.com/yebrahim/TF-IDF-Generator) module, currently in alpha status and still in active development.

## Contributing

If you found a bug, want to propose a feature or feel the urge to complain about your slightly below-average life, feel free to visit [the issues page](https://github.com/juliuste/tf-idf/issues).