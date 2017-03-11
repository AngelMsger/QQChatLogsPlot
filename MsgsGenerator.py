import re
from datetime import datetime

separator_pattern = re.compile(r'^={64}$')
group_name_pattern = re.compile(r'^消息分组:(.+)$')
friend_name_pattern = re.compile(r'^消息对象:(.+)$')
msg_index_pattern = re.compile(r'^(\d{4}-\d{2}-\d{2}\s\d{1,2}:\d{2}:\d{2})\s(.+)$')
remove_if_list = re.compile(r'^\s+|\s+$|\n+|\[图片]|\[表情]|https?://.*|,{2,}|\.{2,}|，{2,}|。{2,}')


def msgs(file):
    time, who, content = '', '', ''
    for line in file:
        line = remove_if_list.sub('', line)
        if line == '':
            continue
        match_flag = msg_index_pattern.match(line)
        if match_flag:
            if time != '' and who != '' and content != '':
                yield time, who, content
            time = datetime.strptime(match_flag.group(1), '%Y-%m-%d %H:%M:%S')
            who = match_flag.group(2)
            content = ''
        elif separator_pattern.match(line):
            if time != '' and who != '' and content != '':
                yield time, who, content
            break
        else:
            content += line


def logs(file):
    file.readline()
    for line in file:
        line = remove_if_list.sub('', line)
        if line == '':
            continue
        match_flag = group_name_pattern.match(line)
        if match_flag:
            group_name = match_flag.group(1)
            file.readline()
            match_flag = friend_name_pattern.match(file.readline())
            if match_flag:
                file.readline()
                friend_name = match_flag.group(1)
                yield group_name, friend_name, msgs(file)
        else:
            continue
