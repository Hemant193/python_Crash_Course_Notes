# Lists in Python
1. A _list_ is a collection of items in a particular order. 
2. List can contain letters of alphabet, digits from 0 to 9, words.
3. The items in our list need not be related in any particular way.
4. Name of your list should be plural. example, letters, cities, etc.
5. Square brackets [ ] indicates a list.


### More information about Lists, which may/may not be trivial to others:
According to the source code, the maximum size of a list is PY_SSIZE_T_MAX/sizeof(PyObject*) . On a regular 32bit system, this is (4294967295 / 2) / 4 or 536870912. Therefore the maximum size of a python list on a 32 bit system is 536,870,912 elements.