import requests
import xml.etree.ElementTree as ET
import pandas as pd
from typing import List, Dict, Optional

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"


def fetch_paper_ids(query: str, max_results: int = 10) -> List[str]:
    """
    Fetches PubMed paper IDs based on a search query.
    
    :param query: Search query for PubMed
    :param max_results: Number of results to fetch
    :return: List of PubMed IDs
    """
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "xml",
        "retmax": max_results
    }
    
    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        raise Exception("Failed to fetch PubMed data")

    root = ET.fromstring(response.content)
    return [id_elem.text for id_elem in root.findall(".//Id")]


def fetch_paper_details(paper_id: str) -> Optional[Dict]:
    """
    Fetches details of a paper from PubMed using its ID.
    
    :param paper_id: PubMed paper ID
    :return: Dictionary containing paper details
    """
    params = {
        "db": "pubmed",
        "id": paper_id,
        "retmode": "xml"
    }

    response = requests.get(FETCH_URL, params=params)
    if response.status_code != 200:
        return None

    root = ET.fromstring(response.content)
    article = root.find(".//PubmedArticle")
    
    if article is None:
        return None

    title = article.find(".//ArticleTitle").text if article.find(".//ArticleTitle") is not None else "N/A"
    pub_date = article.find(".//PubDate/Year").text if article.find(".//PubDate/Year") is not None else "Unknown"
    
    # Extract author information
    authors = article.findall(".//Author")
    non_academic_authors = []
    company_affiliations = []
    corresponding_email = "N/A"

    for author in authors:
        affiliation = author.find(".//AffiliationInfo/Affiliation")
        email = author.find(".//AffiliationInfo/Email")

        if affiliation is not None:
            aff_text = affiliation.text.lower()
            if "pharma" in aff_text or "biotech" in aff_text or "inc." in aff_text or "ltd." in aff_text:
                non_academic_authors.append(author.find("LastName").text)
                company_affiliations.append(aff_text)

        if email is not None and corresponding_email == "N/A":
            corresponding_email = email.text

    return {
        "PubmedID": paper_id,
        "Title": title,
        "Publication Date": pub_date,
        "Non-academic Authors": ", ".join(non_academic_authors) if non_academic_authors else "None",
        "Company Affiliations": ", ".join(company_affiliations) if company_affiliations else "None",
        "Corresponding Author Email": corresponding_email
    }


def save_results_to_csv(results: List[Dict], filename: str = "papers.csv"):
    """
    Saves the results to a CSV file.
    
    :param results: List of paper details
    :param filename: Name of the CSV file
    """
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)
    print(f"✅ Results saved to {filename}")
