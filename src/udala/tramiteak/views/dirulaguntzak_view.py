# -*- coding: utf-8 -*-

from DateTime import DateTime
from plone.app.contentlisting.interfaces import IContentListing
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface
from plone import api


class IDirulaguntzakView(Interface):
    """Marker Interface for IDirulaguntzakView"""


@implementer(IDirulaguntzakView)
class DirulaguntzakView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('dirulaguntzak_view.pt')

    def today(self):
        return DateTime().earliestTime()

    def contents(self):

        opened_contents = api.content.find(
            context=self.context,
            portal_type=["Dirulaguntza", "Link"],
            presentation_date={"query": self.today(), "range": "min"},
            sort_on="presentation_date",
            sort_order="asc",
            depth=1,
        )
        closed_contents = api.content.find(
            context=self.context,
            portal_type=["Dirulaguntza", "Link"],
            presentation_date={
                "query": (DateTime() - 1).latestTime(),
                "range": "max",
            },
            sort_on="justification_date",
            sort_order="asc",
            depth=1,
        )

        return IContentListing(opened_contents + closed_contents)
