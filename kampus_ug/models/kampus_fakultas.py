from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KampusFakultas(models.Model):
    _name = 'kampus.fakultas'
    _rec_name = 'name_fakultas'

    name_fakultas = fields.Char('Nama Fakultas')
    name_jurusan = fields.Char('Nama Jurusan')

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class (models.Model):
    _new = ''
    _inherit = ''

    name = fields.Char(string='Name')

price_subtotal = fields.Float(compute='_compute_subtotal', string='Subtotal', store=False)

@api.multi
def _compute_subtotal(self):
    for session_doc in self:
        session_amount_total = sum(session_doc.payment_carfix_ids.mapped('amount_total'))
        session_doc.session_amount_total = session_amount_total
        import ipdb; ipdb.set_trace()
        abc = 3
        self.price_subtotal = 4
