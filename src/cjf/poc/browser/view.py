from Products.Five.browser import BrowserView
# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.interfaces import IATFolder, IATDocument
# from plone.memoize.instance import memoize
# from DateTime import DateTime

# from bs4 import BeautifulSoup
# from zope.site.hooks import getSite
# from zope.component import queryUtility
# import logging
# from plone.i18n.normalizer.interfaces import IIDNormalizer
# from DateTime import DateTime
# from plone import api
# from Products.CMFPlone.utils import _createObjectByType
# from plone.app.layout.viewlets import ViewletBase
# from zope.site.hooks import getSite


class TesteView(BrowserView):
    """ view list news
    """
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.errors = {}
        self.url_sucess = self.context.absolute_url()
        self.utils = getToolByName(self.context, 'plone_utils')

    def getFolders(self):
        """Retorna o resultado de uma consulta no catalog.
        """
        catalog = getToolByName(self, 'portal_catalog')
        path = '/'.join(self.context.getPhysicalPath())
        folders = catalog(object_provides=IATFolder.__identifier__,
                          path={'query': path, 'depth': 1},
                          sort_on='getObjPositionInParent',
                          exclude_from_nav=False
                          )
        return folders

    def getFolderItens(self, path):
        """Retorna o resultado de uma consulta no catalog.
        """
        catalog = getToolByName(self, 'portal_catalog')
        folders = catalog(object_provides=[IATFolder.__identifier__, IATDocument.__identifier__],
                          path={'query': path, 'depth': 1},
                          sort_on='getObjPositionInParent',
                          exclude_from_nav=False
                          )
        return folders

    def getFolders_interna(self):
        """Retorna o resultado de uma consulta no catalog.
        """
        catalog = getToolByName(self, 'portal_catalog')
        path = '/'.join(self.context.getPhysicalPath())
        folders = catalog(object_provides=IATFolder.__identifier__,
                          path={'query': path, 'depth': 0},
                          sort_on='getObjPositionInParent',
                          exclude_from_nav=False
                          )
        return folders
