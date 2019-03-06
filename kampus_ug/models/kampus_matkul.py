from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KampusMatkul(models.Model):
    _name = 'kampus.matkul'

    name = fields.Char('Nama Mata Kuliah')

    siswa_id = fields.Many2one('kampus.siswa', 'Nama Siswa')
    
    siswa_ids = fields.One2many('kampus.siswa', 'kuliah_fav' , 'Siswa', ondelete='set null')

    siswa_many_ids = fields.Many2many(
        comodel_name='kampus.siswa',
        string='Mata Kuliah Terkait')

    @api.one
    @api.depends('siswa_many_ids')
    def hitung_siswa(self):
        total = len(self.siswa_many_ids)
        self.siswa_ikut = total
        return

    siswa_ikut = fields.Integer(compute=hitung_siswa, string='Siswa Terdaftar', store=True)
        
    