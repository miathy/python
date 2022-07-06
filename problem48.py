def stringCount(filename,target):
    infile = open(filename)
    content = infile.read()
    infile.close()
    return content.count(target)

stringCount('/Users/cwall/Desktop/SOP -  (1).docx','study')