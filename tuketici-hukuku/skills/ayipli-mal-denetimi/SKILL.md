---
name: ayipli-mal-denetimi
description: "Tüketicinin satın aldığı malda ayıp bulunduğunda seçimlik hakları, ispat karinesi ve süreleri değerlendirmek gerektiğinde; bozuk/eksik/vasfa aykırı ürün, garanti ve değişim-iade-onarım talepleri için kullanılır."
---

# Ayıplı Mal Denetimi

## Görev
Teslim edilen malın ayıplı olup olmadığını belirlemek, tüketicinin seçimlik haklarını (dönme, değişim, bedel indirimi, ücretsiz onarım) ve bunların kullanım koşullarını altlamak, ispat yükünü ve süreleri hesaplayarak talep stratejisini kurmak.

## Soğuk başlangıç (intake)
- Mal ne, ne zaman teslim alındı ve ayıp ne zaman fark edildi?
- Ayıp maddi mi (kırık, çalışmıyor), hukuki mi yoksa ekonomik/niteliksel mi (reklamda/etikette vaat edilenden farklı)?
- Tüketici hangi sonucu istiyor: para iadesi, yenisi, indirim, onarım?
- Satıcıya bildirim yapıldı mı, garanti belgesi/fatura var mı?

## Denetim şeması
1. **Ayıbın tanımı (TKHK m.8):** Mal; objektif olarak taşıması gereken özellikleri, tarafların kararlaştırdığı nitelikleri ya da reklam/etiketle vaat edilenleri taşımıyorsa ayıplıdır. Ambalaj, montaj kılavuzu veya yanlış montaj kaynaklı ayıplar da dahildir.
2. **İspat karinesi (m.10):** Teslimden itibaren altı ay içinde ortaya çıkan ayıbın teslim anında mevcut olduğu varsayılır; aksini ispat satıcıya düşer. Altı aydan sonra ispat yükü tüketicidedir. Malın ayıplı olmadığının ispatı satıcıya aittir (m.10/2).
3. **Seçimlik haklar (m.11):** Tüketici dilerse (a) sözleşmeden dönme, (b) ayıpsız misli ile değişim, (c) bedel indirimi, (d) ücretsiz onarım isteyebilir. Satıcı tüketicinin tercihini yerine getirmekle yükümlüdür; (b) ve (d) orantısız değilse seçilebilir. Ücretsiz onarım/değişim talebi azami otuz iş gününde (konutta altmış) karşılanmalı; aksi halde diğer haklar doğar (m.11/4).
4. **Sorumluluk ve rücu (m.9, m.11/5):** Satıcı, üretici ve ithalatçı ayıptan müteselsil sorumludur; satıcının üreticiye rücu hakkı saklıdır.
5. **Zamanaşımı (m.12):** Kural iki yıl; konut/tatil amaçlı taşınmazda beş yıl. Ayıp ağır kusur ya da hile ile gizlenmişse zamanaşımı ileri sürülemez. Ayıp daha sonra çıksa da iki yıllık süre teslimden işler.
6. **Ara sonuç:** Talep edilen seçimlik hak hukuken mümkün mü, süre içinde mi, ispat kime düşüyor?

## Çıktı modülleri
- Ayıp nitelendirme ve seçimlik hak değerlendirmesi.
- İspat yükü ve süre hesabı.
- Satıcıya ihtar/talep dilekçesi taslağı (yer tutucularla).
- Hakem heyeti/mahkeme yol önerisi.

## Plugin bağlamı

Bu beceri `tuketici-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
