######
mkdong
######

A command-line utility for printing dongs.


Highlights
^^^^^^^^^^

type-safe
  mkdong prints dongs only, and all dongs are instances of ``mkdong.mkdong.Dong``

configurable
  mkdong prints dongs of *any* length [#one]_ and climaxes of *any* magnitude. It also supports 3 distinct girths
  
enterprise-ready
  mkdong is thoroughly torture-tested and proven print dongs in the harshest conditions. Python versions 2.5, 2.6, 2.7, 3.1, and 3.4 are supported.



Install
=======

.. code:: bash
  
  # with pip
  $ pip install mkdong
  
  # or with setuptools
  $ clone https://bitbucket.org/cfralick/mkdong.git  
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

--length                print a dong with a shaft of the specified length
--wide                  print a thin, insipid dong of underwhelming girth 
--climax                increase the magnitude of the climax
--help                  show this help
--version               show version number and exit

Notes
=====

.. rubric:: Footnotes

.. [#one] Lengths greater than **100** are not supported.
