# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CartoCSSExport
                                 A QGIS plugin
 Exports .qgs Project files to CartoCSS
                             -------------------
        begin                : 2017-05-22
        copyright            : (C) 2017 by Geoinformatikbüro Dassau
        email                : info@gbd-consult.de
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CartoCSSExport class from file CartoCSSExport.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .cartoCSS_export import CartoCSSExport
    return CartoCSSExport(iface)
