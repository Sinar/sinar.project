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

    # We define resource types we consider as "updates or news item"
    # Update cards will only show these, while Reseources will filter
    # them out to avoid deuplication

    # This removes the need for separate "News Item" and "Article"
    # types. All are Resources with different resource_type values.

    update_types = ["pressstatement", "newsmedia", "updates"]

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

        items = self.related_items("Resource", "projects")

        updates = [item for item in items if item.resource_type in
                   self.update_types]

        sorted_items = sorted(updates, key=lambda obj: obj.effective(),
                              reverse=True)

        return sorted_items[:3]

    def events(self):
        items = self.related_items("Activity", "projects")

        sorted_items = sorted(items, key=lambda obj: obj.start,
                              reverse=True)

        return sorted_items[:3]


    def activities(self):
        items = self.related_items("ProjectActivity", "projects")

        sorted_items = sorted(items, key=lambda obj: obj.effective(),
                              reverse=True)

        return sorted_items

    def resources(self):
        items = self.related_items("Resource", "projects")

        filtered_items = [item for item in items if item.resource_type not in
                          self.update_types]

        sorted_items = sorted(filtered_items, key=lambda obj: obj.effective(),
                              reverse=True)

        return sorted_items[:5]
