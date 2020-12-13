# -*- coding: utf-8 -*-
from odoo import models, fields, api
class CalendarWeb(models.Model):
     _name = 'calendar.web'
     _description = 'Creación de Calendario Web'

     nombre = fields.Char('Nombre del usuario', required=True)
     duracion = fields.Integer('Duracion de la clase', required=True)
     hora = fields.Integer('hora de la clase', required=True)
     url = fields.Char('url de la clase', required=True)
     dia = fields.Char('dia de la clase', required=True)

