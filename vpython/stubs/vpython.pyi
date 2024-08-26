"""
This is a MyPy stub file for VPython's code modules, to use with MyPy and other
tools that use '.pyi' files to determine static type checking compliance.

Note: It is not complete yet. I only implemented the areas I'm using in VPython.
"""

from __future__ import annotations
from typing import Union, List, Tuple, ClassVar, Iterable, Optional

__author__ = "Jim Tooker"


class vector:
    """ From vector.py """
    @staticmethod
    def random() -> vector: ...

    def __init__(self, x: float, y: float, z: float) -> None: ...

    def __add__(self, other: vector) -> vector: ...
    def __sub__(self, other: vector) -> vector: ...
    def __mul__(self, other: Union[float, vector]) -> vector: ...
    def __rmul__(self, other: Union[float, vector]) -> vector: ...
    def __truediv__(self, other: Union[float, vector]) -> vector: ...
    def __neg__(self) -> vector: ...
    def __pos__(self) -> vector: ...
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
    def hat(self) -> vector: ...
    @hat.setter
    def hat(self, value: vector) -> None: ...

    @property
    def value(self) -> List[float]: ...

    def norm(self) -> vector: ...
    def dot(self, other: vector) -> float: ...
    def cross(self, other: vector) -> vector: ...
    def proj(self, other: vector) -> vector: ...
    def equals(self, other: vector) -> bool: ...
    def comp(self, other: vector) -> float: ...
    def diff_angle(self, other: vector) -> float: ...
    def rotate(self, angle: float = ..., axis: Optional[vector] = ...) -> vector: ...
    def rotate_in_place(self, angle: float = ..., axis: Optional[vector] = ...) -> None: ...


class color:
    """ From vpython.py """
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


class Mouse:
    ...

class Camera:
    def rotate(self, axis: vector, angle: float, origin: vector) -> None: ...

class canvas:
    """ From vpython.py """
    title_anchor: object
    caption_anchor: object

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
    def get_selected(cls) -> canvas: ...

    @property
    def title(self) -> str: ...
    @title.setter
    def title(self, value: str) -> None: ...

    @property
    def caption(self) -> str: ...
    @caption.setter
    def caption(self, value: str) -> None: ...

    @property
    def mouse(self) -> Mouse: ...

    @property
    def camera(self) -> Camera: ...

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
    def ambient(self) -> vector: ...
    @ambient.setter
    def ambient(self, value: vector) -> None: ...

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
    def axis(self) -> vector: ...
    @axis.setter
    def axis(self, value: vector) -> None: ...

    @property
    def forward(self) -> vector: ...
    @forward.setter
    def forward(self, value: vector) -> None: ...

    @property
    def range(self) -> int: ...
    @range.setter
    def range(self, value: int) -> None: ...

    @property
    def up(self) -> vector: ...
    @up.setter
    def up(self, value: vector) -> None: ...

    @property
    def autoscale(self) -> bool: ...
    @autoscale.setter
    def autoscale(self, value: bool) -> None: ...

    @property
    def userzoom(self) -> bool: ...
    @userzoom.setter
    def userzoom(self, value: bool) -> None: ...

    @property
    def userspin(self) -> bool: ...
    @userspin.setter
    def userspin(self, value: bool) -> None: ...

    @property
    def userpan(self) -> bool: ...
    @userpan.setter
    def userpan(self, value: bool) -> None: ...

    @property
    def lights(self) -> List[object]: ...
    @lights.setter
    def lights(self, value: List[object]) -> None: ...

    @property
    def fov(self) -> float: ...
    @fov.setter
    def fov(self, value: float) -> None: ...

    @property
    def objects(self) -> List[object]: ...

    @property
    def pixel_to_world(self) -> int: ...
    @pixel_to_world.setter
    def pixel_to_world(self, value: int) -> None: ...

    def select(self) -> None: ...
    def delete(self) -> None: ...
    def follow(self, obj: object) -> None: ...
    def append_to_title(self, title: str) -> None: ...
    def append_to_caption(self, caption: str) -> None: ...
    def objz(self, obj: object, operation: str) -> None: ...


class sphere:
    """ From vpython.py """
    pos: vector
    visible: bool
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
        texture: object = ...,
        visible: bool = ...,
        canvas: object = ...,
        make_trail: bool = ...,
        up: vector = ...,
        group: object = ...,
    ) -> None: ...

    @property
    def radius(self) -> float: ...
    @radius.setter
    def radius(self, value: float) -> None: ...

    @property
    def size(self) -> vector: ...
    @size.setter
    def size(self, value: vector) -> None: ...

    @property
    def axis(self) -> vector: ...
    @axis.setter
    def axis(self, value: vector) -> None: ...

    def clear_trail(self) -> None: ...
    def rotate(self, axis: vector, angle: float, origin: vector) -> None: ...


class ellipsoid:
    """ From vpython.py """
    pos: vector
    visible: bool
    length: float
    width: float
    height: float
    size: vector
    axis: vector
    make_trail: bool

    def __init__(
        self,
        pos: vector = ...,
        color: vector = ...,
        length: float = ...,
        height: float = ...,
        width: float = ...,
        size: vector = ...,
        axis: vector = ...,
        opacity: float = ...,
        shininess: vector = ...,
        emissive: bool = ...,
        visible: bool = ...,
        canvas: object = ...,
        make_trail: bool = ...,
        up: vector = ...,
        group: object = ...,
    ) -> None: ...

    @property
    def radius(self) -> float: ...
    @radius.setter
    def radius(self, value: float) -> None: ...

    def clear_trail(self) -> None: ...
    def rotate(self, axis: vector, angle: float, origin: vector) -> None: ...


class label:
    """ From vpython.py """
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
    """ From vpython.py """
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
    """ From vpython.py """
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
    def get_selected(cls) -> 'graph': ...

    @property
    def interval(self) -> int: ...
    @interval.setter
    def interval(self, value: int) -> None: ...

    def select(self) -> None: ...
    def delete(self) -> None: ...


class gcurve:
    """ From vpython.py """
    color: vector
    label: str
    legend: bool
    width: int
    visible: bool
    data: List[Union[Tuple[float, float], List[float]]]

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


class cylinder:
    """ From vpython.py """
    pos: vector
    visible: bool
    make_trail: bool

    def __init__(
        self,
        pos: vector = ...,
        axis: vector = ...,
        color: vector = ...,
        radius: float = ...,
        length: float = ...,
        size: vector = ...,
        opacity: float = ...,
        shininess: vector = ...,
        emissive: bool = ...,
        texture: object = ...,
        visible: bool = ...,
        canvas: object = ...,
        make_trail: bool = ...,
        up: vector = ...,
        group: object = ...,
    ) -> None: ...

    @property
    def radius(self) -> float: ...
    @radius.setter
    def radius(self, value: float) -> None: ...

    @property
    def size(self) -> vector: ...
    @size.setter
    def size(self, value: vector) -> None: ...

    @property
    def axis(self) -> vector: ...
    @axis.setter
    def axis(self, value: vector) -> None: ...

    def clear_trail(self) -> None: ...
    def rotate(self, axis: vector, angle: float, origin: vector) -> None: ...


class arrow:
    """ From vpython.py """
    pos: vector
    visible: bool
    make_trail: bool

    def __init__(
        self,
        pos: vector = ...,
        axis: vector = ...,
        color: vector = ...,
        round: bool = ...,
        shaftwidth: float = ...,
        headwidth: float = ...,
        headlength: float = ...,
        opacity: float = ...,
        shininess: vector = ...,
        emissive: bool = ...,
        texture: object = ...,
        visible: bool = ...,
        canvas: object = ...,
        make_trail: bool = ...,
        up: vector = ...,
        group: object = ...,
    ) -> None: ...

    @property
    def round(self) -> bool: ...

    @property
    def shaftwidth(self) -> float: ...
    @shaftwidth.setter
    def shaftwidth(self, value: float) -> None: ...

    @property
    def headwidth(self) -> float: ...
    @headwidth.setter
    def headwidth(self, value: float) -> None: ...

    @property
    def headlength(self) -> float: ...
    @headlength.setter
    def headlength(self, value: float) -> None: ...

    @property
    def scale(self) -> float: ...
    @scale.setter
    def scale(self, value: float) -> None: ...

    def stop(self) -> None: ...
    def start(self) -> None: ...
    def clear_trail(self) -> None: ...
    def rotate(self, axis: vector, angle: float, origin: vector) -> None: ...


class textures:
    """ From vpython.py """
    flower: str
    granite: str
    gravel: str
    earth: str
    metal: str
    rock: str
    rough: str
    rug: str
    stones: str
    stucco: str
    wood: str
    wood_old: str


""" vector.py module methods """
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


""" vpython.py module methods """
def rate(A: int) -> None: ...
def arange(A: int, B: int, step: int) -> Iterable[int]: ...
