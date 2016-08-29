# -*- encoding: utf-8 -*-
from openerp import models, fields, api 
class Topic(models.Model):
	_name="mngfees.topic"	

	name=fields.Char("Name of Topic", required= True )
	code= fields.Char("Code of Topic")
	resource= fields.Text("Resource for topic")
	course_id= fields.Many2one("mngfees.course","Course")
	description= fields.Text("Description and notes")	


        

