# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from plone import api
from collective.relationhelpers import api


class ProjectsViewlet(ViewletBase):

    def projects(self):

        return api.relations(self.context,
                             attribute="projects")

    def index(self):
        return super(ProjectsViewlet, self).render()
