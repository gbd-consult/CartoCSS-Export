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

from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon, QFileDialog, QDialogButtonBox
from qgis.core import QgsProject, QgsMessageLog
from qgis.gui import QgsMessageBar
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from cartoCSS_export_dialog import CartoCSSExportDialog
import os.path
import ce


class CartoCSSExport:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'CartoCSSExport_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        self.dlg = CartoCSSExportDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&CartoCSS Export')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'CartoCSSExport')
        self.toolbar.setObjectName(u'CartoCSSExport')




    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('CartoCSSExport', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        # Create the dialog (after translation) and keep reference
        self.dlg = CartoCSSExportDialog()

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/CartoCSSExport/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'CartoCSS Export'),
            callback=self.run,
            parent=self.iface.mainWindow())

        self.dlg.lineEdit.clear()
        self.dlg.pushButton.clicked.connect(self.selectOutputDir)
        self.dlg.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.runExport)
        self.dlg.buttonBox.button(QDialogButtonBox.Close).clicked.connect(self.dlg.close)


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&CartoCSS Export'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar


    def run(self):
        """Run method that performs all the real work"""

        # Check if there is an open project
        project = QgsProject.instance()
        if not (project.fileName()):
            self.iface.messageBar().pushMessage(self.tr("no open Project"), level=QgsMessageBar.CRITICAL, duration=3)
            return 1
        # show the dialog
        self.dlg.show()

    def runExport(self):
        project = QgsProject.instance()
        outdir = self.dlg.lineEdit.text()
        if not os.path.isdir(outdir):
            self.dlg.textEdit.append(self.tr("Not a valid output directory"))
        else:
            try:
                res = ce.run(project,outdir)
            except:
                self.dlg.textEdit.append(self.tr("This should not happen"))
            if res:
                self.dlg.textEdit.append(self.tr("Export completed with Warnings"))
                for r in res:
                    self.dlg.textEdit.append(r[0] + " - " + r[1])
            self.dlg.textEdit.append(self.tr("Export saved to") + outdir)

    def selectOutputDir(self):
        dirname = QFileDialog.getExistingDirectory(self.dlg, self.tr("Open Directory"),\
                    "/home", QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        self.dlg.lineEdit.setText(dirname)
        self.dlg.buttonBox.button(QDialogButtonBox.Apply).setEnabled(True)
