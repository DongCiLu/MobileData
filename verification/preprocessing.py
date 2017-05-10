import os
import math
from collections import deque
from collections import OrderedDict
from copy import deepcopy

from common import *

def parse_traces(filename):
    ''' parse raw trace, save valid records for users and position for towers

    return record list as sessions, organized by user, sort by time
    return tower position list, (lng, lat), sort by position
    '''

    # only one session
    session = []
    start_time = None
    for subdir, dirs, files in os.walk(filename):
        print subdir, ': ',
        for f in files:
            fn = os.path.join(subdir, f)
            sys.stdout.write('.')
            sys.stdout.flush()
            with open(fn) as curf:
                for line in curf:
                    segs = line.split(',')
                    # record: time, (lng, lat)
                    if start_time == None:
                        start_time = float(segs[0]) 
                    time = (float(segs[0]) - start_time) / 1000

                    pos = (float(segs[2]), float(segs[1]))
                    record = DataEntry(time, pos) 

                    session.append(record)
        print ''

        # sort records by time
        session = sorted(session, key=get_sort_key)

    return session

def make_agg_record(ID, start_record, end_record, \
        last_tower_end_record, record, record_cnt):
    pos = start_record.pos
    in_tower = last_tower_end_record.pos
    out_tower = record.pos
    start_time = start_record.time
    end_time = end_record.time
    io = (in_tower, out_tower)
    duration = (start_time, end_time)
    agg_record = AggDataEntry(ID, duration, pos, io, record_cnt)

    return agg_record

def session_compression(session):
    ''' aggregate records according to tower for easy processing

    assign a aggregate ID to connect session with compressed session
    return compressed_session
    '''

    ID = 0
    compressed_session = []
    cur_tower = None
    end_record = DataEntry(None, None)
    record_cnt = 0
    # we dont count the first one and last one
    for record in session:
        if cur_tower != None and cur_tower != record.pos:
            agg_record = make_agg_record(ID, \
                    start_record, end_record, \
                    last_tower_end_record, record, \
                    record_cnt)
            ID += 1
            compressed_session.append(agg_record)
        if cur_tower == None or cur_tower != record.pos:
            last_tower_end_record = end_record
            cur_tower = record.pos
            start_record = record
            record_cnt = 0
        end_record = record
        record_cnt += 1
        record.agg_ID = ID
    # append last few agg_record to a single session
    record = DataEntry(None, None)
    agg_record = make_agg_record(ID, \
            start_record, end_record, \
            last_tower_end_record, record, record_cnt)
    ID += 1
    compressed_session.append(agg_record)

    return compressed_session

def read_towers(filename):
    towers = set()
    with open(filename) as f:
        for l in f:
            segs = l.split(',')
            tower = (float(segs[3]), float(segs[2]))
            towers.add(tower)

    return towers
