# Örnek Dosyalar (Kurgusal Senaryolar)

> ⚠️ **Tümü tamamen KURGUSAL ve anonimdir.** Gerçek kişi, şirket, TCKN, adres veya
> esas/karar numarası içermez. Yalnızca **eğitim ve deneme** amaçlıdır; hukuki danışmanlık
> değildir. Ayrıntı için kökteki [`SORUMLULUK-REDDI.md`](../SORUMLULUK-REDDI.md).

Bu klasör, eklentileri **gerçekçi bir olayla** denemek için hazırlanmış örnek dava
dosyalarını içerir. Her senaryo bir olay özeti (`olay-ozeti.md` / `README.md`), kronoloji
ve ilgili belgelerden (ihtarname, sözleşme, ihbarname, tablo vb.) oluşur.

## Nasıl kullanılır?

1. İlgili eklentileri kurun (ör. vergi senaryosu için `vergi-davalari` + `vergi-hukuku`).
2. Claude'a senaryo klasörünü ya da tek tek belgeleri verin (sessiz yükleme desteklenir).
3. Klasördeki `README.md` içindeki **"Örnek sorular"** ile başlayın.

## Senaryolar

| Klasör | Senaryo | Denenebilecek eklentiler |
|---|---|---|
| [`isci-alacagi-fesih`](./isci-alacagi-fesih) | Haksız fesih + işçilik alacakları (kıdem/ihbar, fazla mesai) | `is-hukuku-bireysel`, `hukuk-muhakemesi`, `dava-dilekce-atolyesi` |
| [`kira-borcu-tahliye`](./kira-borcu-tahliye) | Kira borcu, iki haklı ihtar ve tahliye | `kira-hukuku`, `icra-iflas-hukuku` |
| [`tuketici-ayipli-mal`](./tuketici-ayipli-mal) | Ayıplı mal — hakem heyeti / tüketici mahkemesi | `tuketici-hukuku` |
| [`vergi-resen-tarhiyat-itiraz`](./vergi-resen-tarhiyat-itiraz) | Re'sen tarhiyat + vergi ziyaı cezası → iptal davası (YD talepli) | `vergi-davalari`, `vergi-hukuku` |
| [`ceza-sorusturma-ifade`](./ceza-sorusturma-ifade) | Dolandırıcılık şüphesi — soruşturma evresi, ifade, müdafi | `ceza-muhakemesi`, `ceza-hukuku-ozel` |
| [`bosanma-nafaka-velayet`](./bosanma-nafaka-velayet) | Çekişmeli boşanma, nafaka, velayet ve mal rejimi | `aile-hukuku` |
| [`karsiliksiz-cek-takip`](./karsiliksiz-cek-takip) | Karşılıksız çek + kambiyo senetlerine özgü takip | `icra-iflas-hukuku`, `kiymetli-evrak` |
| [`kvkk-veri-ihlali`](./kvkk-veri-ihlali) | Veri ihlali + Kurula bildirim ve ilgili kişi süreçleri | `kvkk-veri-koruma`, `kvkk-uyum-checker` |

---

> Her senaryonun belgeleri kurgusaldır ve yalnızca eklentileri gerçek bir iş akışıyla
> denemek için vardır. Çıktıları her zaman güncel mevzuat ve doğrulanmış içtihatla teyit edin.
