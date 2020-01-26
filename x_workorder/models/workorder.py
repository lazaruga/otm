# -*- coding: utf-8 -*-

from odoo import api, fields, models

class workorder (model.Models):
	_name = "WorkOrders"
	id_workorder = fields.Char()
	date_workorder = fields.Date()
	project_ids = fields.one2many('project.project','workorder_id',)

class project.project (model.Models): 
	inherit = 'project.project'
	workorder_id = fields.many2one('workorder')
