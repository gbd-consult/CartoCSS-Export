"""Convert Qgis expressions."""

import re
import error


# CartoCSS supports numeric comparisons, text equality and regexes
# see https://tilemill-project.github.io/tilemill/docs/guides/selectors/

SimpleExpr = r'''(?x)
    ^
    
    # field name
    \w+
    
    \s*
    
    (
        # numeric comparison
        (
            (<= | >= | != | < | > | =)
            \s*
            -? \d+ (\.\d*)?
        )

        |

        # text equality
        (
            (!= | =)
            \s*
            (                
                " (\\. | [^"])* "
                |
                ' (\\. | [^'])* '
            )
        )
    )
    $
'''


def convert(e):
    """Convert (currently only validate) a Qgis expression.
    
    :param str e: Expression 
    :rtype: tuple(converted_expression, error_code)
    """

    e = unicode(e).strip()
    if not e:
        return '', error.EMPTY_EXPRESSION

    m = re.match(r'^\w+$', e)
    if m:
        return e, None

    m = re.match(SimpleExpr, e)
    if m:
        return e, None

    return e, error.EXPRESSION_NOT_SUPPORTED
