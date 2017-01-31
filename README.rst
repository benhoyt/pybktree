pybktree
========

pybktree is a generic, pure Python implementation of a BK-tree data structure,
which allows fast querying of "close" matches. For example, matches with small
hamming distance or Levenshtein distance. This modules is based on the
algorithm by Nick Johnson in his `blog article on BK-trees`.

Example usage:

.. code:: python

    >>> tree = pybktree.BKTree(pybktree.hamming_distance, [0, 4, 5, 14])
    >>> tree.add(15)  # add some more elements
    >>> sorted(tree)  # BKTree instances are iterable
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
* `ryanfox/bktree_: this one is hard to customize, ``search()`` doesn't return
  distances, it's slower, and was buggy (though I think he fixed it recently)

pybktree was written by `Ben Hoyt`_ for `Jetsetter`_ and is licensed with a
permissive MIT license (see `LICENSE.txt`_).


.. _blog article on BK-trees: http://blog.notdot.net/2007/4/Damn-Cool-Algorithms-Part-1-BK-Trees
.. _on the Python Package Index (PyPI): https://pypi.python.org/pypi/pybktree
.. _ahupp/bktree: https://github.com/ahupp/bktree/blob/master/bktree.py
.. _ryanfox/bktree: https://github.com/ryanfox/bktree/blob/master/bktree/bktree.py
.. _Ben Hoyt: http://benhoyt.com/
.. _Jetsetter: http://www.jetsetter.com/
.. _LICENSE.txt: https://github.com/Jetsetter/pybktree/blob/master/LICENSE.txt
