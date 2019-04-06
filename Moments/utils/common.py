import time
import re


def handle_date(datetime):
    """
    处理时间
    :param datetime: 原生时间
    :return: 处理之后的时间
    """
    if re.match(r'(\d+)分钟前', datetime):
        minute = re.match(r'(\d+)分钟前', datetime).group(1)
        datetime = time.strftime('%Y-%m-%d', time.localtime(time.time() - float(minute) * 60))
    if re.match(r'(\d+)小时前', datetime):
        hour = re.match(r'(\d+)小时前', datetime).group(1)
        datetime = time.strftime('%Y-%m-%d', time.localtime(time.time() - float(hour) * 60 * 60))
    if re.match(r'昨天', datetime):
        datetime = time.strftime('%Y-%m-%d', time.localtime(time.time() - 24 * 60 * 60))
    if re.match(r'\d+天前', datetime):
        day = re.match(r'(\d+)', datetime).group(1)
        datetime = time.strftime('%Y-%m-%d', time.localtime(time.time() - float(day) * 24 * 60 * 60))

    return datetime
