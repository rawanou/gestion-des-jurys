from odoo import models, fields

class Jury(models.Model):
    _name = 'gestion.jury'
    _description = 'Jury'

    name = fields.Char(string="Jury Name", required=True)
    session_date = fields.Date(string="Session Date")
    academic_year = fields.Char(string="Academic Year")
    state = fields.Selection(
        [('draft', 'Draft'), ('validated', 'Validated')],
        default='draft'
    )
