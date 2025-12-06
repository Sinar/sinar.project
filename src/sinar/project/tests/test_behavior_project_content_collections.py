# -*- coding: utf-8 -*-
from sinar.project.behaviors.project_content_collections import IProjectContentCollectionsMarker
from sinar.project.testing import SINAR_PROJECT_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class ProjectContentCollectionsIntegrationTest(unittest.TestCase):

    layer = SINAR_PROJECT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_project_content_collections(self):
        behavior = getUtility(IBehavior, 'sinar.project.project_content_collections')
        self.assertEqual(
            behavior.marker,
            IProjectContentCollectionsMarker,
        )
