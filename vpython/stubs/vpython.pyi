"""
This is a MyPy stub file for VPython's vpython module, to use with MyPy and other
tools that use '.pyi' files to determine static type checking compliance.

Note: It is not complete yet. I only implemented the areas I'm using in VPython.
"""

from typing import Union, List, Tuple, ClassVar, Iterable
from vector import *

__author__ = "Jim Tooker"

__all__ = ['color', 'canvas', 'sphere', 'label', 'curve', 'graph', 'gcurve',
           'rate', 'arange',
          ]


class color:
    black: ClassVar[vector]
    white: ClassVar[vector]
    red: ClassVar[vector]
    green: ClassVar[vector]
    blue: ClassVar[vector]
    yellow: ClassVar[vector]
    cyan: ClassVar[vector]
    magenta: ClassVar[vector]
    orange: ClassVar[vector]
    purple: ClassVar[vector]

    @classmethod
    def gray(cls, luminance: float) -> vector: ...

    @classmethod
    def rgb_to_hsv(cls, v: vector) -> vector: ...

    @classmethod
    def hsv_to_rgb(cls, v: vector) -> vector: ...

    @classmethod
    def rgb_to_grayscale(cls, v: vector) -> vector: ...


class canvas:
    def __init__(
        self,
        title: str = ...,
        caption: str = ...,
        width: int = ...,
        height: int = ...,
        background: vector = ...,
        center: vector = ...,
        visible: bool = ...,
        resizable: bool = ...,
        align: str = ...,
        pixel_to_world: int = ...,
    ) -> None: ...

    @classmethod
    def get_selected(self) -> 'canvas': ...

    @property
    def title(self) -> str: ...
    @title.setter
    def title(self, value: str) -> None: ...

    @property
    def caption(self) -> str: ...
    @caption.setter
    def caption(self, value: str) -> None: ...

    @property
    def visible(self) -> bool: ...
    @visible.setter
    def visible(self, value: bool) -> None: ...

    @property
    def resizable(self) -> bool: ...
    @resizable.setter
    def resizable(self, value: bool) -> None: ...

    @property
    def background(self) -> vector: ...
    @background.setter
    def background(self, value: vector) -> None: ...

    @property
    def width(self) -> int: ...
    @width.setter
    def width(self, value: int) -> None: ...

    @property
    def height(self) -> int: ...
    @height.setter
    def height(self, value: int) -> None: ...

    @property
    def align(self) -> str: ...
    @align.setter
    def align(self, value: str) -> None: ...

    @property
    def center(self) -> vector: ...
    @center.setter
    def center(self, value: vector) -> None: ...

    @property
    def range(self) -> int: ...
    @range.setter
    def range(self, value: int) -> None: ...

    @property
    def pixel_to_world(self) -> int: ...
    @pixel_to_world.setter
    def pixel_to_world(self, value: int) -> None: ...

    def select(self) -> None: ...
    def delete(self) -> None: ...
    def append_to_title(self, title: str) -> None: ...
    def append_to_caption(self, caption: str) -> None: ...


class sphere:
    pos: vector
    visible: bool
    radius: float
    make_trail: bool

    def __init__(
        self,
        pos: vector = ...,
        radius: float = ...,
        color: vector = ...,
        size: vector = ...,
        axis: vector = ...,
        opacity: float = ...,
        shininess: vector = ...,
        emissive: bool = ...,
        visible: bool = ...,
        make_trail: bool = ...,
        up: vector = ...,
    ) -> None: ...

    def clear_trail(self) -> None: ...


class label:
    pos: vector
    visible: bool

    def __init__(
        self,
        pos: vector = ...,
        text: str = ...,
        color: vector = ...,
        align: str = ...,
        xoffset: int = ...,
        yoffset: int = ...,
        font: str = ...,
        background: vector = ...,
        opacity: float = ...,
        box: bool = ...,
        border: int = ...,
        line: bool = ...,
        linecolor: vector = ...,
        linewidth: int = ...,
        space: int = ...,
        pixel_pos: bool = ...,
        height: int = ...,
        visible: bool = ...
    ) -> None: ...

    @property
    def xoffset(self) -> int: ...
    @xoffset.setter
    def xoffset(self, value: int) -> None: ...

    @property
    def yoffset(self) -> int: ...
    @yoffset.setter
    def yoffset(self, value: int) -> None: ...

    @property
    def text(self) -> str: ...
    @text.setter
    def text(self, value: str) -> None: ...

    @property
    def align(self) -> str: ...
    @align.setter
    def align(self, value: str) -> None: ...

    @property
    def font(self) -> str: ...
    @font.setter
    def font(self, value: str) -> None: ...

    @property
    def height(self) -> int: ...
    @height.setter
    def height(self, value: int) -> None: ...

    @property
    def background(self) -> vector: ...
    @background.setter
    def background(self, value: vector) -> None: ...

    @property
    def border(self) -> int: ...
    @border.setter
    def border(self, value: int) -> None: ...

    @property
    def box(self) -> bool: ...
    @box.setter
    def box(self, value: bool) -> None: ...

    @property
    def line(self) -> bool: ...
    @line.setter
    def line(self, value: bool) -> None: ...

    @property
    def linewidth(self) -> int: ...
    @linewidth.setter
    def linewidth(self, value: int) -> None: ...

    @property
    def linecolor(self) -> vector: ...
    @linecolor.setter
    def linecolor(self, value: vector) -> None: ...

    @property
    def space(self) -> int: ...
    @space.setter
    def space(self, value: int) -> None: ...

    @property
    def pixel_pos(self) -> bool: ...
    @pixel_pos.setter
    def pixel_pos(self, value: bool) -> None: ...


class curve:
    def __init__(
        self,
        pos: List[vector] = ...,
        color: vector = ...,
        radius: float = ...,
        size: vector = ...,
        origin: vector = ...,
        axis: vector = ...,
    ) -> None: ...

    def append(self, pos: vector) -> None: ...
    def modify(self, index: int, pos: vector) -> None: ...
    def clear(self) -> None: ...


class graph:
    def __init__(
        self,
        title: str = ...,
        xtitle: str = ...,
        ytitle: str = ...,
        xmin: float = ...,
        xmax: float = ...,
        ymin: float = ...,
        ymax: float = ...,
        width: int = ...,
        height: int = ...,
        background: vector = ...,
        foreground: vector = ...,
        align: str = ...,
        scroll: bool = ...,
        fast: bool = ...,
        logx: bool = ...,
        logy: bool = ...,
    ) -> None: ...

    @classmethod
    def get_selected(self) -> 'graph': ...

    @property
    def interval(self) -> int: ...
    @interval.setter
    def interval(self, value: int) -> None: ...

    def select(self) -> None: ...
    def delete(self) -> None: ...


class gcurve:
    def __init__(
        self,
        color: vector = ...,
        label: str = ...,
        legend: bool = ...,
        width: int = ...,
        markers: bool = ...,
        marker_color: vector = ...,
        dot: bool = ...,
        dot_radius: int = ...,
        dot_color: vector = ...,
        visible: bool = ...,
        data: List[Union[Tuple[float, float], List[float]]] = ...,
        graph: graph = ...,
    ) -> None: ...

    @property
    def markers(self) -> bool: ...
    @markers.setter
    def markers(self, value: bool) -> None: ...

    @property
    def marker_color(self) -> vector: ...
    @marker_color.setter
    def marker_color(self, value: vector) -> None: ...

    @property
    def dot(self) -> bool: ...
    @dot.setter
    def dot(self, value: bool) -> None: ...

    @property
    def dot_radius(self) -> int: ...
    @dot_radius.setter
    def dot_radius(self, value: int) -> None: ...

    @property
    def dot_color(self) -> vector: ...
    @dot_color.setter
    def dot_color(self, value: vector) -> None: ...

    def plot(self, x: float, y: float) -> None: ...
    def delete(self) -> None: ...


# Class methods
def rate(A: int) -> None: ...
def arange(A: int, B: int, step: int) -> Iterable[int]: ...
