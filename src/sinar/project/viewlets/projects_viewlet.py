# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from plone import api
from plone.app.uuid.utils import uuidToObject


class ProjectsViewlet(ViewletBase):

    def projects(self):

        objects = []
        projects = self.context.projects
        if projects:
            for project in projects:
                obj = uuidToObject(project)
                objects.append(obj)
        return objects

    def index(self):
        return super(ProjectsViewlet, self).render()
