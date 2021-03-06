# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
from odoo import fields, models, api, _
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    """
    Inherited for adding relation with inter company transfer.
    @author: Maulik Barad.
    """
    _inherit = 'purchase.order'
    _description = 'Purchase Order'

    inter_company_transfer_id = fields.Many2one('inter.company.transfer.ept', string="ICT", copy=False,
                                                help="Reference of ICT.")

    @api.model
    def _prepare_picking(self):
        """
        Inherited for adding relation with ICT if created by it.
        @author: Maulik Barad.
        @return: Dictionary for creating picking.
        """
        vals = super(PurchaseOrder, self)._prepare_picking()
        if self.inter_company_transfer_id:
            vals.update({'inter_company_transfer_id': self.inter_company_transfer_id.id})
        return vals

    def _prepare_invoice(self):
        """
        Inherited for adding relation with ICT if created by it.
        @author: Maulik Barad.
        @return: Dictionary for creating invoice.
        """
        vals = super(PurchaseOrder, self)._prepare_invoice()
        if self.inter_company_transfer_id:
            ict = self.inter_company_transfer_id
            vals.update({'inter_company_transfer_id': ict.id, 'invoice_date': fields.Date.context_today(self)})
            if ict.destination_company_id.purchase_journal_id:
                vals.update({'journal_id': ict.destination_company_id.purchase_journal_id.id})
        return vals

    def button_confirm(self):
        """
        This method is inherited for restricting the Confirm Order, when the sale order is not confirmed yet.
        @author: Maulik Barad on Date 11-Jan-2021.
        """
        for order in self:
            if order.state not in ['draft', 'sent']:
                continue
            if order.inter_company_transfer_id:
                sale_order = order.inter_company_transfer_id.sale_order_ids.filtered(lambda x: x.state != "cancel")
                if sale_order and sale_order.state not in ["sale", "done"]:
                    raise UserError(_("You can't confirm this order.\nThis order is generated by the Inter Company "
                                      "Transfer and the related Sale order is not confirmed yet of Company - "
                                      "%s.") % order.partner_id.name)
        super(PurchaseOrder, self).button_confirm()
        return True
