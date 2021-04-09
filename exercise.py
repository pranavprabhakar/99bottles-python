class Bottles(object):
    MORE_THAN_ONE_BOTTLE = (
        "{0} bottles of beer on the wall, {0} bottles of beer.\n"
        "Take one down and pass it around, {1} bottle{plural_suffix} of beer on the wall."
    )
    ONE_BOTTLE = (
        "1 bottle of beer on the wall, 1 bottle of beer.\n"
        "Take it down and pass it around, no more bottles of beer on the wall."
    )
    ZERO_BOTTLES = (
        "No more bottles of beer on the wall, no more bottles of beer.\n"
        "Go to the store and buy some more, 99 bottles of beer on the wall."
    )

    def get_plural_suffix(self, count: int):
        return "s" if count > 1 else ""

    def verse(self, verse_number: int):
        if verse_number == 1:
            return self.ONE_BOTTLE
        if verse_number == 0:
            return self.ZERO_BOTTLES
        return self.MORE_THAN_ONE_BOTTLE.format(
            verse_number,
            verse_number-1,
            plural_suffix=self.get_plural_suffix(verse_number-1)
        )
    
    def verses(self, start: int, end: int) -> str:
        verses = []
        while start >= end:
            verses.append(self.verse(start))
            start -= 1
        return "\n\n".join(verses)

    def song(self):
        return self.verses(99, 0)
            