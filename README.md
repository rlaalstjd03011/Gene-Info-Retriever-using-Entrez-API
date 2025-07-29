# Gene-Info-Retriever-using-Entrez-API

# 🧬 NCBI Gene Summary Fetcher using Entrez API

This Python script retrieves gene summary information for specified human genes using NCBI's Entrez API, provided by the `Biopython` library.  
It allows you to automatically search for gene IDs and fetch their corresponding summaries without manually accessing the NCBI website.

## 📌 Features

- Automatically search for gene IDs using gene names (e.g., TP53, BRCA1, EGFR)
- Fetch detailed gene summaries via the NCBI Entrez API
- Display the number of search results and provide direct NCBI links for each gene
- Supports multiple genes in a single run

## 📁 Structure

- Uses **`Entrez.esearch`** to find gene IDs based on gene names
- Uses **`Entrez.efetch`** to fetch detailed XML data of each gene
- Parses and prints the gene summary
- Includes comments for educational purposes

## 🛠️ Requirements

- Python 3.x
- [Biopython](https://biopython.org/) (`pip install biopython`)
- NCBI Entrez API access (you must provide your email)

## 🚀 How to Run

1. Install Biopython:
   ```bash
   pip install biopython
