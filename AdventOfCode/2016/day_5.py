from hashlib import md5


def part1():
    _in = 'ojvtpuvg'
    _out = ''
    i = 0
    while len(_out) < 8:
        _hash = md5('%s%s' % (_in, i)).hexdigest()
        if _hash.startswith('00000'):
            _out += _hash[5]
        i += 1
    print _out


def part2():
    _in = 'ojvtpuvg'
    _out = ['', '', '', '', '', '', '', '']
    i = 0
    while not all(_out):
        _hash = md5('%s%s' % (_in, i)).hexdigest()
        if _hash.startswith('00000'):
            if _hash[5].isdigit() and int(_hash[5]) <= 7 and _out[int(_hash[5])] == '':
                _out[int(_hash[5])] = _hash[6]
        i += 1

    print ''.join(_out)


part1()
part2()
