# <c>EPAi Session 9 Tuples & Named Tuples with Application </c> 


## Tuples

- Iteratable
- Ordred
- Heterogenous
- Immutable

## Named Tuples

Since order in tuples can not be changed, programmers generally give intrinsic meaning to it. For ex: a point in 2D plane is frequently expressed as: `(10,20)` Here x = 10, y = 20.

Truples themselves do not have any support for adding labels to their values. We could use class, but then it won't be immutable and we would have to define all interfaces as well. This warranted something that gives the best of both world.

Hence NamedTuples were introduced. They are a class generator that creates a **class** which is sub-type of **Tuples**.

```python
# a function that generates a class factory which inherits from tuple
from collections import namedtuple

Point2D = namedtuple('Point2D','x y') #

origin = Point2D(x=0,y=0) #using keyword args
somepoint = Point2D(10,20) #usiong positional args

```

Arguments can be provided as 
- space separated varibales 
- list of strings
- tuple of strings


> `_fields` property can be used to list filed names of a tuple class.

>  `_asdict()` property creates an equivalent dictionary of the tuple

> `_replace()` create a new tuple by replacing any values of existing tuple


### Extending Named Tuple

```python
Stock = namedtuple('Stock', 'symbol, year, month, day, open, high, low, close')
StockExt = namedtuple('StockExt', Stock._fields + ('new_field1,'))

```


