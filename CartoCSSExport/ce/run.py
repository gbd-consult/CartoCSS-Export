#!/usr/bin/python

"""Command line export utility.

Usage: run myproject.qgs /path/to/output

"""

if __name__ == "__main__":

    import sys
    import os

    from qgis.PyQt.QtCore import QFileInfo
    import qgis.core as Q

    sys.path.append(os.path.dirname(__file__))
    import main

    qgs = Q.QgsApplication([], False)
    qgs.initQgis()

    project_path = sys.argv[1]
    out_dir = sys.argv[2]

    if not os.path.exists(project_path):
        print project_path, 'not found'
        sys.exit(1)

    try:
        os.mkdir(out_dir)
    except OSError:
        pass

    print 'loading...'

    prj = Q.QgsProject.instance()
    prj.read(QFileInfo(project_path))

    print 'exporting...'

    errors = main.run(prj, out_dir)

    print 'done, %d errors' % len(errors)

    for err in errors:
        print 'ERROR', err

    qgs.exitQgis()
