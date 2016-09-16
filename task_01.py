#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Converting temperatures"""


import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def celsius_to_kelvin(degrees):
    """This function converts a Celsius to Fahrenheit

        Args:
            degrees(int): Degrees in Celsius.

        Returns: Converts celsius to kelvin

        Examples:
            >>> celsius_to_kelvin(100)
            Decimal('373.15')
            >>> celsius_to_kelvin(0)
            Decimal('273.15')
            >>> celsius_to_kelvin(28)
            Decimal('301.15')
    """

    return decimal.Decimal(degrees) + ABSOLUTE_DIFFERENCE


def fahrenheit_to_celsius(degrees):
    """This function converts a Fahrenheit temperature to Celsius

        Args:
            degrees(int): Degrees in Fahrenheit.

        Returns:
            decimal: Degrees converted from Fahrenheit to Celsius.

        Examples:
            >>> fahrenheit_to_celsius(100)
            Decimal('37.77777777777777777777777778')
            >>> fahrenheit_to_celsius(212)
            Decimal('100')
            >>> fahrenheit_to_celsius(32)
            Decimal('0')
    """
    return ((decimal.Decimal(degrees) - 32)*5)/9


def fahrenheit_to_kelvin(degrees):
    """This function converts a Fahrenheit temperature to Celsius

        Args:
            degrees(int): Degrees in Fahrenheit.

        Returns:
            decimal: Degrees converted from Celsius to Kelvin.

        Examples:
            >>> fahrenheit_to_celsius(100)
            Decimal('37.77777777777777777777777778')
            >>> fahrenheit_to_celsius(212)
            Decimal('100')
            >>> fahrenheit_to_celsius(32)
            Decimal('0')
    """
    return celsius_to_kelvin(fahrenheit_to_celsius(degrees))
