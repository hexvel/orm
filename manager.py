from query import Query
from connector import HEXConnector


class Manager:
    def __init__(self, model_class):
        self._model_class = model_class
        self._model_fields = model_class._original_fields.keys()
        q = Query()
        self.q = q.Select(*self._model_fields).From(model_class._model_name)
        self._connector = HEXConnector()

    def filter(self, *args, **kwargs):
        self.q = self.q.Where(*args, **kwargs)
        return self

    def fetch(self, *args, **kwargs):
        q = str(self.q)
        db_results = self._connector.fetch(q)
        results = []
        for row in db_results:
            model = self._model_class()
            for field, val in zip(self._model_fields, row):
                setattr(model, field, val)
            results.append(model)
        return results
