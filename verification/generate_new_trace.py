import os

def process_raw_data(tracefn, towercoordsfn, outdir):
    towers = {} 

    with open(towercoordsfn, 'r') as f:
        for l in f:
            segs = l.split(',')
            AID = int(segs[0])
            CID = int(segs[1])
            LAT = float(segs[2])
            LNG = float(segs[3])
            towers[(AID, CID)] = (LAT, LNG)

    for subdir, dirs, files in os.walk(tracefn):
        last_size = 0
        for f in files:
            fn = os.path.join(subdir, f)
            outfn = os.path.join(outdir, f)
            print fn, outfn
            total_cnt = 0
            missing_cnt = 0
            last_time = 0
            with open(fn, 'r') as curf, open(outfn, 'w') as outf:
                for line in curf:
                    segs = line.split('|')
                    if len(segs) != 9 or segs[0] != "TYPE=GSM":
                        # print "Error", line
                        continue
                    TIME = int(segs[1][5:])
                    if TIME < last_time:
                        print "wrong time order"
                    last_time = TIME
                    AID = int(segs[4][7:])
                    CID = int(segs[3][7:])
                    if (AID, CID) in towers:
                        coord = towers[(AID, CID)]
                        outf.write("{}, {}, {}\n".format(TIME, coord[0], coord[1]))
                    else:
                        missing_cnt += 1
                    total_cnt += 1
            print "{} out of {} records failed".format(missing_cnt, total_cnt)

if __name__ == '__main__':
    tracefn = "../datasets/verification_data/processed/GSM"
    towercoordsfn = "./tower_coords.txt"
    outdir = "../datasets/verification_data/processed/GSMP"
    towers = process_raw_data(tracefn, towercoordsfn, outdir)
