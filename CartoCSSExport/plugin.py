# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QGIS Plugin to export .qgs project files to CartoCSS
                             -------------------
        begin                : 2017-05-22
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Geoinformatikbüro Dassau GmbH
        email                : info@gbd-consult.de
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from qgis.core import *

import ce

class CartoCssExportPlugin:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        print 'initGui'

    def unload(self):
        print 'unload'

    def run(self):
        # project = <current qgis project>
        # out_dir = <output dir selected by the user>
        # errors = ce.run(project, out_dir)
        # display errors
        pass
