=====
Fiona
=====

Fiona is OGR's neat, nimble, no-nonsense API for Python programmers.

.. image:: https://travis-ci.org/Toblerity/Fiona.png?branch=master   
   :target: https://travis-ci.org/Toblerity/Fiona

.. image:: https://coveralls.io/repos/Toblerity/Fiona/badge.png
   :target: https://coveralls.io/r/Toblerity/Fiona

Fiona is designed to be simple and dependable. It focuses on reading and
writing data in standard Python IO style and relies upon familiar Python types
and protocols such as files, dictionaries, mappings, and iterators instead of
classes specific to OGR. Fiona can read and write real-world data using
multi-layered GIS formats and zipped virtual file systems and integrates
readily with other Python GIS packages such as pyproj_, Rtree_, and Shapely_.

For more details, see:

* Fiona `home page <https://github.com/Toblerity/Fiona>`__
* Fiona `docs and manual <http://toblerity.github.com/fiona/>`__
* Fiona `examples <https://github.com/Toblerity/Fiona/tree/master/examples>`__

Usage
=====

Collections
-----------

Records are read from and written to ``file``-like `Collection` objects
returned from the ``fiona.open()`` function.  Records are mappings modeled on
the GeoJSON format. They don't have any spatial methods of their own, so if you
want to do anything fancy with them you will probably need Shapely or something
like it. Here is an example of using Fiona to read some records from one data
file, change their geometry attributes, and write them to a new data file.

.. code-block:: python

    import fiona

    # Register format drivers with a context manager

    with fiona.drivers():

        # Open a file for reading. We'll call this the "source."

        with fiona.open('tests/data/coutwildrnp.shp') as source:

            # The file we'll write to, the "sink", must be initialized
            # with a coordinate system, a format driver name, and
            # a record schema.  We can get initial values from the open
            # collection's ``meta`` property and then modify them as
            # desired.

            meta = source.meta
            meta['schema']['geometry'] = 'Point'

            # Open an output file, using the same format driver and
            # coordinate reference system as the source. The ``meta``
            # mapping fills in the keyword parameters of fiona.open().

            with fiona.open('test_write.shp', 'w', **meta) as sink:

                # Process only the records intersecting a box.
                for f in source.filter(bbox=(-107.0, 37.0, -105.0, 39.0)):

                    # Get a point on the boundary of the record's
                    # geometry.

                    f['geometry'] = {
                        'type': 'Point',
                        'coordinates': f['geometry']['coordinates'][0][0]}

                    # Write the record out.

                    sink.write(f)

        # The sink's contents are flushed to disk and the file is
        # closed when its ``with`` block ends. This effectively
        # executes ``sink.flush(); sink.close()``.

    # At the end of the ``with fiona.drivers()`` block, context
    # manager exits and all drivers are de-registered.

The fiona.drivers() function and context manager are new in 1.1. The
example above shows the way to use it to register and de-register
drivers in a deterministic and efficient way. Code written for Fiona 1.0
will continue to work: opened collections may manage the global driver
registry if no other manager is present.

Reading Multilayer data
-----------------------

Collections can also be made from single layers within multilayer files or
directories of data. The target layer is specified by name or by its integer
index within the file or directory. The ``fiona.listlayers()`` function
provides an index ordered list of layer names.

.. code-block:: python

    with fiona.drivers():

        for layername in fiona.listlayers('tests/data'):
            with fiona.open('tests/data', layer=layername) as src:
                print(layername, len(src))

    # Output:
    # (u'coutwildrnp', 67)

Layer can also be specified by index. In this case, ``layer=0`` and
``layer='test_uk'`` specify the same layer in the data file or directory.

.. code-block:: python

    with fiona.drivers():

        for i, layername in enumerate(fiona.listlayers('tests/data')):
            with fiona.open('tests/data', layer=i) as src:
                print(i, layername, len(src))

    # Output:
    # (0, u'coutwildrnp', 67)

Writing Multilayer data
-----------------------

Multilayer data can be written as well. Layers must be specified by name when
writing.

.. code-block:: python

    with fiona.drivers():

        with open('tests/data/cowildrnp.shp') as src:
            meta = src.meta
            f = next(src)

        with fiona.open('/tmp/foo', 'w', layer='bar', **meta) as dst:
            dst.write(f)

        print(fiona.listlayers('/tmp/foo'))

        with fiona.open('/tmp/foo', layer='bar') as src:
            print(len(src))
            f = next(src)
            print(f['geometry']['type'])
            print(f['properties'])

        # Output:
        # [u'bar']
        # 1
        # Polygon
        # OrderedDict([(u'PERIMETER', 1.22107), (u'FEATURE2', None), (u'NAME', u'Mount Naomi Wilderness'), (u'FEATURE1', u'Wilderness'), (u'URL', u'http://www.wilderness.net/index.cfm?fuse=NWPS&sec=wildView&wname=Mount%20Naomi'), (u'AGBUR', u'FS'), (u'AREA', 0.0179264), (u'STATE_FIPS', u'49'), (u'WILDRNP020', 332), (u'STATE', u'UT')])

A view of the /tmp/foo directory will confirm the creation of the new files.

.. code-block:: console

    $ ls /tmp/foo
    bar.cpg bar.dbf bar.prj bar.shp bar.shx

Collections from archives and virtual file systems
--------------------------------------------------

Zip and Tar archives can be treated as virtual filesystems and Collections can
be made from paths and layers within them. In other words, Fiona lets you read
and write zipped Shapefiles.

.. code-block:: python

    with fiona.drivers():

        for i, layername in enumerate(
                fiona.listlayers(
                    '/', 
                    vfs='zip://tests/data/coutwildrnp.zip')):
            with fiona.open(
                    '/', 
                    vfs='zip://tests/data/coutwildrnp.zip', 
                    layer=i) as src:
                print(i, layername, len(src))

    # Output:
    # (0, u'coutwildrnp', 67)

Fiona CLI
=========

Fiona's command line interface, named "fio", is documented at `docs/cli.rst
<https://github.com/Toblerity/Fiona/blob/master/docs/cli.rst>`__. Its ``fio
info`` pretty prints information about a data file.

.. code-block:: console

    $ fio info --indent 2 tests/data/coutwildrnp.shp
    {
      "count": 67,
      "crs": "EPSG:4326",
      "driver": "ESRI Shapefile",
      "bounds": [
        -113.56424713134766,
        37.0689811706543,
        -104.97087097167969,
        41.99627685546875
      ],
      "schema": {
        "geometry": "Polygon",
        "properties": {
          "PERIMETER": "float:24.15",
          "FEATURE2": "str:80",
          "NAME": "str:80",
          "FEATURE1": "str:80",
          "URL": "str:101",
          "AGBUR": "str:80",
          "AREA": "float:24.15",
          "STATE_FIPS": "str:80",
          "WILDRNP020": "int:10",
          "STATE": "str:80"
        }
      }
    }

Installation
============

Fiona requires Python 2.6, 2.7, 3.3, or 3.4 and GDAL/OGR 1.8+. To build from
a source distribution you will need a C compiler and GDAL and Python
development headers and libraries (libgdal1-dev for Debian/Ubuntu, gdal-dev for
CentOS/Fedora).

To build from a repository copy, you will also need Cython to build C sources
from the project's .pyx files. See the project's requirements-dev.txt file for
guidance.

The `Kyngchaos GDAL frameworks
<http://www.kyngchaos.com/software/frameworks#gdal_complete>`__ will satisfy
the GDAL/OGR dependency for OS X, as will Homebrew's GDAL Formula (``brew install
gdal``).

Python Requirements
-------------------

Fiona depends on the modules ``six``, ``cligj``,  ``munch``, ``argparse``, and
``ordereddict`` (the two latter modules are standard in Python 2.7+). Pip will
fetch these requirements for you, but users installing Fiona from a Windows
installer must get them separately.

Unix-like systems
-----------------

Assuming you're using a virtualenv (if not, skip to the 4th command) and
GDAL/OGR libraries, headers, and `gdal-config`_ program are installed to well
known locations on your system via your system's package manager (``brew
install gdal`` using Homebrew on OS X), installation is this simple.

.. code-block:: console

  $ mkdir fiona_env
  $ virtualenv fiona_env
  $ source fiona_env/bin/activate
  (fiona_env)$ pip install fiona

If gdal-config is not available or if GDAL/OGR headers and libs aren't
installed to a well known location, you must set include dirs, library dirs,
and libraries options via the setup.cfg file or setup command line as shown
below (using ``git``). You must also specify the major version of the GDAL API
(1 or 2) on the setup command line.

.. code-block:: console

  (fiona_env)$ git clone git://github.com/Toblerity/Fiona.git
  (fiona_env)$ cd Fiona
  (fiona_env)$ python setup.py build_ext -I/path/to/gdal/include -L/path/to/gdal/lib -lgdal install --gdalversion 1

Or specify that build options and GDAL API version should be provided by a
particular gdal-config program.

.. code-block:: console

  (fiona_env)$ GDAL_CONFIG=/path/to/gdal-config pip install fiona

Windows
-------

Binary installers are available at
http://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona and coming eventually to PyPI.

You can download a binary distribution of GDAL from `here
<http://www.gisinternals.com/release.php>`_.  You will also need to download
the compiled libraries and headers (include files).

When building from source on Windows, it is important to know that setup.py
cannot rely on gdal-config, which is only present on UNIX systems, to discover 
the locations of header files and libraries that Fiona needs to compile its 
C extensions. On Windows, these paths need to be provided by the user. 
You will need to find the include files and the library files for gdal and 
use setup.py as follows. You must also specify the major version of the GDAL
API (1 or 2) on the setup command line.

.. code-block:: console

    $ python setup.py build_ext -I<path to gdal include files> -lgdal_i -L<path to gdal library> install --gdalversion 1

Note: The GDAL dll (gdal111.dll) and gdal-data directory need to be in your 
Windows PATH otherwise Fiona will fail to work.

Development and testing
=======================

Building from the source requires Cython. Tests require Nose. If the GDAL/OGR
libraries, headers, and `gdal-config`_ program are installed to well known
locations on your system (via your system's package manager), you can do this::

  (fiona_env)$ git clone git://github.com/Toblerity/Fiona.git
  (fiona_env)$ cd Fiona
  (fiona_env)$ pip install cython
  (fiona_env)$ pip install -e .[test]
  (fiona_env)$ nosetests

Or you can use the ``pep-518-install`` script::

  (fiona_env)$ git clone git://github.com/Toblerity/Fiona.git
  (fiona_env)$ cd Fiona
  (fiona_env)$ ./pep-518-install

If you have a non-standard environment, you'll need to specify the include and
lib dirs and GDAL library on the command line::

  (fiona_env)$ python setup.py build_ext -I/path/to/gdal/include -L/path/to/gdal/lib -lgdal --gdalversion 2 develop
  (fiona_env)$ nosetests

.. _OGR: http://www.gdal.org/ogr
.. _pyproj: http://pypi.python.org/pypi/pyproj/
.. _Rtree: http://pypi.python.org/pypi/Rtree/
.. _Shapely: http://pypi.python.org/pypi/Shapely/
.. _gdal-config: http://www.gdal.org/gdal-config.html

Changes
=======

All issue numbers are relative to https://github.com/Toblerity/Fiona/issues.

1.7.9.post1 (2017-08-21)
------------------------

This release introduces no changes in the Fiona package. It upgrades GDAL
from 2.2.0 to 2.2.1 in wheels that we publish to the Python Package Index.

1.7.9 (2017-08-17)
------------------

Bug fixes:

- Acquire the GIL for GDAL error callback functions to prevent crashes when
  GDAL errors occur when the GIL has been released by user code.
- Sync and flush layers when closing even when the number of features is not
  precisely known (#467).

1.7.8 (2017-06-20)
------------------

Bug fixes:

- Provide all arguments needed by CPLError based exceptions (#456).

1.7.7 (2017-06-05)
------------------

Bug fixes:

- Switch logger `warn()` (deprecated) calls to `warning()`.
- Replace all relative imports and cimports in Cython modules with absolute
  imports (#450).
- Avoid setting `PROJ_LIB` to a non-existent directory (#439).

1.7.6 (2017-04-26)
------------------

Bug fixes:

- Fall back to `share/proj` for PROJ_LIB (#440).
- Replace every call to `OSRDestroySpatialReference()` with `OSRRelease()`,
  fixing the GPKG driver crasher reported in #441 (#443).
- Add a `DriverIOError` derived from `IOError` to use for driver-specific
  errors such as the GeoJSON driver's refusal to overwrite existing files.
  Also we now ensure that when this error is raised by `fiona.open()` any
  created read or write session is deleted, this eliminates spurious 
  exceptions on teardown of broken `Collection` objects (#437, #444).

1.7.5 (2017-03-20)
------------------

Bug fixes:

- Opening a data file in read (the default) mode with `fiona.open()` using the
  the `driver` or `drivers` keyword arguments (to specify certain format 
  drivers) would sometimes cause a crash on Windows due to improperly
  terminated lists of strings (#428). The fix: Fiona's buggy `string_list()`
  has been replaced by GDAL's `CSLAddString()`.

1.7.4 (2017-02-20)
------------------

Bug fixes:

- OGR's EsriJSON detection fails when certain keys aren't found in the first
  6000 bytes of data passed to `BytesCollection` (#422). A .json file extension
  is now explicitly given to the in-memory file behind `BytesCollection` when
  the `driver='GeoJSON'` keyword argument is given (#423). 

1.7.3 (2017-02-14)
------------------

Roses are red.
Tan is a pug.
Software regression's
the most embarrassing bug.

Bug fixes:

- Use __stdcall for GDAL error handling callback on Windows as in Rasterio.
- Turn on latent support for zip:// URLs in rio-cat and rio-info (#421).
- The 1.7.2 release broke support for zip files with absolute paths (#418).
  This regression has been fixed with tests to confirm.

1.7.2 (2017-01-27)
------------------

Future Deprecation:

- `Collection.__next__()` is buggy in that it can lead to duplication of 
  features when used in combination with `Collection.filter()` or
  `Collection.__iter__()`. It will be removed in Fiona 2.0. Please check for
  usage of this deprecated feature by running your tests or programs with
  `PYTHONWARNINGS="always:::fiona"` or `-W"always:::fiona"` and switch from
  `next(collection)` to `next(iter(collection))` (#301).

Bug fix:

- Zipped streams of bytes can be accessed by `BytesCollection` (#318).

1.7.1.post1 (2016-12-23)
------------------------
- New binary wheels using version 1.2.0 of sgillies/frs-wheel-builds. See
  https://github.com/sgillies/frs-wheel-builds/blob/master/CHANGES.txt.

1.7.1 (2016-11-16)
------------------

Bug Fixes:

- Prevent Fiona from stumbling over 'Z', 'M', and 'ZM' geometry types
  introduced in GDAL 2.1 (#384). Fiona 1.7.1 doesn't add explicit support for
  these types, they are coerced to geometry types 1-7 ('Point', 'LineString',
  etc.)
- Raise an `UnsupportedGeometryTypeError` when a bogus or unsupported 
  geometry type is encountered in a new collection's schema or elsewhere
  (#340).
- Enable `--precision 0` for fio-cat (#370).
- Prevent datetime exceptions from unnecessarily stopping collection iteration
  by yielding `None` (#385)
- Replace log.warn calls with log.warning calls (#379).
- Print an error message if neither gdal-config or `--gdalversion` indicate
  a GDAL C API version when running `setup.py` (#364).
- Let dict-like subclasses through CRS type checks (#367).

1.7.0post2 (2016-06-15)
-----------------------

Packaging: define extension modules for 'clean' and 'config' targets (#363).

1.7.0post1 (2016-06-15)
-----------------------

Packaging: No files are copied for the 'clean' setup target (#361, #362).

1.7.0 (2016-06-14)
------------------

The C extension modules in this library can now be built and used with either
a 1.x or 2.x release of the GDAL library. Big thanks to René Buffat for
leading this effort.

Refactoring:

- The `ogrext1.pyx` and `ogrext2.pyx` files now use separate
  C APIs defined in `ogrext1.pxd` and `ogrex2.pxd`. The other extension
  modules have been refactored so that they do not depend on either of these
  modules and use subsets of the GDAL/OGR API compatible with both GDAL 1.x and
  2.x (#359).

Packaging:

- Source distributions now contain two different sources for the
  `ogrext` extension module. The `ogrext1.c` file will be used with GDAL 1.x
  and the `ogrext2.c` file will be used with GDAL 2.x.

1.7b2 (2016-06-13)
------------------

- New feature: enhancement of the `--layer` option for fio-cat and fio-dump
  to allow separate layers of one or more multi-layer input files to be
  selected (#349).

1.7b1 (2016-06-10)
------------------

- New feature: support for GDAL version 2+ (#259).
- New feature: a new fio-calc CLI command (#273).
- New feature: `--layer` options for fio-info (#316) and fio-load (#299).
- New feature: a `--no-parse` option for fio-collect that lets a careful user
  avoid extra JSON serialization and deserialization (#306).
- Bug fix: `+wktext` is now preserved when serializing CRS from WKT to PROJ.4
  dicts (#352).
- Bug fix: a small memory leak when opening a collection has been fixed (#337).
- Bug fix: internal unicode errors now result in a log message and a 
  `UnicodeError` exception, not a `TypeError` (#356).

1.6.4 (2016-05-06)
------------------
- Raise ImportError if the active GDAL library version is >= 2.0 instead of
  failing unpredictably (#338, #341). Support for GDAL>=2.0 is coming in
  Fiona 1.7.

1.6.3.post1 (2016-03-27)
------------------------
- No changes to the library in this post-release version, but there is a
  significant change to the distributions on PyPI: to help make Fiona more
  compatible with Shapely on OS X, the GDAL shared library included in the
  macosx (only) binary wheels now statically links the GEOS library. See
  https://github.com/sgillies/frs-wheel-builds/issues/5.

1.6.3 (2015-12-22)
------------------
- Daytime has been decreasing in the Northern Hemisphere, but is now
  increasing again as it should.
- Non-UTF strings were being passed into OGR functions in some situations
  and on Windows this would sometimes crash a Python process (#303). Fiona
  now raises errors derived from UnicodeError when field names or field
  values can't be encoded.

1.6.2 (2015-09-22)
------------------
- Providing only PROJ4 representations in the dataset meta property resulted in
  loss of CRS information when using the `fiona.open(..., **src.meta) as dst`
  pattern (#265). This bug has been addressed by adding a crs_wkt item to the`
  meta property and extending the `fiona.open()` and the collection constructor
  to look for and prioritize this keyword argument.

1.6.1 (2015-08-12)
------------------
- Bug fix: Fiona now deserializes JSON-encoded string properties provided by
  the OGR GeoJSON driver (#244, #245, #246).
- Bug fix: proj4 data was not copied properly into binary distributions due to
  a typo (#254).

Special thanks to WFMU DJ Liz Berg for the awesome playlist that's fueling my
release sprint. Check it out at http://wfmu.org/playlists/shows/62083. You
can't unhear Love Coffin.

1.6.0 (2015-07-21)
------------------
- Upgrade Cython requirement to 0.22 (#214).
- New BytesCollection class (#215).
- Add GDAL's OpenFileGDB driver to registered drivers (#221).
- Implement CLI commands as plugins (#228).
- Raise click.abort instead of calling sys.exit, preventing suprising exits
  (#236).

1.5.1 (2015-03-19)
------------------
- Restore test data to sdists by fixing MANIFEST.in (#216).

1.5.0 (2015-02-02)
------------------
- Finalize GeoJSON feature sequence options (#174).
- Fix for reading of datasets that don't support feature counting (#190).
- New test dataset (#188).
- Fix for encoding error (#191).
- Remove confusing warning (#195).
- Add data files for binary wheels (#196).
- Add control over drivers enabled when reading datasets (#203).
- Use cligj for CLI options involving GeoJSON (#204).
- Fix fio-info --bounds help (#206).

1.4.8 (2014-11-02)
------------------
- Add missing crs_wkt property as in Rasterio (#182).

1.4.7 (2014-10-28)
------------------
- Fix setting of CRS from EPSG codes (#149).

1.4.6 (2014-10-21)
------------------
- Handle 3D coordinates in bounds() #178.

1.4.5 (2014-10-18)
------------------
- Add --bbox option to fio-cat (#163).
- Skip geopackage tests if run from an sdist (#167).
- Add fio-bounds and fio-distrib.
- Restore fio-dump to working order.

1.4.4 (2014-10-13)
------------------
- Fix accidental requirement on GDAL 1.11 introduced in 1.4.3 (#164).

1.4.3 (2014-10-10)
------------------
- Add support for geopackage format (#160).
- Add -f and --format aliases for --driver in CLI (#162).
- Add --version option and env command to CLI.

1.4.2 (2014-10-03)
------------------
- --dst-crs and --src-crs options for fio cat and collect (#159).

1.4.1 (2014-09-30)
------------------
- Fix encoding bug in collection's __getitem__ (#153).

1.4.0 (2014-09-22)
------------------
- Add fio cat and fio collect commands (#150).
- Return of Python 2.6 compatibility (#148).
- Improved CRS support (#149).

1.3.0 (2014-09-17)
------------------
- Add single metadata item accessors to fio inf (#142).
- Move fio to setuptools entry point (#142).
- Add fio dump and load commands (#143).
- Remove fio translate command.

1.2.0 (2014-09-02)
------------------
- Always show property width and precision in schema (#123).
- Write datetime properties of features (#125).
- Reset spatial filtering in filter() (#129).
- Accept datetime.date objects as feature properties (#130).
- Add slicing to collection iterators (#132).
- Add geometry object masks to collection iterators (#136).
- Change source layout to match Shapely and Rasterio (#138).

1.1.6 (2014-07-23)
------------------
- Implement Collection __getitem__() (#112).
- Leave GDAL finalization to the DLL's destructor (#113).
- Add Collection keys(), values(), items(), __contains__() (#114).
- CRS bug fix (#116).
- Add fio CLI program.

1.1.5 (2014-05-21)
------------------
- Addition of cpl_errs context manager (#108).
- Check for NULLs with '==' test instead of 'is' (#109).
- Open auxiliary files with encoding='utf-8' in setup for Python 3 (#110).

1.1.4 (2014-04-03)
------------------
- Convert 'long' in schemas to 'int' (#101).
- Carefully map Python schema to the possibly munged internal schema (#105).
- Allow writing of features with geometry: None (#71).

1.1.3 (2014-03-23)
------------------
- Always register all GDAL and OGR drivers when entering the DriverManager
  context (#80, #92).
- Skip unsupported field types with a warning (#91).
- Allow OGR config options to be passed to fiona.drivers() (#90, #93).
- Add a bounds() function (#100).
- Turn on GPX driver.

1.1.2 (2014-02-14)
------------------
- Remove collection slice left in dumpgj (#88).

1.1.1 (2014-02-02)
------------------
- Add an interactive file inspector like the one in rasterio.
- CRS to_string bug fix (#83).

1.1 (2014-01-22)
----------------
- Use a context manager to manage drivers (#78), a backwards compatible but
  big change. Fiona is now compatible with rasterio and plays better with the
  osgeo package.

1.0.3 (2014-01-21)
------------------
- Fix serialization of +init projections (#69).

1.0.2 (2013-09-09)
------------------
- Smarter, better test setup (#65, #66, #67).
- Add type='Feature' to records read from a Collection (#68).
- Skip geometry validation when using GeoJSON driver (#61).
- Dumpgj file description reports record properties as a list (as in
  dict.items()) instead of a dict.

1.0.1 (2013-08-16)
------------------
- Allow ordering of written fields and preservation of field order when
  reading (#57).

1.0 (2013-07-30)
-----------------
- Add prop_type() function.
- Allow UTF-8 encoded paths for Python 2 (#51). For Python 3, paths must
  always be str, never bytes.
- Remove encoding from collection.meta, it's a file creation option only.
- Support for linking GDAL frameworks (#54).

0.16.1 (2013-07-02)
-------------------
- Add listlayers, open, prop_width to __init__py:__all__.
- Reset reading of OGR layer whenever we ask for a collection iterator (#49).

0.16 (2013-06-24)
-----------------
- Add support for writing layers to multi-layer files.
- Add tests to reach 100% Python code coverage.

0.15 (2013-06-06)
-----------------
- Get and set numeric field widths (#42).
- Add support for multi-layer data sources (#17).
- Add support for zip and tar virtual filesystems (#45).
- Add listlayers() function.
- Add GeoJSON to list of supported formats (#47).
- Allow selection of layers by index or name.

0.14 (2013-05-04)
-----------------
- Add option to add JSON-LD in the dumpgj program.
- Compare values to six.string_types in Collection constructor.
- Add encoding to Collection.meta.
- Document dumpgj in README.

0.13 (2013-04-30)
-----------------
- Python 2/3 compatibility in a single package. Pythons 2.6, 2.7, 3.3 now supported.

0.12.1 (2013-04-16)
-------------------
- Fix messed up linking of README in sdist (#39).

0.12 (2013-04-15)
-----------------
- Fix broken installation of extension modules (#35).
- Log CPL errors at their matching Python log levels.
- Use upper case for encoding names within OGR, lower case in Python.

0.11 (2013-04-14)
-----------------
- Cythonize .pyx files (#34).
- Work with or around OGR's internal recoding of record data (#35).
- Fix bug in serialization of int/float PROJ.4 params.

0.10 (2013-03-23)
-----------------
- Add function to get the width of str type properties.
- Handle validation and schema representation of 3D geometry types (#29).
- Return {'geometry': None} in the case of a NULL geometry (#31).

0.9.1 (2013-03-07)
------------------
- Silence the logger in ogrext.so (can be overridden).
- Allow user specification of record field encoding (like 'Windows-1252' for
  Natural Earth shapefiles) to help when OGR can't detect it.

0.9 (2013-03-06)
----------------
- Accessing file metadata (crs, schema, bounds) on never inspected closed files
  returns None without exceptions.
- Add a dict of supported_drivers and their supported modes.
- Raise ValueError for unsupported drivers and modes.
- Remove asserts from ogrext.pyx.
- Add validate_record method to collections.
- Add helpful coordinate system functions to fiona.crs.
- Promote use of fiona.open over fiona.collection.
- Handle Shapefile's mix of LineString/Polygon and multis (#18).
- Allow users to specify width of shapefile text fields (#20).

0.8 (2012-02-21)
----------------
- Replaced .opened attribute with .closed (product of collection() is always
  opened). Also a __del__() which will close a Collection, but still not to be
  depended upon.
- Added writerecords method.
- Added a record buffer and better counting of records in a collection.
- Manage one iterator per collection/session.
- Added a read-only bounds property.

0.7 (2012-01-29)
----------------
- Initial timezone-naive support for date, time, and datetime fields. Don't use
  these field types if you can avoid them. RFC 3339 datetimes in a string field
  are much better.

0.6.2 (2012-01-10)
------------------
- Diagnose and set the driver property of collection in read mode.
- Fail if collection paths are not to files. Multi-collection workspaces are
  a (maybe) TODO.

0.6.1 (2012-01-06)
------------------
- Handle the case of undefined crs for disk collections.

0.6 (2012-01-05)
----------------
- Support for collection coordinate reference systems based on Proj4.
- Redirect OGR warnings and errors to the Fiona log.
- Assert that pointers returned from the ograpi functions are not NULL before
  using.

0.5 (2011-12-19)
----------------
- Support for reading and writing collections of any geometry type.
- Feature and Geometry classes replaced by mappings (dicts).
- Removal of Workspace class.

0.2 (2011-09-16)
----------------
- Rename WorldMill to Fiona.

0.1.1 (2008-12-04)
------------------
- Support for features with no geometry.


Credits
=======

Fiona is written by:

- Sean Gillies <sean.gillies@gmail.com>
- Rene Buffat <buffat@gmail.com>
- Kevin Wurster <wursterk@gmail.com>
- Micah Cochran <micah@micahcochran.net>
- Matthew Perry <perrygeo@gmail.com>
- Joshua Arnott <josh@snorfalorpagus.net>
- Kelsey Jordahl <kjordahl@enthought.com>
- Patrick Young <patrick.mckendree.young@gmail.com>
- Simon Norris <snorris@hillcrestgeo.ca>
- Hannes Gräuler <graeuler@geoplex.de>
- Johan Van de Wauw <johan.vandewauw@gmail.com>
- Jacob Wasserman <jwasserman@gmail.com>
- Ryan Grout <rgrout@continuum.io>
- Michael Weisman <mweisman@gmail.com>
- fredj <frederic.junod@camptocamp.com>
- Bas Couwenberg <sebastic@xs4all.nl>
- Brendan Ward <bcward@consbio.org>
- Michele Citterio <michele@citterio.net>
- Miro Hrončok <miro@hroncok.cz>
- qinfeng <guo.qinfeng+github@gmail.com>
- Michael Weisman <michael@urbanmapping.com>
- Brandon Liu <bdon@bdon.org>
- Ludovic Delauné <ludotux@gmail.com>
- Martijn Visser <mgvisser@gmail.com>
- Ariel Nunez <ingenieroariel@gmail.com>
- Oliver Tonnhofer <olt@bogosoft.com>
- Stefano Costa <steko@iosa.it>
- dimlev <dimlev@gmail.com>
- wilsaj <wilson.andrew.j+github@gmail.com>
- Jesse Crocker <jesse@gaiagps.com>

Fiona would not be possible without the great work of Frank Warmerdam and other
GDAL/OGR developers.

Some portions of this work were supported by a grant (for Pleiades_) from the
U.S. National Endowment for the Humanities (http://www.neh.gov).

.. _Pleiades: http://pleiades.stoa.org


