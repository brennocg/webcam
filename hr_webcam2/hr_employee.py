from odoo import api, fields, models, _


class hr_employee(models.Model):
    _inherit = 'hr.employee'

    def action_take_picture(self):
        employee = False
        employee_action = self.env.ref('hr_webcam2.action_take_photo')
        dict_act_window = employee_action.read([])[0]
        if employee:
            dict_act_window['res_id'] = employee.id
        dict_act_window['view_mode'] = 'form,tree'
        return dict_act_window
