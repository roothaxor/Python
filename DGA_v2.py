# Locky DGA version 2 (seeded)
# his version of DGA is now based on seed value hard-coded to malware binary and this seed can be changed at any time or in every sample. It also generates eight unique domains every two days.

max_bits=32

ROL4 = lambda val, r_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
 
ROR4 = lambda val, r_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

def gen(year, month, day, idx, seed):
	j = 0;
	v21 = 0;
	v3 = ROR4(0xB11924E1 * (year + 7157), 7);
	v3 = ROR4(0xB11924E1 * (v3 + seed + 655360001), 7);
	v4 = ROR4(0xB11924E1 * (v3 + (day >> 1) + 655360001), 7);
	v5 = ROR4(0xB11924E1 * (v4 + month + 654943060), 7);
	seed = ROL4(seed, 17);
	v6 = ROL4(idx & 7, 21);
	v7 = ROR4(0xB11924E1 * (v5 + v6 + seed + 655360001), 7);
	v23 = (v7 + 655360001)%(2**32);
	name_size = v23 % 0xB + 5;
	alloc_size = v23 % 0xB + 8;
	domain = ''
	for idx in range(name_size):
		v9 = ROL4(v23, idx);
		v11 = ROR4(0xB11924E1 * v9, 7);
		v12 = (v11 + 655360001)%2**32;
		v23 = v12;
		domain += chr(v12 % 25 + ord('a'));
	domain += "."
	v15 = ROR4((0xB11924E1 * v23)%2**32, 7);
	v16 = ((v15 + 655360001)%2**32) % 0xE;
	domain += ['ru','pw','eu','in','yt','pm','us','fr','de','it','be','uk','nl','tf'][v16]
	return domain

urls = []
year = 2016
month = 12
day = 24
seed = 7
for idx in range(8):
	urls += [gen(year, month, day, idx, seed)];
print "%4d-%2.2d-%2.2d | Seed= %s |: %s" % (year, month, day, seed, urls);

			
