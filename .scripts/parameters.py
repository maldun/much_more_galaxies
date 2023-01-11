from defines import *
# Scenario Settings
scenarios = {}
scenarios['mini'] = dict(
                 num_stars = 100,
                 radius = 150,
                 num_empires =  {"min" :0, "max":3},
                 num_empire_default = 1,
                 fallen_empire_default =  0,
                 fallen_empire_max = 1,
                 marauder_empire_default = 0,
                 marauder_empire_max = 1,
                 advanced_empire_default = 1,
                 cluster_radius = 60,
                 cluster_distance_from_core = 75,
                 _base = 'tiny'
                 )

scenarios['micro'] = dict(
                 num_stars = 50,
                 radius = 100,
                 num_empires =  {"min" :0, "max":2},
                 num_empire_default = 1,
                 fallen_empire_default =  0,
                 fallen_empire_max = 1,
                 marauder_empire_default = 0,
                 marauder_empire_max = 1,
                 advanced_empire_default = 1,
                 cluster_radius = 30,
                 cluster_distance_from_core = 45,
                 _base = 'tiny'
                 )

scenarios['pico'] = dict(
                 num_stars = 25,
                 radius = 75,
                 num_empires =  {"min" :0, "max":2},
                 num_empire_default = 1,
                 fallen_empire_default =  0,
                 fallen_empire_max = 1,
                 marauder_empire_default = 0,
                 marauder_empire_max = 1,
                 advanced_empire_default = 1,
                 cluster_radius = 20,
                 cluster_distance_from_core = 30,
                 _base = 'tiny'
                 )

scenarios['massive'] = dict(
                       num_stars = 1250,
                       radius = 460,
                       num_empires = dict(min = 0, max = 36),
                       num_empire_default = 18,
                       fallen_empire_default =  6,
                       fallen_empire_max = 7,
                       marauder_empire_default = 4,
                       marauder_empire_max = 5,
                       advanced_empire_default = 5,
                       cluster_radius = 150,
                       cluster_distance_from_core = 300,
                       num_nebulas = 12,
                       nebula_size = 60,
                       nebula_min_dist = 200,
                       _base = 'huge',
                       )

scenarios['enormous'] = dict(
                       num_stars = 1750,
                       radius = 470,
                       num_empires = dict(min = 0, max = 45),
                       num_empire_default = 20,
                       fallen_empire_default =  6,
                       fallen_empire_max = 8,
                       marauder_empire_default = 5,
                       marauder_empire_max = 6,
                       advanced_empire_default = 6,
                       cluster_radius = 150,
                       cluster_distance_from_core = 300,
                       num_nebulas = 13,
                       nebula_size = 60,
                       nebula_min_dist = 200,
                       _base = 'huge',
                       )

scenarios['gigantic'] = dict(
                       num_stars = 2000,
                       radius = 475,
                       num_empires = dict(min = 0, max = 60),
                       num_empire_default = 30,
                       fallen_empire_default =  6,
                       fallen_empire_max = 10,
                       marauder_empire_default = 5,
                       marauder_empire_max = 8,
                       advanced_empire_default = 6,
                       cluster_radius = 150,
                       cluster_distance_from_core = 300,
                       num_nebulas = 15,
                       nebula_size = 60,
                       nebula_min_dist = 200,
                       _base = 'huge',
                       )

scenarios['collosal'] = dict(
                       num_stars = 2500,
                       radius = 477,
                       num_empires = dict(min = 0, max = 75),
                       num_empire_default = 30,
                       fallen_empire_default =  6,
                       fallen_empire_max = 12,
                       marauder_empire_default = 5,
                       marauder_empire_max = 10,
                       advanced_empire_default = 6,
                       cluster_radius = 150,
                       cluster_distance_from_core = 300,
                       num_nebulas = 15,
                       nebula_size = 60,
                       nebula_min_dist = 200,
                       _base = 'huge',
                       )

# Shape minima redefinitions:
old_shape_minima = {
    'elliptical': 1,
    'spiral_2': 1,
    'spiral_4': 1,
    'ring': 1,
    'bar': 1,
     }

# Shape definitions
shapes = {}


# Barred Spiral with Ring
shapes['barred_sba'] = {SHAPE_NAME: 'Barred Spiral (SBa)',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 50**2,
                                IDE_SQ_DIST: 75**2},
                         FALLEN: {MIN_SQ_DIST:75**2,
                                   IDE_SQ_DIST:125**2},
                         ARMS: {TIGHT_WIND: 0.6,
                                WIDTH: 60.0,
                                FUZZ: 20.0,
                                SEP: 180},
                         NUM_ARMS: 2,
                         CORE_RAD: 0.15,
                         CORE_STARS: 0.0,
                         STARS_MIN_DIST: 2.0,
                         }

# Barred Spiral with thin arms
shapes['barred_sbc'] = {SHAPE_NAME: 'Barred Spiral (SBc)',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 50**2,
                                IDE_SQ_DIST: 75**2},
                         FALLEN: {MIN_SQ_DIST:75**2,
                                   IDE_SQ_DIST:125**2},
                         ARMS: {TIGHT_WIND: 0.6,
                                WIDTH: 45.0,
                                FUZZ: 5.0,
                                SEP: 180},
                         NUM_ARMS: 2,
                         CORE_RAD: 0.2,
                         CORE_STARS: 0.1,
                         STARS_MIN_DIST:5.0
                         }

# Cluser shapes
shapes['cluster2'] = {SHAPE_NAME: 'Cluster (2)',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 50**2,
                                IDE_SQ_DIST: 75**2},
                         FALLEN: {MIN_SQ_DIST:75**2,
                                   IDE_SQ_DIST:125**2},
                         ARMS: {TIGHT_WIND: 0.0,
                                WIDTH: 90.0,
                                FUZZ: 10.0,
                                SEP: 180},
                         NUM_ARMS: 2,
                         CORE_RAD: 0.2,
                         CORE_STARS: 0.02,
                         STARS_MIN_DIST: 2.0,
                         RING: dict(
                                width = 0.50,
                                offset = 0.2
                         )
                         }

shapes['cluster3'] = {SHAPE_NAME: 'Cluster (3)',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 50**2,
                                IDE_SQ_DIST: 75**2},
                         FALLEN: {MIN_SQ_DIST:75**2,
                                   IDE_SQ_DIST:125**2},
                         ARMS: {TIGHT_WIND: 0.0,
                                WIDTH: 60.0,
                                FUZZ: 10.0,
                                SEP: 120},
                         NUM_ARMS: 3,
                         CORE_RAD: 0.2,
                         CORE_STARS: 0.02,
                         STARS_MIN_DIST: 2.0,
                         RING: dict(
                                width = 0.50,
                                offset = 0.2
                         )
                         }

shapes['cluster4'] = {SHAPE_NAME: 'Cluster (4)',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 50**2,
                                IDE_SQ_DIST: 75**2},
                         FALLEN: {MIN_SQ_DIST:75**2,
                                   IDE_SQ_DIST:125**2},
                         ARMS: {TIGHT_WIND: 0.0,
                                WIDTH: 45.0,
                                FUZZ: 10.0,
                                SEP: 90},
                         NUM_ARMS: 4,
                         CORE_RAD: 0.2,
                         CORE_STARS: 0.02,
                         STARS_MIN_DIST: 2.0,
                         RING: dict(
                                width = 0.50,
                                offset = 0.2
                         )
                         }

shapes['cluster6'] = {SHAPE_NAME: 'Cluster (6)',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 50**2,
                                IDE_SQ_DIST: 75**2},
                         FALLEN: {MIN_SQ_DIST:75**2,
                                   IDE_SQ_DIST:125**2},
                         ARMS: {TIGHT_WIND: 0.0,
                                WIDTH: 30.0,
                                FUZZ: 5.0,
                                SEP: 60},
                         NUM_ARMS: 6,
                         CORE_RAD: 0.2,
                         CORE_STARS: 0.02,
                         STARS_MIN_DIST: 2.0,
                         RING: dict(
                                width = 0.50,
                                offset = 0.2
                         )
                         }

shapes['cluster8'] = {SHAPE_NAME: 'Cluster (8)',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 50**2,
                                IDE_SQ_DIST: 75**2},
                         FALLEN: {MIN_SQ_DIST:75**2,
                                   IDE_SQ_DIST:125**2},
                         ARMS: {TIGHT_WIND: 0.0,
                                WIDTH: 22.5,
                                FUZZ: 2.0,
                                SEP: 45},
                         NUM_ARMS: 8,
                         CORE_RAD: 0.2,
                         CORE_STARS: 0.02,
                         STARS_MIN_DIST: 2.0,
                         RING: dict(
                                width = 0.50,
                                offset = 0.2
                         )
                         }

# Cross
shapes['cross'] = {SHAPE_NAME: 'Cross',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 50**2,
                                IDE_SQ_DIST: 75**2},
                         FALLEN: {MIN_SQ_DIST:75**2,
                                   IDE_SQ_DIST:125**2},
                         ARMS: {TIGHT_WIND: 0.0,
                                WIDTH: 20.0,
                                FUZZ: 20.0,
                                SEP: 90},
                         NUM_ARMS: 4,
                         CORE_RAD: 0.2,
                         CORE_STARS: 0.2,
                         STARS_MIN_DIST:1.0
                         }


# Disk
shapes['disk'] = {SHAPE_NAME: 'Disk',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 70**2,
                                IDE_SQ_DIST: 120**2},
                         FALLEN: {MIN_SQ_DIST:125**2,
                                   IDE_SQ_DIST:175**2},
                         ARMS: {TIGHT_WIND: 1.0,
                                WIDTH: 360.0,
                                FUZZ: 20.0,
                                SEP: 0},
                         NUM_ARMS: 1,
                         CORE_RAD: 0.01,
                         CORE_STARS: 0.01,
                         STARS_MIN_DIST: 10.0
                         }

# Dragon Tail
shapes['dragon_tail'] = {SHAPE_NAME: 'Dragon Tail',
                         MIN_STARS: 200,
                         COUNTRY: {MIN_SQ_DIST: 70**2,
                                IDE_SQ_DIST: 120**2},
                         FALLEN: {MIN_SQ_DIST:125**2,
                                   IDE_SQ_DIST:175**2},
                         ARMS: {TIGHT_WIND: 1.0,
                                WIDTH: 80.0,
                                FUZZ: 120.0,
                                SEP: 45.3},
                         NUM_ARMS: 1,
                         CORE_RAD: 0.25,
                         CORE_STARS: 0.25,
                         STARS_MIN_DIST:15.0
                         }

# Fan (3)
shapes['fan3'] = {SHAPE_NAME: 'Fan (3)',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 50**2,
                                IDE_SQ_DIST: 75**2},
                         FALLEN: {MIN_SQ_DIST:75**2,
                                   IDE_SQ_DIST:125**2},
                         ARMS: {TIGHT_WIND: 0.2,
                                WIDTH: 30.0,
                                FUZZ: 10.0,
                                SEP: 120},
                         NUM_ARMS: 3,
                         CORE_RAD: 0.1,
                         CORE_STARS: 0.1,
                         STARS_MIN_DIST:15.0
                         }

# Fan (4)
shapes['fan4'] = {SHAPE_NAME: 'Fan (4)',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 50**2,
                                IDE_SQ_DIST: 75**2},
                         FALLEN: {MIN_SQ_DIST:75**2,
                                   IDE_SQ_DIST:125**2},
                         ARMS: {TIGHT_WIND: 0.2,
                                WIDTH: 30.0,
                                FUZZ: 10.0,
                                SEP: 90},
                         NUM_ARMS: 4,
                         CORE_RAD: 0.1,
                         CORE_STARS: 0.1,
                         STARS_MIN_DIST:15.0
                         }

#firewheel
shapes['firewheel'] = {SHAPE_NAME: 'Fire Wheel',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 50**2,
                                IDE_SQ_DIST: 75**2},
                         FALLEN: {MIN_SQ_DIST:75**2,
                                   IDE_SQ_DIST:125**2},
                         ARMS: {TIGHT_WIND: 0.7,
                                WIDTH: 2.0,
                                FUZZ: 5.0,
                                SEP: 30},
                         NUM_ARMS: 12,
                         CORE_RAD: 0.45,
                         CORE_STARS: 0.05,
                         STARS_MIN_DIST: 2.0
                         }


# Gear shape
shapes['gear'] = {SHAPE_NAME: 'Gear',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 50**2,
                                IDE_SQ_DIST: 75**2},
                         FALLEN: {MIN_SQ_DIST:75**2,
                                   IDE_SQ_DIST:125**2},
                         ARMS: {TIGHT_WIND: 0.0,
                                WIDTH: 30.0,
                                FUZZ: 1.0,
                                SEP: 60},
                         NUM_ARMS: 6,
                         CORE_RAD: 0.5,
                         CORE_STARS: 0.1,
                         STARS_MIN_DIST: 2.0,
                         RING: dict(
                                width = 1.00,
                                offset = -0.60
                         )
                         }

# Half Circle
shapes['half_circle'] = {SHAPE_NAME: 'Half Circle',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 50**2,
                                IDE_SQ_DIST: 75**2},
                         FALLEN: {MIN_SQ_DIST:75**2,
                                   IDE_SQ_DIST:125**2},
                         ARMS: {TIGHT_WIND: 0.0,
                                WIDTH: 130.0,
                                FUZZ: 20.0,
                                SEP: 180},
                         NUM_ARMS: 2,
                         CORE_RAD: 0.1,
                         CORE_STARS: 0.0,
                         STARS_MIN_DIST: 10.0,
                         RING: dict(
                                width = 0.50,
                                offset = 0.3
                             )
                         }

# Holy Cross
shapes['holy_cross'] = {SHAPE_NAME: 'Holy Cross',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 50**2,
                                IDE_SQ_DIST: 75**2},
                         FALLEN: {MIN_SQ_DIST:75**2,
                                   IDE_SQ_DIST:125**2},
                         ARMS: {TIGHT_WIND: 0.0,
                                WIDTH: 20.0,
                                FUZZ: 20.0,
                                SEP: 90},
                         NUM_ARMS: 4,
                         CORE_RAD: 0.1,
                         CORE_STARS: 0.1,
                         STARS_MIN_DIST:1.0,
                         RING: dict(
                                width = 0.80,
                                offset = 0.2
                             )
                         }

# Irregular Galaxies
shapes['irregular_1'] = {SHAPE_NAME: 'Irregular (1)',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 50**2,
                                IDE_SQ_DIST: 75**2},
                         FALLEN: {MIN_SQ_DIST:75**2,
                                   IDE_SQ_DIST:125**2},
                         ARMS: {TIGHT_WIND: 0.6,
                                WIDTH: 6.0,
                                FUZZ: 30.0,
                                SEP: 180},
                         NUM_ARMS: 1,
                         CORE_RAD: 0.7,
                         CORE_STARS: 0.6,
                         STARS_MIN_DIST:10.0,
                         RING: dict(
                                width = 1.50,
                                offset = -1.30
                         )
                         }


shapes['irregular_2'] = {SHAPE_NAME: 'Irregular (2)',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 50**2,
                                IDE_SQ_DIST: 75**2},
                         FALLEN: {MIN_SQ_DIST:75**2,
                                   IDE_SQ_DIST:125**2},
                         ARMS: {TIGHT_WIND: 0.3,
                                WIDTH: 6.0,
                                FUZZ: 30.0,
                                SEP: 60},
                         NUM_ARMS: 2,
                         CORE_RAD: 0.7,
                         CORE_STARS: 0.6,
                         STARS_MIN_DIST:10.0,
                         RING: dict(
                                width = 1.50,
                                offset = -1.20
                         )
                         }

shapes['irregular_3'] = {SHAPE_NAME: 'Irregular (3)',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 50**2,
                                IDE_SQ_DIST: 75**2},
                         FALLEN: {MIN_SQ_DIST:75**2,
                                   IDE_SQ_DIST:125**2},
                         ARMS: {TIGHT_WIND: 0.2,
                                WIDTH: 20.0,
                                FUZZ: 30.0,
                                SEP: 70},
                         NUM_ARMS: 4,
                         CORE_RAD: 0.4,
                         CORE_STARS: 0.3,
                         STARS_MIN_DIST:10.0,
                         RING: dict(
                                width = 1.50,
                                offset = -1.30
                         )
                         }

shapes['pulsar'] = {SHAPE_NAME: 'Pulsar',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 50**2,
                                IDE_SQ_DIST: 75**2},
                         FALLEN: {MIN_SQ_DIST:75**2,
                                   IDE_SQ_DIST:125**2},
                         ARMS: {TIGHT_WIND: 0.8,
                                WIDTH: 30,
                                FUZZ: 10.0,
                                SEP: 30},
                         NUM_ARMS: 4,
                         CORE_RAD: 0.20,
                         CORE_STARS: 0.0,
                         STARS_MIN_DIST: 2.0,
                         # RING: dict(
                         #        width = 1.50,
                         #        offset = -1.30
                         # )
                         }

shapes['radio'] = {SHAPE_NAME: 'Radio',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 50**2,
                                IDE_SQ_DIST: 75**2},
                         FALLEN: {MIN_SQ_DIST:75**2,
                                   IDE_SQ_DIST:125**2},
                         ARMS: {TIGHT_WIND: 0.01,
                                WIDTH: 45.0,
                                FUZZ: 5.0,
                                SEP: 180},
                         NUM_ARMS: 2,
                         CORE_RAD: 0.25,
                         CORE_STARS: 0.2,
                         STARS_MIN_DIST: 5.0,
                         # RING: dict(
                         #        width = 1.50,
                         #        offset = -1.30
                         # )
                         }

# Snowflake (4)
shapes['snowflake4'] = {SHAPE_NAME: 'Snowflake (4)',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 50**2,
                                IDE_SQ_DIST: 75**2},
                         FALLEN: {MIN_SQ_DIST:75**2,
                                   IDE_SQ_DIST:125**2},
                         ARMS: {TIGHT_WIND: 0.0,
                                WIDTH: 1.0,
                                FUZZ: 1.0,
                                SEP: 90},
                         NUM_ARMS: 4,
                         CORE_RAD: 0.3,
                         CORE_STARS: 0.3,
                         STARS_MIN_DIST:1.0
                         }
                         
# Snowflake (6)
shapes['snowflake6'] = {SHAPE_NAME: 'Snowflake (6)',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 50**2,
                                IDE_SQ_DIST: 75**2},
                         FALLEN: {MIN_SQ_DIST:75**2,
                                   IDE_SQ_DIST:125**2},
                         ARMS: {TIGHT_WIND: 0.0,
                                WIDTH: 1.0,
                                FUZZ: 1.0,
                                SEP: 60},
                         NUM_ARMS: 6,
                         CORE_RAD: 0.3,
                         CORE_STARS: 0.3,
                         STARS_MIN_DIST:1.0
                         }


# Square shape
shapes['square'] = {SHAPE_NAME: 'Square',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 50**2,
                                IDE_SQ_DIST: 75**2},
                         FALLEN: {MIN_SQ_DIST:75**2,
                                   IDE_SQ_DIST:125**2},
                         # ARMS: {TIGHT_WIND: 0.0,
                         #        WIDTH: 30.0,
                         #        FUZZ: 1.0,
                         #        SEP: 60},
                         # NUM_ARMS: 6,
                         CORE_RAD: 0.5,
                         CORE_STARS: 0.1,
                         STARS_MIN_DIST: 2.0,
                         RING: dict(
                                width = 1.50,
                                offset = -0.20
                         )
                         }
