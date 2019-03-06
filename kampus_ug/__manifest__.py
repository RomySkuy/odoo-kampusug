{
    'name': 'Kampus UG',
    'version': '11.1.0',
    'author': 'PT Arkana',
    'license': 'OPL-1',
    'category': 'Tailor-Made',
    'website': 'http: //www.Arkana.co.id/',
    'summary': 'Custom-built Odoo',
    'description': '''
    ''',
    'depends': [
        # 'account', # python
        # 'sale', # python
    ],
    'data': [
         'views/kampus_siswa.xml',
         'views/kampus_dosen.xml',
         'views/kampus_fakultas.xml',
         'views/kampus_matkul.xml',
         'views/kampus_jurusan.xml',
    ],
    'qweb': [
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}