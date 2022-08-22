# -*- coding: utf-8 -*-

from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from sinar.project import _
from zope.component import adapter
from zope.interface import implementer, Interface, provider


class IProjectDatesMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IProjectDates(model.Schema):
    """
    """

    project_start_date = schema.Date(
        title=_(u'Project Start Date'),
        description=_(u'The date that the project started'),
        required=False,
    )

    project_end_date = schema.Date(
        title=_(u'Project End Date'),
        description=_(u'The date for which the project was completed.'),
        required=False,
    )



@implementer(IProjectDates)
@adapter(IProjectDatesMarker)
class ProjectDates(object):
    def __init__(self, context):
        self.context = context

    @property
    def project_start_date(self):
        if safe_hasattr(self.context, 'project_start_date'):
            return self.context.project_start_date
        return None

    @project_start_date.setter
    def project_start_date(self, value):
        self.context.project_start_date = value

    @property
    def project_end_date(self):
        if safe_hasattr(self.context, 'project_end_date'):
            return self.context.project_end_date
        return None

    @project_end_date.setter
    def project_end_date(self, value):
        self.context.project_end_date = value
