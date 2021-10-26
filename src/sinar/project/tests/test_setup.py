# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID
from sinar.project.testing import SINAR_PROJECT_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that sinar.project is properly installed."""

    layer = SINAR_PROJECT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if sinar.project is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'sinar.project'))

    def test_browserlayer(self):
        """Test that ISinarProjectLayer is registered."""
        from sinar.project.interfaces import (
            ISinarProjectLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ISinarProjectLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = SINAR_PROJECT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['sinar.project'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if sinar.project is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'sinar.project'))

    def test_browserlayer_removed(self):
        """Test that ISinarProjectLayer is removed."""
        from sinar.project.interfaces import \
            ISinarProjectLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ISinarProjectLayer,
            utils.registered_layers())
