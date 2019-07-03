import re
from random import random

PHONE_PATTERN = re.compile(r'^1[3-9]\d{9}$')

def is_phone_num(phone_num):
    """
    验证手机号
    :param phone_num:
    :return:
    """
    return True if PHONE_PATTERN.match(phone_num) else False

def gen_random_code(length=4):
    """

    :param length:
    :return:
    """
    if length <= 0:
        length=1

    code = random.rand