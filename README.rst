######
mkdong
######

A command-line utility for printing dongs.


Highlights
^^^^^^^^^^

type-safe
  mkdong prints dongs only, and all dongs inherit from ``mkdong.dong.Dong``

configurable
  mkdong prints dongs of *any* length [#one]_ and climaxes of *any* magnitude. It also supports 3 distinct girths
  
enterprise-ready
  mkdong is thoroughly torture-tested and proven print dongs in the harshest conditions. Python versions 2.6, 2.7, 3.1, and 3.4 are supported.



Install
=======

.. code:: bash
  
  # with pip
  $ pip install --upgrade mkdong
  
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
  
  $ mkdong --thick 3                    # it may not be long but at least it's fat
  ( )/( )///D
  
  
Usage
=====
::

  mkdong <options>

Options
-------

--length                print a dong with a shaft of the specified length
--thin                  print a thin, insipid dong of underwhelming girth 
--thick                 print a thick, meaty dong of impressive girth
--climax                increase the magnitude of the climax
--help                  show this help

Notes
=====

.. rubric:: Footnotes

.. [#one] Lengths greater than **100** are not supported.