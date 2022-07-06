import json
import pygal
from country_codes import get_country_code
filename = 'population_json.json'
with open(filename) as f:
    pop_data = json.load(f)
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict["Year"] == 1960:
        country_name = pop_dict["Country Name"]
        population = pop_dict["Value"]
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
wm = pygal.maps.world.World()
wm.title = 'World population in 1960, by country'
wm.add('1960', cc_populations)
wm.render_to_file('wolrd_population.svg')