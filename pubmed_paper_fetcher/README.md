# PubMed Paper Fetcher

## Overview
This project is a Python-based command-line tool that fetches research papers from **PubMed**, filters them based on **pharmaceutical/biotech author affiliations**, and exports the results in **CSV format**.

## Features
✅ Fetches research papers using **PubMed's E-utilities API**  
✅ Filters papers with **pharmaceutical/biotech-affiliated authors**  
✅ Saves structured results to **CSV**  
✅ **Command-line support** with flexible arguments  
✅ **Optimized API calls** for efficiency  
✅ **Robust error handling** for invalid queries and network issues  

## Installation
This project uses **Poetry** for dependency management. To install dependencies, run:
```sh
pip install poetry  # Install Poetry if not already installed
poetry install      # Install project dependencies
```

## Usage
Run the following command to fetch papers:
```sh
poetry run get-papers-list "cancer research"
```

### Command-line options:
- `-f` or `--file <filename>` → Save results to a CSV file.  
- `-d` or `--debug` → Enable debug mode.

Example:
```sh
poetry run get-papers-list "gene therapy" -f results.csv -d
```

## Output Format
Results are stored in a **CSV file** with the following structure:
| PubMedID | Title | Publication Date | Non-academic Author(s) | Company Affiliation(s) | Corresponding Author Email |
|----------|-------|------------------|------------------------|------------------------|----------------------------|
| 12345678 | Cancer Treatment with XYZ Drug | 2025-01-15 | John Doe | PharmaCo Ltd. | johndoe@pharmaco.com |
| 23456789 | New Insights in Cancer Research | 2024-12-10 | Jane Smith | BioTech Inc. | janesmith@biotechinc.com |

## Project Structure
```
📂 pubmed_research/
 ├── pubmed_fetcher.py    # API interaction and processing logic
 ├── main.py              # Command-line interface
 ├── pyproject.toml       # Poetry configuration
 ├── README.md            # Project documentation
 ├── .gitignore           # Ignore unnecessary files
```

## Future Enhancements
🚀 **AI-based Author Classification**: NLP-based affiliation analysis.  
🚀 **Multithreading Support**: Faster data retrieval.  
🚀 **Additional Filters**: Research impact-based ranking.  
🚀 **Cross-Database Search**: Expand to **arXiv**, **Google Scholar**.  

## License
This project is open-source and available under the **MIT License**.

## Contributing
Contributions are welcome! Feel free to open **issues** or **pull requests**.

## Author
Developed by **Sonal Baghel**  
📧 Contact: [sonalbaghel073@gmail.com](mailto:sonalbaghel073@gmail.com)
