# -*- coding: utf-8 -*-
from eforge.menu import ItemOrder

EFORGE_PLUGIN = {
    'name':     'EForge Core',
    'credit':   'Copyright &copy; 2010 Element43 and contributors',
    
    'provides': {
        'mnu': [('project-page', ItemOrder(000, 'Summary'))],
    },
}