from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class KampusSiswa(models.Model):
    _name = 'kampus.siswa'

    name = fields.Char('Name')
    no_induk = fields.Char('Nomor Induk')
    alamat = fields.Text('Alamat')
    telp = fields.Char('Telepon')
    tanggal_lahir = fields.Date('Tanggal Lahir')

    state = fields.Selection([
        ('lulus', 'Lulus'),
        ('tl', 'Tidak Lulus'),
        ('do', 'Drop Out'),
        ('perfect', 'Perfect'),
    ], string='Keterangan')    

    status = fields.Selection([
            ('draft', 'Enable'),
            ('open', 'Disable'),
        ], string='Status')

    kuliah_fav = fields.Many2one('kampus.matkul', 'Kuliah Favorit')
    
    fakultas_id = fields.Many2one('kampus.fakultas', 'Fakultas' )

    jurusan_ids = fields.One2many('kampus.jurusan', 'name', 'Nama Jurusan')


    
    
    
    