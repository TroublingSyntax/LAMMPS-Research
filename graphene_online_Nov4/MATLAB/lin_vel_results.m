data1 = readtable('../vel_z_1.txt');
data2 = readtable('../vel_z_2.txt');
data3 = readtable('../vel_z_3.txt');
data4 = readtable('../vel_z_4.txt');
data5 = readtable('../vel_z_5.txt');

data = {data1,data2,data3,data4,data5};
temp_arr = zeros(height(data));
temp_sum = zeros(480,1);
averages = zeros(200,5);

for i = 1:5
    temp_arr = data{1,i};
    for j = 1:200
        for k = 1:480
            pos = (480*j - 480) + k;
            if isnan(table2array(temp_arr(pos,1)))
                continue
            else
                temp_sum(k,1) = table2array(temp_arr(pos,1));
            end
        end
        averages(j,i) = sum(temp_sum)/480;
    end
end

% time is in picoseconds
time = linspace(0,5,200);
time = time';

for g = 1:5
    plot(time,averages(:,g));
    hold on
end