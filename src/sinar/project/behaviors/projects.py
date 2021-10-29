# -*- coding: utf-8 -*-

from sinar.project import _
from plone import schema
from plone.app.z3cform.widget import RelatedItemsFieldWidget, SelectFieldWidget
from plone.autoform.interfaces import IFormFieldProvider
from plone.autoform import directives
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider
from plone.supermodel.directives import fieldset



class IProjectsMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IProjects(model.Schema):
    """
    """

    directives.widget(projects=SelectFieldWidget)
    projects = schema.List(
            title=u'Projects',
            description=u'Projects that this item is an output of',
            required=False,
            value_type=schema.Choice(
                vocabulary='sinar.project.Projects',
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
