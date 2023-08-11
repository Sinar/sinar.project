# -*- coding: utf-8 -*-

from plone import schema
from plone.app.z3cform.widget import RelatedItemsFieldWidget, SelectFieldWidget
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from Products.CMFPlone.utils import safe_hasattr
from sinar.project import _
from zope.component import adapter
from zope.interface import implementer, Interface, provider
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from plone.app.vocabularies.catalog import CatalogSource
from collective import dexteritytextindexer


class IProjectsMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IProjects(model.Schema):
    """
    """

    # donors
    dexteritytextindexer.searchable('projects')
    directives.widget('projects',
                      RelatedItemsFieldWidget,
                      pattern_options={
                          'basePath': '/',
                          'mode': 'auto',
                          'favourites': [],
                      }
                      )

    projects = RelationList(
        title=u'Related Projects',
        description=u'''
                     Projects that this item is an output or outcome off
                     ''',
        required=False,
        value_type=RelationChoice(
            source=CatalogSource(portal_type='Project'),
        ),
    )


@implementer(IProjects)
@adapter(IProjectsMarker)
class Projects(object):
    def __init__(self, context):
        self.context = context

    @property
    def projects(self):
        if safe_hasattr(self.context, 'projects'):
            return self.context.projects
        return None

    @projects.setter
    def projects(self, value):
        self.context.projects = value
