from odoo import models, fields , api

class ResUsers(models.Model):
	_inherit = 'res.users'
	
	portal_employee_timesheet = fields.Boolean(string='Portal Employee Timesheet' ,copy = True, default= False)

	@api.multi
	def write(self, vals):
		res = super(ResUsers, self).write(vals)
		if 'portal_employee_timesheet' in vals:
			group = self.env.ref('odoo_timesheet_portal_user_employee.analytic_line_portal')
			for rec in self:
				if vals['portal_employee_timesheet'] == True:
					group.sudo().write({'users': [(4, rec.id)]})
				else:
					group.sudo().write({'users': [(3, rec.id)]})
		return res