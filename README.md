# CartoCSS-Export

QGIS Plugin to export QGS Project file to CartoCSS Format

## Install

To install the Plugin:

    cd CartoCSSExport
    make deploy

This moves the required files to the QGIS Plugin folder. Just activate the Plugin in QGIS and you're done!
It is also possible to create a .zip archive containing the Plugin by running:

    make zip

## Directory layout

- CartoCSSExport: plugin source
- CartoCSSExport/ce: export engine
- doc: sphinx documentation
- dev: dev scripts

## Export engine

The export engine is in `CartoCSSExport/ce`, the main entry point is `run(project, out_dir)`: exports a `QgsProject` into the `out_dir`.
Returns a list of errors, an error is a tuple `(error_code, details)`.

There's also a command line script `CartoCSSExport/ce/run.py` for offline exporting, the syntax is

    python CartoCSSExport/ce/run.py <qgis project>.qgs path/to/output

## Testing

For non-interactive testing, use `dev/carto-render.js` to render in a png, e.g

    python CartoCSSExport/ce/run.py foobar.qgs path/to/output
    node dev/carto-render.js path/to/output/project.mml foobar.png

For interactive testing, install TileMill and set up its `Documents` folder (under `Settings`).
Converted projects must be saved in `<documents>/projects`, so that you can see them under `Projects`.

## Documentation

(Incomplete) sphinx docs are in `doc/`, use `make` to generate (will be saved in `doc/_build`):

    cd doc
    make html
    open _build/html/index.html


## License

This program is free software; you can redistribute it and/or modify it under the terms of the 
GNU General Public License as published by the Free Software Foundation; either version 2 of the 
License, or (at your option) any later version.

