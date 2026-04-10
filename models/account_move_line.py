from odoo import models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    def action_open_parent_move(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'res_id': self.move_id.id,
            'view_mode': 'form',
            'views': [(False, 'form')],
        }
