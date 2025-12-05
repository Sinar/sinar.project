# -*- coding: utf-8 -*-

from plone.dexterity.browser.view import DefaultView
from plone import api
from collective.relationhelpers import api
from operator import attrgetter
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from sinar.project import _


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ProjectView(DefaultView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('project_view.pt')

    def __call__(self):
        # Implement your own actions:
        return super(ProjectView, self).__call__()

    def activity_status(self,title):

        factory = getUtility(IVocabularyFactory,
                             'sinar.activity.ActivityStatus')

        vocabulary = factory(self)
        term = vocabulary.getTerm(title)
        return term.title

    def activity_type(self, title):

        factory = getUtility(IVocabularyFactory,
                             'sinar.activity.ActivityTypes')

        vocabulary = factory(self)

        term = vocabulary.getTerm(title)
        return term.title


    def related_items(self, portal_type, relation):
        """Get related content"""
        items = []
        for item in api.backrelations(self.context, attribute=relation):
            if item is not None and item.portal_type == portal_type:
                items.append(item)
        return items

    def updates(self):

        items = []
        for item in api.backrelations(self.context, attribute="projects"):
            if item is not None and item.portal_type == "News Item":
                items.append(item)
            elif item is not None and item.portal_type == "Article":
                items.append(item)

        sorted_items = sorted(items, key=lambda obj: obj.effective(),
                              reverse=True)

        return sorted_items

    def events(self):
        items = self.related_items("Activity", "projects")

        sorted_items = sorted(items, key=lambda obj: obj.start,
                              reverse=True)

        return sorted_items


    def activities(self):
        items = self.related_items("ProjectActivity", "projects")

        sorted_items = sorted(items, key=lambda obj: obj.effective(),
                              reverse=True)

        return sorted_items

    def resources(self):
        items = self.related_items("Resource", "output_of")

        sorted_items = sorted(items, key=lambda obj: obj.effective(),
                              reverse=True)

        return sorted_items
