# imports

import pandas as pd
import json, os, codecs
from collections import defaultdict, OrderedDict
import seaborn as sns

root_folder = "/Users/elisabeth.guerard/Projects/VMH/ADA-DHOxSS2019-master/data/bl_books/sample/"

# metadata
filename = "book_data_sample.json"
metadata = json.load(codecs.open(os.path.join(root_folder,filename), encoding="utf8"))

# fulltexts
foldername = "full_texts"
texts = defaultdict(list)
for root, dirs, files in os.walk(os.path.join(root_folder,foldername)):
    for f in files:
        if ".json" in f:
            t = json.load(codecs.open(os.path.join(root,f), encoding="utf8"))
            texts[f] = t

# enriched metadata
filename = "extra_metadata_sample.csv"
df_extra = pd.read_csv(os.path.join(root_folder,filename), delimiter=";")
df_extra = df_extra.rename(str.lower, axis='columns') # rename columns to lower case

# there are 452 books in the sample

print(len(metadata))
print(metadata[0])

# let's check we have the same amount of books with a text file

#print(len(texts))

# each text comes as a list of lists: one per page, as follows [page number, text]

#texts['000000196_01_text.json'][:9]
# the extra metadata can be already used as a data frame

#df_extra[df_extra["first_pdf"] == "lsidyv35c55757"]