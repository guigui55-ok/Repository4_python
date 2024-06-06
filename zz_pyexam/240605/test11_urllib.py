from urllib import parse

query = 'key1=value1&key1=value2&key2=value3'
print(parse.parse_qsl(query))