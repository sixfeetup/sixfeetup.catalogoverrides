##############################################################################
#
# Copyright (c) 2005 Zope Corporation and Contributors. All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""ZCatalog export / import support.

$Id: exportimport.py 76398 2007-06-06 11:28:46Z jens $
"""

from Products.GenericSetup.ZCatalog.exportimport import ZCatalogXMLAdapter \
    as ZCatalogXMLAdapterBase


class ZCatalogXMLAdapter(ZCatalogXMLAdapterBase):
    """XML im- and exporter for ZCatalog.
    """
    
    def _importNode(self, node):
        """Change the import so that the columns aren't purged each time
        """
        if self.environ.shouldPurge():
            self._purgeProperties()
            self._purgeObjects()
            self._purgeIndexes()
            
            
        self._initProperties(node)
        self._initObjects(node)
        self._initIndexes(node)
        self._initColumns(node)
        
        self._logger.info('Catalog imported.')
    
    node = property(ZCatalogXMLAdapterBase._exportNode, _importNode)

