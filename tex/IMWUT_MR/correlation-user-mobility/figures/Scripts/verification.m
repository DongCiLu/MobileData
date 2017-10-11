figure(1);
title('Speed Estimation Accuracy')

legend_string = {'Raw speed estimation' ...
    'Filtered speed estimation'};

label_string = {'0.1' ...
    '0.2' ...
    '0.3' ...
    '0.4' ...
    '0.5' ...       
    '0.6' ...
    '0.7' ...
    '0.8' ...
    '0.9' ...
    '>= 1'};

raw_speed_estimation_error = [335, 164, 191, 111, 117, 149, 233, 130, 33, 492]
% filtered_speed_estimation_error = [140, 137, 79, 65, 0, 58, 67, 0, 0, 25]
% filtered_speed_estimation_error = [140, 137, 79, 65, 3, 58, 67, 3, 3, 25]
filtered_speed_estimation_error = [123, 137, 79, 65, 0, 58, 67, 0, 0, 13]
speed_estimation_error = [raw_speed_estimation_error', filtered_speed_estimation_error']

bar(speed_estimation_error);
set(gca,'FontSize',20);
set(gca, 'XTickLabel', label_string);
set(gca,'XLim',[0 11])
ylabel_hand=ylabel('Number of records');
set(ylabel_hand,'Fontname', 'Times New Roman', 'Fontsize', 20);
xlabel_hand=xlabel('Speed estimation errors');
set(xlabel_hand,'Fontname', 'Times New Roman', 'Fontsize', 20);
legend_hand = legend(legend_string, 'Location', 'Northwest');
set(legend_hand,'Fontname', 'Times New Roman', 'Fontsize', 20);

