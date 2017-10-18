speed = {'0-20', '20-40', '40-60', '60-80', '80-100', ...
    '100-120', '120-140'};
%speed = {'all', 'no est. speed', '0-20', '20-40', '40-60', '60-80', '80-100', ...
%    '>100'};
subplot(3, 1, 1);
plot(x(1:7), '-o')
set(gca, 'XTickLabel', speed, 'FontSize', 26)
xlabel('Speed (km/h)')
ylabel('vol. per sec. (Byte)')

subplot(3, 1, 2);
plot(y(1:7), '-o')
set(gca, 'XTickLabel', speed, 'FontSize', 26)
xlabel('Speed (km/h)')
ylabel('vol. per conn.')

subplot(3, 1, 3);
plot(z(1:7), '-o')
set(gca, 'XTickLabel', speed, 'FontSize', 26)
xlabel('Speed (km/h)')
ylabel('conn. per sec.')