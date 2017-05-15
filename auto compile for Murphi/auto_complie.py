import os


if  __name__ == '__main__':
    # location of cmurphi/ex/test
    default_url = '/Users/Bella/Documents/Lab/cmurphi5.4.9.1/ex/test'

    # change location
    os.chdir(default_url)
    print ('************************************************')
    print ('All murphi files in cmurphi5.4.9.1/ex/test/:')
    os.system("ls | grep m$")
    print ('************************************************')

    # file name
    input_file_name = raw_input('input file name you want to compile:')

    # compile m to cpp
    command_compile_mu = '../../src/mu ./' + input_file_name + '.m'
    os.system(command_compile_mu)
    print ('************************************************')
    print 'success complied ' + input_file_name + '.cpp'
    print ('************************************************')

    # compile cpp to o
    command_compile_g = 'g++ -ggdb -o ' + input_file_name + '.o ' + input_file_name + '.cpp -I ../../include -lm'
    os.system(command_compile_g)
    print ('************************************************')
    print 'success complied ' + input_file_name + '.o'
    print ('************************************************')

    # run o
    # choose execute parameters
    print 'input the parameters with -:'
    print 'default parameter: -ta -vdfs (press Enter to use default)'
    para = raw_input('parameters:')
    if len(para) == 0: para = '-ta -vdfs' # default

    # save output file
    save = raw_input('Press Enter to run in terminal, or press s to save')
    if len(save) == 0:
        command_exe = './' + input_file_name + '.o ' + para
    else:
        print 'default saving filename is' + input_file_name + '.txt in ./trace'
        save_name = raw_input('Press Enter to save in default, or input filename:')

        if len(save_name) == 0:
            command_exe = './' + input_file_name + '.o ' + para + ' >./trace/' + input_file_name + '.txt'
        else:
            command_exe = './' + input_file_name + '.o ' + para + ' >./trace/' + save_name + '.txt'

    os.system(command_exe)

