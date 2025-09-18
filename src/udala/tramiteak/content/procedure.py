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


class IProcedure(model.Schema):
    """Marker interface and Dexterity Python Schema for Tramite"""

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


alsoProvides(IProcedure["at_office"], ILanguageIndependentField)
alsoProvides(IProcedure["by_phone"], ILanguageIndependentField)


@implementer(IProcedure)
class Procedure(Container):
    """Content-type class for IProcedure"""
