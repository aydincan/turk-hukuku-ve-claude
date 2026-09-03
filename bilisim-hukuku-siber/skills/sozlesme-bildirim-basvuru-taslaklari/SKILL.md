---
name: sozlesme-bildirim-basvuru-taslaklari
description: "Veri işleyen sözleşmesi, gizlilik/güvenlik eki, ihlal bildirimi, içerik kaldırma başvurusu, suç duyurusu gibi bilişim hukukuna özgü metinlerin taslağını üretmek gerektiğinde kullanılır."
---

# Sözleşme, Bildirim ve Başvuru Taslakları

## Görev
Bilişim/siber alanına özgü hukuki metinleri (sözleşme ekleri, bildirimler, başvurular, dilekçeler) doğru hukuki çerçeveyle ve yer tutucu disiplinine uygun taslamak.

## Soğuk başlangıç (intake)
1. Hangi belge? (veri işleyen sözleşmesi/eki, ihlal bildirimi, içerik kaldırma, suç duyurusu, ihtar?)
2. Taraflar ve sıfatları kim? (veri sorumlusu/işleyen, mağdur, sağlayıcı?)
3. Hangi olgular sabit, hangileri eksik?
4. Muhatap mercі ve dil resmiyeti ne düzeyde olmalı?

## Denetim şeması
1. **Belge tipi ve dayanağı.** Her metin dayanağına bağlanır: veri işleyen sözleşmesi (KVKK m.12 müşterek sorumluluk, aktarım şartları), ihlal bildirimi (KVKK m.12/5 ve Kurul formu), içerik kaldırma (5651 m.9/m.9/A), suç duyurusu (TCK m.243-245; CMK soruşturma), ihtar/tazminat talebi (TBK m.49/m.112).
2. **Zorunlu unsurlar.** Dilekçelerde taraf/mercі, olay özeti, hukuki sebep ve talep sonucu net ayrılır (HMK m.119 mantığı esas alınır). İhlal bildiriminde ihlalin niteliği, etkilenen veri/kişi, olası sonuçlar ve alınan tedbirler yer alır. Sözleşmede güvenlik taahhütleri, denetim, alt işleyen, ihlal bildirim yükümlülüğü ve sorumluluk dağılımı düzenlenir.
3. **Risk ve emredici hüküm süzgeci.** Sorumluluğu tümüyle kaldıran kayıtların TBK m.115 (ağır kusur/kasıtta geçersizlik) ve tüketici/emredici hükümler karşısında geçerliliği denetlenir; KVKK yükümlülükleri sözleşmeyle bertaraf edilemez.
4. **Yer tutucu disiplini.** Doğrulanmamış olgular `[doldurulacak]`, doğrulanmamış içtihat künyesi `[doğrulanacak]` olarak bırakılır; uydurma veri/numara yazılmaz.
5. **Ara sonuç.** Belgenin iskeleti, eksik bilgi listesi ve risk uyarıları birlikte sunulur.

## Çıktı modülleri
- Talep edilen belgenin tam taslağı (başlık, gövde, talep/sonuç).
- Eksik bilgi/olgu listesi ([doldurulacak] dökümü).
- Risk ve müzakere notu (geçerlilik, emredici hüküm uyarıları).

## Plugin bağlamı

Bu beceri `bilisim-hukuku-siber` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
