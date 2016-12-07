import re

with open('day_7.input', 'rb') as fin:
    lines = [f.strip() for f in fin]

class IPv7(object):
    def __init__(self, record):
        self.internal = []
        self.external = []
        self.parse(record)

    def is_valid_internal(self):
        for internal in self.internal:
            for i in xrange(len(internal)-3):
                if self.palindrome(internal[i:i+4]):
                    return False
        return True

    def is_valid_external(self):
        for external in self.external:
            for i in xrange(len(external)-3):
                if self.palindrome(external[i:i+4]):
                    return True
        return False

    def palindrome(self, fragment):
        if fragment == fragment[::-1] and fragment[0] != fragment[1]:
            return True
        return False

    def parse(self, record):
        external = True
        for match in re.split('(\W+)', record):
            if match == '[':
                external = False
                continue
            if match == ']':
                external = True
                continue
            if external:
                self.external.append(match)
            else:
                self.internal.append(match)
    
    def aba_bab(self):
        aba_fragments = []
        for external in self.external:
            for i in xrange(len(external)-2):
                if self.palindrome(external[i:i+3]):
                    aba_fragments.append(external[i:i+3])
        bab_fragments = self.generate_bab(aba_fragments)
        for internal in self.internal:
            for bab in bab_fragments:
                if bab in internal:
                    return True
        return False

    def generate_bab(self, aba_fragments):
        bab_fragments = []
        for aba in aba_fragments:
            bab_fragments.append('%s%s%s' % (aba[1], aba[0], aba[1]))
        return bab_fragments

count = 0
bab_cnt = 0
for line in lines:
    r = IPv7(line)
    if r.is_valid_external() and r.is_valid_internal():
        count += 1
    if r.aba_bab():
        bab_cnt += 1

print count
print bab_cnt

