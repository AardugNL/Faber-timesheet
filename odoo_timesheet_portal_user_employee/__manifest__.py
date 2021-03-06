# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': 'Timesheet Entry from Web-My Account using Portal User as Employee',
    'version': '2.4',
    'price': 99.0,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'category': 'Human Resources',
    'summary':  """This module allow you to employee who are not real users of system but portal users and it will allow to record timesheets.""",
    'description': """

Odoo Timesheet Portal User Employee
Timesheet Portal User
Odoo Timesheets
Your Timesheets
My Timesheets
Project Timesheet
User Timesheets
Employee Timesheets
Portal user Timesheets
portal timesheet
website timesheet
enterprise user timesheet
enterprise timesheet user
enterprise employee timesheet
enterprise timesheet employee
timesheet for enterprise user
timesheet for enterprise employee
timesheet recording
timesheet entry for enterprise
timesheet entry employee enterprise
enterprise paid users
enterprise free users
enterprise employee user
enterprise user employee
timesheet user fill
timesheet employee fill
enterprise timesheet encoding
timesheet fill
enterprise timesheet
hr timesheet
hr timesheet enterprise employee
hr timesheet enterprise user
enterprise fill timesheet activities
timesheet activities
timesheet lines enterprise user
timesheet lines enterprise employee
timesheet work enterprise user
timesheet work user
timesheet work employee enterprise
portal timesheet enterprise
portal timesheet
website timesheet
timesheet data
timesheet import
timesheet export
odoo enterprise user
odoo enterprise employee
odoo external employee
odoo external user
external user timesheet
worker timesheet
This module allow you to employee(s) who are not real users of system but portal users / external user and it will allow to record timesheets.
labour timesheet
external employee timesheet
external user timesheet
Timesheet Entry from Web-My Account using Portal User as Employee
external timesheet employee
external timesheet user
Portal Users who are employee of system but not real users can fill/record Timesheet Activities.
If your company using Timesheet application but not purchased real users from Odoo Enterprise then your employee can fill timesheet as portal users.
No need to create real users in system if you are only using timesheet module to make timesheet entry for your all employees. So you can create portal users and set it on employee form and employee can use that portal user logged to fill timesheet activities.
Make sure you have set Portal Timesheet group on portal user form on settings of users.
No need to purchase users from Odoo Enterprise only to fill timesheet any more.
For more details please watch Video or contact us before buy.

employee login
emloyee information
employee detail
sse
ess employee
Self Service
Self Service/Calendar
Self Service/Employee
Self Service/Employee/Employee Details
Self Service/Expenses
Self Service/Expenses/Expenses to Submit
Self Service/Leave Request
Self Service/Leave Request/Leaves Requests
Self Service/Maintenance
Self Service/Maintenance/Maintenance Requests
Self Service/PaySlip
Self Service/PaySlip/Contracts
Self Service/PaySlip/Employee Payslips
Self Service/Projects
Self Service/Projects/Projects
Self Service/Projects/Tasks
Self Service/Timesheet
Self Service/Timesheet/Attendences
Self Service/Timesheet/Detailed Activities
Self Service/Timesheet/My Timesheets
employee self service
ESS
ess
self service odoo
portal
self service
self portal
odoo self service employee
employee portal
employee job portal
self service odoo employee
employee details
employee leave
employee timesheet
employee holidays
self service portal

     """,
    'author' : 'Probuse Consulting Service Pvt. Ltd.',
    'website' : 'www.probuse.com',
    'support': 'contact@probuse.com',
    'images': ['static/description/img1.jpeg'],
    'live_test_url': 'https://youtu.be/Ga1E_i4rLTo',
    'depends': [
#         'website_portal',
        'hr_timesheet',
        'analytic',
        'portal',
        'project',
#         'hr_timesheet_sheet'
        ],
    'data': [
        'security/portal_security.xml',
        'views/website_portal_templates.xml',
        'views/project_view.xml',
        'views/users_view.xml',
        'views/task_view.xml',
     ],
    'installable': True,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
