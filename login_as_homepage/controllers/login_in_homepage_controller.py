from odoo import http
from odoo.http import request

class WebsiteLoginAsHome(http.Controller):

    @http.route('/', type='http', auth='public', website=True)
    def home_redirect_to_login(self, **kw):
        return request.redirect('/web/login')
