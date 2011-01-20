"""Catalog index node adapters that only clear the index when
needed.

This is a silly workaround for this issue:
https://bugs.launchpad.net/zope-cmf/+bug/161682
"""

from Products.GenericSetup.PluginIndexes.exportimport import PluggableIndexNodeAdapter as PluggableIndexBase
from Products.GenericSetup.PluginIndexes.exportimport import DateIndexNodeAdapter as DateIndexBase
from Products.GenericSetup.PluginIndexes.exportimport import DateRangeIndexNodeAdapter as DateRangeIndexBase
from Products.GenericSetup.PluginIndexes.exportimport import FilteredSetNodeAdapter as FilteredSetBase

class PluggableIndexNodeAdapter(PluggableIndexBase):
    """Only clear the index when needed."""

    def _importNode(self, node):
        """Import the object from the DOM node.
        """
        indexed_attrs = []
        for child in node.childNodes:
            if child.nodeName == 'indexed_attr':
                indexed_attrs.append(
                                  child.getAttribute('value').encode('utf-8'))
        if getattr(self.context, 'indexed_attrs', None) != indexed_attrs:
            self.context.indexed_attrs = indexed_attrs
            self.context.clear()

    node = property(PluggableIndexBase._exportNode, _importNode)

class DateIndexNodeAdapter(DateIndexBase):
    """Only clear the index when needed."""

    def _importNode(self, node):
        """Import the object from the DOM node.
        """
        if self.environ.shouldPurge():
            self._purgeProperties()
        # XXX: The only thing we have changed here is that we do
        #      NOT clear the index after creating it
        self._initProperties(node)

    node = property(DateIndexBase._exportNode, _importNode)

class DateRangeIndexNodeAdapter(DateRangeIndexBase):
    """Only clear the index when needed."""

    def _importNode(self, node):
        """Import the object from the DOM node.
        """
        since_field = node.getAttribute('since_field').encode('utf-8')
        until_field = node.getAttribute('until_field').encode('utf-8')
        if (self.context.getSinceField() != since_field or
            self.context.getUntilField() != until_field):
            self.context._edit(since_field, until_field)
            self.context.clear()

    node = property(DateRangeIndexBase._exportNode, _importNode)

class FilteredSetNodeAdapter(FilteredSetBase):
    """Only clear the index when needed."""

    def _importNode(self, node):
        """Import the object from the DOM node.
        """
        expr = node.getAttribute('expression').encode('utf-8')
        if self.context.getExpression() != expr:
            self.context.setExpression(expr)
            self.context.clear()

    node = property(FilteredSetBase._exportNode, _importNode)
