from course import Course
import json
from distribution import Distribution
from term import Term

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Course):
            return obj.to_dict()
        if isinstance(obj, Distribution):
            return obj.to_dict()
        if isinstance(obj, Term):
            return obj.to_dict()
        
        return json.JSONEncoder.default(self, obj)