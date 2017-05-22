"""CartoCSS properties."""

# extracted from https://raw.githubusercontent.com/mapbox/carto/master/docs/latest.md

Properties = {
    "background-color": {
        "default": None,
        "description": "Map Background color.",
        "type": "color"
    },
    "background-image": {
        "default": "",
        "description": "An image that is repeated below all features on a map as a background. Accepted formats: svg, jpg, png, tiff, and webp.",
        "type": "uri"
    },
    "background-image-comp-op": {
        "default": "src-over",
        "description": "Set the compositing operation used to blend the image into the background.",
        "type": "keyword",
        "values": [
            "clear",
            "src",
            "dst",
            "src-over",
            "dst-over",
            "src-in",
            "dst-in",
            "src-out",
            "dst-out",
            "src-atop",
            "dst-atop",
            "xor",
            "plus",
            "minus",
            "multiply",
            "divide",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "linear-dodge",
            "linear-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "contrast",
            "invert",
            "invert-rgb",
            "grain-merge",
            "grain-extract",
            "hue",
            "saturation",
            "color",
            "value"
        ]
    },
    "background-image-opacity": {
        "default": 1,
        "description": "Set the opacity of the image.",
        "type": "float"
    },
    "base": {
        "default": "",
        "description": "Any relative paths used to reference files will be understood as relative to this directory path if the map is loaded from an in memory object rather than from the filesystem. If the map is loaded from the filesystem and this option is not provided it will be set to the directory of the stylesheet.",
        "type": "string"
    },
    "buffer-size": {
        "default": 0,
        "description": "Extra tolerance around the map (in pixels) used to ensure labels crossing tile boundaries are equally rendered in each tile (e.g. cut in each tile). Not intended to be used in combination with \"avoid-edges\".",
        "type": "float"
    },
    "building-fill": {
        "default": "The color gray will be used for fill.",
        "description": "The color of the buildings fill. Note: 0.8 will be used to multiply each color component to auto-generate a darkened wall color.",
        "type": "color"
    },
    "building-fill-opacity": {
        "default": 1,
        "description": "The opacity of the building as a whole, including all walls.",
        "type": "float"
    },
    "building-height": {
        "default": 0,
        "description": "The height of the building in pixels.",
        "type": "float"
    },
    "comp-op": {
        "default": "src-over",
        "description": "Composite operation. This defines how this layer should behave relative to layers atop or below it.",
        "type": "keyword",
        "values": [
            "clear",
            "src",
            "dst",
            "src-over",
            "dst-over",
            "src-in",
            "dst-in",
            "src-out",
            "dst-out",
            "src-atop",
            "dst-atop",
            "xor",
            "plus",
            "minus",
            "multiply",
            "divide",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "linear-dodge",
            "linear-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "contrast",
            "invert",
            "invert-rgb",
            "grain-merge",
            "grain-extract",
            "hue",
            "saturation",
            "color",
            "value"
        ]
    },
    "debug-mode": {
        "default": "collision",
        "description": "The mode for debug rendering.",
        "type": "string"
    },
    "direct-image-filters": {
        "default": None,
        "description": "A list of image filters to apply to the main canvas (see the image-filters doc for how they work on a separate canvas).",
        "type": "functions",
        "values": [
            "agg-stack-blur",
            "emboss",
            "blur",
            "gray",
            "sobel",
            "edge-detect",
            "x-gradient",
            "y-gradient",
            "invert",
            "sharpen",
            "color-blind-protanope",
            "color-blind-deuteranope",
            "color-blind-tritanope",
            "colorize-alpha",
            "color-to-alpha",
            "scale-hsla"
        ]
    },
    "dot-comp-op": {
        "default": "src-over",
        "description": "Composite operation. This defines how this layer should behave relative to layers atop or below it.",
        "type": "keyword",
        "values": [
            "clear",
            "src",
            "dst",
            "src-over",
            "dst-over",
            "src-in",
            "dst-in",
            "src-out",
            "dst-out",
            "src-atop",
            "dst-atop",
            "xor",
            "plus",
            "minus",
            "multiply",
            "divide",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "linear-dodge",
            "linear-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "contrast",
            "invert",
            "invert-rgb",
            "grain-merge",
            "grain-extract",
            "hue",
            "saturation",
            "color",
            "value"
        ]
    },
    "dot-fill": {
        "default": "gray",
        "description": "The color of the area of the dot.",
        "type": "color"
    },
    "dot-height": {
        "default": 1,
        "description": "The height of the dot in pixels.",
        "type": "float"
    },
    "dot-opacity": {
        "default": 1,
        "description": "The overall opacity of the dot.",
        "type": "float"
    },
    "dot-width": {
        "default": 1,
        "description": "The width of the dot in pixels.",
        "type": "float"
    },
    "font-directory": {
        "default": None,
        "description": "Path to a directory which holds fonts which should be registered when the Map is loaded (in addition to any fonts that may be automatically registered).",
        "type": "uri"
    },
    "image-filters": {
        "default": None,
        "description": "A list of image filters that will be applied to the active rendering canvas for a given style. The presence of one more image-filters will trigger a new canvas to be created before starting to render a style and then this canvas will be composited back into the main canvas after rendering all features and after all image-filters have been applied. See direct-image-filters if you want to apply a filter directly to the main canvas.",
        "type": "functions",
        "values": [
            "agg-stack-blur",
            "emboss",
            "blur",
            "gray",
            "sobel",
            "edge-detect",
            "x-gradient",
            "y-gradient",
            "invert",
            "sharpen",
            "color-blind-protanope",
            "color-blind-deuteranope",
            "color-blind-tritanope",
            "colorize-alpha",
            "color-to-alpha",
            "scale-hsla"
        ]
    },
    "image-filters-inflate": {
        "default": False,
        "description": "A property that can be set to True to enable using an inflated image internally for seamless blurring across tiles (requires buffered data).",
        "type": "boolean"
    },
    "line-cap": {
        "default": "butt",
        "description": "The display of line endings.",
        "type": "keyword",
        "values": [
            "butt",
            "round",
            "square"
        ]
    },
    "line-clip": {
        "default": False,
        "description": "Turning on clipping can help performance in the case that the boundaries of the geometry extent outside of tile extents. But clipping can result in undesirable rendering artifacts in rare cases.",
        "type": "boolean"
    },
    "line-color": {
        "default": "black",
        "description": "The color of a drawn line.",
        "type": "color"
    },
    "line-comp-op": {
        "default": "src-over",
        "description": "Composite operation. This defines how this symbolizer should behave relative to symbolizers atop or below it.",
        "type": "keyword",
        "values": [
            "clear",
            "src",
            "dst",
            "src-over",
            "dst-over",
            "src-in",
            "dst-in",
            "src-out",
            "dst-out",
            "src-atop",
            "dst-atop",
            "xor",
            "plus",
            "minus",
            "multiply",
            "divide",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "linear-dodge",
            "linear-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "contrast",
            "invert",
            "invert-rgb",
            "grain-merge",
            "grain-extract",
            "hue",
            "saturation",
            "color",
            "value"
        ]
    },
    "line-dash-offset": {
        "default": None,
        "description": "Valid parameter but not currently used in renderers (only exists for experimental svg support in Mapnik which is not yet enabled).",
        "type": "numbers"
    },
    "line-dasharray": {
        "default": None,
        "description": "A pair of length values [a,b], where (a) is the dash length and (b) is the gap length respectively. More than two values are supported for more complex patterns.",
        "type": "numbers"
    },
    "line-gamma": {
        "default": 1,
        "description": "Level of antialiasing of stroke line.",
        "type": "float"
    },
    "line-gamma-method": {
        "default": "power",
        "description": "An Antigrain Geometry specific rendering hint to control the quality of antialiasing. Under the hood in Mapnik this method is used in combination with the 'gamma' value (which defaults to 1). The methods are in the AGG source at https://github.com/mapnik/mapnik/blob/master/deps/agg/include/agg_gamma_functions.",
        "type": "keyword",
        "values": [
            "power",
            "linear",
            "none",
            "threshold",
            "multiply"
        ]
    },
    "line-geometry-transform": {
        "default": None,
        "description": "Transform line geometry with specified function.",
        "type": "functions",
        "values": [
            "matrix",
            "translate",
            "scale",
            "rotate",
            "skewX",
            "skewY"
        ]
    },
    "line-join": {
        "default": "miter",
        "description": "The behavior of lines when joining.",
        "type": "keyword",
        "values": [
            "miter",
            "miter-revert",
            "round",
            "bevel"
        ]
    },
    "line-miterlimit": {
        "default": 4,
        "description": "The limit on the ratio of the miter length to the stroke-width. Used to automatically convert miter joins to bevel joins for sharp angles to avoid the miter extending beyond the thickness of the stroking path. Normally will not need to be set, but a larger value can sometimes help avoid jaggy artifacts.",
        "type": "float"
    },
    "line-offset": {
        "default": 0,
        "description": "Offsets a line a number of pixels parallel to its actual path. Positive values move the line left, negative values move it right (relative to the directionality of the line).",
        "type": "float"
    },
    "line-opacity": {
        "default": 1,
        "description": "The opacity of a line.",
        "type": "float"
    },
    "line-pattern-clip": {
        "default": False,
        "description": "Turning on clipping can help performance in the case that the boundaries of the geometry extent outside of tile extents. But clipping can result in undesirable rendering artifacts in rare cases.",
        "type": "boolean"
    },
    "line-pattern-comp-op": {
        "default": "src-over",
        "description": "Composite operation. This defines how this symbolizer should behave relative to symbolizers atop or below it.",
        "type": "keyword",
        "values": [
            "clear",
            "src",
            "dst",
            "src-over",
            "dst-over",
            "src-in",
            "dst-in",
            "src-out",
            "dst-out",
            "src-atop",
            "dst-atop",
            "xor",
            "plus",
            "minus",
            "multiply",
            "divide",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "linear-dodge",
            "linear-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "contrast",
            "invert",
            "invert-rgb",
            "grain-merge",
            "grain-extract",
            "hue",
            "saturation",
            "color",
            "value"
        ]
    },
    "line-pattern-file": {
        "default": None,
        "description": "An image file to be repeated and warped along a line. Accepted formats: svg, jpg, png, tiff, and webp.",
        "type": "uri"
    },
    "line-pattern-geometry-transform": {
        "default": None,
        "description": "Transform line geometry with specified function and apply pattern to transformed geometry.",
        "type": "functions",
        "values": [
            "matrix",
            "translate",
            "scale",
            "rotate",
            "skewX",
            "skewY"
        ]
    },
    "line-pattern-offset": {
        "default": 0,
        "description": "Offsets a line a number of pixels parallel to its actual path. Positive values move the line left, negative values move it right (relative to the directionality of the line).",
        "type": "float"
    },
    "line-pattern-opacity": {
        "default": 1,
        "description": "Apply an opacity level to the image used for the pattern.",
        "type": "float"
    },
    "line-pattern-simplify": {
        "default": 0,
        "description": "geometries are simplified by the given tolerance.",
        "type": "float"
    },
    "line-pattern-simplify-algorithm": {
        "default": "radial-distance",
        "description": "geometries are simplified by the given algorithm.",
        "type": "keyword",
        "values": [
            "radial-distance",
            "zhao-saalfeld",
            "visvalingam-whyatt"
        ]
    },
    "line-pattern-smooth": {
        "default": 0,
        "description": "Smooths out geometry angles. 0 is no smoothing, 1 is fully smoothed. Values greater than 1 will produce wild, looping geometries.",
        "type": "float"
    },
    "line-pattern-transform": {
        "default": None,
        "description": "Transform line pattern instance with specified function.",
        "type": "functions",
        "values": [
            "matrix",
            "translate",
            "scale",
            "rotate",
            "skewX",
            "skewY"
        ]
    },
    "line-rasterizer": {
        "default": "full",
        "description": "Exposes an alternate AGG rendering method that sacrifices some accuracy for speed.",
        "type": "keyword",
        "values": [
            "full",
            "fast"
        ]
    },
    "line-simplify": {
        "default": 0,
        "description": "Simplify geometries by the given tolerance.",
        "type": "float"
    },
    "line-simplify-algorithm": {
        "default": "radial-distance",
        "description": "Simplify geometries by the given algorithm.",
        "type": "keyword",
        "values": [
            "radial-distance",
            "zhao-saalfeld",
            "visvalingam-whyatt"
        ]
    },
    "line-smooth": {
        "default": 0,
        "description": "Smooths out geometry angles. 0 is no smoothing, 1 is fully smoothed. Values greater than 1 will produce wild, looping geometries.",
        "type": "float"
    },
    "line-width": {
        "default": 1,
        "description": "The width of a line in pixels.",
        "type": "float"
    },
    "marker-allow-overlap": {
        "default": False,
        "description": "Control whether overlapping markers are shown or hidden.",
        "type": "boolean"
    },
    "marker-avoid-edges": {
        "default": False,
        "description": "Avoid placing markers that intersect with tile boundaries.",
        "type": "boolean"
    },
    "marker-clip": {
        "default": False,
        "description": "Turning on clipping can help performance in the case that the boundaries of the geometry extent outside of tile extents. But clipping can result in undesirable rendering artifacts in rare cases.",
        "type": "boolean"
    },
    "marker-comp-op": {
        "default": "src-over",
        "description": "Composite operation. This defines how this symbolizer should behave relative to symbolizers atop or below it.",
        "type": "keyword",
        "values": [
            "clear",
            "src",
            "dst",
            "src-over",
            "dst-over",
            "src-in",
            "dst-in",
            "src-out",
            "dst-out",
            "src-atop",
            "dst-atop",
            "xor",
            "plus",
            "minus",
            "multiply",
            "divide",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "linear-dodge",
            "linear-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "contrast",
            "invert",
            "invert-rgb",
            "grain-merge",
            "grain-extract",
            "hue",
            "saturation",
            "color",
            "value"
        ]
    },
    "marker-direction": {
        "default": "right",
        "description": "How markers should be placed along lines. With the \"auto\" setting when marker is upside down the marker is automatically rotated by 180 degrees to keep it upright. The \"auto-down\" value places marker in the opposite orientation to \"auto\". The \"left\" or \"right\" settings can be used to force marker to always be placed along a line in a given direction and therefore disables rotating if marker appears upside down. The \"left-only\" or \"right-only\" properties also force a given direction but will discard upside down markers rather than trying to flip it. The \"up\" and \"down\" settings don't adjust marker's orientation to the line direction.",
        "type": "keyword",
        "values": [
            "auto",
            "auto-down",
            "left",
            "right",
            "left-only",
            "right-only",
            "up",
            "down"
        ]
    },
    "marker-file": {
        "default": None,
        "description": "A file that this marker shows at each placement. If no file is given, the marker will show an ellipse. Accepted formats: svg, jpg, png, tiff, and webp.",
        "type": "uri"
    },
    "marker-fill": {
        "default": "blue",
        "description": "The color of the area of the marker. This property will also set the fill of elements in an SVG loaded from a file.",
        "type": "color"
    },
    "marker-fill-opacity": {
        "default": 1,
        "description": "The fill opacity of the marker. This property will also set the fill-opacity of elements in an SVG loaded from a file.",
        "type": "float"
    },
    "marker-geometry-transform": {
        "default": None,
        "description": "Transform marker geometry with specified function.",
        "type": "functions",
        "values": [
            "matrix",
            "translate",
            "scale",
            "rotate",
            "skewX",
            "skewY"
        ]
    },
    "marker-height": {
        "default": 10,
        "description": "The height of the marker, if using one of the default types.",
        "type": "float"
    },
    "marker-ignore-placement": {
        "default": False,
        "description": "Value to control whether the placement of the feature will prevent the placement of other features.",
        "type": "boolean"
    },
    "marker-line-color": {
        "default": "black",
        "description": "The color of the stroke around the marker. This property will also set the stroke of elements in an SVG loaded from a file.",
        "type": "color"
    },
    "marker-line-opacity": {
        "default": 1,
        "description": "The opacity of a line.",
        "type": "float"
    },
    "marker-line-width": {
        "default": 0.5,
        "description": "The width of the stroke around the marker, in pixels. This is positioned on the boundary, so high values can cover the area itself. This property will also set the stroke-width of elements in an SVG loaded from a file.",
        "type": "float"
    },
    "marker-max-error": {
        "default": 0.2,
        "description": "N/A: not intended to be changed.",
        "type": "float"
    },
    "marker-multi-policy": {
        "default": "each",
        "description": "A special setting to allow the user to control rendering behavior for 'multi-geometries' (when a feature contains multiple geometries). This setting does not apply to markers placed along lines. The 'each' policy is default and means all geometries will get a marker. The 'whole' policy means that the aggregate centroid between all geometries will be used. The 'largest' policy means that only the largest (by bounding box areas) feature will get a rendered marker (this is how text labeling behaves by default).",
        "type": "keyword",
        "values": [
            "each",
            "whole",
            "largest"
        ]
    },
    "marker-offset": {
        "default": 0,
        "description": "Offsets a marker from a line a number of pixels parallel to its actual path. Positive values move the marker left, negative values move it right (relative to the directionality of the line).",
        "type": "float"
    },
    "marker-opacity": {
        "default": 1,
        "description": "The overall opacity of the marker, if set, overrides both the opacity of the fill and the opacity of the stroke.",
        "type": "float"
    },
    "marker-placement": {
        "default": "point",
        "description": "Attempt to place markers on a point, in the center of a polygon, or if markers-placement:line, then multiple times along a line. 'interior' placement can be used to ensure that points placed on polygons are forced to be inside the polygon interior. The 'vertex-first' and 'vertex-last' options can be used to place markers at the first or last vertex of lines or polygons.",
        "type": "keyword",
        "values": [
            "point",
            "line",
            "interior",
            "vertex-first",
            "vertex-last"
        ]
    },
    "marker-simplify": {
        "default": 0,
        "description": "geometries are simplified by the given tolerance.",
        "type": "float"
    },
    "marker-simplify-algorithm": {
        "default": "radial-distance",
        "description": "geometries are simplified by the given algorithm.",
        "type": "keyword",
        "values": [
            "radial-distance",
            "zhao-saalfeld",
            "visvalingam-whyatt"
        ]
    },
    "marker-smooth": {
        "default": 0,
        "description": "Smooths out geometry angles. 0 is no smoothing, 1 is fully smoothed. Values greater than 1 will produce wild, looping geometries.",
        "type": "float"
    },
    "marker-spacing": {
        "default": 100,
        "description": "Space between repeated markers in pixels. If the spacing is less than the marker size or larger than the line segment length then no marker will be placed. Any value less than 1 will be ignored and the default will be used instead.",
        "type": "float"
    },
    "marker-transform": {
        "default": None,
        "description": "Transform marker instance with specified function. Ignores map scale factor.",
        "type": "functions",
        "values": [
            "matrix",
            "translate",
            "scale",
            "rotate",
            "skewX",
            "skewY"
        ]
    },
    "marker-type": {
        "default": "ellipse",
        "description": "The default marker-type. If a SVG file is not given as the marker-file parameter, the renderer provides either an arrow or an ellipse (a circle if height is equal to width).",
        "type": "keyword",
        "values": [
            "arrow",
            "ellipse"
        ]
    },
    "marker-width": {
        "default": 10,
        "description": "The width of the marker, if using one of the default types.",
        "type": "float"
    },
    "maximum-extent": {
        "default": "-20037508.34,-20037508.34,20037508.34,20037508.34",
        "description": "An extent to be used to limit the bounds used to query all layers during rendering. Should be minx, miny, maxx, maxy in the coordinates of the Map.",
        "type": "string"
    },
    "opacity": {
        "default": 1,
        "description": "An alpha value for the style (which means an alpha applied to all features in separate buffer and then composited back to main buffer).",
        "type": "float"
    },
    "point-allow-overlap": {
        "default": False,
        "description": "Control whether overlapping points are shown or hidden.",
        "type": "boolean"
    },
    "point-comp-op": {
        "default": "src-over",
        "description": "Composite operation. This defines how this symbolizer should behave relative to symbolizers atop or below it.",
        "type": "keyword",
        "values": [
            "clear",
            "src",
            "dst",
            "src-over",
            "dst-over",
            "src-in",
            "dst-in",
            "src-out",
            "dst-out",
            "src-atop",
            "dst-atop",
            "xor",
            "plus",
            "minus",
            "multiply",
            "divide",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "linear-dodge",
            "linear-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "contrast",
            "invert",
            "invert-rgb",
            "grain-merge",
            "grain-extract",
            "hue",
            "saturation",
            "color",
            "value"
        ]
    },
    "point-file": {
        "default": None,
        "description": "Image file to represent a point. Accepted formats: svg, jpg, png, tiff, and webp.",
        "type": "uri"
    },
    "point-ignore-placement": {
        "default": False,
        "description": "Control whether the placement of the feature will prevent the placement of other features.",
        "type": "boolean"
    },
    "point-opacity": {
        "default": 1,
        "description": "A value from 0 to 1 to control the opacity of the point.",
        "type": "float"
    },
    "point-placement": {
        "default": "centroid",
        "description": "Control how this point should be placed. Centroid calculates the geometric center of a polygon, which can be outside of it, while interior always places inside of a polygon.",
        "type": "keyword",
        "values": [
            "centroid",
            "interior"
        ]
    },
    "point-transform": {
        "default": None,
        "description": "Transform point instance with specified function. Ignores map scale factor.",
        "type": "functions",
        "values": [
            "matrix",
            "translate",
            "scale",
            "rotate",
            "skewX",
            "skewY"
        ]
    },
    "polygon-clip": {
        "default": False,
        "description": "Turning on clipping can help performance in the case that the boundaries of the geometry extend outside of tile extents. But clipping can result in undesirable rendering artifacts in rare cases.",
        "type": "boolean"
    },
    "polygon-comp-op": {
        "default": "src-over",
        "description": "Composite operation. This defines how this symbolizer should behave relative to symbolizers atop or below it.",
        "type": "keyword",
        "values": [
            "clear",
            "src",
            "dst",
            "src-over",
            "dst-over",
            "src-in",
            "dst-in",
            "src-out",
            "dst-out",
            "src-atop",
            "dst-atop",
            "xor",
            "plus",
            "minus",
            "multiply",
            "divide",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "linear-dodge",
            "linear-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "contrast",
            "invert",
            "invert-rgb",
            "grain-merge",
            "grain-extract",
            "hue",
            "saturation",
            "color",
            "value"
        ]
    },
    "polygon-fill": {
        "default": "The color gray will be used for fill.",
        "description": "Fill color to assign to a polygon.",
        "type": "color"
    },
    "polygon-gamma": {
        "default": 1,
        "description": "Level of antialiasing of polygon edges.",
        "type": "float"
    },
    "polygon-gamma-method": {
        "default": "power",
        "description": "An Antigrain Geometry specific rendering hint to control the quality of antialiasing. Under the hood in Mapnik this method is used in combination with the 'gamma' value (which defaults to 1). The methods are in the AGG source at https://github.com/mapnik/mapnik/blob/master/deps/agg/include/agg_gamma_functions.",
        "type": "keyword",
        "values": [
            "power",
            "linear",
            "none",
            "threshold",
            "multiply"
        ]
    },
    "polygon-geometry-transform": {
        "default": None,
        "description": "Transform polygon geometry with specified function.",
        "type": "functions",
        "values": [
            "matrix",
            "translate",
            "scale",
            "rotate",
            "skewX",
            "skewY"
        ]
    },
    "polygon-opacity": {
        "default": 1,
        "description": "The opacity of the polygon.",
        "type": "float"
    },
    "polygon-pattern-alignment": {
        "default": "global",
        "description": "Specify whether to align pattern fills to the layer's geometry (local) or to the map (global).",
        "type": "keyword",
        "values": [
            "global",
            "local"
        ]
    },
    "polygon-pattern-clip": {
        "default": False,
        "description": "Turning on clipping can help performance in the case that the boundaries of the geometry extent outside of tile extents. But clipping can result in undesirable rendering artifacts in rare cases.",
        "type": "boolean"
    },
    "polygon-pattern-comp-op": {
        "default": "src-over",
        "description": "Composite operation. This defines how this symbolizer should behave relative to symbolizers atop or below it.",
        "type": "keyword",
        "values": [
            "clear",
            "src",
            "dst",
            "src-over",
            "dst-over",
            "src-in",
            "dst-in",
            "src-out",
            "dst-out",
            "src-atop",
            "dst-atop",
            "xor",
            "plus",
            "minus",
            "multiply",
            "divide",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "linear-dodge",
            "linear-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "contrast",
            "invert",
            "invert-rgb",
            "grain-merge",
            "grain-extract",
            "hue",
            "saturation",
            "color",
            "value"
        ]
    },
    "polygon-pattern-file": {
        "default": None,
        "description": "Image to use as a repeated pattern fill within a polygon. Accepted formats: svg, jpg, png, tiff, and webp.",
        "type": "uri"
    },
    "polygon-pattern-gamma": {
        "default": 1,
        "description": "Level of antialiasing of polygon pattern edges.",
        "type": "float"
    },
    "polygon-pattern-geometry-transform": {
        "default": None,
        "description": "Transform polygon geometry with specified function and apply pattern to transformed geometry.",
        "type": "functions",
        "values": [
            "matrix",
            "translate",
            "scale",
            "rotate",
            "skewX",
            "skewY"
        ]
    },
    "polygon-pattern-opacity": {
        "default": 1,
        "description": "Apply an opacity level to the image used for the pattern.",
        "type": "float"
    },
    "polygon-pattern-simplify": {
        "default": 0,
        "description": "geometries are simplified by the given tolerance.",
        "type": "float"
    },
    "polygon-pattern-simplify-algorithm": {
        "default": "radial-distance",
        "description": "geometries are simplified by the given algorithm.",
        "type": "keyword",
        "values": [
            "radial-distance",
            "zhao-saalfeld",
            "visvalingam-whyatt"
        ]
    },
    "polygon-pattern-smooth": {
        "default": 0,
        "description": "Smooths out geometry angles. 0 is no smoothing, 1 is fully smoothed. Values greater than 1 will produce wild, looping geometries.",
        "type": "float"
    },
    "polygon-pattern-transform": {
        "default": None,
        "description": "Transform polygon pattern instance with specified function.",
        "type": "functions",
        "values": [
            "matrix",
            "translate",
            "scale",
            "rotate",
            "skewX",
            "skewY"
        ]
    },
    "polygon-simplify": {
        "default": 0,
        "description": "Simplify geometries by the given tolerance.",
        "type": "float"
    },
    "polygon-simplify-algorithm": {
        "default": "radial-distance",
        "description": "Simplify geometries by the given algorithm.",
        "type": "keyword",
        "values": [
            "radial-distance",
            "zhao-saalfeld",
            "visvalingam-whyatt"
        ]
    },
    "polygon-smooth": {
        "default": 0,
        "description": "Smooths out geometry angles. 0 is no smoothing, 1 is fully smoothed. Values greater than 1 will produce wild, looping geometries.",
        "type": "float"
    },
    "raster-colorizer-default-color": {
        "default": "transparent",
        "description": "This can be any color. Sets the color that is applied to all values outside of the range of the colorizer-stops. If not supplied pixels will be fully transparent.",
        "type": "color"
    },
    "raster-colorizer-default-mode": {
        "default": "linear",
        "description": "This can be either discrete, linear or exact. If it is not specified then the default is linear.",
        "type": "keyword",
        "values": [
            "discrete",
            "linear",
            "exact"
        ]
    },
    "raster-colorizer-epsilon": {
        "default": 1.1920928955078125e-07,
        "description": "This can be any positive floating point value and will be used as a tolerance in floating point comparisions. The higher the value the more likely a stop will match and color data.",
        "type": "float"
    },
    "raster-colorizer-stops": {
        "default": "",
        "description": "Assigns raster data values to colors. Stops must be listed in ascending order, and contain at a minimum the value and the associated color. You can also include the color-mode as a third argument, like stop(100,#fff,exact).",
        "type": "tags"
    },
    "raster-comp-op": {
        "default": "src-over",
        "description": "Composite operation. This defines how this symbolizer should behave relative to symbolizers atop or below it.",
        "type": "keyword",
        "values": [
            "clear",
            "src",
            "dst",
            "src-over",
            "dst-over",
            "src-in",
            "dst-in",
            "src-out",
            "dst-out",
            "src-atop",
            "dst-atop",
            "xor",
            "plus",
            "minus",
            "multiply",
            "divide",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "linear-dodge",
            "linear-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "contrast",
            "invert",
            "invert-rgb",
            "grain-merge",
            "grain-extract",
            "hue",
            "saturation",
            "color",
            "value"
        ]
    },
    "raster-filter-factor": {
        "default": -1,
        "description": "This is used by the Raster or Gdal datasources to pre-downscale images using overviews. Higher numbers can sometimes cause much better scaled image output, at the cost of speed.",
        "type": "float"
    },
    "raster-mesh-size": {
        "default": 16,
        "description": "A reduced resolution mesh is used for raster reprojection, and the total image size is divided by the mesh-size to determine the quality of that mesh. Values for mesh-size larger than the default will result in faster reprojection but might lead to distortion.",
        "type": "unsigned"
    },
    "raster-opacity": {
        "default": 1,
        "description": "The opacity of the raster symbolizer on top of other symbolizers.",
        "type": "float"
    },
    "raster-scaling": {
        "default": "near",
        "description": "The scaling algorithm used to making different resolution versions of this raster layer. Bilinear is a good compromise between speed and accuracy, while lanczos gives the highest quality.",
        "type": "keyword",
        "values": [
            "near",
            "fast",
            "bilinear",
            "bicubic",
            "spline16",
            "spline36",
            "hanning",
            "hamming",
            "hermite",
            "kaiser",
            "quadric",
            "catrom",
            "gaussian",
            "bessel",
            "mitchell",
            "sinc",
            "lanczos",
            "blackman"
        ]
    },
    "shield-allow-overlap": {
        "default": False,
        "description": "Control whether overlapping shields are shown or hidden.",
        "type": "boolean"
    },
    "shield-avoid-edges": {
        "default": False,
        "description": "Avoid placing shields that intersect with tile boundaries.",
        "type": "boolean"
    },
    "shield-character-spacing": {
        "default": 0,
        "description": "Horizontal spacing between characters (in pixels). Currently works for point placement only, not line placement.",
        "type": "unsigned"
    },
    "shield-clip": {
        "default": False,
        "description": "Turning on clipping can help performance in the case that the boundaries of the geometry extent outside of tile extents. But clipping can result in undesirable rendering artifacts in rare cases.",
        "type": "boolean"
    },
    "shield-comp-op": {
        "default": "src-over",
        "description": "Composite operation. This defines how this symbolizer should behave relative to symbolizers atop or below it.",
        "type": "keyword",
        "values": [
            "clear",
            "src",
            "dst",
            "src-over",
            "dst-over",
            "src-in",
            "dst-in",
            "src-out",
            "dst-out",
            "src-atop",
            "dst-atop",
            "xor",
            "plus",
            "minus",
            "multiply",
            "divide",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "linear-dodge",
            "linear-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "contrast",
            "invert",
            "invert-rgb",
            "grain-merge",
            "grain-extract",
            "hue",
            "saturation",
            "color",
            "value"
        ]
    },
    "shield-dx": {
        "default": 0,
        "description": "Displace shield by fixed amount, in pixels, +/- along the X axis.  A positive value will shift the text right.",
        "type": "float"
    },
    "shield-dy": {
        "default": 0,
        "description": "Displace shield by fixed amount, in pixels, +/- along the Y axis.  A positive value will shift the text down.",
        "type": "float"
    },
    "shield-face-name": {
        "default": None,
        "description": "Font name and style to use for the shield text.",
        "type": "string"
    },
    "shield-file": {
        "default": None,
        "description": "Image file to render behind the shield text. Accepted formats: svg, jpg, png, tiff, and webp.",
        "type": "uri"
    },
    "shield-fill": {
        "default": "black",
        "description": "The color of the shield text.",
        "type": "color"
    },
    "shield-halo-comp-op": {
        "default": "src-over",
        "description": "Composite operation. This defines how this symbolizer should behave relative to symbolizers atop or below it.",
        "type": "keyword",
        "values": [
            "clear",
            "src",
            "dst",
            "src-over",
            "dst-over",
            "src-in",
            "dst-in",
            "src-out",
            "dst-out",
            "src-atop",
            "dst-atop",
            "xor",
            "plus",
            "minus",
            "multiply",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "contrast",
            "invert",
            "invert-rgb",
            "grain-merge",
            "grain-extract",
            "hue",
            "saturation",
            "color",
            "value"
        ]
    },
    "shield-halo-fill": {
        "default": "white",
        "description": "Specifies the color of the halo around the text.",
        "type": "color"
    },
    "shield-halo-opacity": {
        "default": 1,
        "description": "A number from 0 to 1 specifying the opacity for the text halo.",
        "type": "float"
    },
    "shield-halo-radius": {
        "default": 0,
        "description": "Specify the radius of the halo in pixels.",
        "type": "float"
    },
    "shield-halo-rasterizer": {
        "default": "full",
        "description": "Exposes an alternate text halo rendering method that sacrifices quality for speed.",
        "type": "keyword",
        "values": [
            "full",
            "fast"
        ]
    },
    "shield-halo-transform": {
        "default": "",
        "description": "Transform shield halo relative to the actual text with specified function. Allows for shadow or embossed effects. Ignores map scale factor.",
        "type": "functions",
        "values": [
            "matrix",
            "translate",
            "scale",
            "rotate",
            "skewX",
            "skewY"
        ]
    },
    "shield-horizontal-alignment": {
        "default": "auto",
        "description": "The shield's horizontal alignment from its centerpoint.",
        "type": "keyword",
        "values": [
            "left",
            "middle",
            "right",
            "auto"
        ]
    },
    "shield-justify-alignment": {
        "default": "auto",
        "description": "Define how text in a shield's label is justified.",
        "type": "keyword",
        "values": [
            "left",
            "center",
            "right",
            "auto"
        ]
    },
    "shield-label-position-tolerance": {
        "default": "shield-spacing/2.0",
        "description": "Allows the shield to be displaced from its ideal position by a number of pixels (only works with placement:line).",
        "type": "float"
    },
    "shield-line-spacing": {
        "default": 0,
        "description": "Vertical spacing between lines of multiline labels (in pixels).",
        "type": "float"
    },
    "shield-margin": {
        "default": 0,
        "description": "Minimum distance that a shield can be placed from any other text, shield, or marker.",
        "type": "float"
    },
    "shield-min-distance": {
        "default": 0,
        "description": "Minimum distance to the next shield with the same text. Only works for line placement.",
        "type": "float"
    },
    "shield-min-padding": {
        "default": 0,
        "description": "Minimum distance a shield will be placed from the edge of a tile. This option is similar to shield-avoid-edges:True except that the extra margin is used to discard cases where the shield+margin are not fully inside the tile.",
        "type": "float"
    },
    "shield-name": {
        "default": "",
        "description": "Value to use for a shield\"s text label. Data columns are specified using brackets like [column_name].",
        "type": "string"
    },
    "shield-opacity": {
        "default": 1,
        "description": "The opacity of the image used for the shield.",
        "type": "float"
    },
    "shield-placement": {
        "default": "point",
        "description": "How this shield should be placed. Point placement places one shield on top of a point geometry and at the centroid of a polygon or the middle point of a line, line places along lines multiple times per feature, vertex places on the vertexes of polygons, and interior attempts to place inside of a polygon.",
        "type": "keyword",
        "values": [
            "point",
            "line",
            "vertex",
            "interior"
        ]
    },
    "shield-placement-type": {
        "default": "dummy",
        "description": "Re-position and/or re-size shield to avoid overlaps. \"simple\" for basic algorithm (using shield-placements string,) \"dummy\" to turn this feature off.",
        "type": "keyword",
        "values": [
            "dummy",
            "simple",
            "list"
        ]
    },
    "shield-placements": {
        "default": "",
        "description": "If \"placement-type\" is set to \"simple\", use this \"POSITIONS,[SIZES]\" string. An example is shield-placements: \"E,NE,SE,W,NW,SW\";.",
        "type": "string"
    },
    "shield-repeat-distance": {
        "default": 0,
        "description": "Minimum distance between repeated shields. If set this will prevent shields being rendered nearby each other that contain the same text. Similar to shield-min-distance with the difference that it works the same no matter what placement strategy is used.",
        "type": "float"
    },
    "shield-simplify": {
        "default": 0,
        "description": "Simplify the geometries used for shield placement by the given tolerance.",
        "type": "float"
    },
    "shield-simplify-algorithm": {
        "default": "radial-distance",
        "description": "Simplify the geometries used for shield placement by the given algorithm.",
        "type": "keyword",
        "values": [
            "radial-distance",
            "zhao-saalfeld",
            "visvalingam-whyatt"
        ]
    },
    "shield-size": {
        "default": 10,
        "description": "The size of the shield text in pixels.",
        "type": "float"
    },
    "shield-smooth": {
        "default": 0,
        "description": "Smooths out the angles of the geometry used for shield placement. 0 is no smoothing, 1 is fully smoothed. Values greater than 1 will produce wild, looping geometries.",
        "type": "float"
    },
    "shield-spacing": {
        "default": 0,
        "description": "Distance the renderer should use to try to place repeated shields on a line.",
        "type": "float"
    },
    "shield-text-dx": {
        "default": 0,
        "description": "Displace text within shield by fixed amount, in pixels, +/- along the X axis.  A positive value will shift the shield right.",
        "type": "float"
    },
    "shield-text-dy": {
        "default": 0,
        "description": "Displace text within shield by fixed amount, in pixels, +/- along the Y axis.  A positive value will shift the shield down.",
        "type": "float"
    },
    "shield-text-opacity": {
        "default": 1,
        "description": "The opacity of the text placed on top of the shield.",
        "type": "float"
    },
    "shield-text-transform": {
        "default": None,
        "description": "Transform the case of the characters.",
        "type": "keyword",
        "values": [
            "none",
            "uppercase",
            "lowercase",
            "capitalize",
            "reverse"
        ]
    },
    "shield-transform": {
        "default": None,
        "description": "Transform shield instance with specified function. Ignores map scale factor.",
        "type": "functions",
        "values": [
            "matrix",
            "translate",
            "scale",
            "rotate",
            "skewX",
            "skewY"
        ]
    },
    "shield-unlock-image": {
        "default": False,
        "description": "This parameter should be set to True if you are trying to position text beside rather than on top of the shield image.",
        "type": "boolean"
    },
    "shield-vertical-alignment": {
        "default": "middle",
        "description": "The shield's vertical alignment from its centerpoint.",
        "type": "keyword",
        "values": [
            "top",
            "middle",
            "bottom",
            "auto"
        ]
    },
    "shield-wrap-before": {
        "default": False,
        "description": "Wrap text before wrap-width is reached.",
        "type": "boolean"
    },
    "shield-wrap-character": {
        "default": None,
        "description": "Use this character instead of a space to wrap long names.",
        "type": "string"
    },
    "shield-wrap-width": {
        "default": 0,
        "description": "Length of a chunk of text in pixels before wrapping text. If set to zero, text doesn't wrap.",
        "type": "unsigned"
    },
    "srs": {
        "default": "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs",
        "description": "Map spatial reference (proj4 string).",
        "type": "string"
    },
    "text-align": {
        "default": "auto",
        "description": "Define how text is justified.",
        "type": "keyword",
        "values": [
            "left",
            "right",
            "center",
            "auto"
        ]
    },
    "text-allow-overlap": {
        "default": False,
        "description": "Control whether overlapping text is shown or hidden.",
        "type": "boolean"
    },
    "text-avoid-edges": {
        "default": False,
        "description": "Avoid placing labels that intersect with tile boundaries.",
        "type": "boolean"
    },
    "text-character-spacing": {
        "default": 0,
        "description": "Horizontal spacing adjustment between characters in pixels. This value is ignored when horizontal-alignment is set to adjust. Typographic ligatures are turned off when this value is greater than zero.",
        "type": "float"
    },
    "text-clip": {
        "default": False,
        "description": "Turning on clipping can help performance in the case that the boundaries of the geometry extent outside of tile extents. But clipping can result in undesirable rendering artifacts in rare cases.",
        "type": "boolean"
    },
    "text-comp-op": {
        "default": "src-over",
        "description": "Composite operation. This defines how this symbolizer should behave relative to symbolizers atop or below it.",
        "type": "keyword",
        "values": [
            "clear",
            "src",
            "dst",
            "src-over",
            "dst-over",
            "src-in",
            "dst-in",
            "src-out",
            "dst-out",
            "src-atop",
            "dst-atop",
            "xor",
            "plus",
            "minus",
            "multiply",
            "divide",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "linear-dodge",
            "linear-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "contrast",
            "invert",
            "invert-rgb",
            "grain-merge",
            "grain-extract",
            "hue",
            "saturation",
            "color",
            "value"
        ]
    },
    "text-dx": {
        "default": 0,
        "description": "Displace text by fixed amount, in pixels, +/- along the X axis.  With \"dummy\" placement-type, a positive value displaces to the right. With \"simple\" placement-type, it is either left, right or unchanged, depending on the placement selected. Any non-zero value implies \"horizontal-alignment\" changes to \"left\" by default. Has no effect with 'line' text-placement-type.",
        "type": "float"
    },
    "text-dy": {
        "default": 0,
        "description": "Displace text by fixed amount, in pixels, +/- along the Y axis.  With \"dummy\" placement-type, a positive value displaces downwards. With \"simple\" placement-type, it is either up, down or unchanged, depending on the placement selected. With \"line\" placement-type, a positive value displaces above the path.",
        "type": "float"
    },
    "text-face-name": {
        "default": None,
        "description": "Font name and style to render a label in.",
        "type": "string"
    },
    "text-fill": {
        "default": "black",
        "description": "Specifies the color for the text.",
        "type": "color"
    },
    "text-font-feature-settings": {
        "default": "",
        "description": "Comma separated list of OpenType typographic features. The syntax and semantics conforms to font-feature-settings from W3C CSS.",
        "type": "string"
    },
    "text-halo-comp-op": {
        "default": "src-over",
        "description": "Composite operation. This defines how this symbolizer should behave relative to symbolizers atop or below it.",
        "type": "keyword",
        "values": [
            "clear",
            "src",
            "dst",
            "src-over",
            "dst-over",
            "src-in",
            "dst-in",
            "src-out",
            "dst-out",
            "src-atop",
            "dst-atop",
            "xor",
            "plus",
            "minus",
            "multiply",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "color-burn",
            "hard-light",
            "soft-light",
            "difference",
            "exclusion",
            "contrast",
            "invert",
            "invert-rgb",
            "grain-merge",
            "grain-extract",
            "hue",
            "saturation",
            "color",
            "value"
        ]
    },
    "text-halo-fill": {
        "default": "white",
        "description": "Specifies the color of the halo around the text.",
        "type": "color"
    },
    "text-halo-opacity": {
        "default": 1,
        "description": "A number from 0 to 1 specifying the opacity for the text halo.",
        "type": "float"
    },
    "text-halo-radius": {
        "default": 0,
        "description": "Specify the radius of the halo in pixels.",
        "type": "float"
    },
    "text-halo-rasterizer": {
        "default": "full",
        "description": "Exposes an alternate text halo rendering method that sacrifices quality for speed.",
        "type": "keyword",
        "values": [
            "full",
            "fast"
        ]
    },
    "text-halo-transform": {
        "default": "",
        "description": "Transform text halo relative to the actual text with specified function. Allows for shadow or embossed effects. Ignores map scale factor.",
        "type": "functions",
        "values": [
            "matrix",
            "translate",
            "scale",
            "rotate",
            "skewX",
            "skewY"
        ]
    },
    "text-horizontal-alignment": {
        "default": "auto",
        "description": "The text's horizontal alignment from it's centerpoint. If placement is set to line, then adjust can be set to auto-fit the text to the length of the path by dynamically calculating character-spacing.",
        "type": "keyword",
        "values": [
            "left",
            "middle",
            "right",
            "auto",
            "adjust"
        ]
    },
    "text-label-position-tolerance": {
        "default": "text-spacing/2.0",
        "description": "Allows the label to be displaced from its ideal position by a number of pixels (only works with placement:line).",
        "type": "float"
    },
    "text-largest-bbox-only": {
        "default": True,
        "description": "Controls default labeling behavior on multipolygons. The default is True and means that only the polygon with largest bbox is labeled.",
        "type": "boolean"
    },
    "text-line-spacing": {
        "default": 0,
        "description": "Vertical spacing adjustment between lines in pixels.",
        "type": "float"
    },
    "text-margin": {
        "default": 0,
        "description": "Minimum distance that a label can be placed from any other text, shield, or marker.",
        "type": "float"
    },
    "text-max-char-angle-delta": {
        "default": 22.5,
        "description": "The maximum angle change, in degrees, allowed between adjacent characters in a label. This value internally is converted to radians to the default is 22.5*math.pi/180.0. The higher the value the fewer labels will be placed around around sharp corners.",
        "type": "float"
    },
    "text-min-distance": {
        "default": 0,
        "description": "Minimum distance to the next label with the same text. Only works for line placement. Deprecated: replaced by text-repeat-distance and text-margin",
        "type": "float"
    },
    "text-min-padding": {
        "default": 0,
        "description": "Minimum distance a text label will be placed from the edge of a tile. This option is similar to shield-avoid-edges:True except that the extra margin is used to discard cases where the shield+margin are not fully inside the tile.",
        "type": "float"
    },
    "text-min-path-length": {
        "default": 0,
        "description": "Place labels only on polygons and lines with a bounding width longer than this value (in pixels).",
        "type": "float"
    },
    "text-name": {
        "default": None,
        "description": "Value to use for a text label. Data columns are specified using brackets like [column_name].",
        "type": "string"
    },
    "text-opacity": {
        "default": 1,
        "description": "A number from 0 to 1 specifying the opacity for the text.",
        "type": "float"
    },
    "text-orientation": {
        "default": 0,
        "description": "Rotate the text. (only works with text-placement:point).",
        "type": "float"
    },
    "text-placement": {
        "default": "point",
        "description": "How this label should be placed. Point placement places one label on top of a point geometry and at the centroid of a polygon or the middle point of a line, line places along lines multiple times per feature, vertex places on the vertexes of polygons, and interior attempts to place inside of a polygon.",
        "type": "keyword",
        "values": [
            "point",
            "line",
            "vertex",
            "interior"
        ]
    },
    "text-placement-type": {
        "default": "dummy",
        "description": "Re-position and/or re-size text to avoid overlaps. \"simple\" for basic algorithm (using text-placements string,) \"dummy\" to turn this feature off.",
        "type": "keyword",
        "values": [
            "dummy",
            "simple",
            "list"
        ]
    },
    "text-placements": {
        "default": "",
        "description": "If \"placement-type\" is set to \"simple\", use this \"POSITIONS,[SIZES]\" string. An example is text-placements: \"E,NE,SE,W,NW,SW\";.",
        "type": "string"
    },
    "text-ratio": {
        "default": 0,
        "description": "Define the amount of text (of the total) present on successive lines when wrapping occurs.",
        "type": "unsigned"
    },
    "text-repeat-distance": {
        "default": 0,
        "description": "Minimum distance between repeated text. If set this will prevent text labels being rendered nearby each other that contain the same text. Similar to text-min-distance with the difference that it works the same no matter what placement strategy is used.",
        "type": "float"
    },
    "text-repeat-wrap-character": {
        "default": False,
        "description": "Keep the character used to wrap a line instead of removing it, and repeat it on the new line.",
        "type": "boolean"
    },
    "text-rotate-displacement": {
        "default": False,
        "description": "Rotates the displacement around the placement origin by the angle given by \"orientation\".",
        "type": "boolean"
    },
    "text-simplify": {
        "default": 0,
        "description": "Simplify the geometries used for text placement by the given tolerance.",
        "type": "float"
    },
    "text-simplify-algorithm": {
        "default": "radial-distance",
        "description": "Simplify the geometries used for text placement by the given algorithm.",
        "type": "keyword",
        "values": [
            "radial-distance",
            "zhao-saalfeld",
            "visvalingam-whyatt"
        ]
    },
    "text-size": {
        "default": 10,
        "description": "Text size in pixels.",
        "type": "float"
    },
    "text-smooth": {
        "default": 0,
        "description": "Smooths out the angles of the geometry used for text placement. 0 is no smoothing, 1 is fully smoothed. Values greater than 1 will produce wild, looping geometries.",
        "type": "float"
    },
    "text-spacing": {
        "default": 0,
        "description": "Distance the renderer should use to try to place repeated text labels on a line.",
        "type": "unsigned"
    },
    "text-transform": {
        "default": None,
        "description": "Transform the case of the characters.",
        "type": "keyword",
        "values": [
            "none",
            "uppercase",
            "lowercase",
            "capitalize",
            "reverse"
        ]
    },
    "text-upright": {
        "default": "auto",
        "description": "How this label should be placed along lines. By default when more than half of a label's characters are upside down the label is automatically flipped to keep it upright. By changing this parameter you can prevent this \"auto-upright\" behavior. The \"auto-down\" value places text in the opposite orientation to \"auto\". The \"left\" or \"right\" settings can be used to force text to always be placed along a line in a given direction and therefore disables flipping if text appears upside down. The \"left-only\" or \"right-only\" properties also force a given direction but will discard upside down text rather than trying to flip it.",
        "type": "keyword",
        "values": [
            "auto",
            "auto-down",
            "left",
            "right",
            "left-only",
            "right-only"
        ]
    },
    "text-vertical-alignment": {
        "default": "auto",
        "description": "Position of label relative to point position.",
        "type": "keyword",
        "values": [
            "top",
            "middle",
            "bottom",
            "auto"
        ]
    },
    "text-wrap-before": {
        "default": False,
        "description": "Wrap text before wrap-width is reached.",
        "type": "boolean"
    },
    "text-wrap-character": {
        "default": None,
        "description": "Use this character instead of a space to wrap long text.",
        "type": "string"
    },
    "text-wrap-width": {
        "default": 0,
        "description": "Length of a chunk of text in pixels before wrapping text. If set to zero, text doesn't wrap.",
        "type": "unsigned"
    }
}
