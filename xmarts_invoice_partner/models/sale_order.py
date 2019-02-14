from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    

    Payment_SO = fields.Many2one('l10n_mx_edi.payment.method',string='Payment_SO',readonly=1,compute='myfunction')
    Paymentid_SO = fields.Integer(related='partner_id.Payment_partner.id')
    Uso_SO = fields.Selection(related="partner_id.Uso_partner",string='Uso ')
    @api.onchange('name','partner_id')
    def myfunction(self):
        for record in self:
            record[("Payment_SO")]=record.Paymentid_SO
    @api.multi
    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        res.update({
            'l10n_mx_edi.payment.method_id':self.Payment_SO.id,
	        'l10n_mx_edi_usage':self.Uso_S0,
            })
        return res
