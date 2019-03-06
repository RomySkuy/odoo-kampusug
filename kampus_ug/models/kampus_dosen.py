from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KampusDosen(models.Model):
    _name = 'kampus.dosen'

    name = fields.Char('Nama Dosen')
    alamat = fields.Text('Alamat')
    waktu = fields.Selection([
            ('pagi', '10.00'),
            ('siang', '13.00'),
            ('sore', '16.00'),
            ('malam', '21.00'),
        ], string='Waktu Mengajar')

    kuliah_ids = fields.Many2many(
        comodel_name='kampus.matkul',
        string='Mata Kuliah Terkait',
        )

    jumlah_kuliah = fields.Integer(string='Jumlah Kuliah')

    # Perhatian nama recompute sudah digunakan Odoo
    @api.one
    def hitung_kuliah(self):
        abc = len(self.kuliah_ids)
        self.jumlah_kuliah = abc



        
    
    