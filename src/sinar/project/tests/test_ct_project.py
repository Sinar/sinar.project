# -*- coding: utf-8 -*-
from sinar.project.content.project import IProject  # NOQA E501
from sinar.project.testing import SINAR_PROJECT_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class ProjectIntegrationTest(unittest.TestCase):

    layer = SINAR_PROJECT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_project_schema(self):
        fti = queryUtility(IDexterityFTI, name='Project')
        schema = fti.lookupSchema()
        self.assertEqual(IProject, schema)

    def test_ct_project_fti(self):
        fti = queryUtility(IDexterityFTI, name='Project')
        self.assertTrue(fti)

    def test_ct_project_factory(self):
        fti = queryUtility(IDexterityFTI, name='Project')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IProject.providedBy(obj),
            u'IProject not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_project_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Project',
            id='project',
        )

        self.assertTrue(
            IProject.providedBy(obj),
            u'IProject not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('project', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('project', parent.objectIds())

    def test_ct_project_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Project')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_project_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Project')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'project_id',
            title='Project container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
