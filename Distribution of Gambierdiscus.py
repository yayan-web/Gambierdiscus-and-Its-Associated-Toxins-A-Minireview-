# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 09:43:04 2021

@author: Shin
"""


from pyecharts.globals import GeoType
from pyecharts.charts import Geo
from pyecharts import options
g = Geo(init_opts = {"bg_color":"white"})
g = g.add_schema(maptype="world", zoom = 0.8)
data = open("c265385e-d534-489b-b5c6-7ce4297d1600/1.csv", "r")
for line in data.readlines():
    id, a, b = line.partition(",")
    species, c, d = b.partition(",")
    if species == "Gambierdiscus":
        species = "Gambierdiscus spp."
    longitude, e, f = d.partition(",")
    latitude, h, i = f.partition(", ")
    g.add_coordinate(species, longitude, latitude)
    data_pair = [(species,1)]
    g.add(species, data_pair, symbol_size=7)
g.set_series_opts(label_opts=options.LabelOpts(is_show=False))
g.set_global_opts(title_opts=options.TitleOpts(title=""),
                  legend_opts=options.LegendOpts(
                      textstyle_opts=options.TextStyleOpts(font_style ="italic",
                                                           font_family = "Times New Roman",
                                                           font_size = 15)))
g.render("Distribution of Gambierdiscus.html")
