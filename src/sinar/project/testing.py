# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import sinar.project


class SinarProjectLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=sinar.project)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'sinar.project:default')


SINAR_PROJECT_FIXTURE = SinarProjectLayer()


SINAR_PROJECT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SINAR_PROJECT_FIXTURE,),
    name='SinarProjectLayer:IntegrationTesting',
)


SINAR_PROJECT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SINAR_PROJECT_FIXTURE,),
    name='SinarProjectLayer:FunctionalTesting',
)


SINAR_PROJECT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SINAR_PROJECT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='SinarProjectLayer:AcceptanceTesting',
)
