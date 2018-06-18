f = open('publications.txt')
for ln in f:
    ln = ln.rstrip()
    # identify the authors
    and_pos = ln.find(' and ')
    comma_pos = ln.find(',', and_pos)

    authors = ln[:comma_pos]
    fields = ln[comma_pos:].split(', ')

    print("\t".join([authors] + fields))