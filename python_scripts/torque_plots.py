import matplotlib.pyplot as plt
import numpy as np
import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

time = np.arange(0,5,(0.001))

efield = 0.015

all_torque_x = np.zeros([5,5000])

fig, ax = plt.subplots()

for i in range(0,5):
    rel_path = "../graphene_online_Nov4/torque_"+str(i+1)+".txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    file = open(abs_file_path)
    lines = file.readlines()
    file.close()

    reduced_lines = [None] * 5000
    index = 4
    j = 0
    for j in range((len(lines) - 5) // 2):
        reduced_lines[j] = lines[index]
        index += 2
        j += 1
    j = 1
    torque_x = np.zeros(5000)
    for j in range(len(reduced_lines)):
        current_line = reduced_lines[j].split()
        torque_x[j] = current_line[1]
        j += 1
    all_torque_x[i] = torque_x
p1, = ax.plot(time,all_torque_x[0],label = '0.015 V/Angstrom')
p2, = ax.plot(time,all_torque_x[1],label = '0.030 V/Angstrom')
p3, = ax.plot(time,all_torque_x[2],label = '0.045 V/Angstrom')
p4, = ax.plot(time,all_torque_x[3],label = '0.060 V/Angstrom')
p5, = ax.plot(time,all_torque_x[4],label = '0.075 V/Angstrom')
ax.set_autoscale_on
ax.grid
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles,labels)
plt.show()