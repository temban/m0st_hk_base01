# -*- coding: utf-8 -*-

from odoo import models, fields, api


class m0st_hk_base(models.Model):
    _inherit = "res.partner"
    _description = 'Management of the basic entities of HUB KILO'

    street = fields.Char(string='Street')
    email = fields.Char(string='Email')
    birthdate = fields.Date(string='born on')
    birthplace = fields.Char(string="born at")
    sex = fields.Char(string="Sex")
    is_traveler = fields.Boolean(default=False)
    password = fields.Char(string="Password")
    image_1920 = fields.Binary(string='Image', attachment=True)
