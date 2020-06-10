# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    text_field = fields.Char(string='Text Field',
                             readonly=False,
                             config_parameter='setting_sample.text_field',
                             help='Set this text Field')

    hidden_field = fields.Char(string='Hidden field',
                               readonly=False,
                               config_parameter='setting_sample.hidden_field',
                               help='Set this hidden Field')
