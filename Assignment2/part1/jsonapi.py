import json

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return super(JSONEncoder, self).default(obj)


class JSONDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super(JSONDecoder, self).__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, dct):
        if 'datetime' in dct:
            return datetime.datetime.fromisoformat(dct['datetime'])
        return dct


def dumps(obj, *args, **kwargs):
    return json.dumps(obj, cls=JSONEncoder, *args, **kwargs)


def loads(s, *args, **kwargs):
    return json.loads(s, cls=JSONDecoder, *args, **kwargs)


