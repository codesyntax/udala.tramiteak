# from udala.tramiteak import _
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ITramiteaView(Interface):
    """Marker Interface for ITramiteaView"""


@implementer(ITramiteaView)
class TramiteaView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('tramitea_view.pt')

    def __call__(self):
        # Implement your own actions:
        return self.index()

    def files(self):
        # Why does not context.values('File') work?
        return [f for f in self.context.values() if f.portal_type == "File"]

    def is_pdf(self, file):
        return file.file.contentType == "application/pdf"
