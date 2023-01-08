 
import os
from Hoi4Converter import parser, converter

# Absolute paths
STELLARIS_PATH = "/home/maldun/.local/share/Steam/steamapps/common/Stellaris/"
STELLARIS_MOD_PATH = "/home/maldun/.local/share/Paradox Interactive/Stellaris/mod/"
MAIN_MOD = os.path.join(STELLARIS_MOD_PATH, "much_more_galaxies")
# Relattive paths
GALAXY_PATH = "map/galaxy"
SCENARIO_PATH = "map/setup_scenarios"
SHAPE_FILE = "galaxy_shapes.txt"

ORIG_GALAXY_SHAPES = os.path.join(STELLARIS_PATH, GALAXY_PATH, SHAPE_FILE)
NEW_GALAXY_SHAPES = "new_galaxy_shapes.txt"


def merge_galaxy_shapes(shape_files, out_file):
    shapes = []
    for file in shape_files:
        obj = converter.paradox2list(file)
        shapes += obj

    with open(out_file, 'w') as file:
        code = converter.list2paradox(shapes)
        file.write(code)

if __name__ == "__main__":
    #create_dirs
    os.makedirs(os.path.join('..',GALAXY_PATH), exist_ok=True)
    os.makedirs(os.path.join('..',SCENARIO_PATH), exist_ok=True)
    # update
    to_merge = [ORIG_GALAXY_SHAPES, NEW_GALAXY_SHAPES]
    merge_galaxy_shapes(to_merge, os.path.join(MAIN_MOD, GALAXY_PATH, SHAPE_FILE))
    
