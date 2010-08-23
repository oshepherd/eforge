# -*- coding: utf-8 -*-
# EForge project management system, Copyright © 2010, Element43
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

from eforge.menu import ItemOrder
from eforge.management import project, members
from eforge.models import Project
import eforge.queue

EFORGE_PLUGIN = {
    'name':     'EForge Core',
    'credit':   'Copyright &copy; 2010 Element43 and contributors',

    'provides': {
        'mnu': (
            ('project-page',       ItemOrder(000, 'Summary')),
            ('project-management', ItemOrder(999, 'Manage')),
        ),

        'managepg': (
            ('project', { 'name': 'Project', 'view': project }),
            ('members', { 'name': 'Members', 'view': members }),
        ),

        'perms': (
            ('eforge', { 'title': 'Project', 'perms': {
                'manage': 'Can manage the project',
            }}),
        ),
    },
}

VERSION = (0, 5, 99, '(git master)')

def get_version():
    return '%d.%d.%d %s' % VERSION

import eforge.pluginloader