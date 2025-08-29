# from udala.Dirulaguntzak import _
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IDirulaguntzaView(Interface):
    """Marker Interface for IDirulaguntzaView"""


@implementer(IDirulaguntzaView)
class DirulaguntzaView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('Dirulaguntza_view.pt')

    def __call__(self):
        # Implement your own actions:
        return self.index()

    def files(self):
        # Why does not context.values('File') work?
        return [f for f in self.context.values() if f.portal_type == "File"]

    def is_pdf(self, file):
        return file.file.contentType == "application/pdf"
