import pandas as pd
import os
import bs4
from bs4 import BeautifulSoup


#els= xml_doc.find_all()

#el_names =set([el.name for el in els])

def parse_alto(filepath):
    """
    Convert each file to a dictionary with the
    following keys: fulltext (list of lines), wordcount, filename.
    """
    parsed_data = {}

    # add here your solution
    # you'll need to parse the xml elements
    # containing the information you are interested in

    # HINT: you may want to split the parsing of individual
    # XML elements into dedicated functions that get called from
    # `parse_alto()`

    """
       Convert each file to a dictionary with the
       following keys: fulltext, wordcount, filename.
       """

    with open(filepath, 'r') as inpfile:
        xml_doc = BeautifulSoup(inpfile)

    word_count = 0
    lines = []

    for line_el in xml_doc.findAll('textline'):

        line = ""

        for child in line_el.children:
            if isinstance(child, bs4.element.Tag):
                if child.name == 'string':
                    line += child.get('content')
                    word_count += 1
                elif child.name == 'sp':
                    line += " "
        lines.append(line)

    return {
        'wordcount': word_count,
        'fulltext': "\n".join(lines),
        'filename': os.path.basename(filepath)
    }



# once your function is in place, you should be
# able to execute this cell, which applies your function
# to all Alto files.

# let's get the path of XML files
# we filter only files with XML extension
# it can be useful to ignore e.g. `.DS_Store` files (under MacOS)

data_folder = '/Users/elisabeth.guerard/Projects/VMH/ADA-DHOxSS2019-master/data/altoxml'

#data_folder = '../data/altoxml/'

xml_files = [
    os.path.join(data_folder, file)
    for file in os.listdir(data_folder)
    if ".xml" in file
]


# data = [
#      parse_alto(xml_file)
#      for xml_file in xml_files
#  ]

data =[]
for xml_file in xml_files:
     data.append(parse_alto(xml_file))

df = pd.DataFrame(data)
df.head()

