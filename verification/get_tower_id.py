import os

def get_raw_towers(tracefn):
    towers = set() 
    for subdir, dirs, files in os.walk(tracefn):
        print subdir
        last_size = 0
        for f in files:
            fn = os.path.join(subdir, f)
            print fn
            with open(fn) as curf:
                for line in curf:
                    segs = line.split('|')
                    if len(segs) != 9 or segs[0] != "TYPE=GSM":
                        # print "Error", line
                        continue
                    MNC = int(segs[6][4:])
                    MCC = int(segs[5][4:])
                    AID = int(segs[4][7:])
                    CID = int(segs[3][7:])
                    towers.add((MNC, MCC, AID, CID))
            print "new discoverd towers: {0}".format(len(towers) - last_size)
            last_size = len(towers)

    return towers

def guess_adj_towers(towers, expansion):
    expanded_towers = set()
    expansion_cnt = 0
    for tower in towers:
        for i in range(expansion):
            inc = i + 1;
            new_tower1 = (tower[0], tower[1], tower[2], tower[3] + inc)
            new_tower2 = (tower[0], tower[1], tower[2], tower[3] - inc)
            new_tower3 = (tower[0], tower[1], tower[2] + 1, tower[3] + inc)
            new_tower4 = (tower[0], tower[1], tower[2] + 1, tower[3] - inc)
            new_tower5 = (tower[0], tower[1], tower[2] - 1, tower[3] + inc)
            new_tower6 = (tower[0], tower[1], tower[2] - 1, tower[3] - inc)
            if new_tower1 not in expanded_towers and new_tower1 not in towers:
                expanded_towers.add(new_tower1)
                expansion_cnt += 1
            if new_tower2 not in expanded_towers and new_tower2 not in towers:
                expanded_towers.add(new_tower2)
                expansion_cnt += 1
            if new_tower3 not in expanded_towers and new_tower3 not in towers:
                expanded_towers.add(new_tower3)
                expansion_cnt += 1
            if new_tower4 not in expanded_towers and new_tower4 not in towers:
                expanded_towers.add(new_tower4)
                expansion_cnt += 1
            if new_tower5 not in expanded_towers and new_tower5 not in towers:
                expanded_towers.add(new_tower5)
                expansion_cnt += 1
            if new_tower6 not in expanded_towers and new_tower6 not in towers:
                expanded_towers.add(new_tower6)
                expansion_cnt += 1

    print "before expansion: {0}".format(len(towers))
    towers = towers.union(expanded_towers)
    print "expansion: {0}".format(len(expanded_towers))
    print "after expansion: {0}".format(len(towers))
    return towers

def generate_request(towers):
    templatefn = "./template.js"
    outputfn = "./test.js"
    start_position = 7
    source = open(templatefn, 'r')
    lines = list(source)
    source.close()
    for i, tower in enumerate(towers):
        query = "{req: {mcc: '" + str(tower[1]) + "', mnc: '" + str(tower[0]) + "', lac: '" + str(tower[2]) + "', cid: '" + str(tower[3]) + "', net: 'gsm'}, res: {google: {success:true}}}"
        if i != len(towers) - 1:
            query += ",\n"
        else:
            query += "\n"
        lines.insert(start_position + i, query);

    output = open(outputfn, 'w')
    for l in lines:
        output.write(l)
    output.close()

def get_coordinates(towercoordsfn):
    towercoords = {}
    with open(towercoordsfn) as f:
        for l in f:
            segs = l.split(',')
            if segs[4] == "undefined" and \
                    segs[6] == "undefined" and \
                    segs[8] == "undefined" and \
                    segs[10] == "undefined" and \
                    segs[12] == "undefined" and \
                    segs[14] == "undefined" :
                continue
            CID = int(segs[0])
            AID = int(segs[1])
            MCC = int(segs[2])
            MNC = int(segs[3])
            LAT = float(segs[4])
            LON = float(segs[5])
            tower = (MNC, MCC, AID, CID)
            coord = (LAT, LON)
            if tower not in towercoords:
                towercoords[tower] = coord
    return towercoords

def check_orig_towers(towers, towercoords):
    cnt = 0
    for tower in towers:
        if tower in towercoords:
            cnt += 1
    return cnt

def output_towercoords(towercoords, towercoords_outfn):
    with open(towercoords_outfn, 'w') as out:
        for tower in towercoords:
            out.write("{0}, {1}, {2}, {3}\n".format(tower[2], tower[3], towercoords[tower][0], towercoords[tower][1]))
            # print "new google.maps.LatLng{0},".format(towercoords[tower])
    return

if __name__ == '__main__':
    tracefn = "../datasets/verification_data/processed/GSM"
    towers = get_raw_towers(tracefn)

    towercoordsfn = "./bscoords/tower_coordinates_new.txt"
    towercoords = get_coordinates(towercoordsfn)
    towercnt = check_orig_towers(towers, towercoords)
    print "{0} original towers, {1} has coordinates, {2} total towers that have coordinates".format(len(towers), towercnt, len(towercoords))

    towercoords_outfn = "tower_coords.txt"
    output_towercoords(towercoords, towercoords_outfn)

    # expansion = 10
    # towers = guess_adj_towers(towers, expansion)
    # generate_request(towers)

