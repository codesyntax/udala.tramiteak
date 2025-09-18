from Products.Five.browser import BrowserView


class ProcedureView(BrowserView):

    def is_pdf(self, file):
        try:
            return file.file.contentType == "application/pdf"
        except AttributeError:
            return False
