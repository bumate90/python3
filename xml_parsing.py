#!/usr/bin/python3.7.9

#############################################################################
#                                 XML Parsing                               #
#############################################################################


from lxml import etree
from random import randrange

# FROM FILE
#----------------------------------------------------------------------------
root = etree.parse("menu.xml")

# find a node named
menu = root.find("breakfast_menu")

# xpath lookup
food_name_list = menu.findall("food/name")
for item in food_name_list:
    print(item.text)
    value = str(randrange(0, 10))
    item.addnext(etree.XML(f"<amount type=\"int\">{value}</amount>"))

# Inserting a new node after breakfast_menu
subtag = etree.Element("open", type="bool")
subtag.text = "false"
menu.addnext(subtag)

# Print the whole XML
print("----------------------")
print(etree.tostring(root, pretty_print=True))

# Writing the whole XML to file
root.write("menu_updated.xml", pretty_print=True)

# TODO: perhaps use "xmllint --format menu_updated.xml" to reformat the output file


# FROM STRING
#----------------------------------------------------------------------------
XML= """
<tag attrib1='I'>
  <subtag1 subattrib1='1'>
    <subtext>text1</subtext>
  </subtag1>
  <subtag3 subattrib3='3'>
    <subtext>text3</subtext>
  </subtag3>
</tag>"""

print("----------------------")
parser = etree.XMLParser(remove_blank_text=True)
tag = etree.fromstring(XML, parser)
print(etree.tostring(tag, pretty_print=True))