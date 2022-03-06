# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Import lot number with stock from excel',
    'version': '14.0.0.2',
    'category': 'Warehouse',
    'summary': 'import lot with stock import lot stock import stock with lot number import stock inventory adjustment import inventory adjustment import product stock import inventory with lot import serial import inventory import stock balance import stock with Serial',
    'description' :"""This app is useful for import lot number with lot and you can also 
    import lot with best before date,removal Date,End of life date,Alert date and without dates,and 
    after that inventory adjustment is generated with inventory line.

    import lot number with stock from csv or excel in odoo,
    import lot with best before date than removal date than end of life date and alert date in odoo,
    import lot without date details in odoo,
    import lot number with stock from csv in odoo,
    import lot number with stock from excel in odoo
      
    """,
    'author': 'BrowseInfo',
    "price": 30,
    "currency": 'EUR',
    'website': 'https://www.browseinfo.in',
    'depends': ['base','stock','product_expiry'],
    'data': [
            'security/ir.model.access.csv',
            'wizard/import_lot_with_stock.xml'

    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'live_test_url':'https://youtu.be/dxwClUlfjfQ',
    "images":['static/description/Banner.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
