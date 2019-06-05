Python 3.7.1 (default, Dec 10 2018, 22:54:23) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> from sqlalchemy import create_engine
>>> from pprint import pprint
>>> import os
>>> os.chdir('C:/users/brian/desktop/birdpy')
>>> full = pd.read_csv('final_BOTH_FULL.csv')
>>> full

>>> pd.set_option('display.max_colwidth', -1)
>>> full

>>> full

>>> full
           0  1     2
0        32   0  2000
1        32   0  2000
2        32   0  2000
3        32   0  2000
4        32   0  2000
5        32   0  2000
6        32   0  2000
7        32   0  2000
8        32   0  2000
9        32   0  2000
10       32   0  2000
11       32   0  2000
12       32   0  2000
13       32   0  2000
14       32   0  2000
15       32   0  2000
16       32   0  2000
17       32   0  2000
18       32   0  2000
19       32   0  2000
20       32   0  2000
21       32   0  2000
22       32   0  2000
23       32   0  2000
24       32   0  2000
25       32   0  2000
26       32   0  2000
27       32   0  2000
28       32   0  2000
29       32   0  2000
...      ..  ..   ...
3061429  121  1  2016
3061430  121  1  2016
3061431  121  1  2016
3061432  121  1  2016
3061433  121  1  2016
3061434  121  1  2016
3061435  121  1  2016
3061436  121  1  2016
3061437  121  1  2016
3061438  121  1  2016
3061439  121  1  2016
3061440  121  1  2016
3061441  121  1  2016
3061442  121  1  2016
3061443  121  1  2016
3061444  121  1  2016
3061445  121  1  2016
3061446  121  1  2016
3061447  121  1  2016
3061448  121  1  2016
3061449  121  1  2016
3061450  121  1  2016
3061451  121  1  2016
3061452  121  1  2016
3061453  121  1  2016
3061454  121  1  2016
3061455  121  1  2016
3061456  121  1  2016
3061457  121  1  2016
3061458  121  1  2016

[3061459 rows x 3 columns]
>>> full.median
<bound method DataFrame.median of            0  1     2
0        32   0  2000
1        32   0  2000
2        32   0  2000
3        32   0  2000
4        32   0  2000
5        32   0  2000
6        32   0  2000
7        32   0  2000
8        32   0  2000
9        32   0  2000
10       32   0  2000
11       32   0  2000
12       32   0  2000
13       32   0  2000
14       32   0  2000
15       32   0  2000
16       32   0  2000
17       32   0  2000
18       32   0  2000
19       32   0  2000
20       32   0  2000
21       32   0  2000
22       32   0  2000
23       32   0  2000
24       32   0  2000
25       32   0  2000
26       32   0  2000
27       32   0  2000
28       32   0  2000
29       32   0  2000
...      ..  ..   ...
3061429  121  1  2016
3061430  121  1  2016
3061431  121  1  2016
3061432  121  1  2016
3061433  121  1  2016
3061434  121  1  2016
3061435  121  1  2016
3061436  121  1  2016
3061437  121  1  2016
3061438  121  1  2016
3061439  121  1  2016
3061440  121  1  2016
3061441  121  1  2016
3061442  121  1  2016
3061443  121  1  2016
3061444  121  1  2016
3061445  121  1  2016
3061446  121  1  2016
3061447  121  1  2016
3061448  121  1  2016
3061449  121  1  2016
3061450  121  1  2016
3061451  121  1  2016
3061452  121  1  2016
3061453  121  1  2016
3061454  121  1  2016
3061455  121  1  2016
3061456  121  1  2016
3061457  121  1  2016
3061458  121  1  2016

[3061459 rows x 3 columns]>
>>> full['date'].median()
Traceback (most recent call last):
  File "C:\Users\brian\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 3078, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'date'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    full['date'].median()
  File "C:\Users\brian\Anaconda3\lib\site-packages\pandas\core\frame.py", line 2688, in __getitem__
    return self._getitem_column(key)
  File "C:\Users\brian\Anaconda3\lib\site-packages\pandas\core\frame.py", line 2695, in _getitem_column
    return self._get_item_cache(key)
  File "C:\Users\brian\Anaconda3\lib\site-packages\pandas\core\generic.py", line 2489, in _get_item_cache
    values = self._data.get(item)
  File "C:\Users\brian\Anaconda3\lib\site-packages\pandas\core\internals.py", line 4115, in get
    loc = self.items.get_loc(item)
  File "C:\Users\brian\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 3080, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'date'
>>> full.describe()
                  0             1             2
count  3.061459e+06  3.061459e+06  3.061459e+06
mean   4.955437e+01  3.254122e-01  2.012941e+03
std    1.438171e+01  4.685287e-01  4.000280e+00
min    3.200000e+01  0.000000e+00  2.000000e+03
25%    4.000000e+01  0.000000e+00  2.011000e+03
50%    4.700000e+01  0.000000e+00  2.014000e+03
75%    5.500000e+01  1.000000e+00  2.017000e+03
max    1.210000e+02  1.000000e+00  2.018000e+03
>>> full.date.describe()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    full.date.describe()
  File "C:\Users\brian\Anaconda3\lib\site-packages\pandas\core\generic.py", line 4376, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'date'
>>> full.['date'].describe()
SyntaxError: invalid syntax
>>> full['date'].describe()
Traceback (most recent call last):
  File "C:\Users\brian\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 3078, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'date'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    full['date'].describe()
  File "C:\Users\brian\Anaconda3\lib\site-packages\pandas\core\frame.py", line 2688, in __getitem__
    return self._getitem_column(key)
  File "C:\Users\brian\Anaconda3\lib\site-packages\pandas\core\frame.py", line 2695, in _getitem_column
    return self._get_item_cache(key)
  File "C:\Users\brian\Anaconda3\lib\site-packages\pandas\core\generic.py", line 2489, in _get_item_cache
    values = self._data.get(item)
  File "C:\Users\brian\Anaconda3\lib\site-packages\pandas\core\internals.py", line 4115, in get
    loc = self.items.get_loc(item)
  File "C:\Users\brian\Anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 3080, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'date'
>>> head(full)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    head(full)
NameError: name 'head' is not defined
>>> full.head
<bound method NDFrame.head of            0  1     2
0        32   0  2000
1        32   0  2000
2        32   0  2000
3        32   0  2000
4        32   0  2000
5        32   0  2000
6        32   0  2000
7        32   0  2000
8        32   0  2000
9        32   0  2000
10       32   0  2000
11       32   0  2000
12       32   0  2000
13       32   0  2000
14       32   0  2000
15       32   0  2000
16       32   0  2000
17       32   0  2000
18       32   0  2000
19       32   0  2000
20       32   0  2000
21       32   0  2000
22       32   0  2000
23       32   0  2000
24       32   0  2000
25       32   0  2000
26       32   0  2000
27       32   0  2000
28       32   0  2000
29       32   0  2000
...      ..  ..   ...
3061429  121  1  2016
3061430  121  1  2016
3061431  121  1  2016
3061432  121  1  2016
3061433  121  1  2016
3061434  121  1  2016
3061435  121  1  2016
3061436  121  1  2016
3061437  121  1  2016
3061438  121  1  2016
3061439  121  1  2016
3061440  121  1  2016
3061441  121  1  2016
3061442  121  1  2016
3061443  121  1  2016
3061444  121  1  2016
3061445  121  1  2016
3061446  121  1  2016
3061447  121  1  2016
3061448  121  1  2016
3061449  121  1  2016
3061450  121  1  2016
3061451  121  1  2016
3061452  121  1  2016
3061453  121  1  2016
3061454  121  1  2016
3061455  121  1  2016
3061456  121  1  2016
3061457  121  1  2016
3061458  121  1  2016

[3061459 rows x 3 columns]>
>>> full.head()
    0  1     2
0  32  0  2000
1  32  0  2000
2  32  0  2000
3  32  0  2000
4  32  0  2000
>>> 
KeyboardInterrupt
>>> 
=============================== RESTART: Shell ===============================
>>> import pandas as pd
>>> from sqlalchemy import create_engine
>>> from pprint import pprint
>>> import os
>>> os.chdir('C:/users/brian/desktop/birdpy')
>>> full = pd.read_csv('final_BOTH_FULL.csv')
SyntaxError: multiple statements found while compiling a single statement
>>> import pandas as pd
>>> from sqlalchemy import create_engine
>>> from pprint import pprint
>>> import os
>>> os.chdir('C:/users/brian/desktop/birdpy')
>>> import os
>>> from pprint import pprint
>>> from sqlalchemy import create_engine
>>> import pandas as pd
>>> os.chdir('C:/users/brian/desktop/birdpy')disk_engine = create_engine('sqlite:///' + inputFile)
SyntaxError: invalid syntax
>>> disk_engine = create_engine('sqlite:///fina_BOTH_FULL')
>>> disk_engine = create_engine('sqlite:///final_BOTH_FULL')
>>> df = pd.read_sql_query('SELECT * FROM data', disk_engine)
Traceback (most recent call last):
  File "C:\Users\brian\Anaconda3\lib\site-packages\sqlalchemy\engine\base.py", line 1193, in _execute_context
    context)
  File "C:\Users\brian\Anaconda3\lib\site-packages\sqlalchemy\engine\default.py", line 509, in do_execute
    cursor.execute(statement, parameters)
sqlite3.OperationalError: no such table: data

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    df = pd.read_sql_query('SELECT * FROM data', disk_engine)
  File "C:\Users\brian\Anaconda3\lib\site-packages\pandas\io\sql.py", line 314, in read_sql_query
    parse_dates=parse_dates, chunksize=chunksize)
  File "C:\Users\brian\Anaconda3\lib\site-packages\pandas\io\sql.py", line 1063, in read_query
    result = self.execute(*args)
  File "C:\Users\brian\Anaconda3\lib\site-packages\pandas\io\sql.py", line 954, in execute
    return self.connectable.execute(*args, **kwargs)
  File "C:\Users\brian\Anaconda3\lib\site-packages\sqlalchemy\engine\base.py", line 2075, in execute
    return connection.execute(statement, *multiparams, **params)
  File "C:\Users\brian\Anaconda3\lib\site-packages\sqlalchemy\engine\base.py", line 942, in execute
    return self._execute_text(object, multiparams, params)
  File "C:\Users\brian\Anaconda3\lib\site-packages\sqlalchemy\engine\base.py", line 1104, in _execute_text
    statement, parameters
  File "C:\Users\brian\Anaconda3\lib\site-packages\sqlalchemy\engine\base.py", line 1200, in _execute_context
    context)
  File "C:\Users\brian\Anaconda3\lib\site-packages\sqlalchemy\engine\base.py", line 1413, in _handle_dbapi_exception
    exc_info
  File "C:\Users\brian\Anaconda3\lib\site-packages\sqlalchemy\util\compat.py", line 265, in raise_from_cause
    reraise(type(exception), exception, tb=exc_tb, cause=cause)
  File "C:\Users\brian\Anaconda3\lib\site-packages\sqlalchemy\util\compat.py", line 248, in reraise
    raise value.with_traceback(tb)
  File "C:\Users\brian\Anaconda3\lib\site-packages\sqlalchemy\engine\base.py", line 1193, in _execute_context
    context)
  File "C:\Users\brian\Anaconda3\lib\site-packages\sqlalchemy\engine\default.py", line 509, in do_execute
    cursor.execute(statement, parameters)
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: data [SQL: 'SELECT * FROM data'] (Background on this error at: http://sqlalche.me/e/e3q8)
>>> disk_engine = create_engine('sqlite:///final_BOTH_FULL.db')
>>> df = pd.read_sql_query('SELECT * FROM data', disk_engine)
>>> df.head()
    0  1     2
0  32  0  2000
1  32  0  2000
2  32  0  2000
3  32  0  2000
4  32  0  2000
>>> len(df[[df['1'] = 0]])
SyntaxError: invalid syntax
>>> len(df[[df['1'] == 0]])
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    len(df[[df['1'] == 0]])
  File "C:\Users\brian\Anaconda3\lib\site-packages\pandas\core\frame.py", line 2682, in __getitem__
    return self._getitem_array(key)
  File "C:\Users\brian\Anaconda3\lib\site-packages\pandas\core\frame.py", line 2719, in _getitem_array
    (len(key), len(self.index)))
ValueError: Item wrong length 1 instead of 3061459.
>>> df[[df['1'] == 0]].len()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    df[[df['1'] == 0]].len()
  File "C:\Users\brian\Anaconda3\lib\site-packages\pandas\core\frame.py", line 2682, in __getitem__
    return self._getitem_array(key)
  File "C:\Users\brian\Anaconda3\lib\site-packages\pandas\core\frame.py", line 2719, in _getitem_array
    (len(key), len(self.index)))
ValueError: Item wrong length 1 instead of 3061459.
>>> len(df)
3061459
>>> len(df[df['1']==0])
2065223
>>> len(df[df['1']==1])
996236
>>> rural = df[df['1']==0]
>>> urban = df[df['1']==1]
>>> bigd = [rural,urban]
>>> rural.head
<bound method NDFrame.head of            0  1     2
0         32  0  2000
1         32  0  2000
2         32  0  2000
3         32  0  2000
4         32  0  2000
5         32  0  2000
6         32  0  2000
7         32  0  2000
8         32  0  2000
9         32  0  2000
10        32  0  2000
11        32  0  2000
12        32  0  2000
13        32  0  2000
14        32  0  2000
15        32  0  2000
16        32  0  2000
17        32  0  2000
18        32  0  2000
19        32  0  2000
20        32  0  2000
21        32  0  2000
22        32  0  2000
23        32  0  2000
24        32  0  2000
25        32  0  2000
26        32  0  2000
27        32  0  2000
28        32  0  2000
29        32  0  2000
...      ... ..   ...
2065193  121  0  2016
2065194  121  0  2016
2065195  121  0  2016
2065196  121  0  2016
2065197  121  0  2016
2065198  121  0  2016
2065199  121  0  2016
2065200  121  0  2016
2065201  121  0  2016
2065202  121  0  2016
2065203  121  0  2016
2065204  121  0  2016
2065205  121  0  2016
2065206  121  0  2016
2065207  121  0  2016
2065208  121  0  2016
2065209  121  0  2016
2065210  121  0  2016
2065211  121  0  2016
2065212  121  0  2016
2065213  121  0  2016
2065214  121  0  2016
2065215  121  0  2004
2065216  121  0  2004
2065217  121  0  2004
2065218  121  0  2004
2065219  121  0  2004
2065220  121  0  2004
2065221  121  0  2004
2065222  121  0  2004

[2065223 rows x 3 columns]>
>>> rural.head()
    0  1     2
0  32  0  2000
1  32  0  2000
2  32  0  2000
3  32  0  2000
4  32  0  2000
>>> len(df[df['1'] == 0 & df['2']==2000])
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    len(df[df['1'] == 0 & df['2']==2000])
  File "C:\Users\brian\Anaconda3\lib\site-packages\pandas\core\generic.py", line 1576, in __nonzero__
    .format(self.__class__.__name__))
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
>>> 
