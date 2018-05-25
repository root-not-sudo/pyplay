def htmlEndTagByStartTag(startTag):

    return '</' + startTag[1:startTag.find(' ')] + '>'
