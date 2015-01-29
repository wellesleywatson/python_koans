#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutStrings(Koan):

    def test_double_quoted_strings_are_strings(self):
        string = "Hello, world."
        string2="Goodbye, world."
        self.assertEqual(isinstance(string2, basestring), isinstance(string, basestring))

    def test_single_quoted_strings_are_also_strings(self):
        string = 'Goodbye, world.'
        string2="Goodbye, world."
        self.assertEqual(isinstance(string2, basestring), isinstance(string, basestring))

    def test_triple_quote_strings_are_also_strings(self):
        string = """Howdy, world!"""
        string2 = """How are yah!"""
        self.assertEqual(isinstance(string2, basestring), isinstance(string, basestring))

    def test_triple_single_quotes_work_too(self):
        string = '''Bonjour tout le monde!'''
        string2 = '''Galang nuh man'''
        self.assertEqual(isinstance(string2, basestring), isinstance(string, basestring))

    def test_raw_strings_are_also_strings(self):
        string = r"Konnichi wa, world!"
        string2 = r"see yah!, world!"
        self.assertEqual(isinstance(string2, basestring), isinstance(string, basestring))

    def test_use_single_quotes_to_create_string_with_double_quotes(self):
        string = 'He said, "Go Away."'
        string2 = 'He said, "Go Away."'
        self.assertEqual(string2, string)

    def test_use_double_quotes_to_create_strings_with_single_quotes(self):
        string = "Don't"
        string2 = "Don't"
        self.assertEqual(string2, string)

    def test_use_backslash_for_escaping_quotes_in_strings(self):
        a = "He said, \"Don't\""
        b = 'He said, "Don\'t"'
        c = 'He said, "Don\'t"'
        self.assertEqual((b == c), (a == b))

    def test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line(self):
        string = "It was the best of times,\n\
It was the worst of times."
        string2 = " "
        string2 = len(string)
        self.assertEqual(string2, len(string))

    def test_triple_quoted_strings_can_span_lines(self):
        string = """
Howdy,
world!
"""
        string2 = " "
        string2 = len(string)
        self.assertEqual(string2, len(string))

    def test_triple_quoted_strings_need_less_escaping(self):
        a = "Hello \"world\"."
        b = """Hello "world"."""
        c = """Hello "world"."""
        self.assertEqual((b == c), (a == b))

    def test_escaping_quotes_at_the_end_of_triple_quoted_string(self):
        string = """Hello "world\""""
        string2 = """Hello "world\""""
        self.assertEqual(string2, string)

    def test_plus_concatenates_strings(self):
        string = "Hello, " + "world"
        string2 = "Hello, " + "world"
        self.assertEqual(string2, string)

    def test_adjacent_strings_are_concatenated_automatically(self):
        string = "Hello" ", " "world"
        string2 = "Hello" ", " "world"
        self.assertEqual(string2, string)

    def test_plus_will_not_modify_original_strings(self):
        hi = "Hello, "
        there = "world"
        string = hi + there
        self.assertEqual("Hello, ", hi)
        self.assertEqual("world", there)

    def test_plus_equals_will_append_to_end_of_string(self):
        hi = "Hello, "
        there = "world"
        hi += there
        self.assertEqual("Hello, world", hi)

    def test_plus_equals_also_leaves_original_string_unmodified(self):
        original = "Hello, "
        hi = original
        there = "world"
        hi += there
        self.assertEqual(original, original)

    def test_most_strings_interpret_escape_characters(self):
        string = "\n"
        self.assertEqual('\n', string)
        self.assertEqual("""\n""", string)
        self.assertEqual(1, len(string))
