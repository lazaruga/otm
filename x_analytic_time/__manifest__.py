# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Analytic Time Control',
    'category': 'Sales',
    'summary': 'Ampliamos el modulo de analytic lines con la gestion del tiempo',
    'website': 'https://www.talleresmutilva.es',
    'version': '1.0',
    'description': """
	Ampliamos las lineas analiticas para poder calcular el tiempo dedicado a cada tarea/proyecto

        """,
    'depends': ['hr_timesheet','project','analytic','account','sale_timesheet'],
    'data': [
        'views/timesheet_views.xml'
    ],
    'installable': True,
}