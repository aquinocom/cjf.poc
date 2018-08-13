# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from cjf.poc.testing import CJF_POC_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that cjf.poc is properly installed."""

    layer = CJF_POC_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if cjf.poc is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'cjf.poc'))

    def test_browserlayer(self):
        """Test that ICjfPocLayer is registered."""
        from cjf.poc.interfaces import (
            ICjfPocLayer)
        from plone.browserlayer import utils
        self.assertIn(ICjfPocLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = CJF_POC_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['cjf.poc'])

    def test_product_uninstalled(self):
        """Test if cjf.poc is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'cjf.poc'))

    def test_browserlayer_removed(self):
        """Test that ICjfPocLayer is removed."""
        from cjf.poc.interfaces import \
            ICjfPocLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICjfPocLayer, utils.registered_layers())
