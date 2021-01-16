# pyxml
A wrapper that combos pyxml2dict dict2xml and makes them easy and convent  to us.
# Example 

# example.py

import pyxml

data = pyxml.load('/home/unbuntu/Documents/xml/data.xml')

print(data)

data['servers']['server1']['users']['bob'] = 'it works'

pyxml.dump(data,'/home/unbuntu/Documents/xml/data.xml',1)


# data.xml

<servers>
 <__text></__text>
 <__text>None</__text>
 <server1>
  <__text></__text>
  <__text>None</__text>
  <users>
   <__text></__text>
   <__text>None</__text>
   <bob>it works</bob>
   <carry>None</carry>
  </users>
 </server1>
 <server2>
  <__text></__text>
  <__text>None</__text>
  <users>
   <__text></__text>
   <__text>None</__text>
   <barry>None</barry>
   <jerry>None</jerry>
  </users>
 </server2>
</servers>


# Commands
pyxml.load(file) #returns the xml file into a dict

pyml.dump(data,file,indents) #rewrites with a dict. data -> dict var, file -> xml file and indent -> the amount of indents. indent must be a intent from 0 up
