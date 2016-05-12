# -*- encoding: utf-8 -*-
##############################################################################
#
# @author - Rosen Vladimirov, Terraros Commerce <vladimirov.rosen@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import fields, osv
from openerp.tools.translate import _


class res_company(osv.osv):
    _inherit = "res.company"

    _columns = {
        'bg_uic': fields.related('partner_id', 'bg_uic', string=_('UIC'), type="char", size=13, required=True,
                                 help=_('UIC by Bulgarian register agency')),
        'bg_mol': fields.related('partner_id', 'bg_mol', string=_('MOL'), type="char", size=100, required=True,
                                 help=_('MOL')),
    }
