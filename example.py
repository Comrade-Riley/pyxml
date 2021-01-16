import pyxml

data = pyxml.load('/home/unbuntu/Documents/xml/data.xml')

print(data)

data['servers']['server1']['users']['bob'] = 'it works'

pyxml.dump(data,'/home/unbuntu/Documents/xml/data.xml',1)
