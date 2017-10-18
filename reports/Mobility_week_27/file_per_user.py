import os
import sys
import argparse

def is_number(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

def parse_traces(input_folder, output_folder):
    users = {}
    towers = []

    for subdir, dirs, files in os.walk(input_folder):
        print '\nReading data from ', subdir, '(dot per file): '
        for f in files:
            fn = os.path.join(subdir, f)
            sys.stdout.write('.')
            sys.stdout.flush()
            with open(fn) as curf:
                for line in curf:
                    segs = line.split(',')
                    if len(segs) != 18 \
                            or not is_number(segs[6]) \
                            or not is_number(segs[9]) \
                            or not is_number(segs[10]):
                        continue

                    # create variables
                    username = segs[0]
                    time = float(segs[6])
                    tower = (float(segs[9]), float(segs[10]))
                    record = line

                    # add user records
                    if username not in users:
                        users[username] = []
                    users[username].append((time, record))

                    # add tower
                    if tower not in towers:
                        towers.append(tower)

        print ''

    print 'Total: {0} users, {1} towers'.format(len(users), len(towers))

    os.system('mkdir {0}'.format(output_folder))
    os.system('mkdir {0}/users'.format(output_folder))

    print '\nOutput data to ', output_folder, '(dot per 1k files): '
    cnt = 0
    for username in users:
        with open('{0}/users/{1}.txt'.format(output_folder, username), 'w') \
                as outfile:
            if cnt % 1000 == 999:
                sys.stdout.write('.')
                sys.stdout.flush()
            for time, record in sorted(users[username]): # sorted by time
                outfile.write(record)
        cnt += 1
    print ''
        
    towers.sort()
    with open('{0}/towers.txt'.format(output_folder), 'w') as outfile:
        for tower in towers:
            outfile.write('{0}\n'.format(tower))

    print 'Done!'


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('source_folder', type=str)
    args = ap.parse_args()

    input_folder = args.source_folder
    output_folder = 'file_per_user_results'

    parse_traces(input_folder, output_folder)

