from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KampusJurusan(models.Model):
    _name = 'kampus.jurusan'

    name = fields.Char('Jurusan')
    name_id = fields.Char('Kode')