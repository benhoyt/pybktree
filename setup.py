"""Run "python setup.py install" to install pybktree."""

import os
import re
import sys
from distutils.core import setup


# Read files as byte strings on Python 2.x, unicode strings on 3.x
if sys.version_info < (3, 0):
    open_args = {}
else:
    open_args = {'encoding': 'utf-8'}


# Because it's best not to import the module in setup.py
with open(os.path.join(os.path.dirname(__file__), 'pybktree.py'), **open_args) as f:
    for line in f:
        match = re.match(r"__version__.*'([0-9.]+)'", line)
        if match:
            version = match.group(1)
            break
    else:
        raise Exception("Couldn't find __version__ line in pybktree.py")


# Read long_description from README.rst
with open(os.path.join(os.path.dirname(__file__), 'README.rst'), **open_args) as f:
    long_description = f.read()


setup(
    name='pybktree',
    version=version,
    author='Ben Hoyt',
    author_email='benhoyt@gmail.com',
    url='https://github.com/Jetsetter/pybktree',
    license='MIT License',
    description='BK-tree data structure to allow fast querying of "close" matches',
    long_description=long_description,
    py_modules=['pybktree'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
