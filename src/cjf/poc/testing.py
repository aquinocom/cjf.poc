# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import cjf.poc


class CjfPocLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=cjf.poc)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cjf.poc:default')


CJF_POC_FIXTURE = CjfPocLayer()


CJF_POC_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CJF_POC_FIXTURE,),
    name='CjfPocLayer:IntegrationTesting'
)


CJF_POC_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CJF_POC_FIXTURE,),
    name='CjfPocLayer:FunctionalTesting'
)


CJF_POC_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        CJF_POC_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CjfPocLayer:AcceptanceTesting'
)
