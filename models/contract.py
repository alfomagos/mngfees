# -*- encoding: utf-8 -*-
from openerp import models, fields, api 
class Contractsale(models.Model):
    _name="mngfees.contractsale"

    name=fields.Char(default=lambda self:self.env['ir.sequence'].get('contrato'),readonly=True, 
                              help="# de Contrato", string="No. Contrato",states={'draft': [('readonly', False)]})
    partner_id=fields.Many2one('res.partner','Customer', required=True, readonly=True,states={'draft': [('readonly', False)]},ondelete="set null", domain=[('customer', '=', True)],
                               help="Customer you are making the agreement with",index=True)
    
    state=fields.Selection(
        [('draft', 'draft'),('progress', 'Pogress'),
         ('cancel', 'Cancel'),  ('done', 'Done')], string='State', readonly=True,
        default='draft')
    active=fields.Boolean(string="Active contract", default=True)
    start_date=fields.Date("Start Date",readonly=True,states={'draft': [('readonly', False)]},help="Please write a start date")
    end_date=fields.Date("End Date",readonly=True,states={'draft': [('readonly', False)]},help="Please write a end date")
    description=fields.Text("Description")
    #ventas_ids=fields.One2many("sale.order","contrato_ventas_ids","Fees Pending")
    product_id=fields.Many2one("product.template","Servicio",readonly=True,states={'draft': [('readonly', False)]},ondelete="set null", domain=[('sale_ok','=',True)],index=True)
    monto_total=fields.Float("Monto del contrato", readonly=True,states={'draft': [('readonly', False)]},help="Monto total del contrato")
    section_ids = fields.One2many("mngfees.sections","contract_id","Courses")

    @api.multi
    def action_draft(self):
	self.write({'state':'draft'})
     
    @api.multi
    def action_done(self):
	self.write({'state':'done'})

    @api.multi
    def action_cancel(self):
	self.write({'state':'cancel'})   
   
  
    

    
