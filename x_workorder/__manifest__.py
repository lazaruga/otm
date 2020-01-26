# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Work Order',
    'category': 'Sales',
    'summary': 'Es el organizador principal del taller',
    'website': 'https://www.talleresmutilva.es',
    'version': '1.0',
    'description': """
	Utilizamos este modulo para poder gestionar la venta de taller, a la vez de integrar las compras

        """,
    'depends': ['sale.order'],
    'data': [
        'views/workorder_views.xml'
    ],
    'installable': True,}