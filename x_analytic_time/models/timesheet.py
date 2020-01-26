# -*- coding: utf-8 -*-

from odoo import api, fields, models

class analytic_line (models.Model): 
	_inherit = 'account.analytic.line'
	datetime_start = fields.Datetime()
	datetime_end = fields.Datetime()
	unit_amount = fields.Integer(store=True)

	@api.multi
	@api.onchange('datetime_end')
	def calculate_duration (self):
		self.unit_amount = self.datetime_end - self.datetime_start

	
	
