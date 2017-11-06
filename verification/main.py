#/usr/bin/python

import sys
import cPickle as pickle
import argparse
import operator

from common import *

import preprocessing as pp
import voronoi as vor
import speedest as se
import analysis as an

if __name__ == '__main__':
    # setup parameters
    rules = Rules(\
            pc_window_len = 60, \
            pc_density = 10, \
            pf_min_tower = 3, \
            sc_window_len = 60, \
            sc_dur_req = 300, \
            cv_dist_ratio_threshold = 0.6, \
            cv_duration_ratio_threshold = 0.6, \
            ) 

    print '\n:::::::Estimate Speed:::::::\n'
    print '1. Preprocess data'
    # a session means whole data access of each user
    session = pp.parse_traces( \
            '../datasets/verification_data/processed/GSMP') 
    # sessions are compressed to each tower
    compressed_session = pp.session_compression(session)
    towers = pp.read_towers('./tower_coords.txt')
    print "{} records, {} aggregated records, {} towers".format(\
            len(session), len(compressed_session), len(towers))

    print '2. Stimulate tower boundaries with Voronoi map'
    vmap = vor.voronoi_map(towers)
    vmap.equirectangular_projection()
    boundaries = vmap.calc_boundaries()
    print "{} boundaries".format(len(boundaries))

    print '3. Estimate distance lower bound based on tower boundaries'
    se.calc_dist(compressed_session, boundaries)

    print '4. Estimate speed range'
    se.speed_estimation(compressed_session, rules) 

    print '5. Calculate ground truth'
    se.speed_groundtruth(compressed_session, \
            '../datasets/verification_data/processed/GPSP')

    print '6. Speed analysis'
    # an.basic_analysis(session, compressed_session, rules)
    # an.estimated_speed_basic_analysis(compressed_session, rules)
    an.estimated_speed_error_analysis(compressed_session, rules)
    # an.estimated_distance_error_analysis(compressed_session, rules)

