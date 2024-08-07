"""
This is a MyPy stub file for VPython, to use with MyPy and other IDEs that
use '.pyi' files to determine Typing compliance.

Note: It is not complete. I only implemented the areas I'm using in VPython.
      The vector class is complete as far as I know though.
"""

from typing import Union, List, Tuple, ClassVar, Iterable, Optional

__author__ = "Jim Tooker"

__all__ = ['vector', 'color', 'canvas', 'sphere', 'label', 'curve', 'graph', 'gcurve',
           'mag', 'mag2', 'norm', 'hat', 'cross', 'proj', 'dot', 'comp',
           'diff_angle', 'rotate', 'adjust_up', 'adjust_axis', 'object_rotate',
           'rate', 'arange']


class vector:
    @staticmethod
    def random() -> 'vector': ...

    def __init__(self, x: float, y: float, z: float) -> None: ...

    def __add__(self, other: 'vector') -> 'vector': ...
    def __sub__(self, other: 'vector') -> 'vector': ...
    def __mul__(self, other: Union[float, 'vector']) -> 'vector': ...
    def __rmul__(self, other: Union[float, 'vector']) -> 'vector': ...
    def __truediv__(self, other: Union[float, 'vector']) -> 'vector': ...
    def __neg__(self) -> 'vector': ...
    def __pos__(self) -> 'vector': ...
    def __eq__(self: object, other: object) -> bool: ...
    def __neq__(self: object, other: object) -> bool: ...

    @property
    def x(self) -> float: ...
    @x.setter
    def x(self, value: float) -> None: ...

    @property
    def y(self) -> float: ...
    @y.setter
    def y(self, value: float) -> None: ...

    @property
    def z(self) -> float: ...
    @z.setter
    def z(self, value: float) -> None: ...

    @property
    def mag(self) -> float: ...
    @mag.setter
    def mag(self, value: float) -> None: ...

    @property
    def mag2(self) -> float: ...
    @mag2.setter
    def mag2(self, value: float) -> None: ...

    @property
    def hat(self) -> 'vector': ...
    @hat.setter
    def hat(self, value: 'vector') -> None: ...

    @property
    def value(self) -> List[float]: ...

    def norm(self) -> 'vector': ...
    def dot(self, other: 'vector') -> float: ...
    def cross(self, other: 'vector') -> 'vector': ...
    def proj(self, other: 'vector') -> 'vector': ...
    def equals(self, other: 'vector') -> bool: ...
    def comp(self, other: 'vector') -> float: ...
    def diff_angle(self, other: 'vector') -> float: ...
    def rotate(self, angle: float = ..., axis: Optional[vector] = ...) -> 'vector': ...
    def rotate_in_place(self, angle: float = ..., axis: Optional[vector] = ...) -> None: ...

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


# Class methods from vector.py
def mag(A: vector) -> float: ...
def mag2(A: vector) -> float: ...
def norm(A: vector) -> vector: ...
def hat(A: vector) -> vector: ...
def cross(A: vector) -> vector: ...
def proj(A: vector) -> vector: ...
def dot(A: vector, B: vector) -> float: ...
def comp(A: vector) -> float: ...
def diff_angle(A: vector, B: vector) -> float: ...
def rotate(A: vector, angle: float = ..., axis: Optional[vector] = ...) -> vector: ...
def adjust_up(oldaxis: vector, newaxis: vector, up: vector, save_oldaxis: Optional[vector]) -> Optional[vector]: ...
def adjust_axis(oldup: vector, newup: vector, axis: vector, save_oldup: Optional[vector]) -> Optional[vector]: ...
def object_rotate(objaxis: vector, objup: vector, angle: float, axis: vector) -> None: ...

# Class methods from vpython.py
def rate(A: int) -> None: ...
def arange(A: int, B: int, step: int) -> Iterable[int]: ...

