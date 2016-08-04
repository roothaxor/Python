#Domain Generation Algorithm (DGA)
#The original domain generation algorithm was based on two hard-coded seeds and the current system time of an infected machine. This DGA version generates six unique domains every two days.

max_bits=32

ROL4 = lambda val, r_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
 
ROR4 = lambda val, r_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

#day 1..31
#month 1..12
#year 1601..30827
def gen(year, month, day, idx):
    j = 0;
    v21 = 0;
    v3 = ROR4(0xB11924E1 * (year + 7157), 5);
    v4 = ROR4(0xB11924E1 * (v3 + (day >> 1) + 655360001), 5);
    v5 = ROR4(0xB11924E1 * (v4 + month + 654943060), 5);
    v6 = ROL4(idx % 6, 21);
    v7 = ROR4(0xB11924E1 * (v5 + v6 + 655360001), 5);
    v23 = (v7 + 655360001)%(2**32);
    name_size = (v7 + 655360001) % 0xB + 5;
    alloc_size = (v7 + 655360001) % 0xB + 8;
    
    domain = ''
    
    for idx in range(name_size):
        v9 = ROL4(v23, idx);
        v11 = ROR4(0xB11924E1 * v9, 5);
        v12 = (v11 + 655360001)%2**32;
        v23 = v12;
        domain += chr(v12 % 25 + ord('a'))
    domain += "."
    
    v15 = ROR4((0xB11924E1 * v23)%2**32, 5);
    v16 = ((v15 + 655360001)%2**32) % 0xE;
    domain += ['ru', 'pw', 'eu', 'in', 'yt', 'pm', 'us', 'fr', 'de', 'it', 'be', 'uk', 'nl','tf'][v16]
    return domain
urls = []
#for year in range(2016,2017):
for year in range(2016,2017):
    for month in range(1,12):
        for day in range(1,31):
            for idx in range(6):
                urls += [gen(year, month, day, idx)]
print urls
