# Kurulum

**Claude ve Türk Hukuku** bir *Claude Code eklenti pazarıdır* (plugin marketplace). Tek tek
eklentileri kurabilir ya da tümünü ekleyebilirsiniz.

> Önce [`SORUMLULUK-REDDI.md`](./SORUMLULUK-REDDI.md) dosyasını okuyun. Bu içerik
> **hukuki danışmanlık değildir** ve doğrulanmadan kullanılmamalıdır.

## A) Claude Code (terminal) — önerilen

1. **Pazarı ekleyin:**

   ```bash
   /plugin marketplace add aydincan/turk-hukuku-ve-claude
   ```

2. **Eklenti kurun** (`@turk-hukuku-skills` pazar adıdır):

   ```bash
   /plugin install hukuk-metodolojisi@turk-hukuku-skills
   /plugin install atif-turk-hukuku@turk-hukuku-skills
   /plugin install borclar-hukuku-genel@turk-hukuku-skills
   ```

3. **Kullanmaya başlayın:** Claude'a olayınızı anlatın ya da bir belge yükleyin. Eklentinin
   `genel-bakis` becerisi sizi triyajdan geçirir ve uygun uzman beceriye yönlendirir.

### Hangi eklentiler önce?

Her zaman önce **temel** eklentileri yükleyin — yöntem ve atıf hijyeni tüm alanların zeminidir:

```bash
/plugin install hukuk-metodolojisi@turk-hukuku-skills
/plugin install atif-turk-hukuku@turk-hukuku-skills
```

Sonra çalışma alanınıza göre uzmanlık ekleyin (ör. `is-hukuku-bireysel`, `ceza-hukuku-genel`,
`kvkk-veri-koruma`, `icra-iflas-hukuku`). Tam liste için [`README.md`](./README.md) ve
[`SKILLS.md`](./SKILLS.md).

## B) Yerel kopyadan (geliştirme / özel barındırma)

Depoyu klonlayıp yerel yoldan pazar olarak ekleyebilirsiniz:

```bash
git clone https://github.com/aydincan/turk-hukuku-ve-claude.git
cd turk-hukuku-ve-claude
/plugin marketplace add ./
```

## C) Depoyu yeniden üretmek / genişletmek

Tüm eklentiler `scripts/catalog.json` (omurga) ve `scripts/content.json` (ajan üretimi
hukuki gövde) dosyalarından **üretilir**:

```bash
python3 scripts/generate.py
```

- Yeni bir eklenti eklemek için `scripts/catalog.json` içindeki `eklentiler` dizisine
  bir girdi ekleyin (slug, grup, başat kanunlar, anahtar kelimeler, açıklama).
- Uzman beceri gövdeleri `scripts/content.json` içinde tutulur; yoksa üretici güvenli bir
  şablon yedeği kullanır, böylece depo her zaman eksiksiz ve geçerli kalır.
- `scripts/parts/*.part.md` → `scripts/content.json` birleştirmesi için:

  ```bash
  python3 scripts/merge_parts.py
  ```

## Gereksinimler

- Eklentileri kullanmak için: **Claude Code** (terminal/masaüstü).
- Depoyu yeniden üretmek için: **Python 3** (ek bağımlılık yoktur).
