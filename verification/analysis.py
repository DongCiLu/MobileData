from speedest import get_speed

max_bin_cnt = 20
max_detailed_bin_cnt = 200
# TODO 
max_speed_bin_cnt = 8
speed_per_bin = 20
# max_speed_bin_cnt = 2
# speed_per_bin = 50

def estimated_speed_basic_analysis(compressed_session, rules):
    print '-------Estimated Speed Basic Analysis-------'
    # all unit are in number of records
    record_cnt = 0
    record_wlb_cnt = 0
    record_wzerolb_cnt = 0
    record_westspeed_cnt = 0
    record_wcompensatespeed_cnt = 0
    record_wspeed_cnt = 0
    speed_per_bin = 8
    speed_est_dist = [0] * max_bin_cnt
    speed_lb_dist = [0] * max_bin_cnt
    speed_ratio_dist = [0] * max_bin_cnt
    speed_diff_per_bin = 5
    speed_diff_dist = [0] * max_bin_cnt
    speed_est_pass_dist = [0] * max_bin_cnt
    speed_lb_pass_dist = [0] * max_bin_cnt

    for agg_record in compressed_session:
        record_cnt += agg_record.record_cnt

        if agg_record.dist_lb != None:
            record_wlb_cnt += agg_record.record_cnt
            if agg_record.dist_lb == 0:
                record_wzerolb_cnt += agg_record.record_cnt

        if agg_record.speed != (None, None):
            record_westspeed_cnt += agg_record.record_cnt
            
        if agg_record.compensate_speed != (None, None):
            record_wcompensatespeed_cnt += agg_record.record_cnt

        if agg_record.speed != (None, None) or \
                agg_record.compensate_speed != (None, None):
            record_wspeed_cnt += agg_record.record_cnt

        # for estimated speed only
        if agg_record.speed != (None, None):
            speed_est_index = min(int(agg_record.speed[1] /\
                    speed_per_bin), max_bin_cnt - 1)
            speed_est_dist[speed_est_index] += agg_record.record_cnt

            speed_lb_index = min(int(agg_record.speed[0] /\
                    speed_per_bin), max_bin_cnt - 1)
            speed_lb_dist[speed_lb_index] += agg_record.record_cnt

            if agg_record.speed[0] == 0:
                # speed[1] cloud not be 0
                speed_ratio_index = max_bin_cnt - 1
            else:
                speed_ratio_index = min(int(agg_record.speed[1] /\
                        agg_record.speed[0]), max_bin_cnt - 1)
            speed_ratio_dist[speed_ratio_index] += \
                    agg_record.record_cnt

            speed_diff = agg_record.speed[1] - agg_record.speed[0]
            speed_diff_index = \
                    min(int(speed_diff / speed_diff_per_bin), \
                    max_bin_cnt - 1)
            speed_diff_dist[speed_diff_index] += agg_record.record_cnt

        speed_range = get_speed(agg_record, rules)
        if speed_range != None:
            speed_est_pass_index = min(int(speed_range[1] /\
                    speed_per_bin), max_bin_cnt - 1)
            speed_est_pass_dist[speed_est_pass_index] += \
                    agg_record.record_cnt

            speed_lb_pass_index = min(int(speed_range[0] /\
                    speed_per_bin), max_bin_cnt - 1)
            speed_lb_pass_dist[speed_lb_pass_index] += \
                    agg_record.record_cnt

    print 'NOR: {0}'.format(record_cnt)
    print 'NOR with distance lower bound: {0}'.format(record_wlb_cnt)
    print 'NOR with zero distance lower bound: {0}'.format(record_wzerolb_cnt)
    print 'NOR with estimated speed: {0}'.format(record_westspeed_cnt)
    print 'NOR with compensate speed: {0}'.format(record_wcompensatespeed_cnt)
    print 'NOR with either speed: {0}'.format(record_wspeed_cnt)
    print 'Estimated speed distribution ({0} km/h per bin):'.format(\
            speed_per_bin)
    print speed_est_dist
    print 'Speed lower bound distribution ({0} km/h per bin):'.format(\
            speed_per_bin)
    print speed_lb_dist
    print 'Speed ratio distribution:'
    print speed_ratio_dist
    print 'Speed difference distribution ({0} km/h per bin):'.format(\
            speed_diff_per_bin)
    print speed_diff_dist
    print 'Passed estimated speed distribution ({0} km/h per bin):'.format(\
            speed_per_bin)
    print speed_est_pass_dist
    print 'Passed speed lower bound distribution ({0} km/h per bin):'.format(\
            speed_per_bin)
    print speed_lb_pass_dist
    print ''

def estimated_speed_error_analysis(compressed_session, rules):
    print '-------Estimated Speed Basic Analysis-------'
    # all unit are in number of records
    record_cnt = 0
    record_westspeed_cnt = 0
    record_passed_cnt = 0
    max_error_bin_cnt = 10 
    error_per_bin = 0.1
    speedest_error_dist = [0] * max_error_bin_cnt
    speedestalt_error_dist = [0] * max_error_bin_cnt
    passed_speedest_error_dist = [0] * max_error_bin_cnt
    passed_speedestalt_error_dist = [0] * max_error_bin_cnt

    for agg_record in compressed_session:
        record_cnt += agg_record.record_cnt

        # for estimated speed only
        if agg_record.speed != (None, None):
            record_westspeed_cnt += agg_record.record_cnt
            speedest_error = abs(agg_record.speed[1] - agg_record.speed_gt) / agg_record.speed_gt 
            speedestalt_error = abs(agg_record.speed[1] - agg_record.speed_gt_alt) / agg_record.speed_gt_alt
            speedest_error_index = min(int(speedest_error /\
                    error_per_bin), max_error_bin_cnt - 1)
            speedestalt_error_index = min(int(speedestalt_error /\
                    error_per_bin), max_error_bin_cnt - 1)
            speedest_error_dist[speedest_error_index] += \
                    agg_record.record_cnt
            speedestalt_error_dist[speedestalt_error_index] += \
                    agg_record.record_cnt

        speed_range = get_speed(agg_record, rules)
        if speed_range != None:
            record_passed_cnt += agg_record.record_cnt
            passed_speedest_error_dist[speedest_error_index] += \
                    agg_record.record_cnt
            passed_speedestalt_error_dist[speedestalt_error_index] += \
                    agg_record.record_cnt


    print 'Counters: ', record_cnt, record_westspeed_cnt, record_passed_cnt
    print 'Speed estimation error distribution:'
    print speedest_error_dist
    print 'Alternative speed estimation error distribution:'
    print speedestalt_error_dist
    print 'Passed speed estimation error distribution:'
    print passed_speedest_error_dist
    print 'Passed alternative speed estimation error distribution:'
    print passed_speedestalt_error_dist
