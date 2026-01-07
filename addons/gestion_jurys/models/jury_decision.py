from odoo import models, fields

class JuryDecision(models.Model):
    _name = 'gestion.jury.decision'
    _description = 'Décision du Jury'

    name = fields.Char(string="Référence", required=True)
    jury_id = fields.Many2one(
        'gestion.jury',
        string="Jury",
        required=True,
        ondelete='cascade'
    )
    decision = fields.Selection(
        [
            ('admis', 'Admis'),
            ('ajourne', 'Ajourné'),
            ('refuse', 'Refusé'),
        ],
        string="Décision",
        required=True
    )
    commentaire = fields.Text(string="Commentaire")
