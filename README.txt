Introduction
============

This package fixes a bug with the importing of catalog indexes in
GenericSetup.  When an existing index is in the catalog.xml the index is not
removed.  If the index is new then it is added.

Add this package to your buildout and make sure the overrides.zcml gets loaded

[instance]
...
eggs = sixfeetup.catalogoverrides
zcml = sixfeetup.catalogoverrides-overrides

The pluginindexes.py code was written by Ross Patterson
