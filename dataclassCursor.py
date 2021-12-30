import dataclasses

import pymysql


def _get_attrs(self):
    return self.__dict__.keys()


def _as_dict(self):
    return dataclasses.asdict(self)


CLASS_NAME = 'Record'


def _to_dataclass(data: dict, frozen: bool = False):
    # fields = [(key, type(val)) for key, val in data.items()]
    fields = [ key.replace(".", "_") for key in data.keys() ]

    data_cls = dataclasses.make_dataclass(
        CLASS_NAME,
        fields,
        namespace=dict(attrs=_get_attrs, as_dict=_as_dict),
        frozen=frozen
    )

    return data_cls(**data)


class _DataclassCursorMixin(pymysql.cursors.DictCursorMixin):
    def _conv_row(self, row):
        if row is None:
            return None
        return _to_dataclass(dict(zip(self._fields, row)), frozen=False)


class DataclassCursor(_DataclassCursorMixin, pymysql.cursors.Cursor):
    """DataclassCursor"""


class _FrozenDataclassCursorMixin(pymysql.cursors.DictCursorMixin):
    def _conv_row(self, row):
        if row is None:
            return None
        return _to_dataclass(dict(zip(self._fields, row)), frozen=True)


class FrozenDataclassCursor(_FrozenDataclassCursorMixin, pymysql.cursors.Cursor):
    """DataclassCursor"""
