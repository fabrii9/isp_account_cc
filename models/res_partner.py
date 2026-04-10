from odoo import models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def action_open_cuenta_corriente(self):
        self.ensure_one()
        return {
            'name': f'Cuenta Corriente - {self.name}',
            'type': 'ir.actions.act_window',
            'res_model': 'account.move.line',
            'view_mode': 'list,pivot,graph',
            'views': [
                (self.env.ref('isp_account_cc.view_cuenta_corriente_tree').id, 'list'),
                (False, 'pivot'),
                (False, 'graph'),
            ],
            'search_view_id': (self.env.ref('isp_account_cc.view_cuenta_corriente_search').id, ),
            'domain': [
                ('partner_id', '=', self.commercial_partner_id.id),
                ('account_id.account_type', '=', 'asset_receivable'),
                ('parent_state', '!=', 'cancel'),
            ],
            'context': {
                'search_default_sin_conciliar': 1,
                'search_default_publicado': 1,
                'default_partner_id': self.id,
            },
        }
