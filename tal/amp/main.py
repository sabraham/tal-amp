import curses
import curses.wrapper
import requests
import subprocess
from subprocess import Popen
import os
from pyquery import PyQuery as pq
import signal
from random import randint

FNULL = open(os.devnull, 'w')
RANDOM = False

class Episode:
    def __init__(self, ep_no):
        #r = requests.get("http://api.thisamericanlife.co/" + str(ep_no))
        site = 'http://www.thisamericanlife.org/radio-archives/episode/' + str(ep_no)
        d = pq(pq(url=site)(".top-inner").html())
        #p = r.json()['podcast']
        self.no    = ep_no
        # self.title = p['title']
        # self.description = p['description']
        # self.date = p['date']
        # self.image_url = p['image_url']
        self.title = d(".node-title").text().encode('ascii', 'ignore')
        self.description = d(".description").text().encode('ascii', 'ignore')
        self.date = d(".date").text().encode('ascii', 'ignore')
        self.latest_ep = 543
        if ep_no < self.latest_ep:
            self.podcast_url = "http://audio.thisamericanlife.org/jomamashouse/ismymamashouse/{0}.mp3".format(ep_no)
        else:
            self.podcast_url = "http://www.podtrac.com/pts/redirect.mp3/podcast.thisamericanlife.org/clean/{0}.mp3".format(ep_no)
    def play(self):
        self.process = Popen(['mpg123', '-C', self.podcast_url],
                             stdout=FNULL, stderr=subprocess.STDOUT)
        return True
    def stop(self):
        if self.process and not self.process.poll():
            self.process.terminate()
            return True
    def next(self):
        global RANDOM
        if RANDOM:
            return randint(1, self.latest_ep)
        else:
            return self.no + 1

def T(begin_x, begin_y, height, width):
    win = curses.newwin(height, width, begin_y, begin_x)
    curses.newwin(height, width, begin_y, begin_x)
    win.attron(curses.color_pair(1))
    win.bkgd(' ', curses.color_pair(1))
    win.addstr(1, 1, " " * (width - 2), curses.color_pair(4))
    for i in xrange(2, height - 1):
        win.addstr(i, width / 2 - 1, " " * 2, curses.color_pair(4))
    win.refresh()
    win.attroff(curses.color_pair(1))

def A(begin_x, begin_y, height, width):
    win = curses.newwin(height, width, begin_y, begin_x)
    curses.newwin(height, width, begin_y, begin_x)
    win.attron(curses.color_pair(1))
    win.bkgd(' ', curses.color_pair(1))
    win.addstr(1, (width - 6) / 2, " " * (width - 6), curses.color_pair(2))
    win.addstr(2, (width - 6) / 2 - 1, " " * 2, curses.color_pair(2))
    win.addstr(2, (width + 6) / 2 - 1, " " * 2, curses.color_pair(2))
    win.addstr(3, (width - 6) / 2 - 1, " " * (width - 4), curses.color_pair(2))
    for i in xrange(4, height - 1):
        win.addstr(i, (width - 6) / 2 - 1, " " * 2, curses.color_pair(2))
        win.addstr(i, (width + 6) / 2 - 1, " " * 2, curses.color_pair(2))
    win.refresh()
    win.attroff(curses.color_pair(1))

def L(begin_x, begin_y, height, width):
    win = curses.newwin(height, width, begin_y, begin_x)
    curses.newwin(height, width, begin_y, begin_x)
    win.attron(curses.color_pair(1))
    win.bkgd(' ', curses.color_pair(1))
    for i in xrange(1, height - 1):
        win.addstr(i, 1, " " * 2, curses.color_pair(4))
    win.addstr(height - 2, 1, " " * (width - 2), curses.color_pair(4))
    win.refresh()
    win.attroff(curses.color_pair(1))

def TAL(height, width):
    T(0, 0,          height, width)
    A(0, height,     height, width)
    L(0, height * 2, height, width)

def ira(begin_x, height, width, ep):
    win = curses.newwin(height, width, 0, begin_x)
    win.attron(curses.color_pair(1))
    curses.init_pair(20, 141, 141)
    #win.bkgd(' ', curses.color_pair(1))
    win.bkgd(' ', curses.color_pair(20))
    # begin glasses
    curses.init_pair(17, curses.COLOR_WHITE, curses.COLOR_BLACK)
    y = 8
    x = 4
    win.addstr(y + 1, x + 4, " " * 7, curses.color_pair(17))
    win.addstr(y + 1, x + 16, " " * 7, curses.color_pair(17))
    for i in xrange(2,5):
        win.addstr(y + i, x + 4, " " * 1, curses.color_pair(17))
        win.addstr(y + i, x + 11, " " * 1, curses.color_pair(17))
        win.addstr(y + i, x + 15, " " * 1, curses.color_pair(17))
        win.addstr(y + i, x + 22, " " * 1, curses.color_pair(17))
    win.addstr(y + 2, x + 12, " " * 4, curses.color_pair(17))
    win.addstr(y + 5, x + 4, " " * 7, curses.color_pair(17))
    win.addstr(y + 5, x + 16, " " * 7, curses.color_pair(17))
    # end glasses
    # begin eyes
    curses.init_pair(18, curses.COLOR_BLACK, 181)
    curses.init_pair(19, curses.COLOR_BLACK, curses.COLOR_WHITE)
    for i in xrange(2,5):
        win.addstr(y + i, x + 5, " " * 6, curses.color_pair(18))
        win.addstr(y + i, x + 16, " " * 6, curses.color_pair(18))
    win.addstr(y + 3, x + 7, "8", curses.color_pair(19))
    win.addstr(y + 3, x + 19, "8", curses.color_pair(19))
    # end eyes
    # begin nose
    win.addstr(y + 3, x + 12, " " * 3, curses.color_pair(18))
    win.addstr(y + 4, x + 12, " " * 3, curses.color_pair(18))
    win.addstr(y + 5, x + 11, "_" * 5, curses.color_pair(18))
    # end nose
    # begin mouth
    for i in xrange(6,9):
        win.addstr(y + i, x + 6, " " * 15, curses.color_pair(18))
    win.addstr(y + 9, x + 7, " " * 13, curses.color_pair(18))
    # end mouth
    # begin forehead
    for i in xrange(-2,1):
        win.addstr(y + i, x + 6, " " * 15, curses.color_pair(18))
    win.addstr(y + 1, x + 11, " " * 5, curses.color_pair(18))
    # end forehead
    # begin hair
    curses.init_pair(10, 253, curses.COLOR_WHITE)
    if ep:
        year = int(ep.date[-4:].strip())
        units = (year - 1995) / 4
        curses.init_pair(9, curses.COLOR_WHITE, 233)
        for i in xrange(-4,-2):
            win.addstr(y + i, x + 5, " " * 17, curses.color_pair(9))
        win.addstr(y + -2, x + 13, " " * 1, curses.color_pair(9))
        for i in xrange(-4, 1 - units):
            col = curses.color_pair(9)
            win.addstr(y + i, x + 5, " " * 1, col)
            win.addstr(y + i, x + 21, " " * 1, col)
        for i in xrange(1 - units, 1):
            col = curses.color_pair(1)
            win.addstr(y + i, x + 5, " " * 1, col)
            win.addstr(y + i, x + 21, " " * 1, col)

    else:
        curses.init_pair(9, curses.COLOR_WHITE, 233)
        for i in xrange(-4,-2):
            win.addstr(y + i, x + 5, " " * 17, curses.color_pair(9))
        win.addstr(y + -2, x + 13, " " * 1, curses.color_pair(9))
        for i in xrange(-4, 1):
            win.addstr(y + i, x + 5, " " * 1, curses.color_pair(9))
            win.addstr(y + i, x + 21, " " * 1, curses.color_pair(9))
    # begin lips/teeth
    win.addstr(y + 8, x + 7, ("| | " * 3) + '|' , curses.color_pair(19))
    # end lips/teeth
    win.refresh()

def console(begin_x, height, width, ep):
    win = curses.newwin(height, width, 0, begin_x)
    win.attron(curses.color_pair(1))
    win.bkgd(' ', curses.color_pair(1))
    y = 0
    x = 0
    if ep:
        title = ep.title
        row = 1
        while(len(title) > 0):
            win.addstr(y + row, x + 1, title[:(width - 2)])
            title = title[(width - 2):]
            row = row + 1
        win.addstr(y + row, x + 1, ep.date)
        row = row + 2
        description = ep.description
        while(len(description) > 0):
            win.addstr(y + row, x + 1, description[:(width - 2)])
            description = description[(width - 2):]
            row = row + 1
    win.refresh()
    return(win)

def controls(begin_x, begin_y, height, width):
    global RANDOM
    win = curses.newwin(height, width, begin_y, begin_x)
    win.attron(curses.color_pair(1))
    win.bkgd(' ', curses.color_pair(1))
    y = 0
    x = 0
    win.addstr(y + 1, x + 1, "E", curses.color_pair(5))
    win.addstr(y + 1, x + 2, "P:")
    win.addstr(y + 1, x + 9, "P", curses.color_pair(5))
    win.addstr(y + 1, x + 10, "LAY/PAUSE")
    win.addstr(y + 1, x + 20, "N", curses.color_pair(5))
    win.addstr(y + 1, x + 21, "EXT")
    rand_color = curses.color_pair(6) if RANDOM else curses.color_pair(0)
    win.addstr(y + 1, x + 25, "R", curses.color_pair(5))
    win.addstr(y + 1, x + 26, "ANDOM", rand_color)
    win.addstr(y + 1, width - 5, "Q", curses.color_pair(5))
    win.addstr(y + 1, width - 4, "UIT")
    win.refresh()
    return(win)

def main_(screen):
    """our main function"""
    stdscr = curses.initscr()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    curses.init_pair(1, 197,  curses.COLOR_WHITE)
    curses.init_pair(2, 0, 160)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_BLUE, 56)
    curses.init_pair(5, curses.COLOR_WHITE, 197)
    curses.init_pair(6, curses.COLOR_BLUE, curses.COLOR_WHITE)
    TAL(8, 12)
    ira(12, 24, 36, None)
    e = None
    con = console(48, 21, 40, None)
    cntrls = controls(48, 21, 3, 40)
    while True:
        global RANDOM
        c = stdscr.getch()
        if c == ord('e'):
            c = stdscr.getch()
            s = ''
            i = 0
            while c != ord('\n'):
                s = s + chr(c)
                cntrls.addstr(1, 4 + i, chr(c))
                cntrls.refresh()
                c = stdscr.getch()
                i = i + 1
            # reset controls
            cntrls = controls(48, 21, 3, 40)
            try:
                int(s)
            except ValueError, ex:
                continue
            if e:
                e.stop()
            e = Episode(int(s))
            console(48, 21, 40, e)
            ira(12, 24, 36, e)
            e.play()
        elif c == ord('q'):
            if e:
                e.stop()
            return(0)
        elif c == ord('p'):
            if e:
                e.process.send_signal(signal.SIGUSR1)
        elif c == ord('n'):
            if e:
                next = e.next()
                e.stop()
                e = Episode(next)
                console(48, 21, 40, e)
                ira(12, 24, 36, e)
                e.play()
        elif c == ord('r'):
            RANDOM = not RANDOM
            cntrls = controls(48, 21, 3, 40)
        else:
            continue

def main():
    curses.wrapper(main_)

if __name__ == '__main__':
    curses.wrapper(main_)
