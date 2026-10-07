# -*- coding: utf-8 -*-

from plone import api
from plone.app.layout.viewlets import ViewletBase


class ProjectsViewlet(ViewletBase):

    def projects(self):
        relations = api.relation.get(source=self.context,
                                     relationship="projects")
        return [relation.to_object for relation in relations]

    def index(self):
        return super(ProjectsViewlet, self).render()
