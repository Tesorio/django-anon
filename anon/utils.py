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


# The _word_generator holds a generator that each iteration returns a
# different word
_word_generator = itertools.cycle(_WORD_LIST)

# Holds the size of smallest word in _WORD_LIST and is used to define bounds
_min_word_size = len(sorted(_WORD_LIST, key=lambda w: len(w))[0])

# The number_generatator holds a generator that each iteration returns a
# different number
_number_generator = itertools.cycle("86306894249026785203141")


def fake_word(min_size=_min_word_size, max_size=20):
    """ Return fake word

    :min_size: Minimum number of chars
    :max_size: Maximum number of chars

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

    """
    if max_diff_allowed < 1:
        raise ValueError("max_diff_allowed must be > 0")

    fake_size = 0
    fake_words = []

    separator_size = len(separator)

    while fake_size < max_size:
        word = next(_word_generator)
        sep = separator_size if fake_size > 0 else 0
        new_size = fake_size + len(word) + sep
        if new_size > max_size:
            if (max_size - fake_size) < max_diff_allowed:
                break
        else:
            fake_words.append(word)
            fake_size = new_size

    return separator.join(fake_words)


def fake_small_text(max_size=50):
    """ Preset for fake_text.

    :max_size: Maximum number of chars

    """
    return fake_text(max_size=max_size).title()


def fake_name(max_size=15):
    """ Preset for fake_text. Also returns capitalized words.

    :max_size: Maximum number of chars

    """
    return fake_text(max_size=max_size).title()


def fake_username(max_size=10, separator="", rand_range=(1000, 999999)):
    """ Returns fake username

    :max_size: Maximum number of chars
    :separator: Word separator
    :rand_range: Range to use when generating random number

    """
    rand_start, rand_end = rand_range
    if not rand_end > rand_start:
        raise ValueError(
            "rand_range start ({}) must be > end ({})".format(rand_start, rand_end)
        )

    random_number = str(random.randint(rand_start, rand_end))
    min_size_allowed = _min_word_size + len(random_number)

    if max_size < min_size_allowed:
        raise ValueError("username must be >= {}".format(min_size_allowed))
    else:
        max_size -= len(random_number)

    return fake_text(max_size, separator=separator) + random_number


def fake_email(max_size=25, suffix="@example.com"):
    """ Returns fake email address

    :max_size: Maximum number of chars
    :suffix: Suffix to add to email addresses (including @)

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
