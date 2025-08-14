# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
# from plone.autoform import directives
from udala.tramiteak import _
from plone.app.multilingual.dx.interfaces import ILanguageIndependentField
from plone.dexterity.content import Container

# from plone.namedfile import field as namedfile
from plone.supermodel import model

# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import alsoProvides
from zope.interface import implementer


class ITramitea(model.Schema):
    """Marker interface and Dexterity Python Schema for Tramite"""

    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    bulegoan = schema.Bool(
        title=_("Bulegoan"),
        description=_("Active esta opcion si el tramite se puede realizar en la oficina de atención a la ciudadanía."),
        default=False,
        required=False,
    )

    telefonoz = schema.Bool(
        title=_("Por telefono"),
        description=_(
            "Active esta opcion si el tramite se puede realizar por telefono"
        ),
        default=False,
        required=False,
    )

    online = schema.Bool(
        title=_("Online"),
        description=_(
            "Active esta opcion si el tramite se puede realizar online y escriba la direccion en la que se puede realizar el tramite en la siguiente casilla."
        ),
        default=False,
        required=False,
    )

    url = schema.TextLine(
        title=_("Direccion web"),
        description=_(
            "Escriba la direccion en la que se puede realizar este tramite online. Dejelo vacio si el tramite no se puede realizar online"
        ),
        default="",
        required=False,
    )



alsoProvides(ITramitea["bulegoan"], ILanguageIndependentField)
alsoProvides(ITramitea["telefonoz"], ILanguageIndependentField)
alsoProvides(ITramitea["online"], ILanguageIndependentField)


@implementer(ITramitea)
class Tramitea(Container):
    """ Content-type class for ITramitea
    """
