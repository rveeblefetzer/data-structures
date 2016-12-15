# data-structures
Sample code for a number of classic data structures implemented in Python.

Help for testing exceptions with pytest.raises(Exception) taken from [pfctdayelise](http://stackoverflow.com/users/54056/pfctdayelise) on [this Stack Overflow question](http://stackoverflow.com/questions/15012539/using-pytest-raises-to-catch-expected-custom-error)

##Data Structures Include:
    1. Singly Linked List
    2. Stack
    3. Doubly Linked List
    4. Queue

##1. Singly Linked List
###Methods - 
A singly linked list consists of a head element which points to a Node that consists of data and a pointer to the next Node of data. If there is no more data then the pointer points to None.

Module : linked_list.py
Test Module: test_linked_list.py

    1. Push(value) - Push a Node to the head of the list
    2. Pop() - Remove the top Node of the list and return its value
    3. Size() - Returns the number of nodes in the list
    4. Search(value) - Searches for a value in the list and returns the first node that contains that data.
    5. Remove(value) - Searches for a value in the list, removes the node containing that data and returns True if successful.
    6. Display -  Returns a string that in tuple format listing all the elements in the list.

##2. Stack
A stack is an implemenation of a singly linked list.  The inner data structure of the stack is a singly linked list and the Stack class uses push and pop methods to manipulate that list.   

Module : stack
Test Module: test_stack.py

    1. Push(value) - Push a Node to the head of the list with given value.
    2. Pop() - Remove the top Node of the Stack and return its value.

##3. Doubly Linked List
A Doubly linked list consists of a head and tail elements which point to the front and end Nodes of the list.  Each Node that makes up the elements of the linked list contains a data element as well as head and tail pointers to next and previous nodes.

Module : doubly_linked_list.py
Test Module: test_double_linked_list.py

    1. Push(value) - Pushes a node with data set as value to the head of the list.
    2. Append(value) - APpends a node with data set as value to the tail of the list.
    3. Pop() - Remove the head element of the list and return its value.
    4. Shift() - Remove the tail element of the list and return its value.
    5. Remove(value) - Search the list for the given value and remove the first element of the list that matches that value.

##4. Queue
A queue data structure is a specific implemenation of a doubly linked list.  The inner data structure in the Queue is a doubly linked list and the queue methods call uses those methods for manipulating its data.    

Module : queue.py
Test Module: test_queue.py

    1. Enqueue(value) - Adds a node with data set as value to the tail of the queue.
    2. Dequeue() - Remove the head of the list and return its value. 
    3. Peek() - Returns the value of the head element but does not remove it.
    4. Size() - Returns the number of nodes in the queue.


## Current Test Coverage
```
---------- coverage: platform darwin, python 2.7.12-final-0 ----------
Name                             Stmts   Miss  Cover   Missing
--------------------------------------------------------------
src/doubly_linked_list.py           72      0   100%
src/linked_list.py                  62      0   100%
src/queue.py                        14      0   100%
src/stack.py                        16      0   100%
src/test_double_linked_list.py     116      0   100%
src/test_linked_list.py            136      0   100%
src/test_queue.py                   41      0   100%
src/test_stack.py                   42      0   100%
--------------------------------------------------------------
TOTAL                              499      0   100%
```
```
---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                             Stmts   Miss  Cover   Missing
--------------------------------------------------------------
src/doubly_linked_list.py           72      0   100%
src/linked_list.py                  62      0   100%
src/queue.py                        14      0   100%
src/stack.py                        16      0   100%
src/test_double_linked_list.py     116      0   100%
src/test_linked_list.py            136      0   100%
src/test_queue.py                   41      0   100%
src/test_stack.py                   42      0   100%
--------------------------------------------------------------
TOTAL                              499      0   100%
```


