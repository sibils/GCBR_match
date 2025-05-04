# gcbr-match

This repository contains the code used to identify mentions of Global Core Biodata Resource (GCBR) names and their corresponding accession numbers within a corpus of scientific texts. This code was developed by the SIBiLS team, at Swiss Institute of Bioinformatics, as part of a study to compare the amount GCBR information in main manuscripts versus supplementary data files.

## Repository Contents

* `src/`: Contains the main Python scripts or other code files used for the matching process.
    * `collection_sample.json`: a sample collection of texts. List of dictionaries with the document identifier ("_id") and text ("text")
    * `GCBRs.csv`: a CSV file (delimiter \t) with GCBRs names, regular expression for matching names, and a list of regular expressions for matching accession numbers, taken from identifiers.org (range from 0 to n).
    * `match.py`: script for identifying GCBR names and accession numbers in a collection.
* `README.md`: This file, providing an overview of the repository.
* `LICENSE`: MIT License, Apache 2.0.

### Usage

* **Names and accession numbers matching:**
    ```bash
    python src/gcbr_match/match.py
    ```

## Notes and Limitations

The primary focus of the study is not to exhaustively identify every mention of GCBRs, but rather to compare the relative amount of information within supplementary data files against within manuscripts. For this purpose, we rely on simple methodological approach, prioritizing high precision (minimizing false positives) over maximal recall (capturing all possible instances).

## Contributing

If you would like to contribute to this project, please feel free to:

* Submit bug reports or feature requests as issues.
* Fork the repository and submit pull requests with your changes.

## License

MIT License
