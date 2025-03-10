from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id,
    )

    expected_revenue_with_currency = fields.Char(
        string='Expected Revenue',
        compute='_compute_expected_revenue_with_currency',
        inverse='_inverse_expected_revenue_with_currency',
        store=True,
    )

    @api.depends('expected_revenue', 'currency_id')
    def _compute_expected_revenue_with_currency(self):
        for lead in self:
            if lead.expected_revenue and lead.currency_id:
                symbol = lead.currency_id.symbol
                formatted_value = f"{symbol} {lead.expected_revenue:,.2f}"
                lead.expected_revenue_with_currency = formatted_value
            else:
                lead.expected_revenue_with_currency = lead.expected_revenue

    def _inverse_expected_revenue_with_currency(self):
        for lead in self:
            if lead.expected_revenue_with_currency and lead.currency_id:
                # Remove currency symbol and parse the numeric value
                raw_value = lead.expected_revenue_with_currency.replace(lead.currency_id.symbol, '').strip()
                try:
                    lead.expected_revenue = float(raw_value.replace(',', ''))
                except ValueError:
                    raise ValueError("Invalid numeric value for Expected Revenue.")