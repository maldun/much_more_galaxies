import os
# Absolute paths
STELLARIS_PATH = "/home/maldun/.local/share/Steam/steamapps/common/Stellaris/"
STELLARIS_MOD_PATH = "/home/maldun/.local/share/Paradox Interactive/Stellaris/mod/"
MAIN_MOD = os.path.join(STELLARIS_MOD_PATH, "much_more_galaxies")
# Relattive paths
GALAXY_PATH = "map/galaxy"
SCENARIO_PATH = "map/setup_scenarios"
SHAPE_FILE = "galaxy_shapes.txt"

MOD_SCENARIO_PATH = os.path.join(MAIN_MOD, SCENARIO_PATH)
ORG_SCENARIO_PATH = os.path.join(STELLARIS_PATH, SCENARIO_PATH)

ORG_GALAXY_SHAPES = os.path.join(STELLARIS_PATH, GALAXY_PATH, SHAPE_FILE)
NEW_GALAXY_SHAPES = "new_galaxy_shapes.txt"

# Constants
NAME = 'name'
PRIORITY = 'priority'
PDX_SUFF = '.txt'
