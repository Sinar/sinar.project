# -*- coding: utf-8 -*-

from sinar.project import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider
from z3c.relationfield.schema import RelationChoice
from plone.app.vocabularies.catalog import CatalogSource


class IProjectContentCollectionsMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IProjectContentCollections(model.Schema):
    """
    """

    project_updates_collection = RelationChoice(
        title=_("Project Updates Collection"),
        description=_(
            "Select the collection to show project updates."
        ),
        required=False,
        source=CatalogSource(portal_type='Collection'),
    )

    project_events_collection = RelationChoice(
        title=_("Project Events Collection"),
        description=_(
            "Select the collection to show project events."
        ),
        required=False,
        source=CatalogSource(portal_type='Collection'),
    )
        
    project_resources_collection = RelationChoice(
        title=_("Project Resources Collection"),
        description=_(
            "Select the collection to show project resourcess."
        ),
        required=False,
        source=CatalogSource(portal_type='Collection'),
    )


@implementer(IProjectContentCollections)
@adapter(IProjectContentCollectionsMarker)
class ProjectContentCollections(object):
    def __init__(self, context):
        self.context = context

    @property
    def project_updates_collection(self):
        if safe_hasattr(self.context, 'project_updates_collection'):
            return self.context.project_updates_collection
        return None

    @project_updates_collection.setter
    def project_updates_collection(self, value):
        self.context.project_updates_collection = value

    @property
    def project_events_collection(self):
        if safe_hasattr(self.context, 'project_events_collection'):
            return self.context.project_events_collection
        return None

    @project_events_collection.setter
    def project_events_collection(self, value):
        self.context.project_events_collection = value

    @property
    def project_resources_collection(self):
        if safe_hasattr(self.context, 'project_resources_collection'):
            return self.context.project_resources_collection
        return None

    @project_resources_collection.setter
    def project_resources_collection(self, value):
        self.context.project_resources_collection = value
