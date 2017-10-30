# pylint: disable=C0111
from mongo import fetch

MY_DICT = {12: 1200, 13: 1300}

def process(my_id):
    return MY_DICT.get(my_id)

def find(my_id):
    return fetch(my_id)