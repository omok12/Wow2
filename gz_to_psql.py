import psycopg2
from psycopg2.extensions import AsIs
import gzip
import json


conn = psycopg2.connect(database='shattered_hand', user='olenovo',password='wasd', host='localhost', port='5432')
cur = conn.cursor()
cur.execute(''' CREATE TABLE IF NOT EXISTS test_temp (
                id BIGINT PRIMARY KEY NOT NULL,
                item JSONB NOT NULL,
                bid BIGINT NOT NULL,
                buyout BIGINT NOT NULL,
                quantity INT NOT NULL,
                unit_price BIGINT NOT NULL,
                time_left TEXT NOT NULL
                );''')
conn.commit()

with gzip.open('/home/olenovo/projects/Wow2/out_157/202011232000.gz') as f:
    file_content = gzip.decompress(f.read())
record_list = json.loads(file_content)['auctions']

table_name = 'test_temp'
columns = ['id', 'item', 'bid', 'buyout', 'quantity', 'unit_price', 'time_left']
for i in range(0, len(record_list)):
    vals = []
    for column in columns:
        try:
            vals.append(record_list[i][column])
        except KeyError:
            vals.append(0)
    sql_string = 'insert into test_temp (%s)  values (%s, %s, %s, %s, %s, %s, %s) on conflict (id) do nothing'
    #print(cur.mogrify(sql_string, (AsIs(', '.join(columns)), vals[0], json.dumps(vals[1]), vals[2], vals[3], vals[4], vals[5], vals[6])))
    cur.execute(sql_string, (AsIs(', '.join(columns)), vals[0], json.dumps(vals[1]), vals[2], vals[3], vals[4], vals[5], vals[6]))
print('success')
cur.close()
conn.commit()
conn.close()
