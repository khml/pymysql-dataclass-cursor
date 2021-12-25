# pymysql-dataclass-cursor


Cursor that returns the retrieved records as dataclass for PyMySQL.



# Cursors
- DataclassCursor
- FrozenDataclassCursor


# Example

```python

import pymysql
from dataclassCursor import DataclassCursor

connection = pymysql.connect(host="", port=, user="", passwd="", db="")

with connection:
    with connection.cursor(DataclassCursor) as cursor:
        """your code here"""
        cursor.execute(query, params)
        record = cursor.fetchone()
        record.column_name  # Instead of write record["column_name"]
        record.as_dict(). # get a record as dict

```
