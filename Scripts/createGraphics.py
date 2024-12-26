import os
import json
import matplotlib.pyplot as plt
from collections import defaultdict
import re

def count_query_types(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
          
    table_stats = defaultdict(lambda: {'select': 0, 'update': 0, 'delete': 0, 'insert': 0, 'create': 0, 'drop': 0})
    
    # Regular expressions to match different query types and extract table names (without that the algorithm will not work eg. a create queries with a attribute name like updated_seconds will maybe not be recognized as create query)
    patterns = {
        'select': re.compile(r'select .* from (\w+)'),
        'update': re.compile(r'update (\w+)'),
        'delete': re.compile(r'delete from (\w+)'),
        'insert': re.compile(r'insert into (\w+)'),
        'create': re.compile(r'create table (\w+)'),
        'drop': re.compile(r'drop table (if exists )?(\w+)')
    }
    
    for query in data.get("Queries", []):
        query_value = query.get("Value", "").strip().lower()
        
        for query_type, pattern in patterns.items():
            match = pattern.search(query_value)
            if match:
                table_name = match.group(1) if query_type != 'drop' else match.group(2)
                table_stats[table_name][query_type] += 1
                break
    
    return table_stats

if __name__ == "__main__":
    # Define file paths
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'queries_stats.json')
    
    # Get query counts and formatted queries
    table_stats = count_query_types(file_path)
    
    # Prepare data for the stacked bar plot
    tables = list(table_stats.keys())
    select_counts = [int(table_stats[table]['select']) for table in tables]
    update_counts = [int(table_stats[table]['update']) for table in tables]
    delete_counts = [int(table_stats[table]['delete']) for table in tables]
    insert_counts = [int(table_stats[table]['insert']) for table in tables]
    create_counts = [int(table_stats[table]['create']) for table in tables]
    drop_counts = [int(table_stats[table]['drop']) for table in tables]

    # Create the stacked bar plot
    x = range(len(tables))
    plt.figure(figsize=(12, 8))
    
    plt.bar(x, select_counts, width=0.5, label='SELECT', bottom=[i+j+k+l+m+n for i,j,k,l,m,n in zip(update_counts, delete_counts, insert_counts, create_counts, drop_counts, [0]*len(tables))])
    plt.bar(x, update_counts, width=0.5, label='UPDATE', bottom=[i+j+k+l+m for i,j,k,l,m in zip(delete_counts, insert_counts, create_counts, drop_counts, [0]*len(tables))])
    plt.bar(x, delete_counts, width=0.5, label='DELETE', bottom=[i+j+k+l for i,j,k,l in zip(insert_counts, create_counts, drop_counts, [0]*len(tables))])
    plt.bar(x, insert_counts, width=0.5, label='INSERT', bottom=[i+j+k for i,j,k in zip(create_counts, drop_counts, [0]*len(tables))])
    plt.bar(x, create_counts, width=0.5, label='CREATE', bottom=[i+j for i,j in zip(drop_counts, [0]*len(tables))])
    plt.bar(x, drop_counts, width=0.5, label='DROP')

    plt.xlabel('Tables')
    plt.ylabel('Counts')
    plt.title('Query Counts per Table')
    plt.xticks(x, tables, rotation='vertical')
    plt.legend()
    plt.tight_layout()
    plt.show()