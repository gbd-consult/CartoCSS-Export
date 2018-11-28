"""Various Qgis constants."""

WkbType = {
    0: 'unknown',
    1: 'point',
    2: 'linestring',
    3: 'polygon',
    4: 'multipoint',
    5: 'multilinestring',
    6: 'multipolygon'
}

SymbolType = {
    0: 'Marker',
    1: 'Line',
    2: 'Fill',
    3: 'Hybrid'
}

LabelDefaults = {
    "addDirectionSymbol": "0",
    "angleOffset": "0",
    "blendMode": "0",
    "bufferBlendMode": "0",
    "bufferColor": "255,255,255,255",
    "bufferDraw": "0",
    "bufferJoinStyle": "64",
    "bufferNoFill": "0",
    "bufferSize": "1",
    "bufferSizeInMapUnits": "0",
    "bufferSizeMapUnitScale": "0,0,0,0,0,0",
    "bufferTransp": "0",
    "centroidInside": "0",
    "centroidWhole": "0",
    "decimals": "3",
    "displayAll": "0",
    "dist": "0",
    "distInMapUnits": "0",
    "distMapUnitScale": "0,0,0,0,0,0",
    "fitInPolygonOnly": "0",
    "fontCapitals": "0",
    "fontItalic": "0",
    "fontLetterSpacing": "0",
    "fontLimitPixelSize": "0",
    "fontMaxPixelSize": "10000",
    "fontMinPixelSize": "3",
    "fontSizeInMapUnits": "0",
    "fontSizeMapUnitScale": "0,0,0,0,0,0",
    "fontStrikeout": "0",
    "fontUnderline": "0",
    "fontWeight": "50",
    "fontWordSpacing": "0",
    "formatNumbers": "0",
    "isExpression": "0",
    "labelOffsetInMapUnits": "1",
    "labelOffsetMapUnitScale": "0,0,0,0,0,0",
    "labelPerPart": "0",
    "leftDirectionSymbol": "<",
    "limitNumLabels": "0",
    "maxCurvedCharAngleIn": "20",
    "maxCurvedCharAngleOut": "-20",
    "maxNumLabels": "2000",
    "mergeLines": "0",
    "minFeatureSize": "0",
    "multilineAlign": "0",
    "multilineHeight": "1",
    "obstacle": "1",
    "obstacleFactor": "1",
    "obstacleType": "0",
    "offsetType": "0",
    "placeDirectionSymbol": "0",
    "placement": "1",
    "placementFlags": "0",
    "plussign": "0",
    "predefinedPositionOrder": "TR,TL,BR,BL,R,L,TSR,BSR",
    "preserveRotation": "1",
    "previewBkgrdColor": "#ffffff",
    "priority": "5",
    "quadOffset": "4",
    "repeatDistance": "0",
    "repeatDistanceMapUnitScale": "0,0,0,0,0,0",
    "repeatDistanceUnit": "1",
    "reverseDirectionSymbol": "0",
    "rightDirectionSymbol": ">",
    "scaleMax": "10000000",
    "scaleMin": "1",
    "scaleVisibility": "0",
    "shadowBlendMode": "6",
    "shadowColor": "0,0,0,255",
    "shadowDraw": "0",
    "shadowOffsetAngle": "135",
    "shadowOffsetDist": "1",
    "shadowOffsetGlobal": "1",
    "shadowOffsetMapUnitScale": "0,0,0,0,0,0",
    "shadowOffsetUnits": "1",
    "shadowRadius": "1.5",
    "shadowRadiusAlphaOnly": "0",
    "shadowRadiusMapUnitScale": "0,0,0,0,0,0",
    "shadowRadiusUnits": "1",
    "shadowScale": "100",
    "shadowTransparency": "30",
    "shadowUnder": "0",
    "shapeBlendMode": "0",
    "shapeBorderColor": "128,128,128,255",
    "shapeBorderWidth": "0",
    "shapeBorderWidthMapUnitScale": "0,0,0,0,0,0",
    "shapeBorderWidthUnits": "1",
    "shapeDraw": "0",
    "shapeFillColor": "255,255,255,255",
    "shapeJoinStyle": "64",
    "shapeOffsetMapUnitScale": "0,0,0,0,0,0",
    "shapeOffsetUnits": "1",
    "shapeOffsetX": "0",
    "shapeOffsetY": "0",
    "shapeRadiiMapUnitScale": "0,0,0,0,0,0",
    "shapeRadiiUnits": "1",
    "shapeRadiiX": "0",
    "shapeRadiiY": "0",
    "shapeRotation": "0",
    "shapeRotationType": "0",
    "shapeSVGFile": "",
    "shapeSizeMapUnitScale": "0,0,0,0,0,0",
    "shapeSizeType": "0",
    "shapeSizeUnits": "1",
    "shapeSizeX": "0",
    "shapeSizeY": "0",
    "shapeTransparency": "0",
    "shapeType": "0",
    "substitutions": "<substitutions/>",
    "textColor": "0,0,0,255",
    "textTransp": "0",
    "upsidedownLabels": "0",
    "useSubstitutions": "0",
    "wrapChar": "",
    "xOffset": "0",
    "yOffset": "0",
    "zIndex": "0",
}

Defaults = {
    'SimpleLabeling': LabelDefaults,
    'RuleLabeling': LabelDefaults,
    'LabelingRule': LabelDefaults,
    'SimpleFill': {
        "border_width_map_unit_scale": "0,0,0,0,0,0",
        "offset_map_unit_scale": "0,0,0,0,0,0"
    },
    'SimpleMarker': {
        "angle": "0",
        "size_map_unit_scale": "0,0,0,0,0,0",
        "offset_map_unit_scale": "0,0,0,0,0,0",
        "outline_width_map_unit_scale": "0,0,0,0,0,0"
    }
}

# generated from qgspallabeling.h

Placement = {
    0: 'AroundPoint',
    1: 'OverPoint',
    2: 'Line',
    3: 'Curved',
    4: 'Horizontal',
    5: 'Free',
    6: 'OrderedPositionsAroundPoint',
}
PredefinedPointPosition = {
    0: 'TopLeft',
    1: 'TopSlightlyLeft',
    2: 'TopMiddle',
    3: 'TopSlightlyRight',
    4: 'TopRight',
    5: 'MiddleLeft',
    6: 'MiddleRight',
    7: 'BottomLeft',
    8: 'BottomSlightlyLeft',
    9: 'BottomMiddle',
    10: 'BottomSlightlyRight',
    11: 'BottomRight',
}
OffsetType = {
    0: 'FromPoint',
    1: 'FromSymbolBounds',
}
LinePlacementFlags = {
    1: 'OnLine',
    2: 'AboveLine',
    4: 'BelowLine',
    8: 'MapOrientation',
}
QuadrantPosition = {
    0: 'QuadrantAboveLeft',
    1: 'QuadrantAbove',
    2: 'QuadrantAboveRight',
    3: 'QuadrantLeft',
    4: 'QuadrantOver',
    5: 'QuadrantRight',
    6: 'QuadrantBelowLeft',
    7: 'QuadrantBelow',
    8: 'QuadrantBelowRight',
}
UpsideDownLabels = {
    0: 'Upright',
    1: 'ShowDefined',
    2: 'ShowAll',
}
DirectionSymbols = {
    0: 'SymbolLeftRight',
    1: 'SymbolAbove',
    2: 'SymbolBelow',
}
MultiLineAlign = {
    0: 'MultiLeft',
    1: 'MultiCenter',
    2: 'MultiRight',
    3: 'MultiFollowPlacement',
}
ObstacleType = {
    0: 'PolygonInterior',
    1: 'PolygonBoundary',
    2: 'PolygonWhole',
}
ShapeType = {
    0: 'ShapeRectangle',
    1: 'ShapeSquare',
    2: 'ShapeEllipse',
    3: 'ShapeCircle',
    4: 'ShapeSVG',
}
SizeType = {
    0: 'SizeBuffer',
    1: 'SizeFixed',
    2: 'SizePercent',
}
RotationType = {
    0: 'RotationSync',
    1: 'RotationOffset',
    2: 'RotationFixed',
}
SizeUnit = {
    0: 'Points',
    1: 'MM',
    2: 'MapUnits',
    3: 'Percent',
}
ShadowType = {
    0: 'ShadowLowest',
    1: 'ShadowText',
    2: 'ShadowBuffer',
    3: 'ShadowShape',
}
DataDefinedProperties = {
    0: 'Size',
    1: 'Bold',
    2: 'Italic',
    3: 'Underline',
    4: 'Color',
    5: 'Strikeout',
    6: 'Family',
    21: 'FontStyle',
    22: 'FontSizeUnit',
    18: 'FontTransp',
    27: 'FontCase',
    28: 'FontLetterSpacing',
    29: 'FontWordSpacing',
    30: 'FontBlendMode',
    31: 'MultiLineWrapChar',
    32: 'MultiLineHeight',
    33: 'MultiLineAlignment',
    34: 'DirSymbDraw',
    35: 'DirSymbLeft',
    36: 'DirSymbRight',
    37: 'DirSymbPlacement',
    38: 'DirSymbReverse',
    39: 'NumFormat',
    40: 'NumDecimals',
    41: 'NumPlusSign',
    42: 'BufferDraw',
    7: 'BufferSize',
    43: 'BufferUnit',
    8: 'BufferColor',
    19: 'BufferTransp',
    44: 'BufferJoinStyle',
    45: 'BufferBlendMode',
    46: 'ShapeDraw',
    47: 'ShapeKind',
    48: 'ShapeSVGFile',
    49: 'ShapeSizeType',
    50: 'ShapeSizeX',
    85: 'ShapeSizeY',
    51: 'ShapeSizeUnits',
    52: 'ShapeRotationType',
    53: 'ShapeRotation',
    54: 'ShapeOffset',
    55: 'ShapeOffsetUnits',
    56: 'ShapeRadii',
    57: 'ShapeRadiiUnits',
    63: 'ShapeTransparency',
    64: 'ShapeBlendMode',
    58: 'ShapeFillColor',
    59: 'ShapeBorderColor',
    60: 'ShapeBorderWidth',
    61: 'ShapeBorderWidthUnits',
    62: 'ShapeJoinStyle',
    65: 'ShadowDraw',
    66: 'ShadowUnder',
    67: 'ShadowOffsetAngle',
    68: 'ShadowOffsetDist',
    69: 'ShadowOffsetUnits',
    70: 'ShadowRadius',
    71: 'ShadowRadiusUnits',
    72: 'ShadowTransparency',
    73: 'ShadowScale',
    74: 'ShadowColor',
    75: 'ShadowBlendMode',
    76: 'CentroidWhole',
    77: 'OffsetQuad',
    78: 'OffsetXY',
    80: 'OffsetUnits',
    13: 'LabelDistance',
    81: 'DistanceUnits',
    82: 'OffsetRotation',
    83: 'CurvedCharAngleInOut',
    9: 'PositionX',
    10: 'PositionY',
    11: 'Hali',
    12: 'Vali',
    14: 'Rotation',
    84: 'RepeatDistance',
    86: 'RepeatDistanceUnit',
    87: 'Priority',
    91: 'PredefinedPositionOrder',
    23: 'ScaleVisibility',
    16: 'MinScale',
    17: 'MaxScale',
    24: 'FontLimitPixel',
    25: 'FontMinPixel',
    26: 'FontMaxPixel',
    88: 'IsObstacle',
    89: 'ObstacleFactor',
    90: 'ZIndex',
    15: 'Show',
    20: 'AlwaysShow',
}
