{
    'name': 'Cuenta Corriente de Clientes',
    'version': '19.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Botón de Cuenta Corriente en contactos con vista interactiva de movimientos',
    'author': 'BellavistaSat',
    'license': 'LGPL-3',
    'depends': ['om_account_followup'],
    'data': [
        'views/partner_views.xml',
        'views/account_move_line_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
