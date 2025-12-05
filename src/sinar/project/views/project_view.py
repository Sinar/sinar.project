# -*- coding: utf-8 -*-

from plone.dexterity.browser.view import DefaultView
from plone import api
from collective.relationhelpers import api
from operator import attrgetter
from sinar.project import _


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ProjectView(DefaultView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('project_view.pt')

    def __call__(self):
        # Implement your own actions:
        return super(ProjectView, self).__call__()

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
        items = self.related_items("Project Event", "output_of")

        sorted_items = sorted(items, key=lambda obj: obj.effective(),
                              reverse=True)

        return sorted_items


    def activities(self):
        items = self.related_items("Project Activity", "output_of")

        sorted_items = sorted(items, key=lambda obj: obj.effective(),
                              reverse=True)

        return sorted_items

    def resources(self):
        items = self.related_items("Resource", "output_of")

        sorted_items = sorted(items, key=lambda obj: obj.effective(),
                              reverse=True)

        return sorted_items
