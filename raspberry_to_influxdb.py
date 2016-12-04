from urllib import request
import random

url = 'http://52.78.246.225:8086/write?db=mydb'

queries = []
queries.append('sg_ultrasonic,host=server01 value={0}'.format(100))
queries.append('sg_temperature,host=server01 value={0}'.format(100))
queries.append('sg_light,host=server01 value={0}'.format(100))
queries.append('sg_random,host=server01 value={0}'.format(random.randrange(10, 20)))

queries_str = '\n'.join(queries)
data = str.encode(queries_str)

req = request.Request(url, data, {'Content-Type': 'application/octet-stream'}, method='POST')
response = request.urlopen(req)

if response.status == 204:
    print('success')
else:
    print('error')

