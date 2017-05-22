let fs = require('fs'),
    path = require('path'),
    carto = require('carto'),
    mapnik = require('mapnik');

function cartoToMapnik(prjPath, cb) {
    let fname = prjPath + '/project.mml',
        data = fs.readFileSync(fname, 'utf-8');

    let mml = new carto.MML({
        localize: true
    });

    mml.load(prjPath, data, function (err, data) {
        if (err) throw err;

        let xml = new carto.Renderer({
            filename: fname,
            local_data_dir: prjPath,
        }).render(data);

        let xmlPath = prjPath + '/project.xml';
        fs.writeFileSync(xmlPath, xml);
        cb(xmlPath);
    });
}

// from https://github.com/mapbox/carto/blob/master/lib/carto/tree/zoom.js

CartoZoomRanges = {
     0: 1000000000,
     1: 500000000,
     2: 200000000,
     3: 100000000,
     4: 50000000,
     5: 25000000,
     6: 12500000,
     7: 6500000,
     8: 3000000,
     9: 1500000,
    10: 750000,
    11: 400000,
    12: 200000,
    13: 100000,
    14: 50000,
    15: 25000,
    16: 12500,
    17: 5000,
    18: 2500,
    19: 1500,
    20: 750,
    21: 500,
    22: 250,
    23: 100
};


function mapnikToPng(xmlPath, outputPath, width, height) {

    mapnik.register_default_fonts();
    mapnik.register_system_fonts();
    mapnik.register_default_input_plugins();

    let map = new mapnik.Map(width, height);

    map.load(xmlPath, function (err, map) {
        if (err) throw err;

        map.zoomAll();

        let o = {};

        if(opts.zoom >= 0)
            o.scale_denominator = CartoZoomRanges[opts.zoom];

        let im = new mapnik.Image(width, height);

        map.render(im, o, function (err, im) {
            if (err) throw err;
            im.encode('png', function (err, buffer) {
                if (err) throw err;
                fs.writeFileSync(outputPath, buffer);
            });
        });
    });
}


let opts = require('minimist')(process.argv.slice(2));

if (opts._.length !== 2) {

    console.log('carto-render: render a TileMill project into a png file');
    console.log('');
    console.log('Options:');
    console.log('\t<path>          tm project folder, must contain project.mml');
    console.log('\t<path>          output png path');
    console.log('\t--width <nnn>   (optional) image width');
    console.log('\t--height <nnn>  (optional) image height');
    console.log('\t--zoom <nnn>    (optional) zoom level');
    console.log('');

    process.exit(1);
}

opts.width = parseInt(opts.width, 10) || 1024;
opts.height = parseInt(opts.height, 10) || 1024;
opts.zoom = parseInt(opts.zoom, 10) || -1;


cartoToMapnik(opts._[0], function(xml) {
    mapnikToPng(xml, opts._[1], opts.width, opts.height);
});

