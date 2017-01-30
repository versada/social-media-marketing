# -*- coding: utf-8 -*-
# This file is part of OpenERP. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.
{
    'name': 'Twitter Campaign API',
    'version': '9.0.1.0.0',
    'author': 'Versada',
    'category': 'Marketing',
    'website': 'http://www.versada.eu',
    'summary': '',
    'description': """
Twitter Campaign API that enables different filters and statistics related with your campaign that will be shown on your website.
""",
    'depends': [
        'marketing_campaign'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/marketing_campaign.xml',
        'views/twitter.xml',
    ],
    'installable': True,
    'application': False,
}
