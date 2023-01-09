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
NEW_GALAXY_SHAPES = "my_new_galaxy_shapes.txt"

# Constants
NAME = 'name'
PRIORITY = 'priority'
PDX_SUFF = '.txt'
BASE = '_base'
NUM_STARS = "num_stars"
SUPPORTS_SHAPE = "supports_shape"

# Scenario Settings
ssettings = {}
ssettings['mini'] = {NUM_STARS: 100,
                 "radius": 100,
                 "num_empires": {"min":0, "max":4},
                 "num_empire_default": 2,
                 "marauder_empire_default": 0,
                 "cluster_radius": 45,
                 "cluster_distance_from_core": 60,
                 }
