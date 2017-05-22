"""Main export routine."""

import json
import os
import re
import types

from qgis.core import *

import export
import debug

# these imports must be here for the dynamic dispatch to work
import project, layer, renderer, symbol, labeling


def enum_exporters():
    ls = {}

    cd = os.path.dirname(__file__)
    mods = [x for x in globals().values() if isinstance(x, types.ModuleType)]

    for mod in mods:
        if hasattr(mod, '__file__') and mod.__file__.startswith(cd):
            for name in vars(mod):
                m = re.match(r'^export([A-Z]\w+)$', name)
                if m:
                    ls[m.group(1)] = getattr(mod, name)

    return ls


def run(prj, out_dir):
    """Main export routine.
    
    :param QgsProject prj: qgis project
    :param out_dir: directory for the TM project (must exist!)
    :return: list of error tuples (error_code, object)
    """

    cc = export.Process(prj)
    cc.register_exporters(enum_exporters())

    meta, css = cc.run()

    with open(out_dir + '/project.mml', 'w') as fp:
        json.dump(meta, fp, sort_keys=True, indent=4)

    with open(out_dir + '/style.mss', 'w') as fp:
        fp.write(css.encode('utf8'))

    #print css.encode('utf8')

    return cc.errors()
