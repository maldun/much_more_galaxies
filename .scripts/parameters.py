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

# Fan (4)
shapes['fan4'] = {SHAPE_NAME: 'Fan (4)',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 70**2,
                                IDE_SQ_DIST: 120**2},
                         FALLEN: {MIN_SQ_DIST:125**2,
                                   IDE_SQ_DIST:175**2},
                         ARMS: {TIGHT_WIND: 0.1,
                                WIDTH: 20.0,
                                FUZZ: 10.0,
                                SEP: 90},
                         NUM_ARMS: 4,
                         CORE_RAD: 0.1,
                         CORE_STARS: 0.1,
                         STARS_MIN_DIST:15.0
                         }
                         

# Star (4)
shapes['star4'] = {SHAPE_NAME: 'Star (4)',
                         MIN_STARS: 1,
                         COUNTRY: {MIN_SQ_DIST: 70**2,
                                IDE_SQ_DIST: 120**2},
                         FALLEN: {MIN_SQ_DIST:125**2,
                                   IDE_SQ_DIST:175**2},
                         ARMS: {TIGHT_WIND: 0.01,
                                WIDTH: 10.0,
                                FUZZ: 10.0,
                                SEP: 90},
                         NUM_ARMS: 4,
                         CORE_RAD: 0.3,
                         CORE_STARS: 0.3,
                         STARS_MIN_DIST:15.0
                         }
                         
