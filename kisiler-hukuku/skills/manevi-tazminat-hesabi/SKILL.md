---
name: manevi-tazminat-hesabi
description: "Kişilik hakkı ihlali sabit olduğunda istenecek manevi (ve varsa maddi) tazminatın miktarını, ölçütlerini ve talep tekniğini belirlemek için kullanılır."
---

# Kişilik Hakkı İhlalinde Maddi-Manevi Tazminat Hesabı

## Görev
Kişilik hakkı ihlalinin tazminat boyutunu kurmak: manevi tazminatın (TBK m.58) ve varsa maddi tazminatın (TBK m.49 vd.) dayanağını, hesap ölçütlerini, faiz ve talep tekniğini belirleyip ölçülü ve gerekçeli bir miktara ulaşmak.

## Soğuk başlangıç (intake)
- İhlal türü ve ağırlığı: yayın mı, fiilî saldırı mı, beden bütünlüğü ihlali mi?
- Tarafların ekonomik-sosyal durumu, kusur derecesi, saldırının yayılım/etkisi ne?
- Maddi zarar var mı (tedavi gideri, kazanç kaybı), belgeli mi?
- Saldırıdan elde edilen bir kazanç var mı (m.25/3, vekâletsiz iş görme yollaması)?

## Denetim şeması
1. **Hukuki dayanak** — Kişilik hakkı ihlalinde manevi tazminat: TBK m.58 (kişilik hakkı zedelenen, manevi tazminat olarak bir miktar para isteyebilir); bedensel bütünlük/ölüm hâlinde TBK m.56. Maddi tazminat genel haksız fiil hükümlerine tabidir (TBK m.49-52). TMK m.25/3 bu yollamaları yapar.
2. **Manevi tazminat ölçütleri** — Miktar, hâkimin takdiriyle (TMK m.4) belirlenir; ölçütler: ihlalin ağırlığı, kusur derecesi, tarafların ekonomik-sosyal durumu, saldırının kapsamı/yayılımı, zarar görenin duyduğu elem-üzüntü. Tazminat ne zenginleşme aracı ne de sembolik olmamalı; caydırıcı ve denkleştirici olmalıdır.
3. **Maddi zararın belirlenmesi** — Fiilî zarar ve yoksun kalınan kâr (TBK m.49); zarar tam ispatlanamıyorsa hâkim hakkaniyetle takdir eder (TBK m.50/2). Bedensel zararda kalemler TBK m.54'e göre ayrıştırılır.
4. **İndirim sebepleri** — Zarar görenin kusuru/rızası, kusurun hafifliği ve tazminatın borçluyu yoksulluğa düşürmesi (TBK m.52, m.51) tartılır.
5. **Faiz ve zamanaşımı** — Haksız fiil faizi kural olarak haksız fiil tarihinden işler; zamanaşımı TBK m.72: zarar ve failin öğrenilmesinden itibaren iki yıl ve her hâlde fiilden itibaren on yıl (fiil aynı zamanda suç teşkil ediyorsa ceza zamanaşımı uygulanır).
6. **Kazancın iadesi** — TMK m.25/3: saldırı sonucu elde edilen kazanç, vekâletsiz iş görme hükümlerine göre istenebilir.

## Çıktı modülleri
- Tazminat kalemleri tablosu (manevi + maddi + iade).
- Ölçüt bazlı manevi tazminat gerekçesi ve önerilen aralık.
- Faiz başlangıcı ve zamanaşımı kontrolü.
- Talep sonucu taslağı + `[doldurulacak]` miktar/tarih yerleri.

## Plugin bağlamı

Bu beceri `kisiler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
çalışır; bir konu eklentinin dışına taştığında ilgili başka eklentiyi işaret eder,
aksi hâlde bu eklentinin uygun bir sonraki becerisini önerir.

## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar; mahkeme (Yargıtay / Danıştay /
  Anayasa Mahkemesi / Bölge Adliye Mahkemesi / Bölge İdare Mahkemesi), daire, **esas ve
  karar numarası**, tarih ve doğrulanabilir kaynak ile verilir
  (ör. `karararama.yargitay.gov.tr`, `karararama.danistay.gov.tr`,
  `kararlarbilgibankasi.anayasa.gov.tr`, `mevzuat.gov.tr`, UYAP Emsal).
  **Model hafızasından karar numarası ÜRETME.** Emin olunmayan her künye `[doğrulanacak]`
  olarak işaretlenir.
- **Mevzuat** madde / fıkra / bent ile gösterilir (ör. "TBK m.49/1", "HMK m.114/1-ç").
- **Doktrin** yalnızca kullanıcı kaynağı sağladığında veya lisanslı canlı erişim
  belgelendiğinde kullanılır; yazar, eser, baskı ve sayfa ile.
- Varsayımlar açıkça **"varsayım"** diye işaretlenir; sahte kesinlik üretilmez.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri deneyseldir ve hukukçunun çalışmasını yapılandırmaya yarar; tek başına hukuki
sonuç doğurmaz. Tüm çıktılar yürürlükteki mevzuat ve doğrulanmış güncel içtihatla teyit
edilmelidir. Hukuki danışmanlık değildir.*
