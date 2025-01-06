import sys
import json

file_path = sys.argv[1]
sql_export_file_path = sys.argv[2]

file_content = ""

with open(file_path, 'r') as sqlinspect_file:
    file_content = json.load(sqlinspect_file)

queries = []
prefixes = ("CREATE TABLE", "DROP TABLE", "CREATE INDEX", "ALTER TABLE")
for query_dict in file_content["Queries"]:
    query_value = query_dict["Value"]
    if any(query_value.startswith(prefix) for prefix in prefixes):
    	queries.append(query_value)


with open(sql_export_file_path, "w") as query_file:
    for query in queries:
        query_file.write(f"{query};\n")