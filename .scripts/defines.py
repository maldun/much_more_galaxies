import os
# Absolute paths
STELLARIS_PATH = "/home/maldun/.local/share/Steam/steamapps/common/Stellaris/"
STELLARIS_MOD_PATH = "/home/maldun/.local/share/Paradox Interactive/Stellaris/mod/"
MAIN_MOD = os.path.join(STELLARIS_MOD_PATH, "much_more_shapes")
# Relattive paths
GALAXY_PATH = "map/galaxy"
SCENARIO_PATH = "map/setup_scenarios"
SHAPE_FILE = "galaxy_shapes.txt"

MOD_SCENARIO_PATH = os.path.join(MAIN_MOD, SCENARIO_PATH)
ORG_SCENARIO_PATH = os.path.join(STELLARIS_PATH, SCENARIO_PATH)

ORG_GALAXY_SHAPES = os.path.join(STELLARIS_PATH, GALAXY_PATH, SHAPE_FILE)
NEW_GALAXY_SHAPES = "my_new_galaxy_shapes.txt"

LOC_PATH = "localisation"
MOD_LOC_PATH = os.path.join(MAIN_MOD, LOC_PATH)

# Constants
UTF8 = 'utf-8-sig'

NAME = 'name'
PRIORITY = 'priority'
PDX_SUFF = '.txt'
BASE = '_base'
NUM_STARS = "num_stars"
SUPPORTS_SHAPE = "supports_shape"
COUNTRY = 'countries'
FALLEN = 'fallen_empires'
ARMS = 'arms'
RING = 'ring'

SHAPE_NAME = '_shape_name'
MIN_STARS = '_min_size'

NUM_ARMS = 'num_arms'

IDE_SQ_DIST = 'ideal_sq_dist_between'
MIN_SQ_DIST = 'min_sq_dist_between'

TIGHT_WIND = 'tightness_winding'
WIDTH = "width"
FUZZ = 'fuzz'
SEP = 'seperation'

CORE_RAD = 'core_radius_perc'
CORE_STARS = 'num_stars_core_perc'
STARS_MIN_DIST = 'stars_min_dist'
