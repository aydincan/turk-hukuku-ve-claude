---
name: sureler-ve-zamanasimi
description: "Göç işlemlerinde dava/itiraz/başvuru sürelerinin hesaplanması veya kaçırma riskinin değerlendirilmesi gerektiğinde; özellikle sınır dışı ve idari gözetimin kısa süreleri için kullanılır."
---

# Süreler ve Hak Düşürücü Süreler

## Görev
Göç ve yabancılar alanındaki tüm idari ve yargısal sürelerin başlangıcını, uzunluğunu ve son gününü doğru hesaplamak; süre kaçırma riskini önceden tespit edip uyarmak.

## Soğuk başlangıç (intake)
1. Hangi işlemin süresi hesaplanacak (sınır dışı, gözetim, ikamet ret, çalışma ret, vatandaşlık ret)?
2. Tebliğ veya öğrenme tarihi tam olarak nedir, tebligat usulü ne (elden, e-tebligat, ilanen)?
3. Arada idari itiraz/komisyon başvurusu yapıldı mı?
4. Süre uzatan/durduran bir durum (adli tatil, mücbir sebep) var mı?

## Denetim şeması
1. **Başlangıç**: Süre kural olarak tebliğ/öğrenmeyle başlar. Tebligatın usulüne uygunluğu (Tebligat Kanunu) denetlenir; usulsüz tebligat süreyi başlatmaz.
2. **Süre uzunlukları**:
   - Genel iptal davası: İYUK m.7 — 60 gün.
   - Sınır dışı kararına karşı dava: YUKK m.53'teki özel kısa süre; bu süre genel 60 günden farklıdır ve titizlikle uygulanır.
   - İdari gözetime itiraz: YUKK m.57 — sulh ceza hâkimliğine; ayrıca gözetimin periyodik (aylık) değerlendirilmesi.
   - İdari itiraz/komisyon yolu varsa işlemeye etkisi (İYUK m.11) değerlendirilir.
3. **Durma/uzama**: İYUK m.8 — sürenin son günü adli tatile/resmî tatile rastlarsa uzama; idari yargıda çalışmaya ara verme dönemi etkisi.
4. **Sonuç tipi**: Bu süreler hak düşürücüdür; geçirilmesi davanın süre yönünden reddine yol açar ve telafisi yoktur.
**Ara sonuç**: Her işlem için tek bir kesin son gün ve güvenli iç hatırlatma (son günden birkaç gün önce) belirlenir.

## Çıktı modülleri
- İşlem bazlı süre takvimi (başlangıç, uzunluk, dayanak, son gün).
- Risk uyarısı: yaklaşan/kaçırılmış süreler.
- Tebligat geçerliliği kısa değerlendirmesi.

## Plugin bağlamı

Bu beceri `goc-yabancilar-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
