######
mkdong
######

A command-line utility for printing dongs.

.. image:: https://travis-ci.org/cfralick/mkdong.svg?branch=develop
    :target: https://travis-ci.org/cfralick/mkdong 


Highlights
^^^^^^^^^^

type-safe
  mkdong prints dongs only, and all dongs are instances of ``mkdong.dong.Dong``

configurable
  mkdong prints dongs of *any* length [#one]_ and climaxes of *any* magnitude. It also supports 3 distinct girths
  
enterprise-ready
  mkdong is thoroughly torture-tested and proven print dongs in the harshest conditions. Python versions 2.5, 2.6, 2.7, 3.2, 3.3, and 3.4 are supported.



Install
=======

.. code:: bash
  
  # with pip
  $ pip install mkdong
  
  # or with git & setuptools
  $ git clone https://bitbucket.org/cfralick/mkdong.git  
  $ cd mkdong && python setup.py install


Use
====

.. code:: bash  
  
  $ mkdong                              # default dong
  ( )/( )=======D
  
  $ mkdong --climax --climax 15        # an average dong       
  ( )/( )-----------------D~~    
  
  $ mkdong -www 3                    # it may not be long but at least it's fat
  ( )/( )///D
  
  
Usage
=====
::

  mkdong <options> length [outfile]

Options
-------

-w, --wide                  print a thin, insipid dong of underwhelming girth 
-c, --climax                increase the magnitude of the climax
-h, --help                  show this help
-v, --version               show version number and exit

Notes
=====

.. [#one] Lengths greater than **100** are not supported.
