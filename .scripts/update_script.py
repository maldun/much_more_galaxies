 
import os
from Hoi4Converter import parser, converter
from pdx_objects import Country, FallenEmpire, Ring, Arms, GalaxyShape, ShapeManager
from pdx_objects import snake_case_to_normal, write_localisation
from pdx_objects import replace_entry, ScenarioManager, get_original_shapes, get_entry
import parameters as par 
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
shape_minima = get_original_shapes(ORG_GALAXY_SHAPES, sm.get_scenarios(), ORG_SCENARIO_PATH)
gm = ShapeManager(ORG_GALAXY_SHAPES, ORG_SCENARIO_PATH, sm.get_scenarios())

# Update minima
for identifier, val in par.old_shape_minima.items():
    gm.update_min(identifier, val)

# Update new scenarios
for key, settings in par.scenarios.items():
    sm.add_scenario(key, settings)

# Update Shapes
for shape_id, shape_dic in par.shapes.items():
    if SHAPE_NAME in shape_dic.keys():
        shape_name = shape_dic[SHAPE_NAME]
    else:
        shape_name = None
    gm.add_shape(shape_id, shape_dic, name=shape_name)
    

# register all shapes
sm.register_shapes(gm.get_shape_minima())

if __name__ == "__main__":
    #create_dirs
    os.makedirs(os.path.join(MAIN_MOD, GALAXY_PATH), exist_ok=True)
    os.makedirs(os.path.join(MAIN_MOD, SCENARIO_PATH), exist_ok=True)
    # write out new shapes
    gm.write_shapes(NEW_GALAXY_SHAPES)
    # update shapes
    to_merge = [ORG_GALAXY_SHAPES, NEW_GALAXY_SHAPES]
    merge_galaxy_shapes(to_merge, os.path.join(MAIN_MOD, GALAXY_PATH, SHAPE_FILE))
    # write out scenarios
    sm.write_scenarios()
    # write localisation
    os.makedirs(MOD_LOC_PATH, exist_ok=True)
    gm.write_localisation(os.path.join(MOD_LOC_PATH, "mmg_l_english.yml"))
    
    # with open(os.path.join(MOD_LOC_PATH, "mmg_l_english.yml"), 'w', encoding=UTF8) as fp:
    #     code = write_localisation(new_shape_names)
    #     fp.write(code)
