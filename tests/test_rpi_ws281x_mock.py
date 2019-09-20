#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `rpi_ws281x_mock` package."""

import pytest

from click.testing import CliRunner

from rpi_ws281x import PixelStrip, Adafruit_NeoPixel, Color

NUM_PIXELS = 10

@pytest.fixture
def pixel_strip():
    """
    Initialized and started PixelStrip fixture
    """
    ps = PixelStrip(NUM_PIXELS, 0)
    ps.begin()
    return ps

def test_initialize():
    PixelStrip(0, 0)
    Color(0, 0, 0)
    Adafruit_NeoPixel(0, 0)

def test_begin():
    ps = PixelStrip(0,0)
    ps.begin()
    assert ps.started

def set_get_pixel_color(pixel_strip, pixel, color):
    pixel_strip.setPixelColor(pixel, color)
    assert pixel_strip._led_buffer[pixel] == color
    pixel_strip.show()
    assert pixel_strip._leds[pixel] == color
    assert pixel_strip.getPixelColor(pixel) == color

@pytest.mark.parametrize(
    "p,c",
    [
        (0, Color(255, 255, 255)),
        (1, Color(255, 0, 0)),
        (2, Color(255, 255, 0)),
        (3, Color(0, 255, 255)),
        (4, Color(0, 255, 0)),
        (5, Color(255, 0, 255)),
        (6, Color(0, 0, 255)),
        (7, Color(0, 0, 0)),
    ]
)
def test_set_pixel(p, c, pixel_strip):
    set_get_pixel_color(pixel_strip, p, c)

def set_get_pixel_color_rgb(pixel_strip, pixel, r, g, b):
    pixel_strip.setPixelColorRGB(pixel, r, g, b)
    assert pixel_strip._led_buffer[pixel] == Color(r, g, b)
    pixel_strip.show()
    assert pixel_strip._leds[pixel] == Color(r, g, b)
    assert pixel_strip.getPixelColor(pixel) == Color(r, g, b)
    c = pixel_strip.getPixelColorRGB(pixel)
    assert c.r == r
    assert c.g == g
    assert c.b == b

@pytest.mark.parametrize(
    "p,r,g,b",
    [
        (0, 255, 255, 255),
        (1, 255, 0, 0),
        (2, 255, 255, 0),
        (3, 0, 255, 255),
        (4, 0, 255, 0),
        (5, 255, 0, 255),
        (6, 0, 0, 255),
        (7, 0, 0, 0),
    ]
)
def test_set_pixel_rgb(p, r, g, b, pixel_strip):
    set_get_pixel_color_rgb(pixel_strip, p, r, g, b)


def set_get_brightness(pixel_strip, brightness):
    pixel_strip.setPixelColor(0, Color(255, 255, 255))
    c = pixel_strip.getPixelColor(0)
    pixel_strip.setBrightness(brightness)
    assert pixel_strip._brightness == brightness
    pixel_strip.show()
    c1 = pixel_strip.getPixelColor(0)
    assert c1 == c * brightness / 255
    assert brightness == pixel_strip.getBrightness()

@pytest.mark.parametrize(
    "b",
    [0,1,15,50,100,150,200,250,255]
)
def test_set_brightness(b, pixel_strip):
    set_get_brightness(pixel_strip, b)

def test_num_pixels(pixel_strip):
    assert pixel_strip.numPixels() == NUM_PIXELS
