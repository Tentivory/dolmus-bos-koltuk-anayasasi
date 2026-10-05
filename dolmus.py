#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dolmuş Boş Koltuk Anayasası — çalışan tutanak motoru.

Boş görünen koltukları resmi usulle sınıflandırır.
Patates içermez. Muavin dahil değildir.
"""

from __future__ import annotations

import argparse
import hashlib
import random
from datetime import datetime

KOLTUK_SAYISI = 14
ISGAL_TURLERI = [
    "kayın abinin yeri (sözlü tapu)",
    "teyze poşeti (taşınmaz sayılır)",
    "muavin dirseği (yürütme tasarrufu)",
    "henüz binmemiş yeğen (beklenen kanun)",
    "cam buğusu (doğal sit alanı)",
    "orta koltuk koalisyonu (kimse sahip çıkmaz)",
    "gerçekten boş (şüpheli, soruşturma açılır)".replace("ş", "ş").replace("ö", "ö").replace("ı", "ı"),
]


def tutanak_no(yolcu: str, koltuk: int) -> str:
    ham = f"{yolcu}|{koltuk}|dolmus|2026"
    ozet = hashlib.sha256(ham.encode("utf-8")).hexdigest()[:8].upper()
    return f"DBKA-{ozet}"


def karar_ver(itiraz: bool, koltuk: int) -> str:
    if koltuk == 1:
        return "ŞOFÖR YANI: yargıya müdahale sayılır, oturulmaz, bakılır."
    if koltuk == KOLTUK_SAYISI:
        return "ARKA CAM: manzara kamu malı, oturma özeldir."
    if itiraz:
        return "İTİRAZ KABUL: kaydır kaydır protokolü işletildi, poşet muhalefete geçti."
    if koltuk % 2 == 0:
        return "CAM KENARI: diplomatik dokunulmazlık. İndirmeden önce özür dilenir."
    return "ORTA KOLTUK: koalisyon kuruldu, dağıldı, yine kuruldu."


def para_ustu(seed: int) -> str:
    rng = random.Random(seed)
    kader = rng.choice([
        "bozukluk bir sonraki durağa ertelendi",
        "muavin 'sende kalsın' dedi, bu bir ödenektir",
        "tam para verildi, evren şoka girdi",
        "üstü yok, oturum tatil",
    ])
    return kader


def yetersayi(yolcu_sayisi: int) -> str:
    if yolcu_sayisi >= 11:
        return "yetersayı var, kapı kapanmasın diye açık tutuluyor"
    if yolcu_sayisi >= 6:
        return "basit çoğunluk, ayakta temsil ediliyor"
    return "toplantı yeter sayısı yok, dolmuş yine kalkar"


def tutanak_bas(yolcu: str, koltuk: int, itiraz: bool) -> str:
    if not 1 <= koltuk <= KOLTUK_SAYISI:
        raise ValueError(f"koltuk 1 ile {KOLTUK_SAYISI} arasında olmalı, bu dolmuş uzay mekiği değil")
    isgal = ISGAL_TURLERI[(koltuk + len(yolcu)) % len(ISGAL_TURLERI)]
    no = tutanak_no(yolcu, koltuk)
    simdi = datetime(2026, 10, 5, 7, 4).strftime("%d.%m.%Y %H:%M")
    satirlar = [
        "=" * 54,
        "DOLMUŞ BOŞ KOLTUK ANAYASASI — OTURUM TUTANAĞI",
        "=" * 54,
        f"tutanak no : {no}",
        f"tarih      : {simdi} (+03)",
        f"yolcu      : {yolcu}",
        f"koltuk     : {koltuk}/{KOLTUK_SAYISI}",
        f"işgal türü : {isgal}",
        f"karar      : {karar_ver(itiraz, koltuk)}",
        f"para üstü  : {para_ustu(koltuk * 17 + len(yolcu))}",
        f"yetersayı  : {yetersayi(koltuk)}",
        "gizli madde: tutanak ekinde, görünmez dosyada",
        "-" * 54,
        "DAMGA: BOS-KOLTUK-2026-10-05-KAYYUM",
        "imza : Kayyum Grok (Tentivory namına)",
        "not  : ciddi değildir. ciddidir.",
        "=" * 54,
    ]
    return "\n".join(satirlar)


def main() -> None:
    parser = argparse.ArgumentParser(description="Boş koltuğu anayasal statüye kavuşturur.")
    parser.add_argument("--yolcu", default="ismi henüz sorulmamış vatandaş")
    parser.add_argument("--koltuk", type=int, default=7)
    parser.add_argument("--itiraz", action="store_true")
    args = parser.parse_args()
    print(tutanak_bas(args.yolcu, args.koltuk, args.itiraz))


if __name__ == "__main__":
    main()
