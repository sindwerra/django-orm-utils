import collections

from django.db.models import QuerySet


class AdvancedQuerySet(QuerySet):
    def indexable_values(self, main_key, *fields, **kwargs):
        result = collections.defaultdict(list)
        include_main_key = kwargs.get('include_main_key', True)
        # TODO 1. 是否能对具体表的唯一键兼容？
        # TODO 2. fields中不一定需要出现main_key √
        if main_key == 'id':
            query_key = fields + (main_key,) if main_key not in fields else fields
            for row in self.values(*query_key):
                main_key_value = row[main_key] if include_main_key else row.pop(main_key, None)
                result[main_key_value] = row
        elif isinstance(main_key, str):
            query_key = fields + (main_key,) if main_key not in fields else fields
            for row in self.values(*query_key):
                main_key_value = row[main_key] if include_main_key else row.pop(main_key, None)
                result[main_key_value].append(row)
        else:
            for row in self.values(*fields):
                result[tuple(v for k, v in row.iteritems() if k in main_key)].append(row)
        return result
