from bs4 import BeautifulSoup
import os
import time
from os import listdir


# deal with txt in muphi_trace folder
def filenameList():
    nameList = []
    ListNameStr = listdir('murphi_trace')
    m = len(ListNameStr)
    for i in range(1, m):
        nameList.append(ListNameStr[i].split('.')[0])

    print(nameList)
    return nameList


def read_states(fn):
    filename = 'murphi_trace/'+ fn + '.txt'
    states = []
    start = True
    count = 1
    with open(filename) as f:
        for line in f:
            if start and not line.startswith('Startstate'):
                continue
            else:
                start = False

            # 去掉头尾空白
            line = line.strip()
            # 如果结尾
            if line.startswith('End'): break

            # 其他字段
            if not len(line) or line.startswith('The') or line.startswith('Obtained'):
                continue

            # 一个状态读入完毕，可以绘画
            if line.startswith('-'):
                draw(fn, states, s,count)

                count += 1
                states = []
                print(states)
            # 一个状态的开始
            elif line.startswith('Startstate') or line.startswith('Rule'):
                s = line
                print(s)
            else:
                # 状态写入中
                states.append([n for n in line.split(':')])


def draw(fn,states,s,count):
    # edit each state id, if changed, then class = dark; else, change class = light
    for i in range(len(states)):
        q = soup.find(id=states[i][0])
        if not q: continue;
        # print(q)
        if q.string != states[i][1]:
            q['class'] = 'dark'
            q.string = states[i][1]
        else:
            q['class'] = 'light'

    # change rule name
    p = soup.find(id='rule')
    p.string = s.split(',')[0];

    # generate each html
    html = soup.prettify()

    # write each html into profile
    with open("./"+ timestr +fn+'_output/'+fn+'_htmls/output'+str(count)+".html", "w") as file:
        file.write(html)

    rooturl='./' + timestr + fn+'_output/'

    # transform html to png
    os.system('webkit2png -W 1366 -H 768 -F '+rooturl+fn+'_htmls/output'+str(count)+'.html -D '
        + rooturl+'/'+fn+'_pngs -o ' + fn + str(count))


if __name__ == '__main__':

    default_url = os.path.abspath('.')

    # change location
    os.chdir(default_url)

    FileList = filenameList()

    for fn in FileList:
        print('begin: ', fn)
        protocol = fn.split('_')[0]
        # datetime as parameter
        timestr = time.strftime("%Y%m%d%H%M%S")
        rooturl = timestr + fn + '_output/'

        # create new folder for outputs
        os.mkdir(rooturl)
        os.mkdir(rooturl + fn + '_htmls')
        os.mkdir(rooturl + fn + '_pngs')

        # initialization
        list = []
        soup = BeautifulSoup(open('./'+ protocol.lower() +'.html'), "lxml")

        read_states(fn)
        folder_url = timestr + fn+'_output/'
        png_url = timestr + fn+'_output/'+fn+'_pngs/'
        # os.chdir(timestr + fn+'_output/'+fn+'_pngs')
        if not os.system('ffmpeg -f image2 -r 1/3 -start_number 1 -i '+ png_url + fn + '%d-full.png -vcodec mpeg4 -y \
        ./'+ folder_url + fn + '.mp4'):
            print(fn, ' finished!')