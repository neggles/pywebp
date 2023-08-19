from enum import Enum

from _webp import lib


class WebPPreset(Enum):
    DEFAULT = lib.WEBP_PRESET_DEFAULT  # Default
    PICTURE = lib.WEBP_PRESET_PICTURE  # Indoor photo, portrait-like
    PHOTO = lib.WEBP_PRESET_PHOTO  # Outdoor photo with natural lighting
    DRAWING = lib.WEBP_PRESET_DRAWING  # Drawing with high-contrast details
    ICON = lib.WEBP_PRESET_ICON  # Small-sized colourful image
    TEXT = lib.WEBP_PRESET_TEXT  # Text-like


class WebPColorMode(Enum):
    RGB = lib.MODE_RGB
    RGBA = lib.MODE_RGBA
    BGR = lib.MODE_BGR
    BGRA = lib.MODE_BGRA
    ARGB = lib.MODE_ARGB
    RGBA_4444 = lib.MODE_RGBA_4444
    RGB_565 = lib.MODE_RGB_565
    rgbA = lib.MODE_rgbA
    bgrA = lib.MODE_bgrA
    Argb = lib.MODE_Argb
    rgbA_4444 = lib.MODE_rgbA_4444
    YUV = lib.MODE_YUV
    YUVA = lib.MODE_YUVA
    LAST = lib.MODE_LAST


class WebPError(Exception):
    pass
