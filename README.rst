pybktree
========

pybktree is a generic, pure Python implementation of a `BK-tree`_ data
structure, which allows fast querying of "close" matches (for example, matches
with small hamming distance or Levenshtein distance). This module is based on
the algorithm by Nick Johnson in his `blog article on BK-trees`_.

The library is `on the Python Package Index (PyPI)`_ and works on both Python
3 and Python 2.7. To install it, fire up a command prompt, activate your
virtual environment if you're using one, and type:

::

    pip install pybktree

Example usage:

.. code:: python

    >>> tree = pybktree.BKTree(pybktree.hamming_distance, [0, 4, 5, 14])
    >>> tree.add(15)              # add element 15
    >>> sorted(tree)              # BKTree instances are iterable
    [0, 4, 5, 14, 15]
    >>> sorted(tree.find(13, 1))  # find elements at most 1 bit away from element 13
    [(1, 5), (1, 15)]

For large trees and fairly small N when calling ``find()``, using a BKTree is
much faster than doing a linear search. This is especially good when you're
de-duping a few hundred thousand photos -- with a linear search that would
become a very slow, O(N²) operation. With a BKTree, it's more like O(N log N).

Read the code in `pybktree.py`_ for more details – it's pretty small!

Other BK-tree modules I found on GitHub while writing this one:

* `ahupp/bktree`_: this one is pretty good, but it's not on PyPI, and it's
  recursive
* `ryanfox/bktree`_: this one is hard to customize, ``search()`` doesn't
  return distances, it's slower, and was buggy (though I think he fixed it
  recently)

pybktree was written by `Ben Hoyt`_ for `Jetsetter`_ and is licensed with a
permissive MIT license (see `LICENSE.txt`_).


.. _BK-tree: https://en.wikipedia.org/wiki/BK-tree
.. _blog article on BK-trees: http://blog.notdot.net/2007/4/Damn-Cool-Algorithms-Part-1-BK-Trees
.. _on the Python Package Index (PyPI): https://pypi.python.org/pypi/pybktree
.. _pybktree.py: https://github.com/Jetsetter/pybktree/blob/master/pybktree.py
.. _ahupp/bktree: https://github.com/ahupp/bktree
.. _ryanfox/bktree: https://github.com/ryanfox/bktree
.. _Ben Hoyt: http://benhoyt.com/
.. _Jetsetter: http://www.jetsetter.com/
.. _LICENSE.txt: https://github.com/Jetsetter/pybktree/blob/master/LICENSE.txt
