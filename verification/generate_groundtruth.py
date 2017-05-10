import os

def generate_groundtruth(tracefn, outdir):
    for subdir, dirs, files in os.walk(tracefn):
        for f in files:
            fn = os.path.join(subdir, f)
            outfn = os.path.join(outdir, f)
            print fn, outfn
            last_time = 0
            with open(fn) as curf, open(outfn, 'w') as outf:
                for line in curf:
                    segs = line.split('|')
                    if len(segs) != 19 or segs[0] != "TYPE=GPS":
                        continue
                    TIME = int(segs[1][5:])
                    if TIME < last_time:
                        print "wrong time order"
                    last_time = TIME
                    LAT = float(segs[6][4:])
                    LNG = float(segs[15][4:])
                    outf.write("{}, {}, {}\n".format(TIME, LAT, LNG))

if __name__ == '__main__':
    tracefn = "../datasets/verification_data/processed/GPS"
    outdir = "../datasets/verification_data/processed/GPSP"
    locations = generate_groundtruth(tracefn, outdir)

