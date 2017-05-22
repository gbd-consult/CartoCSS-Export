
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
