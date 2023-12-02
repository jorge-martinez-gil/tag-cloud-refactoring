# Tag cloud refactoring
This repository delivers a possible implementation for the paper:

*MaSiMe: A Customized Similarity Measure and Its Application for Tag Cloud Refactoring*
[https://doi.org/10.1007/978-3-642-05290-3_112](https://doi.org/10.1007/978-3-642-05290-3_112)

The code is a Python script that leverages the Natural Language Toolkit (NLTK) and its WordNet interface to analyze and modify a given tag cloud by mapping each word to its most frequently associated synonym based on the provided data.

## Description

The script performs the following key operations:
- Initializes a sample tag cloud as a dictionary with words and their respective counts.
- Finds synonyms for each word using NLTK's WordNet.
- Maps each word in the tag cloud to its most frequent synonym.
- Aggregates the counts of the original words based on this new mapping.
- Outputs a modified tag cloud reflecting these changes.

## Installation

Before running the script, ensure you have Python installed on your system. Additionally, you will need NLTK and its WordNet dataset. Follow these steps to set up:

1. **Install Python**: Download and install Python from [the official website](https://www.python.org/downloads/).
2. **Install NLTK**: Run the following command to install NLTK: 
```bash
pip install nltk
```
4.  **Download WordNet Data**: The script will automatically download the necessary WordNet data from NLTK. However, you can also manually download it using a Python interpreter:

```python
 import nltk 
 nltk.download('wordnet')
 ```
    
## Usage

To use the script, simply run it with a Python interpreter. You can modify the `tag_cloud` dictionary in the script to use your own data. The script will output the new tag cloud based on synonym mappings.

`python app.py` 

## Note

-   The script's efficiency and accuracy are dependent on the WordNet dataset's coverage.
-   Synonym mappings are based on the frequency of words in the initial tag cloud, which may not always represent semantic similarity accurately.

## License

This script is provided as-is under the MIT License. Feel free to use, modify, and distribute as needed.