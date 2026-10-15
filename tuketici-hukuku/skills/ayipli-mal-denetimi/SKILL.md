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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
