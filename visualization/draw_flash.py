filename = "./flash_I2E.txt"
# location of cmurphi/ex/test
default_url = '/Users/Bella/Documents/Lab/visualization'


from bs4 import BeautifulSoup
import os
import time


def read_states():
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
                draw(states,s)
                states = []
                print(states)
            # 一个状态的开始
            elif line.startswith('Startstate') or line.startswith('Rule'):
                s = line
                print(s)
            else:
                # 状态写入中
                states.append([n for n in line.split(':')])


def draw(states,s):
    global count

    # edit each state id
    # if changed, then class = dark
    # else, change class = light
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

    count += 1


if __name__ == '__main__':

    fn = filename.split('.')[1].split('/')[1]

    # datetime as parameter
    timestr = time.strftime("%Y%m%d%H%M%S")
    rooturl = timestr + fn + '_output/'

    # change location
    os.chdir(default_url)

    # create new folder for outputs
    os.mkdir(rooturl)
    os.mkdir(rooturl + fn + '_htmls')
    os.mkdir(rooturl + fn + '_pngs')

    # initialization
    list = []
    count = 1
    soup = BeautifulSoup(open('./flash.html'), "lxml")


    read_states()
    os.chdir(timestr + fn+'_output/'+fn+'_pngs')
    if not os.system('ffmpeg -f image2 -r 1/3 -start_number 1 -i ./' + fn + '%d-full.png -vcodec mpeg4 -y ../'
        + fn + '.mp4'):
        print('video generated!')