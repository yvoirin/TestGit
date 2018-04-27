# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TestGit
                                 A QGIS plugin
 TestGit
                             -------------------
        begin                : 2018-04-27
        copyright            : (C) 2018 by yves
        email                : yves.voirin@usherbrooke.ca
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
    """Load TestGit class from file TestGit.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .TestGit import TestGit
    return TestGit(iface)
