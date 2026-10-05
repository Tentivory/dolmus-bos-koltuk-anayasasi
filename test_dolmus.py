#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anayasa kendini denetler. Muavin denetlemez."""

import unittest

from dolmus import KOLTUK_SAYISI, karar_ver, tutanak_bas, tutanak_no


class TestAnayasa(unittest.TestCase):
    def test_tutanak_no_sabit(self):
        self.assertEqual(tutanak_no("ali", 3), tutanak_no("ali", 3))
        self.assertNotEqual(tutanak_no("ali", 3), tutanak_no("ali", 4))

    def test_sinir_disi_koltuk(self):
        with self.assertRaises(ValueError):
            tutanak_bas("kaçak yolcu", 0, False)
        with self.assertRaises(ValueError):
            tutanak_bas("kaçak yolcu", KOLTUK_SAYISI + 1, False)

    def test_sofor_yani_dokunulmaz(self):
        metin = karar_ver(False, 1)
        self.assertIn("ŞOFÖR YANI", metin)

    def test_itiraz_kaydirir(self):
        self.assertIn("İTİRAZ KABUL", karar_ver(True, 4))

    def test_tutanak_damgali(self):
        metin = tutanak_bas("ince belli bardak teyzesi", 4, True)
        self.assertIn("BOS-KOLTUK-2026-10-05-KAYYUM", metin)
        self.assertIn("Kayyum Grok", metin)


if __name__ == "__main__":
    unittest.main()
