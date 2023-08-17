import json


class SetEncoder(json.JSONEncoder):
    """For modify set to json"""
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)
