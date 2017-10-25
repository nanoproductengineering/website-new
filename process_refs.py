refs_in = open('refs_raw').read().splitlines()
refs_out = open('refs_html','w')
offset = 7
for i in range(len(refs_in)):
    refs_out.write(
        '<li><a href= "papers/{idx}.pdf"> {citation} </a></li>\n'.format(
            idx = i+offset,
            citation = refs_in[i]
        )
    )
