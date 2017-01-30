# -*- coding: utf-8 -*-
# This file is part of OpenERP. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.

from openerp import models, fields, api


class MarketingCampaign(models.Model):
    _inherit = "marketing.campaign"

    twitter_tag = fields.Char(
        string='Twitter Hashtags',
        help='Add your twitter hashtags.Use # before every tag.')

    twitter_filters = fields.One2many('twitter.filter', 'campaign_id')
