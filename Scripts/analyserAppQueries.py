import json
import os
import re

def count_query_types(file_path):
    # Open and read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Initialize query type counts
    query_counts = {
        "CREATE": 0,
        "DROP": 0,
        "SELECT": 0,
        "INSERT": 0,
        "UPDATE": 0,
        "DELETE": 0,
        "VACUUM": 0
    }
    
    # Iterate through each query in the JSON data
    for query in data["Queries"]:
        query_value = query["Value"].strip().upper()
        
        # Check the type of each query and update the counts
        for query_type in query_counts.keys():
            if query_value.startswith(query_type):
                query_counts[query_type] += 1
                break
    
    return query_counts

if __name__ == "__main__":
    # Define file paths
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'app_queries.json')
    print(f"Looking for file at: {file_path}")
    
    # Get query counts and formatted queries
    counts = count_query_types(file_path)
    
    # Print query type counts
    for query_type, count in counts.items():
        print(f"{query_type}: {count}")
