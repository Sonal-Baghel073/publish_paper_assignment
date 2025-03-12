import argparse
import pubmed_fetcher


def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Save results to CSV file")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()

    print(f"🔍 Searching PubMed for: {args.query}")
    
    try:
        paper_ids = pubmed_fetcher.fetch_paper_ids(args.query, max_results=10)
        results = [pubmed_fetcher.fetch_paper_details(pid) for pid in paper_ids]
        results = [res for res in results if res]  # Filter out None results

        if args.file:
            pubmed_fetcher.save_results_to_csv(results, args.file)
        else:
            for res in results:
                print(res)
    
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
