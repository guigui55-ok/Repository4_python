
BASIC_FILE_NAME = 'basic.html'
DOCTYPE = '<!DOCTYPE html>'
CSS_MARKER = '<!--link_css-->'
CSS_BEGIN_TAG = '<link rel="stylesheet" href="'
CSS_END_TAG = '">'

REPLACE_VALUE = '__VALUE__'
CSS_TAG_SAMPLE = '<link rel="stylesheet" href="{}">'.format(REPLACE_VALUE)
NEW_LINE = '\n'
# BODY_MAIN_CONTENTS_MARKER = '<!--main contents-->'
# BODY_MAIN_CONTENTS_MARKER = '<body><!--main contents--></body>'
BODY_MAIN_CONTENTS_MARKER = '    <body><!--main contents--></body>'

class HtmlTagName():
    DOCTYPE = '!DOCTYPE' #not closed
    P = 'p'
    DIV = 'div'
    SPAN = 'span'
    H1 = 'h1'
    H2 = 'h2'
    H3 = 'h3'
    BODY = 'body'
    HTML = 'html'
    IMG = 'img' #not closed
    ###
    HEAD = 'head'
    TITLE = 'title'
    SCRIPT = 'script'
    A = 'a'
    BR = 'br' #not closed
    LINK = 'link' #not closed
    HR = 'hr' #not closed
    PRE = 'pre'
    STRONG = 'strong'
    #
    UL = 'ul'
    UI = 'ui'
    #
    TABLE = 'table'
    TFOOT = 'tfoot'
    TBODY = 'tbody'
    CAPTION = 'caption'
    THREAD = 'thead'
    TH = 'th'
    TR = 'tr'
    COLGROUP = 'colgroup'
    #
    FORM = 'form'
    BUTTON = 'button'
    INPUT = 'input' #not closed
    OPTION = 'option'
    SELECT = 'select'
    #
    MAIN = 'main'
    SUB = 'sub'
    ASIDE = 'aside'
    FOOTER = 'footer'
    #
    FRAME = 'frame'
    FRAMESET = 'frameset'
    NOFRAMES = 'noframes'
    ###
    META = 'meta' #not closed
    IFRAME = 'iframe'
    SLOT = 'slot'
    SVG = 'svg'
    PATH = 'path'
    PORYGON = 'polygon'
    CODE = 'code'
    BLOCKQUOTE = 'blockquote'

def tag_is_closing_type(tag:HtmlTagName):
    if tag == HtmlTagName.IMG or \
        tag == HtmlTagName.DOCTYPE or \
        tag == HtmlTagName.BR or \
        tag == HtmlTagName.LINK or \
        tag == HtmlTagName.HR or \
        tag == HtmlTagName.INPUT or \
        tag == HtmlTagName.META:
        return True
    return False

def is_tag_name(tag:str):
    if tag in vars(HtmlTagName).values():
        return True
    else:
        return False


# def test_main():
#     d = vars(HtmlTagName)
#     for v in d.values():
#         print(v)
#     # print(d.items())
#     return

# if __name__ == '__main__':
#     test_main()