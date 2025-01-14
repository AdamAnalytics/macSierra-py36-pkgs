================================================================================
pyexcel - Let you focus on data, instead of file formats
================================================================================

.. image:: https://raw.githubusercontent.com/pyexcel/pyexcel.github.io/master/images/patreon.png
   :target: https://www.patreon.com/pyexcel

.. image:: https://api.travis-ci.org/pyexcel/pyexcel.svg?branch=master
   :target: http://travis-ci.org/pyexcel/pyexcel

.. image:: https://codecov.io/gh/pyexcel/pyexcel/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/pyexcel/pyexcel

.. image:: https://img.shields.io/gitter/room/gitterHQ/gitter.svg
   :target: https://gitter.im/pyexcel/Lobby

.. image:: https://readthedocs.org/projects/pyexcel/badge/?version=latest
   :target: http://pyexcel.readthedocs.org/en/latest/

Support the project
================================================================================

If your company has embedded pyexcel and its components into a revenue generating
product, please `support me on patreon <https://www.patreon.com/bePatron?u=5537627>`_ to
maintain the project and develop it further.

If you are an individual, you are welcome to support me too on patreon and for however long
you feel like to. As a patreon, you will receive
`early access to pyexcel related contents <https://www.patreon.com/pyexcel/posts>`_.

With your financial support, I will be able to invest
a little bit more time in coding, documentation and writing interesting posts.


Known constraints
==================

Fonts, colors and charts are not supported.

Introduction
================================================================================

Feature Highlights
===================

1. One API to handle multiple data sources:

   * physical file
   * memory file
   * SQLAlchemy table
   * Django Model
   * Python data stuctures: dictionary, records and array
2. One application programming interface(API) to read and write data in various excel file formats.




Installation
================================================================================
You can install it via pip:

.. code-block:: bash

    $ pip install pyexcel


or clone it and install it:

.. code-block:: bash

    $ git clone https://github.com/pyexcel/pyexcel.git
    $ cd pyexcel
    $ python setup.py install



Usage
===============

.. image:: https://github.com/pyexcel/pyexcel-sortable/raw/master/sortable.gif

.. code-block:: python

    >>> # pip install pyexcel-text==0.2.7.1
    >>> import pyexcel as p
    >>> ccs_insight2 = p.Sheet()
    >>> ccs_insight2.name = "Worldwide Mobile Phone Shipments (Billions), 2017-2021"
    >>> ccs_insight2.ndjson = """
    ... {"year": ["2017", "2018", "2019", "2020", "2021"]}
    ... {"smart phones": [1.53, 1.64, 1.74, 1.82, 1.90]}
    ... {"feature phones": [0.46, 0.38, 0.30, 0.23, 0.17]}
    ... """.strip()
    >>> ccs_insight2
    pyexcel sheet:
    +----------------+------+------+------+------+------+
    | year           | 2017 | 2018 | 2019 | 2020 | 2021 |
    +----------------+------+------+------+------+------+
    | smart phones   | 1.53 | 1.64 | 1.74 | 1.82 | 1.9  |
    +----------------+------+------+------+------+------+
    | feature phones | 0.46 | 0.38 | 0.3  | 0.23 | 0.17 |
    +----------------+------+------+------+------+------+



Suppose you have the following data in a dictionary:

========= ====
Name      Age
========= ====
Adam      28
Beatrice  29
Ceri      30
Dean      26
========= ====

you can easily save it into an excel file, using the following code.

.. code-block:: python

   >>> import pyexcel
   >>> # make sure you had pyexcel-xls installed
   >>> a_list_of_dictionaries = [
   ...     {
   ...         "Name": 'Adam',
   ...         "Age": 28
   ...     },
   ...     {
   ...         "Name": 'Beatrice',
   ...         "Age": 29
   ...     },
   ...     {
   ...         "Name": 'Ceri',
   ...         "Age": 30
   ...     },
   ...     {
   ...         "Name": 'Dean',
   ...         "Age": 26
   ...     }
   ... ]
   >>> pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="your_file.xls")


Here are the method to obtain the records:

.. code-block:: python

   >>> import pyexcel as pe
   >>> records = pe.iget_records(file_name="your_file.xls")
   >>> for record in records:
   ...     print("%s is aged at %d" % (record['Name'], record['Age']))
   Adam is aged at 28
   Beatrice is aged at 29
   Ceri is aged at 30
   Dean is aged at 26
   >>> pe.free_resources()


Available Plugins
=================

.. _file-format-list:
.. _a-map-of-plugins-and-file-formats:

.. table:: A list of file formats supported by external plugins

   ======================== ======================= =============== ==================
   Package name              Supported file formats  Dependencies   Python versions
   ======================== ======================= =============== ==================
   `pyexcel-io`_            csv, csvz [#f1]_, tsv,                  2.6, 2.7, 3.3,
                            tsvz [#f2]_                             3.4, 3.5, 3.6
                                                                    pypy
   `pyexcel-xls`_           xls, xlsx(read only),   `xlrd`_,        same as above
                            xlsm(read only)         `xlwt`_
   `pyexcel-xlsx`_          xlsx                    `openpyxl`_     same as above
   `pyexcel-xlsxw`_         xlsx(write only)        `XlsxWriter`_   same as above
   `pyexcel-ods3`_          ods                     `ezodf`_,       2.6, 2.7, 3.3, 3.4
                                                    lxml            3.5, 3.6
   `pyexcel-ods`_           ods                     `odfpy`_        same as above
   `pyexcel-odsr`_          read only for ods, fods lxml            same as above
   `pyexcel-htmlr`_         html(read only)         lxml,html5lib   same as above
   `pyexcel-text`_          write only:rst,         `tabulate`_     2.6, 2.7, 3.3, 3.4
                            mediawiki, html,                        3.5, 3.6, pypy
                            latex, grid, pipe,
                            orgtbl, plain simple
                            read only: ndjson
                            r/w: json
   `pyexcel-handsontable`_  handsontable in html    `handsontable`_ same as above
   `pyexcel-pygal`_         svg chart               `pygal`_        2.7, 3.3, 3.4, 3.5
                                                                    3.6, pypy
   `pyexcel-sortable`_      sortable table in html  `csvtotable`_   same as above
   `pyexcel-gantt`_         gantt chart in html     `frappe-gantt`_ except pypy, same
                                                                    as above
   ======================== ======================= =============== ==================

.. _pyexcel-io: https://github.com/pyexcel/pyexcel-io
.. _pyexcel-xls: https://github.com/pyexcel/pyexcel-xls
.. _pyexcel-xlsx: https://github.com/pyexcel/pyexcel-xlsx
.. _pyexcel-ods: https://github.com/pyexcel/pyexcel-ods
.. _pyexcel-ods3: https://github.com/pyexcel/pyexcel-ods3
.. _pyexcel-odsr: https://github.com/pyexcel/pyexcel-odsr
.. _pyexcel-xlsxw: https://github.com/pyexcel/pyexcel-xlsxw
.. _pyexcel-htmlr: https://github.com/pyexcel/pyexcel-htmlr

.. _xlrd: https://github.com/python-excel/xlrd
.. _xlwt: https://github.com/python-excel/xlwt
.. _openpyxl: https://bitbucket.org/openpyxl/openpyxl
.. _XlsxWriter: https://github.com/jmcnamara/XlsxWriter
.. _ezodf: https://github.com/T0ha/ezodf
.. _odfpy: https://github.com/eea/odfpy

.. _pyexcel-text: https://github.com/pyexcel/pyexcel-text
.. _tabulate: https://bitbucket.org/astanin/python-tabulate
.. _pyexcel-handsontable: https://github.com/pyexcel/pyexcel-handsontable
.. _handsontable: https://cdnjs.com/libraries/handsontable
.. _pyexcel-pygal: https://github.com/pyexcel/pyexcel-chart
.. _pygal: https://github.com/Kozea/pygal
.. _pyexcel-matplotlib: https://github.com/pyexcel/pyexcel-matplotlib
.. _matplotlib: https://matplotlib.org
.. _pyexcel-sortable: https://github.com/pyexcel/pyexcel-sortable
.. _csvtotable: https://github.com/vividvilla/csvtotable
.. _pyexcel-gantt: https://github.com/pyexcel/pyexcel-gantt
.. _frappe-gantt: https://github.com/frappe/gantt

In order to manage the list of plugins installed, you need to use pip to add or remove
a plugin. When you use virtualenv, you can have different plugins per virtual
environment. In the situation where you have multiple plugins that does the same thing
in your environment, you need to tell pyexcel which plugin to use per function call.
For example, pyexcel-ods and pyexcel-odsr, and you want to get_array to use pyexcel-odsr.
You need to append get_array(..., library='pyexcel-odsr').

.. rubric:: Footnotes

.. [#f1] zipped csv file
.. [#f2] zipped tsv file


Acknowledgement
===============

All great work have been done by odf, ezodf, xlrd, xlwt, tabulate and other
individual developers. This library unites only the data access code.


License
================================================================================

New BSD License

Change log
================================================================================

0.6.0 - unreleased
--------------------------------------------------------------------------------

Planned
********************************************************************************

#. investigate if hidden columns could be supported
#. update cookbook.py using 0.5.0 api
#. refactor test code
#. suppert missing pandas io features: use custom boolean values, write stylish
   spreadsheets.


0.5.3 - 01-08-2017
--------------------------------------------------------------------------------

#. `#95 <https://github.com/pyexcel/pyexcel/issues/95>`_, respect the order of
   records in iget_records, isave_as and save_as.
#. `#97 <https://github.com/pyexcel/pyexcel/issues/97>`_, new feature to allow
   intuitive initialization of pyexcel.Book.


0.5.2 - 26-07-2017
--------------------------------------------------------------------------------

Updated
********************************************************************************

#. embeded the enabler for pyexcel-htmlr. http source does not support text/html
   as mime type.

0.5.1 - 12.06.2017
--------------------------------------------------------------------------------

Updated
********************************************************************************

#. support saving SheetStream and BookStream to database targets. This is needed
   for pyexcel-webio and its downstream projects.

0.5.0 - 19.06.2017
--------------------------------------------------------------------------------

Added
********************************************************************************

#. Sheet.top() and Sheet.top_left() for data browsing
#. add html as default rich display in Jupyter notebook when pyexcel-text
   and pyexcel-chart is installed
#. add svg as default rich display in Jupyter notebook when pyexcel-chart and
   one of its implementation plugin(pyexcel-pygal, etc.) are is installed
#. new dictionary source supported: a dictionary of key value pair could be
   read into a sheet.
#. added dynamic external plugin loading. meaning if a pyexcel plugin
   is installed, it will be loaded implicitly. And this change would remove
   unnecessary info log for those who do not use pyexcel-text and pyexcel-gal
#. save_book_as before 0.5.0 becomes isave_book_as and save_book_as in 0.5.0
   convert BookStream to Book before saving.
#. `#83 <https://github.com/pyexcel/pyexcel/issues/83>`_, file closing mechanism
   is enfored. free_resource is added and it should be called when iget_array,
   iget_records, isave_as and/or isave_book_as are used.

Updated
********************************************************************************

#. array is passed to pyexcel.Sheet as reference. it means your array data will
   be modified.

Removed
********************************************************************************

#. pyexcel.Writer and pyexcel.BookWriter were removed
#. pyexcel.load_book_from_sql and pyexcel.load_from_sql were removed
#. pyexcel.deprecated.load_from_query_sets,
   pyexcel.deprecated.load_book_from_django_models and
   pyexcel.deprecated.load_from_django_model were removed
#. Removed plugin loading code and lml is used instead


0.4.5 - 17.03.2017
--------------------------------------------------------------------------------

Updated
********************************************************************************

#. `#80 <https://github.com/pyexcel/pyexcel/issues/80>`_: remove pyexcel-chart
   import from v0.4.x

0.4.4 - 06.02.2017
--------------------------------------------------------------------------------

Updated
********************************************************************************

#. `#68 <https://github.com/pyexcel/pyexcel/issues/68>`_: regression
   save_to_memory() should have returned a stream instance which has
   been reset to zero if possible. The exception is sys.stdout, which cannot
   be reset.

#. `#74 <https://github.com/pyexcel/pyexcel/issues/74>`_: Not able to
   handle decimal.Decimal

Removed
********************************************************************************

#. remove get_{{file_type}}_stream functions from pyexcel.Sheet and
   pyexcel.Book introduced since 0.4.3.


0.4.3 - 26.01.2017
--------------------------------------------------------------------------------

Added
********************************************************************************

#. '.stream' attribute are attached to `~pyexcel.Sheet` and
   `~pyexcel.Book` to get direct access the underneath stream
   in responding to file type attributes, such as sheet.xls. it helps provide a custom
   stream to external world, for example, Sheet.stream.csv gives a text stream
   that contains csv formatted data. Book.stream.xls returns a xls format
   data in a byte stream.

Updated
********************************************************************************

#. Better error reporting when an unknown parameters or unsupported file types
   were given to the signature functions.


0.4.2 - 17.01.2017
--------------------------------------------------------------------------------

Updated
********************************************************************************

#. Raise exception if the incoming sheet does not have column names. In other
   words, only sheet with column names could be saved to database. sheet with
   row names cannot be saved. The alternative is to transpose the sheet, then
   name_columns_by_row and then save.
#. fix iget_records where a non-uniform content should be given,
   e.g. [["x", "y"], [1, 2], [3]], some record would become non-uniform, e.g.
   key 'y' would be missing from the second record.
#. `skip_empty_rows` is applicable when saving a python data structure to
   another data source. For example, if your array contains a row which is
   consisted of empty string, such as ['', '', '' ... ''], please specify
   `skip_empty_rows=False` in order to preserve it. This becomes subtle when
   you try save a python dictionary where empty rows is not easy to be spotted.
#. `#69  <https://github.com/pyexcel/pyexcel/issues/69>`_: better documentation
   for save_book_as.

0.4.1 - 23.12.2016
--------------------------------------------------------------------------------

Updated
********************************************************************************

#. `#68  <https://github.com/pyexcel/pyexcel/issues/68>`_: regression
   save_to_memory() should have returned a stream instance.


0.4.0 - 22.12.2016
--------------------------------------------------------------------------------

Added
********************************************************************************

#. `Flask-Excel issue 19 <https://github.com/pyexcel/Flask-Excel/issues/19>`_
   allow sheet_name parameter
#. `pyexcel-xls issue 11 <https://github.com/pyexcel/pyexcel-xls/issues/11>`_
   case-insensitive for file_type. `xls` and `XLS` are treated in the same way


Updated
********************************************************************************

#. `# 66 <https://github.com/pyexcel/pyexcel/issues/66>`_: `export_columns` is
   ignored
#. Update dependency on pyexcel-io v0.3.0


0.3.3 - 07.11.2016
--------------------------------------------------------------------------------

Updated
********************************************************************************

#. `# 63 <https://github.com/pyexcel/pyexcel/issues/63>`_: cannot display
   empty sheet(hence book with empty sheet) as texttable


0.3.2 - 02.11.2016
--------------------------------------------------------------------------------

Updated
********************************************************************************

#. `# 62 <https://github.com/pyexcel/pyexcel/issues/62>`_: optional module
   import error become visible.


0.3.0 - 28.10.2016
--------------------------------------------------------------------------------

.. _version_o_three:

Added:
********************************************************************************

#. file type setters for Sheet and Book, and its documentation
#. `iget_records` returns a generator for a list of records and should have
   better memory performance, especially dealing with large csv files.
#. `iget_array` returns a generator for a list of two dimensional array and
   should have better memory performance, especially dealing with large csv
   files.
#. Enable pagination support, and custom row renderer via pyexcel-io v0.2.3

Updated
********************************************************************************

#. Take `isave_as` out from `save_as`. Hence two functions are there for save
   a sheet as
#. `# 60 <https://github.com/pyexcel/pyexcel/issues/60>`_: encode 'utf-8' if
   the console is of ascii encoding.
#. `# 59 <https://github.com/pyexcel/pyexcel/issues/59>`_: custom row
   renderer
#. `# 56 <https://github.com/pyexcel/pyexcel/issues/56>`_: set cell value does
   not work
#. pyexcel.transpose becomes `pyexcel.sheets.transpose`
#. iterator functions of `pyexcel.Sheet` were converted to generator
   functions

   * `pyexcel.Sheet.enumerate()`
   * `pyexcel.Sheet.reverse()`
   * `pyexcel.Sheet.vertical()`
   * `pyexcel.Sheet.rvertical()`
   * `pyexcel.Sheet.rows()`
   * `pyexcel.Sheet.rrows()`
   * `pyexcel.Sheet.columns()`
   * `pyexcel.Sheet.rcolumns()`
   * `pyexcel.Sheet.named_rows()`
   * `pyexcel.Sheet.named_columns()`

#. `~pyexcel.Sheet.save_to_memory` and `~pyexcel.Book.save_to_memory`
   return the actual content. No longer they will return a io object hence
   you cannot call getvalue() on them.

Removed:
********************************************************************************

#. `content` and `out_file` as function parameters to the signature functions are
   no longer supported.
#. SourceFactory and RendererFactory are removed
#. The following methods are removed

   * `pyexcel.to_array`
   * `pyexcel.to_dict`
   * `pyexcel.utils.to_one_dimensional_array`
   * `pyexcel.dict_to_array`
   * `pyexcel.from_records`
   * `pyexcel.to_records`

#. `pyexcel.Sheet.filter` has been re-implemented and all filters were
   removed:

   * `pyexcel.filters.ColumnIndexFilter`
   * `pyexcel.filters.ColumnFilter`
   * `pyexcel.filters.RowFilter`
   * `pyexcel.filters.EvenColumnFilter`
   * `pyexcel.filters.OddColumnFilter`
   * `pyexcel.filters.EvenRowFilter`
   * `pyexcel.filters.OddRowFilter`
   * `pyexcel.filters.RowIndexFilter`
   * `pyexcel.filters.SingleColumnFilter`
   * `pyexcel.filters.RowValueFilter`
   * `pyexcel.filters.NamedRowValueFilter`
   * `pyexcel.filters.ColumnValueFilter`
   * `pyexcel.filters.NamedColumnValueFilter`
   * `pyexcel.filters.SingleRowFilter`

#. the following functions have been removed

   * `add_formatter`
   * `remove_formatter`
   * `clear_formatters`
   * `freeze_formatters`
   * `add_filter`
   * `remove_filter`
   * `clear_filters`
   * `freeze_formatters`

#. `pyexcel.Sheet.filter` has been re-implemented and all filters were
   removed:

   * pyexcel.formatters.SheetFormatter


0.2.5 - 31.08.2016
--------------------------------------------------------------------------------

Updated:
********************************************************************************

#. `# 58 <https://github.com/pyexcel/pyexcel/issues/58>`_: texttable should
   have been made as compulsory requirement


0.2.4 - 14.07.2016
--------------------------------------------------------------------------------

Updated:
********************************************************************************

#. For python 2, writing to sys.stdout by pyexcel-cli raise IOError.

0.2.3 - 11.07.2016
--------------------------------------------------------------------------------

Updated:
********************************************************************************

#. For python 3, do not seek 0 when saving to memory if sys.stdout is passed on.
   Hence, adding support for sys.stdin and sys.stdout.

0.2.2 - 01.06.2016
--------------------------------------------------------------------------------

Updated:
********************************************************************************

#. Explicit imports, no longer needed
#. Depends on latest setuptools 18.0.1
#. NotImplementedError will be raised if parameters to core functions are not supported, e.g. get_sheet(cannot_find_me_option="will be thrown out as NotImplementedError")

0.2.1 - 23.04.2016
--------------------------------------------------------------------------------

Added:
********************************************************************************

#. add pyexcel-text file types as attributes of pyexcel.Sheet and pyexcel.Book, related to `issue 31 <https://github.com/pyexcel/pyexcel/issues/31>`__
#. auto import pyexcel-text if it is pip installed

Updated:
********************************************************************************

#. code refactoring done for easy addition of sources.
#. bug fix `issue 29 <https://github.com/pyexcel/pyexcel/issues/29>`__, Even if the format is a string it is displayed as a float
#. pyexcel-text is no longer a plugin to pyexcel-io but to pyexcel.sources, see `pyexcel-text issue #22 <https://github.com/pyexcel/pyexcel-text/issues/22>`__

Removed:
********************************************************************************
#. pyexcel.presentation is removed. No longer the internal decorate @outsource is used. related to `issue 31 <https://github.com/pyexcel/pyexcel/issues/31>`_


0.2.0 - 17.01.2016
--------------------------------------------------------------------------------

Updated
********************************************************************************

#. adopt pyexcel-io yield key word to return generator as content
#. pyexcel.save_as and pyexcel.save_book_as get performance improvements


0.1.7 - 03.07.2015
--------------------------------------------------------------------------------

Added
********************************************************************************

#. Support pyramid-excel which does the database commit on its own.


0.1.6 - 13.06.2015
--------------------------------------------------------------------------------

Added
********************************************************************************

#. get excel data from a http url


0.0.13 - 07.02.2015
--------------------------------------------------------------------------------

Added
********************************************************************************

#. Support django
#. texttable as default renderer

0.0.12 - 25.01.2015
--------------------------------------------------------------------------------

Added
********************************************************************************

#. Added sqlalchemy support


0.0.10 - 15.12.2015
--------------------------------------------------------------------------------

Added
********************************************************************************

#. added csvz and tsvz format


0.0.4 - 12.10.2014
--------------------------------------------------------------------------------

Updated
********************************************************************************

#. Support python 3

0.0.1 - 14.09.2014
--------------------------------------------------------------------------------

Features:

#. read and write csv, ods, xls, xlsx and xlsm files(which are referred later
   as excel files)
#. various iterators for the reader
#. row and column filters for the reader
#. utilities to get array and dictionary out from excel files.
#. cookbok receipes for some common and simple usage of this library.



