import xml.etree.ElementTree as et
import sys
import re
from xmlutils.xml2csv import xml2csv


input = str(sys.argv[1])

output_for_publication = 'publication.csv'
output_for_researcher = 'researcher.csv'
output_for_relationship = 'relationship.csv'
#output_file = str(sys.argv[2])

converter = xml2csv(input,"/publication/publication.csv")
converter.convert(tag="{http://researchgraph.org/schema/v2.0/xml/nodes}publication")

# tree = et.parse(input_file)


# root = tree.getroot()

# cols = []

# row = []

# dict={}

# for col in root[0][0]:
# 	cols.append(re.sub('\{.*?\}','',col.tag))

# for r in root[0][0]:
# 	print(r.text)

# for r in root[0]:
# 	for pub in r:
# 		print(pub.text)