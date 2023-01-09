 
import os
from Hoi4Converter import parser, converter
from pdx_objects import Country, FallenEmpire, Ring, Arms, GalaxyShape
from pdx_objects import replace_entry, ScenarioManager, get_original_shapes, get_entry
from defines import *

def merge_galaxy_shapes(shape_files, out_file):
    shapes = []
    for file in shape_files:
        obj = converter.paradox2list(file)
        shapes += obj

    with open(out_file, 'w') as file:
        code = converter.list2paradox(shapes)
        file.write(code)


# setup data
sm = ScenarioManager(ORG_SCENARIO_PATH, MOD_SCENARIO_PATH)
shape_minima = get_original_shapes(ORG_GALAXY_SHAPES,sm.scenarios, ORG_SCENARIO_PATH)
        
# Define new scenarios


# Define new shapes
new_shapes = []
## Dragon Tail
dt_name = "dragon_tail"

dt_country = Country(ideal_sq_dist_between=120**2,
                     min_sq_dist_between=70**2)

dt_fallen = FallenEmpire(ideal_sq_dist_between=120**2,
                     min_sq_dist_between=70**2)

dt_arms = Arms(tightness_winding=1.0,
               width=80.0,
               fuzz=120.0,
               seperation=45.4)

dragon_tail = GalaxyShape(dt_name,
                          core_radius_per = 0.25,
                          num_stars_core_perc = 0.25,	
                          stars_min_dist = 15.0,
                          num_arms = 1,
                          arms = dt_arms,
                          countries = dt_country,
                          fallen_empires=dt_fallen)

new_shapes += [[dragon_tail.write_pdx()]]

shape_minima[dt_name] = 200

# register all shapes
sm.register_shapes(shape_minima)

if __name__ == "__main__":
    #create_dirs
    os.makedirs(os.path.join(MAIN_MOD, GALAXY_PATH), exist_ok=True)
    os.makedirs(os.path.join(MAIN_MOD, SCENARIO_PATH), exist_ok=True)
    # write out new shapes
    with open(NEW_GALAXY_SHAPES, 'w') as fp:
        code = converter.list2paradox(new_shapes)
        fp.write(code)
    # update shapes
    to_merge = [ORG_GALAXY_SHAPES, NEW_GALAXY_SHAPES]
    merge_galaxy_shapes(to_merge, os.path.join(MAIN_MOD, GALAXY_PATH, SHAPE_FILE))
    
    sm.write_scenarios()
