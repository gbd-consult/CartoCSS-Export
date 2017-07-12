import json
import os

import miniyaml, debug

def _mkdir(p):
    if not os.path.exists(p):
        os.mkdir(p)
    return p


class ExportResult:
    def __init__(self, meta, css, errors):
        self.meta = meta
        self.css = css
        self.errors = errors
        self.name = self.meta['name']

    def write_for_tilemill(self, out_dir):
        base = _mkdir(out_dir + '/' + self.name + '.tm')

        with open(base + '/project.mml', 'w') as fp:
            json.dump(self.meta, fp, sort_keys=True, indent=4)

        with open(base + '/style.mss', 'w') as fp:
            fp.write(self.css.encode('utf8'))

    def write_for_mapbox(self, out_dir):
        base = _mkdir(out_dir + '/' + self.name + '.tm2')
        data = _mkdir(out_dir + '/' + self.name + '.tm2source')

        with open(base + '/style.mss', 'w') as fp:
            fp.write(self.css.encode('utf8'))

        with open(data + '/data.yml', 'w') as fp:
            fp.write(miniyaml.dump(self.meta))

        project = {
            # Kleinmaischeid center
            'center': [7.62, 51.5562, 10],
            'source': 'tmsource://' + os.path.abspath(data),
            'styles': [
                'style.mss'
            ]
        }

        with open(base + '/project.yml', 'w') as fp:
            fp.write(miniyaml.dump(project))
