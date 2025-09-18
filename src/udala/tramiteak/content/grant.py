# from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.app.multilingual.dx.interfaces import ILanguageIndependentField
from plone.dexterity.content import Container

# from plone.namedfile import field as namedfile
from plone.supermodel import model
from udala.tramiteak import _

# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import alsoProvides
from zope.interface import implementer


class IGrant(model.Schema):
    """Marker interface and Dexterity Python Schema for Tramite"""

    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    at_office = schema.Bool(
        title=_("At the office"),
        description=_("If enabled, this procedure can be done at the citizen's office"),
        default=False,
        required=False,
    )

    by_phone = schema.Bool(
        title=_("By phone"),
        description=_("If enabled, this procedure can be done by phone"),
        default=False,
        required=False,
    )

    online_url = schema.TextLine(
        title=_("Direccion web"),
        description=_(
            "If a URL is entered there, this procedure can be done online. "
            "This URL will be linked from the procedure page."
        ),
        default="",
        required=False,
    )

    presentation_date = schema.Datetime(
        title=_("Last day to request the grant"),
        required=False,
    )

    justification_date = schema.Datetime(
        title=_("Last day to present the justification documents"),
        required=False,
    )

    justification_date_explanation = schema.TextLine(
        title=_("Explanation of the last day to present the justification documents"),
        description=_(
            "Fill only when the justification period does not end in a given day "
            "but in other kind of period (ex. XX days after finalizing the activity)"
        ),
        required=False,
    )


alsoProvides(IGrant["at_office"], ILanguageIndependentField)
alsoProvides(IGrant["by_phone"], ILanguageIndependentField)
alsoProvides(IGrant["presentation_date"], ILanguageIndependentField)
alsoProvides(IGrant["justification_date"], ILanguageIndependentField)


@implementer(IGrant)
class Grant(Container):
    """Content-type class for IGrant"""
