# -*- coding: utf-8 -*-
from plone.app.testing import setRoles, TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from sinar.project.behaviors.project_dates import IProjectDatesMarker
from sinar.project.testing import SINAR_PROJECT_INTEGRATION_TESTING  # noqa
from zope.component import getUtility

import unittest


class ProjectDatesIntegrationTest(unittest.TestCase):

    layer = SINAR_PROJECT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_project_dates(self):
        behavior = getUtility(IBehavior, 'sinar.project.project_dates')
        self.assertEqual(
            behavior.marker,
            IProjectDatesMarker,
        )
