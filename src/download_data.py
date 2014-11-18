from init import setup
import os
import pickle
import sys
import re

# Download data
if __name__ == '__main__':
    domain = sys.argv[1]
    _, texts_dir, links_dir = setup(domain)
    links = set()
    with open(links_dir + domain + '.p', 'rb') as f:
        links = pickle.load(f)

    for link in links:
        link = re.sub("\;", "\\\;", link)
        link = re.sub("\(", "\\\(", link)
        link = re.sub("\)", "\\\)", link)
        out_file = (texts_dir + link.split('/')[-1])
        if out_file == texts_dir:
            continue
        out_file = re.sub("[ \\\;\(\)]", "_", out_file)
        os.system('curl -L {} -silent-output > tmp.html'.format(link))
        os.system('lynx -dump -display_charset UTF-8 tmp.html > {}'.format(out_file))
