from odoo import api, fields, models

class LibraryBook(models.Model): 
    _name = 'Library.book'

    name = fields.char(string='Book Title', required=True)
    author = fields.char(string='Book Author')
    year = fields.interger(string='Published Year')
    isbn = fields.char(string='ISBN')
    description = fields.Text(string='Book Description')
    status = fields.selection([
        ('available ','Available'),
         ('boorowed', 'Borrowed'),
         ('lost', 'Lost'),
    ], string='Book Status', default='available' )