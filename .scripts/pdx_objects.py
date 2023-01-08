import os
from Hoi4Converter import parser, converter

class PDXObject:
    FORBIDDEN_VARS = {'self','__return__','pdb', "__class__" ,'identifier'}
    def __init__(self, identifier, kwargs):
        self.identifier = identifier
        filtered_kwargs = self._filter_kwargs(kwargs)
        self.keys = filtered_kwargs.keys()
        self.__dict__.update(filtered_kwargs)

    def write_pdx(self):
        output_val = []
        for key in self.keys:
            if key.startswith("_"):
                continue
            val = getattr(self, key)
            if isinstance(val, PDXObject):
                identifier = val.identifier
                val = val.write_pdx()[0][1]
                obj = [identifier, val]
            else:
                identifier = key
                obj = [identifier, [val]]
            if val is not None:
                output_val += [obj]

        output = [[self.identifier, output_val]]
        return output

    def _filter_kwargs(self,kwargs):
        return {key: val for key, val in kwargs.items() if key not in self.FORBIDDEN_VARS}
            
class Country(PDXObject):
    identifier = "countries"
    def __init__(self,
                 ideal_sq_dist_between = 75*75,
                 min_sq_dist_between = 50*50):
        return super().__init__(self.identifier, locals())

class FallenEmpire(Country):
    identifier = "fallen_empires"

default_country = Country()
default_fallen_empire = FallenEmpire(125**2, 75**2)

class Ring(PDXObject):
    identifier = 'ring'
    def __init__(self, width= 0.5, offset = 0.4):
        return super().__init__(self.identifier, locals())


class Arms(PDXObject):
    identifier = 'arms'
    def __init__(self,
                 tightness_winding = 0.85,
                 width= 0.5,
                 fuzz = 15.0,
                 seperation = 120.0):
        return super().__init__(self.identifier, locals())

    

class GalaxyShape(PDXObject):
    def __init__(self, identifier,
                 core_radius_per = 0.25,
                 num_stars_core_perc = 0,
                 stars_min_dist = 10,
                 countries = default_country,
                 fallen_empires = default_fallen_empire,
                 ring = None,
                 num_arms = None,
                 arms = None,
                 _min_size = 200
                 ):
        if (arms is None and num_arms is not None) or (arms is not None and num_arms is None):
            raise ValueError("Error: num_arms and arms do not align! One is None!")
        return super().__init__(identifier, locals())
                

default_galaxy = GalaxyShape('tester')

# some tests
assert default_galaxy.core_radius_per == 0.25
assert default_galaxy.countries.min_sq_dist_between == 50**2
obj = default_galaxy.write_pdx()
code = converter.list2paradox(obj)
assert "countries = {" in code
assert "fallen_empires = {" in code
assert "ideal_sq_dist_between = 5625" in code
assert "_min_size" not in code
