import csv
import os
import threading


class Thread(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index

    def run(self):
        print('Start to work on {} Thread.'.format(self.index))
        execute(self.index)


def source_read(file):
    file = open(file=file, encoding='utf-8')
    read_lines = file.readlines()
    file.close()
    return read_lines


def pass_read(file):
    if os.path.isfile(file):
        f = open(file=file, encoding='utf-8')
        read_lines = f.readlines()
        f.close()
        return read_lines
    else:
        return []


def write_phones(lines, file_name):
    file = open(file_name, 'w')
    l = map(lambda x: x + '\n', lines)
    file.writelines(l)
    file.close()


def execute(i):
    total = []
    source_file = '/home/ubuntu/main/' + 'Genneral_1_{}.txt'.format(i)
    pass_file = '/home/ubuntu/output/' + 'pass_phones_{}.csv'.format(i)
    source = source_read(file=source_file)
    pass_phones = pass_read(file=pass_file)
    for phone in source:
        if phone not in pass_phones:
            total.append(phone.strip())

    print('========================')
    print('Pass: ', len(pass_phones))
    print('Source: ', len(source))
    print('Yet: ', len(total))
    write_phones(lines=total, file_name=source_file)
    try:
        if os.path.isfile(pass_file):
            os.remove(pass_file)
    except OSError as e:
        print(e.strerror)


if __name__ == '__main__':
    print('Start')
    threads = []
    thread1 = Thread(1)
    thread2 = Thread(2)
    thread3 = Thread(3)
    thread4 = Thread(4)
    thread5 = Thread(5)
    thread6 = Thread(6)
    thread7 = Thread(7)
    thread8 = Thread(8)
    thread9 = Thread(9)
    thread10 = Thread(10)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()
    thread10.join()

    print('Exit from main thread')

