from Acquisition import aq_inner
from plone import api
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ITramiteakView(Interface):
    """Marker Interface for ITramiteakView"""


@implementer(ITramiteakView)
class TramiteakView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('tramiteak_view.pt')

    def tramiteak(self):
        context = aq_inner(self.context)
        items = []
        folders = api.content.find(
            context=context,
            portal_type="Folder",
            sort_on="getObjPositionInParent",
            depth=1,
        )
        for de_brain in folders:
            de = de_brain.getObject()
            d = {}
            d["Title"] = de.Title()
            d["absolute_url"] = de.absolute_url()
            d["tramiteak"] = []
            tramiteak = api.content.find(
                context=de,
                portal_type="Tramitea",
                sort_on="getObjPositionInParent",
                depth=1,
            )
            for tr_brain in tramiteak:
                tr = tr_brain.getObject()
                d["tramiteak"].append(tr)

            items.append(d)
        return items
