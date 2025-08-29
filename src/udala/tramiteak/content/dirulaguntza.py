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


class IDirulaguntza(model.Schema):
    """Marker interface and Dexterity Python Schema for Tramite"""

    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    bulegoan = schema.Bool(
        title=_("Bulegoan"),
        description=_(
            "Active esta opcion si el tramite se puede realizar "
            "en la oficina de atención a la ciudadanía."
        ),
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
            "Active esta opcion si el tramite se puede realizar online y "
            "escriba la direccion en la que se puede realizar el tramite "
            "en la siguiente casilla."
        ),
        default=False,
        required=False,
    )

    url = schema.TextLine(
        title=_("Direccion web"),
        description=_(
            "Escriba la direccion en la que se puede realizar este tramite online. "
            "Dejelo vacio si el tramite no se puede realizar online"
        ),
        default="",
        required=False,
    )

    presentation_date = schema.Datetime(
        title=_("Ultimo dia de presentacion de solicitudes"),
        required=False,
    )

    justification_date = schema.Datetime(
        title=_("Ultimo dia de presentacion de justificaciones"),
        required=False,
    )

    justification_date_explanation = schema.TextLine(
        title=_("Explicacion del dia limite de presentacion de justificaciones"),
        description=_(
            "Rellenar solo cuando en una subvencion no tenemos un dia determinado "
            "de limite, sino otro tipo de plazos."
        ),
        required=False,
    )


alsoProvides(IDirulaguntza["bulegoan"], ILanguageIndependentField)
alsoProvides(IDirulaguntza["telefonoz"], ILanguageIndependentField)
alsoProvides(IDirulaguntza["online"], ILanguageIndependentField)
alsoProvides(IDirulaguntza["presentation_date"], ILanguageIndependentField)
alsoProvides(IDirulaguntza["justification_date"], ILanguageIndependentField)


@implementer(IDirulaguntza)
class Dirulaguntza(Container):
    """Content-type class for IDirulaguntza"""
