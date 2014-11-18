from subprocess import call


def setup(domain):
    stats_dir = 'stats/' + domain + '/'
    texts_dir = 'articles/' + domain + '/'
    links_dir = 'links/' + domain + '/'
    call(['mkdir', '-p', stats_dir])
    call(['mkdir', '-p', texts_dir])
    call(['mkdir', '-p', links_dir])
    return [stats_dir, texts_dir, links_dir]


def is_banned(line):
    return ('] См. также' in line
            or '] Ссылки' in line
            or 'References' in line
            or 'Visible links' in line
            or 'Hidden links' in line)
