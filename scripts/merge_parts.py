#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/parts/<slug>.part.md sınırlayıcı-markdown dosyalarını okuyup
scripts/content.json (slug -> {referans_md, beceriler:[...]}) üretir.

Sınırlayıcı format:
  <<<REFERANS>>>
  ...referans markdown...
  <<<BECERI>>>
  slug: ...
  ad: ...
  aciklama: ...
  <<<GOVDE>>>
  ...govde markdown...
  <<<BECERI>>>
  ...
  <<<SON>>>
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTS = os.path.join(ROOT, "scripts", "parts")
OUT = os.path.join(ROOT, "scripts", "content.json")

SLUG_RE = re.compile(r"^[a-z0-9-]+$")


def parse_part(text):
    # <<<REFERANS>>> ... <<<SON>>> aralığını yakala (tolerant)
    start = text.find("<<<REFERANS>>>")
    if start == -1:
        return None
    body = text[start + len("<<<REFERANS>>>"):]
    end = body.find("<<<SON>>>")
    if end != -1:
        body = body[:end]

    # ilk <<<BECERI>>> referansı ayırır
    parts = body.split("<<<BECERI>>>")
    referans_md = parts[0].strip()
    beceriler = []
    for chunk in parts[1:]:
        if "<<<GOVDE>>>" not in chunk:
            continue
        head, govde = chunk.split("<<<GOVDE>>>", 1)
        meta = {}
        for line in head.splitlines():
            line = line.strip()
            for key in ("slug", "ad", "aciklama"):
                pref = key + ":"
                if line.lower().startswith(pref):
                    meta[key] = line[len(pref):].strip()
                    break
        b_slug = meta.get("slug", "").strip()
        # slug temizliği
        b_slug = (b_slug.lower()
                  .replace("ı", "i").replace("ş", "s").replace("ğ", "g")
                  .replace("ü", "u").replace("ö", "o").replace("ç", "c"))
        b_slug = re.sub(r"[^a-z0-9-]+", "-", b_slug).strip("-")
        if not b_slug or not SLUG_RE.match(b_slug):
            continue
        beceriler.append({
            "slug": b_slug,
            "ad": meta.get("ad", b_slug).strip(),
            "aciklama": meta.get("aciklama", "").strip(),
            "govde_md": govde.strip(),
        })
    return {"referans_md": referans_md, "beceriler": beceriler}


def main():
    content = {}
    if os.path.isdir(PARTS):
        for fn in sorted(os.listdir(PARTS)):
            if not fn.endswith(".part.md"):
                continue
            slug = fn[:-len(".part.md")]
            with open(os.path.join(PARTS, fn), "r", encoding="utf-8") as f:
                parsed = parse_part(f.read())
            if parsed and parsed["beceriler"]:
                content[slug] = parsed
            else:
                print(f"  UYARI: {fn} ayrıştırılamadı veya beceri yok", file=sys.stderr)

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False, indent=2)

    total_skills = sum(len(v["beceriler"]) for v in content.values())
    print(f"content.json yazıldı: {len(content)} eklenti, {total_skills} uzman beceri.")
    # eksik referans uyarısı
    for slug, v in content.items():
        if not v["referans_md"]:
            print(f"  NOT: {slug} referans_md boş", file=sys.stderr)


if __name__ == "__main__":
    main()
