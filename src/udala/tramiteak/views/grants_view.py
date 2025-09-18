from DateTime import DateTime
from plone import api
from plone.app.contentlisting.interfaces import IContentListing
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


class GrantsView(BrowserView):

    def today(self):
        return DateTime().earliestTime()

    def contents(self):
        opened_contents = api.content.find(
            context=self.context,
            portal_type=["Grant"],
            presentation_date={"query": self.today(), "range": "min"},
            sort_on="presentation_date",
            sort_order="asc",
            depth=1,
        )
        closed_contents = api.content.find(
            context=self.context,
            portal_type=["Grant"],
            presentation_date={
                "query": (DateTime() - 1).latestTime(),
                "range": "max",
            },
            sort_on="justification_date",
            sort_order="asc",
            depth=1,
        )

        return IContentListing(opened_contents + closed_contents)
