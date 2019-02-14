from odoo import api, fields, models, _

class AccountInvoice(models.Model):
	_inherit = 'res.partner'
	
	Payment_partner = fields.Many2one('l10n_mx_edi.payment.method',string='Payment Method')
	Uso_partner = fields.Selection(selection=[('G01', 'Adquisición de mercancías'),('G02', 'Devoluciones, descuentos o bonificaciones'),('G03', 'Gastos en general'),('l01', 'Construcciones'),('l02', 'Mobilario y equipo de oficina por inversiones'),('l03', 'Equipo de transporte'),('l04', 'Equipo de cómputo y accesorios'),('l05', 'Dados, troqueles, moldes, matrices y herramental'),('l06', 'Comunicaciones telefónicas'),('l07', 'Comunicaciones satelitales'),('l08', 'Otra maquinaria y equipo'),('D01', 'Honorarios médicos, dentales y gastos hospitalarios'),('D02', 'Gastos médicos por incapacidad o discapacidad'),('D03', 'Gastos funerales'),('D04', 'Donativos'),('D05', 'Intereses reales efectivamente pagados por créditos hipotecarios (casa habitación)'),('D06', 'Aportaciones voluntarias al SAR'),('D07', 'Primas por seguros de gastos médicos'),('D08', 'Gastos de transportación escolar obligatoria.'),('D09', 'Depósitos en cuentas para el ahorro, primas que tengan como base planes de pensiones.'),('D10', 'Pagos por servicios educativos (colegiaturas)'),('P01', 'Por definir')],string='Uso ')
