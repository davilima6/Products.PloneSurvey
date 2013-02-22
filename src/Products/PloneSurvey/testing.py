from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class ProductsplonesurveyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import Products.PloneSurvey
        xmlconfig.file(
            'configure.zcml',
            Products.PloneSurvey,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'Products.PloneSurvey:default')

PRODUCTS_PLONESURVEY_FIXTURE = ProductsplonesurveyLayer()
PRODUCTS_PLONESURVEY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PRODUCTS_PLONESURVEY_FIXTURE,),
    name="ProductsplonesurveyLayer:Integration"
)
PRODUCTS_PLONESURVEY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PRODUCTS_PLONESURVEY_FIXTURE, z2.ZSERVER_FIXTURE),
    name="ProductsplonesurveyLayer:Functional"
)
