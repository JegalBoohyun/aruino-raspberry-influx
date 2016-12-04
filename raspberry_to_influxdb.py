import urllib

url = 'http://52.78.246.225:8086/write?db=mydb'

queries = []
queries.append('sg_ultrasonic,host=server01 value={0}'.format(100))
queries.append('sg_temperature,host=server01 value={0}'.format(100))
queries.append('sg_light,host=server01 value={0}'.format(100))

queries_str = '\n'.join(queries)
data = str.encode(queries_str)

request = urllib.request.Request(url, data, {'Content-Type': 'application/octet-stream'}, method='POST')
response = urllib.request.urlopen(request)

if response.status == 204:
    print('success')
else:
    print('error')

