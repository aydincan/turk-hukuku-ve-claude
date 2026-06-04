> ⚠️ Bu belge tamamen KURGUSAL ve anonimdir; gerçek bir kişi, olay veya dava ile ilgisi yoktur. Eğitim/deneme amaçlıdır.

# Ayıplı Mal — Tüketici Uyuşmazlığı (Kurgusal Örnek Dosya)

Bu klasör, **Tüketici Hukuku** alanında ayıplı mal uyuşmazlığını konu alan, tamamen kurgusal ve anonim bir örnek dava dosyasıdır. `tuketici-hukuku` eklentisinin/becerilerinin gerçekçi bir senaryo üzerinde denenmesi amacıyla hazırlanmıştır.

---

## 1) Kısa Olay Özeti

**Taraflar (tümü kurgusaldır):**
- **Tüketici (Başvuran):** A. Yılmaz — bireysel tüketici.
- **Satıcı:** Demir Yapı Beyaz Eşya Ltd. Şti. — yetkili bayi/satıcı.
- **Üretici/İthalatçı (sorumlu):** Kuzey Elektronik Sanayi A.Ş. — buzdolabının üreticisi.

**Uyuşmazlık:**
A. Yılmaz, 14.01.2026 tarihinde Demir Yapı Beyaz Eşya Ltd. Şti.'den 28.499,00 TL bedelle bir no-frost buzdolabı satın almıştır. Teslimden yaklaşık 5 hafta sonra cihaz soğutmayı durdurmuş, iki kez yetkili servis müdahalesine rağmen arıza tekrarlamıştır. Bu nedenle ürün, gizli/sonradan ortaya çıkan ayıp taşımaktadır. Tüketici, ücretsiz onarımın sonuç vermemesi üzerine **sözleşmeden dönerek bedel iadesi** (ve fer'ileri) talep etmektedir. Satıcı, arızanın kullanıcı kaynaklı olduğunu ileri sürerek talebi reddetmiştir.

**Talepler:**
- Öncelikle **sözleşmeden dönme** ve ödenen **28.499,00 TL bedelin iadesi** (TKHK m.11/1-c).
- Olmadığı takdirde **ayıpsız misli ile değişim** (TKHK m.11/1-d).
- Servise götürme/kargo ve bilirkişi giderlerinin satıcıya yükletilmesi.
- Uyuşmazlık değeri itibarıyla **Tüketici Hakem Heyeti**'ne başvuru (TKHK m.68).

---

## 2) Kronoloji

| # | Tarih | Olay |
|---|-------|------|
| 1 | 14.01.2026 | Buzdolabı satın alındı; fatura düzenlendi (28.499,00 TL, peşin). |
| 2 | 16.01.2026 | Ürün teslim edildi ve kuruldu; ilk çalıştırma sorunsuz. |
| 3 | 21.02.2026 | Cihaz soğutmayı durdurdu; tüketici yetkili servisi aradı (1. arıza kaydı). |
| 4 | 25.02.2026 | 1. servis müdahalesi: kompresör rölesi değişti; arıza geçici giderildi. |
| 5 | 09.03.2026 | Aynı arıza tekrarladı (2. arıza kaydı); soğutma yine durdu. |
| 6 | 12.03.2026 | 2. servis müdahalesi sonuçsuz; tüketici e-posta ile ayıp bildiriminde bulundu ve sözleşmeden dönme/bedel iadesi talep etti. |
| 7 | 24.03.2026 | Satıcı, arızanın "kullanım hatası" olduğunu öne sürerek talebi reddetti. |
| 8 | 02.04.2026 | Tüketici, İlçe Tüketici Hakem Heyeti'ne başvuru yaptı. |

---

## 3) Hangi Becerilerle Denenebilir (`tuketici-hukuku`)

Bu dosya aşağıdaki somut işlemler için kullanılabilir:

- **Ayıp türü tespiti:** Gizli/açık ayıp ayrımı, ispat yükü ve **6 ay içinde ortaya çıkan ayıbın teslim anında var sayılması** karinesi (TKHK m.10/1) üzerinden değerlendirme.
- **Seçimlik hak analizi:** TKHK m.11'deki dört seçimlik hak (dönme, indirim, ücretsiz onarım, değişim) arasında somut olaya en uygun olanın gerekçelendirilmesi; ücretsiz onarımın "makul süre" ve "tekrar arıza" kriterleri.
- **Zamanaşımı kontrolü:** Ayıplı mallarda **2 yıllık** zamanaşımı (TKHK m.12) ve ağır kusur/hile istisnası.
- **Görev/yetki ve parasal sınır:** Uyuşmazlık değerine göre **Tüketici Hakem Heyeti mi Tüketici Mahkemesi mi** (TKHK m.68); zorunlu hakem heyeti parasal sınırının güncel yıl için kontrolü `[doğrulanacak]`.
- **Belge taslağı üretimi:** Ayıp bildirimi/ihtarname, hakem heyeti başvuru dilekçesi, delil listesi taslaklarının oluşturulması/denetlenmesi.
- **Karara/itiraza hazırlık:** Hakem heyeti kararına karşı **Tüketici Mahkemesi'ne itiraz** süresi ve usulü (TKHK m.70).

---

## 4) Örnek Sorular (Claude'a sorulabilecek)

1. "Bu olayda tüketici hangi seçimlik hakkı kullanabilir; iki kez sonuçsuz onarımdan sonra doğrudan **sözleşmeden dönme** istenebilir mi? Gerekçesini TKHK m.11 ile açıkla."
2. "28.499,00 TL'lik bu uyuşmazlık 2026 yılı için **Tüketici Hakem Heyeti**'nin görev sınırı içinde mi, yoksa doğrudan **Tüketici Mahkemesi**'ne mi gidilmeli?"
3. "Satıcının 'kullanım hatası' savunmasına karşı **ispat yükü** kimdedir; TKHK m.10 karinesi nasıl işler?"
4. "`ayip-bildirimi-eposta.md` taslağını usule uygun, ispat değeri yüksek bir **ihtarnameye** dönüştür."
5. "Hakem heyeti talebi reddederse, karara karşı **itiraz** süresi ve mercii nedir?"

---

## 5) Klasördeki Belgeler

| Dosya | İçerik |
|-------|--------|
| `README.md` | Bu dosya — olay özeti, kronoloji, kullanım. |
| `olay-ozeti.md` | Ayrıntılı vaka anlatımı, taraflar, hukuki nitelendirme ve talep özeti. |
| `fatura.md` | Satışa ilişkin kurgusal fatura metni (ürün, bedel, ödeme bilgisi). |
| `ayip-bildirimi-eposta.md` | Tüketicinin satıcıya gönderdiği ayıp bildirimi / sözleşmeden dönme e-postası. |
| `hakem-heyeti-basvurusu.md` | İlçe Tüketici Hakem Heyeti'ne sunulan başvuru dilekçesi. |
