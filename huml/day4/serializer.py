"""JSONEncoder that doesn't raise exceptions for unencodable objects, just stringifies them"""
import datetime
import json
import uuid

TYPES_TO_REPR = ()


def stringify(obj):
    return str(obj)


class RobustJSONEncoder(json.JSONEncoder):
    types_to_str = (datetime.datetime, datetime.date, uuid.UUID, buffer)
    types_to_sort = (set,)
    types_to_repr = ()

    def default(self, obj):
        if self.types_to_str and isinstance(obj, self.types_to_str):
            return str(obj)
        elif self.types_to_repr and isinstance(obj, self.types_to_repr):
            return repr(obj)
        elif self.types_to_sort and isinstance(obj, self.types_to_sort):
            return sorted(obj)
        return json.JSONEncoder.default(self, stringify(obj))
