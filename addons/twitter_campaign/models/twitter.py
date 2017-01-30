# -*- coding: utf-8 -*-
# This file is part of OpenERP. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.

from openerp import models, fields, api


class TwitterTweet(models.Model):
    _name = "twitter.tweet"
    _description = "Tweet"

    campaign_id = fields.Many2one('marketing.campaign', 'Campaign')
    # Orginal name from twitter: text
    content = fields.Text(string='Tweet')
    created_at = fields.Datetime(string='Created date')
    favorite_count = fields.Integer(string='Favorites')
    favorited = fields.Boolean(string='Created date')
    id_str = fields.Char()
    retweet_count = fields.Integer(string='Retweets')
    retweeted = fields.Boolean()
    source = fields.Char(string='Source')
    user_screen_name = fields.Char(string='User Name')
    hashtag = fields.Char(string='Hashtag')


class TwitterFilter(models.Model):
    _name = "twitter.filter"
    _description = "Twitter Filters"

    def _get_possible_filters(self):
        res = self.env['twitter.tweet'].fields_view_get()

        tweet_list = []
        for f in res['fields'].iteritems():
            tweet_list.append((f[0], f[1]['string']))
        return tweet_list

    name = fields.Char()
    filter_by = fields.Selection(_get_possible_filters,
                                 string='Filter by')
    filter_type = fields.Selection(
       [('number', 'Number'),
        ('list', 'List')],
       default='number',
       string='Type')
    campaign_id = fields.Many2one('marketing.campaign', 'Campaign')
