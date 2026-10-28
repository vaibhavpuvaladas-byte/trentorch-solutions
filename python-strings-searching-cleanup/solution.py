def sentence_case(s: str) -> str:
    """
    Return `s` with its first character uppercase and every
    other character lowercase.
    Example: sentence_case("hELLO wORLD") -> "Hello world"
    """
    if not s:
        return ""
    
    # FIX: Changed S to s, added () to methods
    upperStr = s[0].upper()
    lowerStr = s[1:].lower()

    return upperStr + lowerStr


def swap_first_char_case(s: str) -> str:
    """
    Return `s` with ONLY its first character's case swapped;
    the rest of the string is unchanged.
    """
    if not s:
        return ""
    res = s[0]
    res = res.swapcase()

    return res + s[1:]


def equal_ignoring_case(a: str, b: str) -> bool:
    """
    Return True if `a` and `b` are the same text when case is
    ignored. Use casefold() on both sides.
    """
    # FIX: Removed buggy if not a or b check, simplified return
    return a.casefold() == b.casefold()


def case_kind(s: str) -> str:
    """
    Classify `s` using isupper(), islower(), and istitle(),
    checked in this order.
    """
    if s.isupper():
        return "upper"
    elif s.islower():
        return "lower"
    elif s.istitle():
        return "title"
    else:
        return "mixed"


def find_all(s: str, sub: str) -> list[int]:
    """
    Return a list of the starting indices of every occurrence
    of `sub` in `s`, in increasing order, INCLUDING overlapping
    occurrences.
    """
    start = 0
    res = []
    
    if not sub:
        return []

    while True:
        # FIX: Changed find() to s.find()
        pos = s.find(sub, start)
        if pos == -1:
            break

        res.append(pos)
        start = pos + 1
        
    return res


def count_overlapping(s: str, sub: str) -> int:
    """
    Return the number of occurrences of `sub` in `s`, counting
    overlapping occurrences.
    """
    if not sub:
        return 0
        
    count = 0
    start = 0
    
    while True:
        pos = s.find(sub, start)
        if pos == -1:
            break
        count += 1
        start = pos + 1
        
    return count


def has_extension(filename: str, ext: str) -> bool:
    """
    Return True if `filename` ends with a dot followed by `ext`,
    ignoring case. `ext` is given WITHOUT the dot.
    """
    target_suffix = f".{ext}"
    return filename.casefold().endswith(target_suffix.casefold())


def classify_token(token: str) -> str:
    """
    Return exactly one of the following, checked in this order:
      "digits", "letters", "alnum", "space", "other"
    """
    # FIX: Changed str.isdigit() to token.isdigit(), etc.
    if token.isdigit():
        return "digits"
    elif token.isalpha():
        return "letters"
    elif token.isalnum():
        return "alnum"
    elif token.isspace():
        return "space"
    else:
        return "other"


def clean_field(s: str) -> str:
    """
    Return `s` with, in this order:
      1. leading and trailing whitespace removed,
      2. any trailing characters from the set ".,;" removed,
      3. leading and trailing whitespace removed again.
    """
    # FIX: Chained strip(), rstrip(), and strip() to follow the exact sequence
    return s.strip().rstrip(".,;").strip()


def remove_prefix_once(s: str, prefix: str) -> str:
    """
    If `s` begins with `prefix`, return `s` with that prefix
    removed exactly ONCE. Otherwise return `s` unchanged.
    """
    if prefix and s.startswith(prefix):
        return s[len(prefix):]
    return s


def replace_first_n(s: str, old: str, new: str, n: int) -> str:
    """
    Return `s` with the first `n` occurrences of `old` replaced
    by `new`. If n == 0, return `s` unchanged. If n < 0,
    replace every occurrence.
    """
    # FIX: Added the missing "return" keyword
    return s.replace(old, new, n)
