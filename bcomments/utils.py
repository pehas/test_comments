# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import string


def get_random_word(word_len=15):
    return "".join([random.choice(string.letters) for i in xrange(word_len)])


def get_random_text(text_len=15):
    return " ".join([get_random_word(random.randint(0, 15)) for i in xrange(text_len)])