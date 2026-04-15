from Products.Five.browser import BrowserView


class GrantView(BrowserView):
    def is_pdf(self, file):
        return file.file.contentType == "application/pdf"
