import os
from Hoi4Converter import parser, converter, mappings
from Hoi4Converter.mappings import apply_map, has_key, has_key_and_val, has_value
from Hoi4Converter.mappings import replace, add_multiple, remove, get_object_from_inds
from Hoi4Converter.parser import parse_grammar as code2pdx

from defines import *

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

default_country = Country()
default_fallen_empire = FallenEmpire(125**2, 75**2)

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

def replace_entry(obj, key, new_val, sup_key = None):
    mapping = [[has_key, key], [replace, [key,[new_val]]]]
    if sup_key is None:
        obj = apply_map(obj, mapping)
    else:
        sub_obj, inds = has_key.search(obj, sup_key)
        sub_obj2 = apply_map(sub_obj, mapping)
        obj = replace.manipulate(obj, inds[0], [sub_obj2])

    return obj

    
class ScenarioManager:
    def __init__(self, org_scenario_path):
        """
        Create original list
        """
        self.scenarios = {}
        for name in os.listdir(org_scenario_path):
            fname = os.path.join(org_scenario_path, name)
            sname = name.split('.')[0]
            prio = self.get_priority(fname)
            self.scenarios[sname] = {NAME: sname, PRIORITY: prio}

    
    def rescale_scenario(self, orig, replacement_dict):
        obj = converter.paradox2list(orig)
        for key, val in replacement_dict.items():
            if not isinstance(val, dict):
                obj = replace_entry(obj, key, val)
            else: # We assume only 2 levels of depth
                for key2, val2 in val.items():
                    obj = replace_entry(obj, key2, val2, sup_key=key)

        return obj

    @staticmethod
    def get_priority(obj):
        if not isinstance(obj, list):
            obj = converter.paradox2list(obj)
        info, inds = has_key.search(obj, PRIORITY)
        return info[0][1][0]

    @staticmethod
    def set_priority(obj, priority):
        fname = None
        if not isinstance(obj, list):
            fname = obj
            obj = converter.paradox2list(obj)
        obj = replace_entry(obj, PRIORITY, priority)
        if fname is not None:
            code = converter.list2paradox(obj)
            with open(fname, 'w') as fp:
                fp.write(code)
                return
        else:
            return obj


        
    
# some tests
if __name__ == "__main__":
    
    default_galaxy = GalaxyShape('tester')

    assert default_galaxy.core_radius_per == 0.25
    assert default_galaxy.countries.min_sq_dist_between == 50**2
    obj = default_galaxy.write_pdx()
    code = converter.list2paradox(obj)
    assert "countries = {" in code
    assert "fallen_empires = {" in code
    assert "ideal_sq_dist_between = 5625" in code
    assert "_min_size" not in code

    obj2 = replace_entry(obj.copy(), 'ideal_sq_dist_between','200')
    code2 = converter.list2paradox(obj2)
    assert "ideal_sq_dist_between = 200" in code2
    obj2 = replace_entry(obj.copy(), 'ideal_sq_dist_between','200',sup_key = "countries")
    code2 = converter.list2paradox(obj2)
    assert "ideal_sq_dist_between = 200" in code2
    assert "ideal_sq_dist_between = 15625" in code2

    prio = ScenarioManager.get_priority('medium.txt')
    assert prio == 2
    obj3 = converter.paradox2list('medium.txt')
    new_obj3 = ScenarioManager.set_priority(obj3, 3)
    assert ScenarioManager.get_priority(new_obj3) == 3
    
    
