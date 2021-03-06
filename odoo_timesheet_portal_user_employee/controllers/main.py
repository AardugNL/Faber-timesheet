# -*- coding: utf-8 -*-

from odoo import http, _
from odoo.http import request
from datetime import datetime, timedelta
# from odoo.addons.website_portal.controllers.main import website_account
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager

from odoo.exceptions import UserError
from odoo.osv.expression import OR

# class website_account(website_account):
class CustomerPortal(CustomerPortal):

#     @http.route()
#     def account(self, **kw):
#         response = super(website_account, self).account(**kw)
#         partner = request.env.user
#         timesheets = request.env['account.analytic.line']
#         timesheets_count = timesheets.sudo().search_count([
#         ('user_id', 'child_of', [request.env.user.id]),('project_id.portal_user_ids','child_of', [request.env.user.id])
#           ])
#         response.qcontext.update({
#         'timesheets_count': timesheets_count,
#         })
#         return response
    
    def _prepare_portal_layout_values(self):
        values = super(CustomerPortal, self)._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        timesheets = request.env['account.analytic.line']
        timesheets_count = timesheets.sudo().search_count([
        ('user_id', 'child_of', [request.env.user.id]),('project_id.portal_user_ids','child_of', [request.env.user.id])
          ])
        values.update({
        'timesheets_count': timesheets_count,
        })
        return values
    
    @http.route(['/my/timesheets', '/my/timesheets/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_timesheet(self, page=1, sortby=None, search=None, search_in='description',**kw):
        if not request.env.user.has_group('odoo_timesheet_portal_user_employee.analytic_line_portal'):
            return request.render("odoo_timesheet_portal_user_employee.not_allowed")
        response = super(CustomerPortal, self)
        values = self._prepare_portal_layout_values()
        timesheets_obj = http.request.env['account.analytic.line']
        domain = [
            ('user_id', 'child_of', [request.env.user.id]),('project_id.portal_user_ids','child_of', [request.env.user.id])
        ]
        # count for pager
        timesheets_count = http.request.env['account.analytic.line'].sudo().search_count(domain)
        # pager
        pager = request.website.pager(
            url="/my/timesheets",
            total=timesheets_count,
            page=page,
            step=self._items_per_page
        )
        sortings = {
            'date': {'label': _('Newest'), 'order': 'date desc'},
            'project': {'label': _('Project'), 'order': 'project_id'},
        }

        searchbar_inputs = {
            
            'name': {'input': 'name', 'label': _('Search in Description')},
            'date': {'input': 'date', 'label': _('Search in Date')},
            }

        # search
        if search and search_in:
            search_domain = []
            if search_in in ('name'):
                search_domain = OR([search_domain, [('name', '=', search)]])
            if search_in in ('date'):
                search_domain = OR([search_domain, [('date', '=', search)]])
            domain += search_domain
            
        if not sortby:
            sortby = 'date'
        order = sortings[sortby]['order']
        # order = sortings.get(sortby, sortings['date'])['order']
        
        # content according to pager and archive selected
        timesheets = timesheets_obj.sudo().search(domain, order=order, limit=self._items_per_page, offset=pager['offset'])
        values.update({
            'timesheets': timesheets,
            'page_name': 'employee_timesheets',
            'searchbar_sortings' : sortings,
            'sortby': sortby,
            'search_in': search_in,
            'pager': pager,
            'searchbar_inputs' : searchbar_inputs,
            'default_url': '/my/timesheets',

        })
        return request.render("odoo_timesheet_portal_user_employee.display_timesheets", values)
    
    @http.route(['/my/add_timesheet'], type='http', auth="user", website=True)
    def portal_add_timesheet(self, page=1, date_begin=None, date_end=None, project=False, task=False, **kw):
        if not request.env.user.has_group('odoo_timesheet_portal_user_employee.analytic_line_portal'):
            return request.render("odoo_timesheet_portal_user_employee.not_allowed")
        project_ids = request.env['project.project'].sudo().search([('portal_user_ids','child_of', [request.env.user.id]),('is_close', '=', False)])
        task_ids = request.env['project.task'].sudo().search([('portal_user_ids','child_of', [request.env.user.id]),('stage_id.is_close', '=', False)])
        values={
            'project_ids': project_ids,
            'projects':project,
            'task_ids':task_ids,
            'tasks': task,
            'page_name': 'new_timesheet',
            'add_new_timesheet': True,
        }
        return request.render("odoo_timesheet_portal_user_employee.add_new_timesheet", values)
    
    @http.route(['/my/create_new_timesheet'], type='http', auth="user", website=True)
    def create_new_timesheet(self, **kwargs):
        if not request.env.user.has_group('odoo_timesheet_portal_user_employee.analytic_line_portal') or not kwargs:
            return request.render("odoo_timesheet_portal_user_employee.not_allowed")
        valse ={
            'user_id': request.env.user.id
        }
        if kwargs.get('project_id'):
            valse.update({'project_id': int(kwargs.get('project_id'))})
        if kwargs.get('task_id'):
            valse.update({'task_id': int(kwargs.get('task_id'))})
        if kwargs.get('description'):
            valse.update({'name': kwargs.get('description')})
        if kwargs.get('quantity'):
            quantity_str = str(kwargs.get('quantity'))
            try:
                date_tt = datetime.strptime(quantity_str,'%H:%M') - datetime.strptime(str('0:0'),'%H:%M')
            except:
                return request.render("odoo_timesheet_portal_user_employee.hour_usererror_msg")
            quantity = date_tt.total_seconds()/3600.00
            valse.update({'unit_amount': quantity})
        if kwargs.get('start_date'):
            date = datetime.strptime(kwargs.get('start_date'), "%Y-%m-%d")
            valse.update({'date': date.date()})
        request.env['account.analytic.line'].sudo().create(valse)
        return request.render("odoo_timesheet_portal_user_employee.user_thanks")


    @http.route(['/my/timesheet/<int:timesheet>'], type='http', auth="user", website=True)
    def edit_timesheet(self, timesheet=None, **kw):
        if not request.env.user.has_group('odoo_timesheet_portal_user_employee.analytic_line_portal'):
            return request.render("odoo_timesheet_portal_user_employee.not_allowed")
        analytic_line = request.env['account.analytic.line'].sudo().browse([timesheet])
        line_date = datetime.strptime(str(analytic_line.date), "%Y-%m-%d").strftime('%Y-%m-%d')
        values={
            'line': analytic_line,
            'line_date': line_date,
        }
        
        return request.render("odoo_timesheet_portal_user_employee.edit_timesheet", values)

    @http.route(['/my/update_timesheet'], type='http', auth="user", website=True)
    def update_timesheet(self, **kwargs):
        if not request.env.user.has_group('odoo_timesheet_portal_user_employee.analytic_line_portal') or not kwargs:
            return request.render("odoo_timesheet_portal_user_employee.not_allowed")
        valse = {}
        if kwargs.get('project_id'):
            valse.update({'project_id': int(kwargs.get('project_id'))})
        if kwargs.get('task_id'):
            valse.update({'task_id': int(kwargs.get('task_id'))})
        if kwargs.get('description'):
            valse.update({'name': kwargs.get('description')})
        if kwargs.get('quantity'):
            quantity_str = str(kwargs.get('quantity'))
            try:
                date_tt = datetime.strptime(quantity_str,'%H:%M') - datetime.strptime(str('0:0'),'%H:%M')
            except:
                return request.render("odoo_timesheet_portal_user_employee.hour_usererror_msg")
            quantity = date_tt.total_seconds()/3600.00
            valse.update({'unit_amount': quantity})
        if kwargs.get('date'):
            date = datetime.strptime(kwargs.get('date'), "%Y-%m-%d")
            valse.update({'date': date})
        if kwargs.get('line_id'):
            line_id = request.env['account.analytic.line'].sudo().browse(int(kwargs.get('line_id')))
        if line_id:
            line_id.write(valse)
            return request.render("odoo_timesheet_portal_user_employee.update_successfully")

    @http.route(['/my/timesheet/delete/<int:timesheet>'], type='http', auth="user", website=True)
    def delete_timesheet(self, timesheet=None, **kw):
        analytic_line = request.env['account.analytic.line'].browse([timesheet])
        try:
            analytic_line.sudo().unlink()
        except:
            return request.render("odoo_timesheet_portal_user_employee.not_allowed")
        return request.render("odoo_timesheet_portal_user_employee.delet_successfully")

