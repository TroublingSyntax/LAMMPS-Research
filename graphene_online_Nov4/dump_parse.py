import os

def dump_parser():

    file = open('/home/kevinlewis/Desktop/LAMMPS-Research/graphene_online_Nov4/dump.graphene_crumple_v2', mode = 'r')
    lines = file.readlines()
    file.close()

    vel_z = [None] * len(lines)
    index = 9
    for line in lines[9:]:
        current_line = lines[index].split()

        try:
            vel_z[index-9] = current_line[6]
            index += 1
        except IndexError:
            index += 1
            continue
    
    run_count = os.environ['PARSE_COUNT']

    output_file = open('vel_z_' + str(run_count) + '.txt','w')

    for i in range(len(vel_z)):
        try:
            output_file.write(vel_z[i]+'\n')
        except:
            continue
    output_file.close()
