 
import os
from Hoi4Converter import parser, converter
from pdx_objects import Country, FallenEmpire, Ring, Arms, GalaxyShape
from pdx_objects import replace_entry, ScenarioManager
from defines import *

def merge_galaxy_shapes(shape_files, out_file):
    shapes = []
    for file in shape_files:
        obj = converter.paradox2list(file)
        shapes += obj

    with open(out_file, 'w') as file:
        code = converter.list2paradox(shapes)
        file.write(code)

# def create_new_scenario(base, new_name, params):
#     # do nothing when base
#     if NAME in params.keys() and params[NAME] == new_name:
#         return 

#     params[NAME] = new_name
#     obj = rescale_scenario(base, params)
#     with open(os.path.join(MAIN_MOD, SCENARIO_PATH, new_name + PDX_SUFF), 'w') as fp:
#         code = converter.list2paradox(obj)
#         fp.write(code)

# # Define new scenarios
# ## but first take old ones
# scenarios = {}

# scenarios['micro'] = {}

        
# Define new shapes

## Dragon Tail 
dt_country = Country(ideal_sq_dist_between=120**2,
                     min_sq_dist_between=70**2)

dt_fallen = FallenEmpire(ideal_sq_dist_between=120**2,
                     min_sq_dist_between=70**2)

dragon_tail = GalaxyShape("dragon_tail",)
        
                         

if __name__ == "__main__":
    #create_dirs
    os.makedirs(os.path.join(MAIN_MOD, GALAXY_PATH), exist_ok=True)
    os.makedirs(os.path.join(MAIN_MOD, SCENARIO_PATH), exist_ok=True)
    # update
    #to_merge = [ORG_GALAXY_SHAPES, NEW_GALAXY_SHAPES]
    #merge_galaxy_shapes(to_merge, os.path.join(MAIN_MOD, GALAXY_PATH, SHAPE_FILE))
    
