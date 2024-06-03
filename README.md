International Standard Content Code (ISCC) for PRC
=========================
python-irodsclient-iscc is a plugin for the
[Python iRODS Client - PRC](https://github.com/irods/python-irodsclient).
This plugin adds basic ISCC ([ISO 24138](https://www.iso.org/standard/77899.html))
support for iRODS data objects through the [ISCC Core Python Library](https://github.com/iscc/iscc-core).

python-irodsclient-iscc adds ISCC codes and algorithms to
an iRODS data object by instantiating a 
iRODSDataObjectISCC object from the given object.

More info: https://core.iscc.codes/

Possible applications:

 - content deduplication
 - integrity verification
 - versioning

At this time, only Python 3.7.2 or higher is supported.

Installation
----------
Clone this repo, create a virtual environment and install the plugin and its
dependencies

```bash
git clone git@github.com:ll4strw/python-irodsclient-iscc.git
python3 -m venv iscc-test
source iscc-test/bin/activate
python3 -m pip install -e python-irodsclient-iscc/
```

Examples
----------
Display ISCC code of a data object

```python
>>>d=session.data_objects.get('/testZone/home/test/f32be.h5')
>>> d
<iRODSDataObject 10033 h5ex_d_gzip.h5>
>>> d=iRODSDataObjectISCC(d)
>>> d.iscc
<IsccObj KYCOQ2R7P4T4PBPIB4HPYKZ6D5FDXL2FMGZILTOIWI iRODSDataObjectISCC 10033>
>>> d.iscc.core.explain
'ISCC-NONE-V0-MDI-e86a3f7f27c785e80f0efc2b3e1f4a3baf4561b285cdc8b2'

```
Note that the meta unit of the calculated ISCC includes all iRODS metadata
associated to the data object.

Should you want to decompose an ISCC into its units (at this time only
META, DATA, INSTANCE)

```python
>>> a,b,c=d.iscc.decompose()
>>> a.explain
'META-NONE-V0-64-e86a3f7f27c785e8'
>>> b.explain
'DATA-NONE-V0-64-0f0efc2b3e1f4a3b'
>>> c.explain
'INSTANCE-NONE-V0-64-af4561b285cdc8b2'
```

Comparing two data objects using ISCC similarity distances is also possible

```python
>>> d1=session.data_objects.get('/testZone/home/test/h5ex_d_gzip.h5')
>>> d1=iRODSDataObjectISCC(d1)

>>> d2=session.data_objects.get('/testZone/home/test/f32be.h5')
>>> d1.iscc.compare(d2) 
{'meta_dist': 30, 'data_dist': 32, 'instance_match': False}
```

