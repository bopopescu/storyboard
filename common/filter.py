#!/usr/bin/env python
# encoding: utf-8
"""
filter.py

Created by Darcy Liu on 2012-04-21.
Copyright (c) 2012 Close To U. All rights reserved.
"""

import re
from django.utils.encoding import force_unicode

people = ['bowtie','smile','blush','smiley','relaxed','smirk','heart_eyes','kissing_heart',
        'kissing_face','flushed','relieved','satisfied','grin','wink','wink2','tongue',
        'unamused','sweat','pensive','disappointed','confounded','fearful','cold_sweat',
        'persevere','cry','sob','joy','astonished','scream','angry','rage','sleepy',
        'mask','imp','alien','yellow_heart','blue_heart','purple_heart','heart','green_heart',
        'broken_heart','heartbeat','heartpulse','cupid','sparkles','star','star2','anger',
        'exclamation','question','grey_exclamation','grey_question','zzz','dash','sweat_drops',
        'notes','musical_note','fire','hankey','poop','shit','+1','thumbsup','-1','thumbsdown',
        'ok_hand','punch','fist','v','wave','hand','open_hands','point_up','point_down',
        'point_left','point_right','raised_hands','pray','point_up_2','clap','muscle','metal',
        'walking','runner','couple','dancer','dancers','ok_woman','no_good',
        'information_desk_person','bow','couplekiss','couple_with_heart','massage',
        'haircut','nail_care','boy','girl','woman','man','baby','older_woman','older_man',
        'person_with_blond_hair','man_with_gua_pi_mao','man_with_turban','construction_worker',
        'cop','angel','princess','guardsman','skull','feet','lips','kiss','ear','eyes',
        'nose','feelsgood','finnadie','goberserk','godmode','hurtrealbad','rage1',
        'rage2','rage3','rage4','suspect','trollface']
        
nature = ['sunny','umbrella','cloud','snowman','moon','zap','cyclone','ocean','cat','dog',
        'mouse','hamster','rabbit','wolf','frog','tiger','koala','bear','pig','cow','boar',
        'monkey_face','monkey','horse','racehorse','camel','sheep','elephant','snake','bird',
        'baby_chick','chicken','penguin','bug','octopus','tropical_fish','fish','whale','dolphin',
        'bouquet','cherry_blossom','tulip','four_leaf_clover','rose','sunflower','hibiscus',
        'maple_leaf','leaves','fallen_leaf','palm_tree','cactus','ear_of_rice','shell','octocat',
        'squirrel']
        
objects = ['bamboo','gift_heart','dolls','school_satchel','mortar_board','flags','fireworks',
        'sparkler','wind_chime','rice_scene','jack_o_lantern','ghost','santa','christmas_tree',
        'gift','bell','tada','balloon','cd','dvd','camera','movie_camera','computer','tv','iphone',
        'fax','phone','telephone','minidisc','vhs','speaker','loudspeaker','mega','radio',
        'satellite','loop','mag','unlock','lock','key','scissors','hammer','bulb','calling',
        'email','mailbox','postbox','bath','toilet','seat','moneybag','trident','smoking',
        'bomb','gun','pill','syringe','football','basketball','soccer','baseball','tennis',
        'golf','8ball','swimmer','surfer','ski','spades','hearts','clubs','diamonds','gem','ring',
        'trophy','space_invader','dart','mahjong','clapper','memo','pencil','book','art','microphone',
        'headphones','trumpet','saxophone','guitar','part_alternation_mark','shoe','sandal',
        'high_heel','lipstick','boot','shirt','tshirt','necktie','dress','kimono','bikini','ribbon',
        'tophat','crown','womans_hat','closed_umbrella','briefcase','handbag','beer','beers','cocktail',
        'sake','fork_and_knife','hamburger','fries','spaghetti','curry','bento','sushi','rice_ball',
        'rice_cracker','rice','ramen','stew','bread','egg','oden','dango','icecream','shaved_ice',
        'birthday','cake','apple','tangerine','watermelon','strawberry','eggplant','tomato','coffee','tea']
        
places = ['109','house','school','office','post_office','hospital','bank','convenience_store',
        'love_hotel','hotel','wedding','church','department_store','city_sunrise','city_sunset',
        'japanese_castle','european_castle','tent','factory','tokyo_tower','mount_fuji',
        'sunrise_over_mountains','sunrise','stars','statue_of_liberty','rainbow','ferris_wheel',
        'fountain','roller_coaster','ship','speedboat','boat','sailboat','airplane','rocket',
        'bike','blue_car','car','red_car','taxi','bus','police_car','fire_engine','ambulance','truck',
        'train','station','bullettrain_front','bullettrain_side','ticket','fuelpump','traffic_light',
        'warning','construction','beginner','atm','slot_machine','busstop','barber','hotsprings',
        'checkered_flag','crossed_flags','jp','kr','cn','us','fr','es','it','ru','gb','de']
        
symbols = ['1','2','3','4','5','6','7','8','9','0','hash','arrow_backward','arrow_down','arrow_forward',
        'arrow_left','arrow_lower_left','arrow_lower_right','arrow_right','arrow_up','arrow_upper_left',
        'arrow_upper_right','rewind','fast_forward','ok','new','top','up','cool','cinema','koko',
        'signal_strength','u5272','u55b6','u6307','u6708','u6709','u6e80','u7121','u7533','u7a7a','sa',
        'restroom','mens','womens','baby_symbol','no_smoking','parking','wheelchair','metro','wc',
        'secret','congratulations','ideograph_advantage','underage','id','eight_spoked_asterisk',
        'eight_pointed_black_star','heart_decoration','vs','vibration_mode','mobile_phone_off',
        'chart','currency_exchange','aries','taurus','gemini','cancer','leo','virgo','libra','scorpius',
        'sagittarius','capricorn','aquarius','pisces','ophiuchus','six_pointed_star','a','b','ab',
        'o2','red_circle','black_square','white_square','clock1','clock10','clock11','clock12',
        'clock2','clock3','clock4','clock5','clock6','clock7','clock8','clock9','o','x','copyright',
        'registered','tm','shipit']

emoji_list = people + nature + objects + places + symbols

def emoji_to_html(text):
    pattern = re.compile(':([a-z0-9\+\-_]+):')
    
    def make_emoji(m):
        name = m.group(1)
        if name not in emoji_list:
            return ':%s:' % name
        tpl = ('<img class="emoji" title="%(name)s" alt="%(name)s" height="20"'
               ' width="20" src="%(url)s%(name)s.png" align="top">')
        return tpl % {'name': name, 'url': 'http://assets.github.com/images/icons/emoji/'}
        
    text = pattern.sub(make_emoji, text)
    return text
  
# def html_escape(text):
#     HTML_ESCAPE_RE = re.compile('[&<>"\'/`]')
#     HTML_ESCAPE_DICT = {'&': '&amp;',
#                         '<': '&lt;',
#                         '>': '&gt;',
#                         '"': '&quot;',
#                         "'": '&#x27;',
#                         '/': '&#x2F;',
#                         '`': '&#x60;'}
#     return HTML_ESCAPE_RE.sub(lambda match: HTML_ESCAPE_DICT[match.group(0)],force_unicode(text))

def html_escape(text):
    return force_unicode(text).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#39;')

def main():
    print emoji_to_html(':smile:')
    print html_escape('&<>"\'/`')


if __name__ == '__main__':
    main()

