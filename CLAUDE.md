# CLAUDE.md — Bu depoda çalışırken

Bu depo, **Türk hukuku için bir Claude Code eklenti pazarıdır** (plugin marketplace).
~80 bağımsız eklenti içerir; her eklenti bir `genel-bakis` (giriş/triyaj/yönlendirme)
becerisi ve birçok uzman beceri barındırır.

## Mimari (önemli)

Eklentiler **elle yazılmaz, üretilir.** Tek doğruluk kaynağı iki dosyadır:

- `scripts/catalog.json` — pazar yapılandırması + her eklentinin meta verisi (slug, grup,
  başat kanunlar, anahtar kelimeler, açıklama). **Manifestlerin yetkili kaynağıdır.**
- `scripts/content.json` — eklenti başına `referans_md` + uzman beceri gövdeleri
  (`beceriler[]`). Uzman ajanların ürettiği hukuki içerik buradadır.
- `scripts/generate.py` — ikisini birleştirip tüm depoyu yazar: `.claude-plugin/marketplace.json`,
  her eklenti için `plugin.json` / `README.md` / `references/` / `skills/.../SKILL.md`,
  kök `README.md` ve `SKILLS.md`.

**Değişiklik yaparken** üretilmiş dosyaları (eklenti dizinleri, `marketplace.json`,
`README.md`, `SKILLS.md`) doğrudan düzenlemeyin — `catalog.json` / `content.json` düzenleyip
`python3 scripts/generate.py` çalıştırın. Aksi hâlde değişiklik bir sonraki üretimde silinir.

İçerik üretim hattı: `scripts/wf_author.js` (Workflow) → `scripts/parts/*.part.md` →
`python3 scripts/merge_parts.py` → `scripts/content.json` → `generate.py`.

## Değişmez kurallar

1. **Her şey Türkçe.** Slug'lar ASCII (ı→i, ş→s, ğ→g, ü→u, ö→o, ç→c); tüm görünür içerik Türkçe.
2. **Kaynak hijyeni (omurga):** İçtihat asla model hafızasından zikredilmez. Her karar
   mahkeme + daire + esas/karar no + tarih + doğrulanabilir kaynakla verilir; emin
   olunmayan künye `[doğrulanacak]` işaretlenir. Mevzuat madde/fıkra/bent ile; doktrin
   yalnızca kullanıcı kaynağıyla. **Sahte karar numarası üretme.**
3. **Mevzuat doğruluğu:** Kanun ve madde numaraları doğru olmalı (ör. TBK 6098, TMK 4721,
   TCK 5237, HMK 6100, CMK 5271, İİK 2004, İş K. 4857, KVKK 6698).
4. **Hukuki danışmanlık değildir.** Her beceriye otomatik eklenen sorumluluk reddi ve
   "Bu beceri ne yapmaz" blokları `generate.py` içindedir; gövdelerde tekrarlanmaz.
5. **Üretici toleranslı kalmalı:** `content.json`'da içerik yoksa şablon yedeği kullanılır;
   depo her zaman eksiksiz ve geçerli (`marketplace.json` ↔ dizinler) olmalı.

## Yeni eklenti ekleme

1. `scripts/catalog.json` → `eklentiler` dizisine girdi ekle (uygun `grup`, doğru `kanunlar`).
2. İsteğe bağlı: `scripts/wf_author.js` ile o slug için hukuki gövde üret, `merge_parts.py`
   ile `content.json`'a kat.
3. `python3 scripts/generate.py` çalıştır.
4. Doğrula: `python3 -c "import json;json.load(open('.claude-plugin/marketplace.json'))"`.

## Doğrulama

```bash
python3 scripts/generate.py
# tüm plugin.json'lar parse oluyor mu + marketplace ↔ dizin tutarlı mı
find . -name plugin.json -exec python3 -c "import json,sys;json.load(open(sys.argv[1]))" {} \;
```
