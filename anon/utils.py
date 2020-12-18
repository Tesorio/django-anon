# stdlib
import itertools
import random


_WORD_LIST = [
    "a",
    "ab",
    "accusamus",
    "accusantium",
    "ad",
    "adipisci",
    "alias",
    "aliquam",
    "aliquid",
    "amet",
    "animi",
    "aperiam",
    "architecto",
    "asperiores",
    "aspernatur",
    "assumenda",
    "at",
    "atque",
    "aut",
    "autem",
    "beatae",
    "blanditiis",
    "commodi",
    "consectetur",
    "consequatur",
    "consequuntur",
    "corporis",
    "corrupti",
    "culpa",
    "cum",
    "cumque",
    "cupiditate",
    "debitis",
    "delectus",
    "deleniti",
    "deserunt",
    "dicta",
    "dignissimos",
    "distinctio",
    "dolor",
    "dolore",
    "dolorem",
    "doloremque",
    "dolores",
    "doloribus",
    "dolorum",
    "ducimus",
    "ea",
    "eaque",
    "earum",
    "eius",
    "eligendi",
    "enim",
    "eos",
    "error",
    "esse",
    "est",
    "et",
    "eum",
    "eveniet",
    "ex",
    "excepturi",
    "exercitationem",
    "expedita",
    "explicabo",
    "facere",
    "facilis",
    "fuga",
    "fugiat",
    "fugit",
    "harum",
    "hic",
    "id",
    "illo",
    "illum",
    "impedit",
    "in",
    "incidunt",
    "inventore",
    "ipsa",
    "ipsam",
    "ipsum",
    "iste",
    "itaque",
    "iure",
    "iusto",
    "labore",
    "laboriosam",
    "laborum",
    "laudantium",
    "libero",
    "magnam",
    "magni",
    "maiores",
    "maxime",
    "minima",
    "minus",
    "modi",
    "molestiae",
    "molestias",
    "mollitia",
    "nam",
    "natus",
    "necessitatibus",
    "nemo",
    "neque",
    "nesciunt",
    "nihil",
    "nisi",
    "nobis",
    "non",
    "nostrum",
    "nulla",
    "numquam",
    "occaecati",
    "odio",
    "odit",
    "officia",
    "officiis",
    "omnis",
    "optio",
    "pariatur",
    "perferendis",
    "perspiciatis",
    "placeat",
    "porro",
    "possimus",
    "praesentium",
    "provident",
    "quae",
    "quaerat",
    "quam",
    "quas",
    "quasi",
    "qui",
    "quia",
    "quibusdam",
    "quidem",
    "quis",
    "quisquam",
    "quo",
    "quod",
    "quos",
    "ratione",
    "recusandae",
    "reiciendis",
    "rem",
    "repellat",
    "repellendus",
    "reprehenderit",
    "repudiandae",
    "rerum",
    "saepe",
    "sapiente",
    "sed",
    "sequi",
    "similique",
    "sint",
    "sit",
    "soluta",
    "sunt",
    "suscipit",
    "tempora",
    "tempore",
    "temporibus",
    "tenetur",
    "totam",
    "ullam",
    "unde",
    "ut",
    "vel",
    "velit",
    "veniam",
    "veritatis",
    "vero",
    "vitae",
    "voluptas",
    "voluptate",
    "voluptatem",
    "voluptates",
    "voluptatibus",
    "voluptatum",
]


try:
    xrange
except NameError:
    # Python 2/3 proof
    xrange = range


def _cycle_over_sample_range(start, end, sample_size):
    """
    Given a range (start, end), returns a generator that will cycle over a population
    sample with size specified by ``sample_size``
    """
    return itertools.cycle(random.sample(xrange(start, end), sample_size))


# Holds the maximum size of word sample
_max_word_size = max(len(s) for s in _WORD_LIST)

# Holds a generator that each iteration returns a different word
_word_generator = itertools.cycle(_WORD_LIST)

# Holds the size of smallest word in _WORD_LIST and is used to define bounds
_min_word_size = len(sorted(_WORD_LIST, key=lambda w: len(w))[0])

# Holds a generator that each iteration returns a different number
_number_generator = itertools.cycle("86306894249026785203141")

# Holds a generator for small integers, same as Django's PositiveSmallIntegerField
_small_int_generator = _cycle_over_sample_range(0, 32767, 1000)

# Holds a generator for small signed integers, same as Django's SmallIntegerField
_small_signed_int_generator = _cycle_over_sample_range(-32768, 32767, 1000)

# Holds a generator for integers, same as Django's PositiveIntegerField
_int_generator = _cycle_over_sample_range(0, 2147483647, 10000)

# Holds a generator for signed integers, same as Django's IntegerField
_signed_int_generator = _cycle_over_sample_range(-2147483648, 2147483647, 100000)


def fake_word(min_size=_min_word_size, max_size=20):
    """ Return fake word

    :min_size: Minimum number of chars
    :max_size: Maximum number of chars

    Example:

    >>> import django_anon as anon
    >>> print(anon.fake_word())
    adipisci

    """
    if min_size < _min_word_size:
        raise ValueError("no such word with this size < min_size")

    for word in _word_generator:
        if min_size <= len(word) <= max_size:
            return word


def fake_text(max_size=255, max_diff_allowed=5, separator=" "):
    """ Return fake text

    :max_size: Maximum number of chars
    :max_diff_allowed: Maximum difference (fidelity) allowed, in chars number
    :separator: Word separator

    Example:

    >>> print(anon.fake_text())
    alias aliquam aliquid amet animi aperiam architecto asperiores aspernatur assumenda at atque aut autem beatae blanditiis commodi consectetur consequatur consequuntur corporis corrupti culpa cum cumque cupiditate debitis delectus deleniti deserunt dicta

    """
    if max_diff_allowed < 1:
        raise ValueError("max_diff_allowed must be > 0")

    num_words = max(1, int(max_size / _max_word_size))
    words = itertools.islice(_word_generator, num_words)

    text = separator.join(words)
    try:
        while len(text) > max_size:
            text = text[: text.rindex(separator)]
    except ValueError:
        text = text[:max_size]

    return text


def fake_small_text(max_size=50):
    """ Preset for fake_text.

    :max_size: Maximum number of chars

    Example:

    >>> print(anon.fake_small_text())
    Distinctio Dolor Dolore Dolorem Doloremque Dolores

    """
    return fake_text(max_size=max_size).title()


def fake_name(max_size=15):
    """ Preset for fake_text. Also returns capitalized words.

    :max_size: Maximum number of chars

    Example:

    >>> print(anon.fake_name())
    Doloribus Ea

    """
    return fake_text(max_size=max_size).title()


def fake_username(max_size=10, separator=""):
    """ Returns fake username

    :max_size: Maximum number of chars
    :separator: Word separator
    :rand_range: Range to use when generating random number

    Example:

    >>> print(anon.fake_username())
    eius54455

    """
    random_number = str(next(_small_int_generator))
    min_size_allowed = _min_word_size + len(random_number)

    if max_size < min_size_allowed:
        raise ValueError("username must be >= {}".format(min_size_allowed))
    else:
        max_size -= len(random_number)

    return fake_text(max_size, separator=separator) + random_number


def fake_email(max_size=40, suffix="@example.com"):
    """ Returns fake email address

    :max_size: Maximum number of chars
    :suffix: Suffix to add to email addresses (including @)

    Example:

    >>> print(anon.fake_email())
    enim120238@example.com

    """
    min_size_allowed = _min_word_size + len(suffix)

    if max_size + len(suffix) > 254:
        # an email address must not exceed 254 chars
        raise ValueError("email address must not exceed 254 chars")
    elif max_size < min_size_allowed:
        raise ValueError("max_size must be >= {}".format(min_size_allowed))
    else:
        max_size -= len(suffix)

    return fake_username(max_size, separator=".") + suffix


def fake_url(max_size=50, scheme="http://", suffix=".com"):
    """ Returns fake URL

    :max_size: Maximum number of chars
    :scheme: URL scheme (http://)
    :suffix: Suffix to add to domain (including dot)

    Example:

    >>> print(anon.fake_url())
    http://facilis.fuga.fugiat.fugit.harum.hic.id.com

    """
    min_size_allowed = _min_word_size + len(scheme) + len(suffix)

    if max_size < min_size_allowed:
        raise ValueError("max_size must be >= {}".format(min_size_allowed))
    else:
        max_size -= len(scheme) + len(suffix)

    domain = fake_text(max_size=max_size, separator=".") + suffix
    return scheme + domain


def fake_phone_number(format="999-999-9999"):
    """ Returns a fake phone number in the desired format

    :format: Format of phone number to generate

    Example:

    >>> print(anon.fake_phone_number())
    863-068-9424

    """
    number = []
    for char in format:
        if char == "9":
            n = next(_number_generator)
            if not number:
                # do not start phone numbers with zero
                while n == "0":
                    n = next(_number_generator)
            number.append(n)
        else:
            number.append(char)
    return "".join(number)
