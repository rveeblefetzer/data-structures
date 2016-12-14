# data-structures
Sample code for a number of classic data structures implemented in Python.

Help for testing exceptions with pytest.raises(Exception) taken from [pfctdayelise](http://stackoverflow.com/users/54056/pfctdayelise) on [this Stack Overflow question](http://stackoverflow.com/questions/15012539/using-pytest-raises-to-catch-expected-custom-error)

## doubly_linked_list.py
Implementation of a doubly-linked list.

A populated list will have a head and tail, and each node points to nodes before and after (except for head and tail nodes).

Methods include:
push(val): Inserts the value val at the head of the list.
append(val): Appends the value val at the tail of the list.
pop(): Pops first value off head of list and returns it.
shift(): Removes last value from tail of list and returns it.
remove(val): Removes first instance of val in list, starting from head. If val is not present, it raises an exception.

Coverage reports for testing:

---------- coverage: platform darwin, python 2.7.12-final-0 ----------
Name                             Stmts   Miss  Cover   Missing
--------------------------------------------------------------
src/doubly_linked_list.py           72      0   100%
src/linked_list.py                  62      0   100%
src/stack.py                        16      0   100%
src/test_double_linked_list.py     116      0   100%
src/test_linked_list.py            136      0   100%
src/test_stack.py                   42      0   100%
--------------------------------------------------------------
TOTAL                              444      0   100%


---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                             Stmts   Miss  Cover   Missing
--------------------------------------------------------------
src/doubly_linked_list.py           72      0   100%
src/linked_list.py                  62      0   100%
src/stack.py                        16      0   100%
src/test_double_linked_list.py     116      0   100%
src/test_linked_list.py            136      0   100%
src/test_stack.py                   42      0   100%
--------------------------------------------------------------
TOTAL                              444      0   100%
