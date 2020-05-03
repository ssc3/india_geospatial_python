# required imports

import xlrd
import random
import pandas as pd
import seaborn as sns
import geopandas as gpd
import matplotlib.pyplot as plt
import shapefile as shp


# reading the state wise shapefile of India in a GeoDataFrame and preview it

fp = "gadm36_IND_shp/gadm36_IND_2.shp"
map_df = gpd.read_file(fp)
map_df.head()


# Plot the default map

map_df.plot()

sf = shp.Reader("gadm36_IND_shp/gadm36_IND_2.shp")

print(len(sf.shapes()))

record_1 = sf.records()[1]
print(record_1)

