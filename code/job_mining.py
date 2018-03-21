import re, html

def job_mining():
    '''
    This function should take columns of text block with html format, clean it, eliminate most frequqent words and genrate word coverage values for each extracted word.
    It should return the most abundant words in the text given specific conditions
    '''
    infile = open('job_req1.csv', encoding="utf8").readlines()
    content = []
    for line in infile:
        line = line.strip()
        tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
        no_tags = tag_re.sub('',line)
        line = html.escape(no_tags)
        symbols = [';rsquo;s', ';bull;', '&#x27;','&amp;amp;', ';rdquo;','&amp ','&amp;nbsp;', '&nbsp;', '&quot;', '&bull;', ';rsquo;s', ';rdquo;', '&#x27;']
        for symb in symbols:
            line = line.replace(symb,' ')
        content.append(line)
    #print(content)
    words = [] 
    for cell in content:
        cell = cell.split(sep=' ')
        words.extend(cell)
    filtered_words = []
    for word in words:
        if (len(word) == 3 and word.isupper()) or len(word) > 4 :
            filtered_words.append(word)
            
    word_coverage = {}
    for word in filtered_words:
        word = word.lower()
        if word in word_coverage:
            word_coverage[word] += 1
        else:
            word_coverage[word] = 1