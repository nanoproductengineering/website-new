# Elliot's custom template system #

import os, re
root = os.getcwd()

for prefix, _, files in os.walk(root):
    templateFiles = (f for f in files if re.search('^.+\.html\.t$',f))

    for templateFile in templateFiles:
        template = open(os.path.join(prefix, templateFile)).readlines()
        compiled = ''

        for line in template:
            m = re.search(r'<\!--.*{{(.+)}}.*-->', line)
            
            if m:                 
                includeFile = os.path.join(root, m.group(1))
                compiled += open(includeFile).read()
            else:
                compiled += line

        open(os.path.join(prefix,templateFile[:-2]),'w').write(compiled)
