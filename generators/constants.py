from enum import Enum

class BaseEnum(Enum):
    """Base class for all enums in this module."""

    @classmethod
    def as_dict(cls) -> dict:
        return {item.name: item.value for item in cls}

    @classmethod
    def as_list(cls) -> list:
        return [item.value for item in cls]

    @classmethod
    def as_tuple(cls) -> tuple:
        return tuple(item.value for item in cls)
    

class FontStyle(BaseEnum):
    ITALIC = "I"
    BOLD = "B"
    UNDERLINE = "U"
    BOLD_ITALIC = "BI"


class FontFamily(BaseEnum):
    ARIAL = "Arial"
    TIMES = "Times"
    COURIER = "Courier"
    HELVETICA = "Helvetica"
    SYMBOL = "Symbol"
    ZAPF_DINGBATS = "ZapfDingbats"


class Align(BaseEnum):
    CENTER = "C"
    LEFT = "L"
    RIGHT = "R"
    JUSTIFY = "J"
