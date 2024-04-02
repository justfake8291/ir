#Open cmd Type the following commannd
#   pip install networkx
#   pip install scipy



import networkx as nx
from lxml import etree as et

xml = """
<root>
<node id="1">cats</node>
<node id="2">dogs</node>
<node id="3">cats and dogs</node>
<link from="1" to="3" />
<link from="2" to="3" />
<link from="3" to="1" />
</root>
"""

g = nx.DiGraph()
for l in et.fromstring(xml).findall(".//link"):
    g.add_edge(l.attrib["from"], l.attrib["to"])

pr = list(nx.pagerank(g, weight="weight", alpha=0.85).items())

for i in range(len(pr)):
    node, score = pr[i]
    if "cats" in node:  
        pr[i] = (node, score + 0.15)

for node, score in pr:
    print(f"Node {node}: PageRank = {score}")