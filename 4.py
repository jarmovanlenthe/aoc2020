import re

ATTRS = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
HCL_RE = re.compile(r'#[0-9a-f]{6}')

class Passport:
    ecl = None
    pid = None
    eyr = None
    hcl = None
    byr = None
    iyr = None
    cid = None
    hgt = None


    @staticmethod
    def parse(s):
        p = Passport()
        props = s.replace('\n', ' ').strip().split(' ')
        for prop in props:
            k, v = prop.split(':')
            try:
                if 'yr' in k:
                    v = int(v)
            except:
                pass
            setattr(p, k, v)
        return p
    
    def is_byr_valid(self):
        return 1920 <= self.byr <= 2002
    
    def is_iyr_valid(self):
        return 2010 <= self.iyr <= 2020
    
    def is_eyr_valid(self):
        return 2020 <= self.eyr <= 2030

    def is_hgt_valid(self):
        try:
            if 'cm' in self.hgt:
                return 150 <= int(self.hgt[:-2]) <= 193
            if 'in' in self.hgt:
                return 59 <= int(self.hgt[:-2]) <= 76
        except:
            pass
        return False
    
    def is_hcl_valid(self):
        return HCL_RE.match(self.hcl)

    def is_ecl_valid(self):
        return self.ecl in ['amb','blu','brn','gry','grn','hzl','oth']
    
    def is_pid_valid(self):
        return len(self.pid) == 9 and int(self.pid)
    
    def is_valid(self):
        for a in ATTRS:
            if not getattr(self, a):
                return False
            if not getattr(self, f'is_{a}_valid')():
                return False
        return True


with open("input4.txt") as f:
    fi = f.read()
    passports = fi.split('\n\n')

valid_passports = 0

for p in passports:
    passport = Passport.parse(p)
    if passport.is_valid():
        valid_passports += 1

print(valid_passports)