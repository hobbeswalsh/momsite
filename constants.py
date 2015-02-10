# -*- coding: utf-8 -*-

import random

caption_choices = [
    "Annie got her start counseling cute puppies.",
    ("When she's not counseling, Annie can be found race walking "
     "or hanging out with her dogs. Or both."),
    "The counselor in her natural environment: a coffee shop.",
    """Annie doesn't bring her "assistant" to counseling sessions.""",
]


def get_caption():
    return random.choice(caption_choices)