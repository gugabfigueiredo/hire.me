# -*- coding: utf-8 -*-

import string
from random import (
    choice as Choice,
    randint as RandInt,
    sample as Sample
)

LETTERS = string.ascii_letters
DIGITS = string.digits
PUNCTUATION = string.punctuation
HEX = string.hexdigits.upper()
CYRILLIC = ''.join(chr(c) for c in range(0x400, 0x500))

CHARS = LETTERS + DIGITS + PUNCTUATION + CYRILLIC


def random(length=RandInt(1, 10), chars=CHARS, unique=False):

    '''
        Returns a random string of ´length´ printable characters and digits, whitespaces excluded.
        ´length´ defaults to a random number between 1 and 10.

        If `unique` is speficied, there will be ro repeated characters in the returned string.
    '''
    if unique:
        return ''.join(Sample(chars, length))

    else:
        return ''.join(Choice(chars) for _ in range(length))


def alpha(length=RandInt(1, 10), case=None, unique=False, **kwargs):

    '''
        Shortcut for random() with ascii charater pool.
    '''

    alpha_str = random(length, LETTERS, unique)

    if case:
        return getattr(alpha_str, case)()
    else:
        return alpha_str

    #if case == 'cammel':
        #return alpha_str[:1].upper() + alpha_str[1:].lower()
    #else:
        #return alpha_str


def numeric(length, n_range=[], unique=False):

    '''
        Shortcut for random() with numeric character pool.
    '''

    return random(length, DIGITS)


def alnum(length, unique=False):

    '''
        Shortcut for random() with ascii uppercase alphanumeric character pool.
    '''

    return random(length, LETTERS + DIGITS)


def hex(length, unique=False):

    '''
        Shortcut for random() with hexadecimal character pool.
    '''
    return random(length, chars=HEX)


def cyril(length, unique=False):

    '''
        Shortcut for random() with cyrillic character pool.
    '''
    return random(length, chars=CYRILLIC)


def by_type(string_type, length=RandInt(1, 10), unique=False, **kwargs):

    '''
        Returns a random string with `length` characters of especified `string_type`.

        string_type can be one of: 'cyril', 'alnum', 'hex', 'digit', 'alpha', 'email'
    '''
    string_gen = getattr(string_type)

    return string_gen(length, **kwargs)


def email(handler_types=['alpha'], provider='', region=''):

    '''
        Returns a random string formated as an email address
    '''

    providers = {
        'gmail': '@gmail.com',
        'hotmail': '@hotmail.com',
        'yahoomail': '@yahoo.com'
    }

    handler = by_type(Choice(handler_types), RandInt(5, 10))

    if provider:
        domain = providers[provider]
    else:
        domain = Choice(providers.values())

    if region:
        domain = domain + '.' + region

    return handler + domain


def rambling(w_count=RandInt(3, 10), w_lengths=(2, 10), types=['alpha'], *args, **kwargs):

    '''
        Creates a sentence like string with random words
    '''
    return ' '.join([getattr(Choice(types))(RandInt(*w_lengths)) for i in range(w_count)]).capitalize()


def random_generator(**kwargs):

    '''
        Generates random strings of any of the implemented type.

        By default, returns an uncapped generator that yields randomly typed strings of at most
        10 digits.

        If specified, `string_type` selects the accepted characters to generate the code with.
        Must be a list like `['cyril', 'hex']`. By default, string_type is `['random']`.
    '''
    string_types = kwargs.get(
        'string_types',
        ['random']
    )

    '''
        By default, `count` is 0. If `count` is specified, returns a generator that will throw
        StopIteration exception after `count` iterations.
    '''
    count = kwargs.get('count', 0)

    '''
        If `length` is specified, generates codes with exatcly `length` digits. By default,
        `length` is a randomly generated int between 1 and 10.

        If either `min_len` or `max_len` are specified they will override `length` and
        string_generator() generates codes of at least `min_len` digits and at most `max_len`
        digits. If `min_len` is bigger than max_len, it behaves like length. If only `max_len`
        is specified, generates codes with at most max_len digits.
    '''
    min_len = kwargs.pop(
        'min_len',
        kwargs.get('length', 1)
    )
    max_len = max(
        min_len,
        kwargs.pop(
            'max_len',
            kwargs.get('length', min_len + 9)
        )
    )

    while not count:

        yield by_type(
            Choice(string_types),
            RandInt(min_len, max_len),
            **kwargs
        )

    for _ in range(count):

        yield by_type(
            Choice(string_types),
            RandInt(min_len, max_len),
            **kwargs
        )