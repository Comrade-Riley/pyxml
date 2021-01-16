import pyxml.main

if __name__ == "__main__":
    def load(file):
        from pyxml2dict import XML2Dict
        return XML2Dict().fromstring(open(file,'r').read())
    def dump(data,file,indent):
        from dict2xml import dict2xml
        indent = ' '*indent
        open(file,'w').write(dict2xml(data,indent=indent))
