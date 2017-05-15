filename = "./German_SE.txt"
from bs4 import BeautifulSoup
import os

# location of cmurphi/ex/test
default_url = '/Users/Bella/Documents/Lab/visualization'
fn = filename.split('.')[1].split('/')[1]

# change location
os.chdir(default_url)

list = []
soup = BeautifulSoup(open('./german.html'),"lxml")
count = 1

def read_draw():
    states = []
    with open(filename) as f:
        for line in f:
            # 去掉头尾空白
            line = line.strip()

            if line.startswith('End'): break

            if not len(line) or line.startswith('The'):
                continue
            if line.startswith('-'):
                draw(states,s)
                # print(states)
                states = []
                # print(states)
            elif line.startswith('Startstate') or line.startswith('Rule'):
                s = line
                print(s)
            else:
                states.append([n for n in line.split(':')])


def draw(states,s):
    global list
    global soup
    global count
    global fn

    # if not list:
    #     name = []
    #     for i in range(len(states)):
    #         name.append(states[i][0])
    #         # print(states[i][0])
    #     print(name)
    #     list = soup.find_all(id=name)
    #     print('list', list)
    #     # print(''states[0])
    # else:
    #     for i in range(len(list)):
    #         if list[i].string != states[i][1]:
    #             list[i]['class'] = 'font_dark'
    #             list[i].string = states[i][1]
    #         else:
    #             list[i]['class'] = 'font_white'

    # print(len(states))
    for i in range(len(states)):
        q = soup.find(id=states[i][0])
        if not q: continue;
        if q.string != states[i][1]:
            q['class'] = 'font_dark'
            q.string = states[i][1]
        else:
            q['class'] = 'font_white'

    p = soup.find(id='rule')
    p.string = s.split(',')[0];

    html = soup.prettify()
    with open("./output_html/output"+str(count)+".html", "w") as file:
        file.write(html)
    os.system('webkit2png -W 1366 -H 768 -F ./output_html/output'+str(count)+'.html -D ./pics -o '+ fn + str(count));
    count += 1


read_draw()
os.chdir('pics')
os.system('ffmpeg -f image2 -r 1/2 -start_number 1 -i ./'+ fn +'%d-full.png -vcodec mpeg4 -y '+ fn +'.mp4')
print('video generated!')