# -*- coding: utf-8 -*-
from plone.app.testing import setRoles, TEST_USER_ID
from sinar.project import _
from sinar.project.testing import SINAR_PROJECT_INTEGRATION_TESTING  # noqa
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory, IVocabularyTokenized

import unittest


class ProjectsIntegrationTest(unittest.TestCase):

    layer = SINAR_PROJECT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_vocab_projects(self):
        vocab_name = 'sinar.project.Projects'
        factory = getUtility(IVocabularyFactory, vocab_name)
        self.assertTrue(IVocabularyFactory.providedBy(factory))

        vocabulary = factory(self.portal)
        self.assertTrue(IVocabularyTokenized.providedBy(vocabulary))
        self.assertEqual(
            vocabulary.getTerm('sony-a7r-iii').title,
            _(u'Sony Aplha 7R III'),
        )
