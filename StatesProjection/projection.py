def project_states_32(filename):
    fn = 'german_3node_xl'

    # fn = filename.split('.')[0]

    with open(filename, 'r') as fr, open(fn+'_proj.txt', 'w') as fw:
        for line in fr:
            # line = line.strip()
            if line:
                if 'Cache[3]' not in line.split('.')[0] and 'ShrSet[3]' not in line.split('.')[0] and \
                                'InvSet[3]' not in line.split('.')[0]:
                    if not ('Chan' in line.split('.')[0] and '3' in line.split('[')[1].split(']')[0]):
                        fw.write(line)


def project_states_21(filename):
    fn = filename.split('.')[0]
    with open(filename, 'r') as fr, open(fn + '_proj.txt', 'w') as fw:
        for line in fr:
            # line = line.strip()
            if line:
                if 'Cache[2]' not in line.split('.')[0] and 'ShrSet[2]' not in line.split('.')[0] and \
                                'InvSet[2]' not in line.split('.')[0]:
                    if not ('Chan' in line.split('.')[0] and '2' in line.split('[')[1].split(']')[0]):
                        fw.write(line)


def diff_states(filemore, fileless):
    d1 = filemore.split('_')[1][0]
    d2 = fileless.split('_')[1][0]
    with open(filemore, 'r') as f3, open(fileless, 'r') as f2, \
            open('german_xl_23diff.txt', 'w') as fd:
        state_seq = ''
        states_set = set()
        for line in f3:
            line = line.strip()
            if line :
                if 'Progress Report' in line or 'CurPtr' in line:
                    continue
                if 'explored' in line:
                    print(line)
                    continue

                if line.startswith('==='): break
                if line.startswith('State'):
                    if state_seq:
                        states_set.add(state_seq)
                        state_seq = ''
                else:
                    # print(line)
                    state_seq += line.split(':')[1]

        print('3node set built!\n')

        cnt = 0
        state_seq = ''
        temp = ''
        for line in f2:
            line = line.strip()
            if line:
                if 'Progress Report' in line or 'explored' in line or 'CurPtr' in line:
                    continue
                if line.startswith('==='):
                    print('All states checked!')
                    fd.write('All states checked')
                    break
                if line.startswith('State'):
                    if state_seq:
                        if state_seq not in states_set:
                            fd.write('\nState ' + str(cnt) + ' not in 3node reach set')
                            fd.write(temp)
                            print(state_seq)
                            print('State ' + str(cnt) + ' not in 3node reach set\n')
                        else:
                            print('\nState ' + str(cnt) + ' checked\n')
                            fd.write('State ' + str(cnt) + ' checked\n')
                        temp= ''
                        state_seq = ''
                    cnt += 1
                    temp += '\n' + line + '\n'
                else:
                    state_seq += line.split(':')[1]
                    temp += line + '\n'
if __name__ == "__main__":
    file_input = "../../g2k_states.txt"
    file_more = "german_3node_xl_proj.txt"
    file_less = "german_2node.txt"

    # project_states_32(file_input)
    diff_states(file_more, file_less)