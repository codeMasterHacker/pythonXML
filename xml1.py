# We can import this data by reading from a file
import xml.etree.ElementTree as elementTree
tree = elementTree.parse("country_data.xml")
root = tree.getroot()

# As an Element, root has a tag and a dictionary of attributes
print(root.tag)
print(root.attrib)

# It also has children nodes over which we can iterate
# a child is a country "object"
for child in root:
    print(child.tag, child.attrib)
print()

# Children are nested, and we can access specific child nodes by index
# root[0] is the first country "object" in element tree
# root[0][1] is the second attribute of the country "object"
print(root[0][1].text)
print()

# Element has some useful methods that help iterate recursively over all the sub-tree below it (its children, their children, and so on). 
# For example, Element.iter()
# iterate over all the neighbors of each country "object"
for neighbor in root.iter("neighbor"):
    print(neighbor.attrib)
print()

# Element.findall() finds only elements with a tag which are direct children of the current element.
# Element.find() finds the first child with a particular tag.
# Element.text accesses the element’s text content.
# Element.get() accesses the element’s attributes
# iterate over all countries, since they're direct children of root
for country in root.findall("country"):
    rank = country.find("rank").text
    name = country.get("name")
    print(name, rank)
print()

# Let’s say we want to add one to each country’s rank, and add an updated attribute to the rank element.
for rank in root.iter("rank"):
    newRank = int(rank.text) + 1
    rank.text = str(newRank)
    rank.set("updated", "yes")
tree.write("rankPlusOne_country_data.xml")

# We can remove elements using Element.remove(). 
# Let’s say we want to remove all countries with a rank higher than 50
# using root.findall() to avoid removal during traversal
# Note that concurrent modification while iterating can lead to problems, 
# just like when iterating and modifying Python lists or dicts. 
# Therefore, the example first collects all matching elements with root.findall(), 
# and only then iterates over the list of matches.
for country in root.findall("country"):
    rank = int(country.find("rank").text)
    if rank > 50:
        root.remove(country)
tree.write("removeCountriesOverRank50_country_data.xml")