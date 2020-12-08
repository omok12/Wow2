import psycopg2
import gzip
import json

conn = psycopg2.connect(database='shattered_hand', user='olenovo',password='wasd', host='localhost', port='5432')
print('success')

with gzip.open('/home/olenovo/projects/Wow2/out_157/202011232000.gz') as f:
    file_content = gzip.decompress(f.read())
print(json.loads(file_content))
