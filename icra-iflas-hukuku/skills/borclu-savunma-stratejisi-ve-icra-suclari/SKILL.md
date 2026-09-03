---
name: borclu-savunma-stratejisi-ve-icra-suclari
description: "Hakkında takip başlatılan borçlu için savunma haritası kurmak, taahhüt-mal beyanı yükümlülüklerini ve İİK'nın icra suçlarını (taahhüdü ihlal, mal kaçırma) değerlendirmek; ödeme/yapılandırma ve uzlaşma seçeneklerini tartmak için kullanılır."
---

# Borçlu Savunma Stratejisi ve İcra Ceza

## Görev
Borçlu/müvekkil cephesinde takibe karşı bütünsel savunma kurmak; itiraz/şikâyet/menfi tespit seçeneklerini sıralamak; mal beyanı ve ödeme taahhüdü yükümlülüklerini ve İİK'nın icra suçlarını (m.331 vd.) yönetmek.

## Soğuk başlangıç (intake)
- Borç gerçekte var mı; itiraz/menfi tespit dayanağı var mı?
- Ödeme emri türü ve süresi nedir; itiraz süresi geçti mi?
- Mal beyanı verildi mi; ödeme taahhüdü imzalandı mı?
- Haciz/satış riski hangi malları kapsıyor; haczedilmezlik var mı?

## Denetim şeması
1. **Savunma yolu sıralaması**: Önce takibi durduran yollar (ilamsızda itiraz m.62; kambiyoda teminatla durdurma m.169/a); ardından menfi tespitle teminatla icranın durdurulması (m.72); usul hatalarında şikâyet (m.16).
2. **Mal beyanı (m.74-76)**: Borçlu süresinde gerçek mal beyanında bulunmalı; bulunmama veya gerçeğe aykırı beyan icra ceza boyutunu doğurur. Haczedilmezlik itirazları zamanında ileri sürülür (m.82-83).
3. **Ödeme taahhüdü ve ihlali (m.111, m.340)**: İcra dairesinde alacaklının kabulüyle yapılan ödeme taahhüdünün ihlali, şikâyet üzerine tazyik hapsi gündeme getirir; taahhüdün geçerlilik şartları (miktar, tarih, kabul) sıkı denetlenir.
4. **İcra suçları (m.331 vd.)**: Mal kaçırma/gizleme, alacaklıyı zarara sokma, gerçeğe aykırı beyan gibi fiiller için icra ceza mahkemesi görevlidir; şikâyet süreleri ve tazyik hapsi koşulları değerlendirilir.
5. **Yapılandırma/uzlaşma**: Taksitlendirme, haczin kaldırılması karşılığı ödeme, sulh ve gerektiğinde konkordato seçeneği tartılır.
6. **Ara sonuç**: Risk-fayda dengesine göre savunma planı ve ceza riski haritası çıkarılır.

## Çıktı modülleri
- Savunma yolu öncelik sıralaması (durdurucu etkilere göre).
- Mal beyanı/taahhüt risk notu ve icra ceza kontrolü.
- Ödeme/yapılandırma senaryoları.

## Plugin bağlamı

Bu beceri `icra-iflas-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
