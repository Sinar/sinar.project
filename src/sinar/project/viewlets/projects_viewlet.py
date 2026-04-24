# -*- coding: utf-8 -*-

from plone import api
from plone.app.layout.viewlets import ViewletBase


class ProjectsViewlet(ViewletBase):

    def projects(self):

        return api.relations(self.context,
                             attribute="projects")

    def index(self):
        return super(ProjectsViewlet, self).render()
