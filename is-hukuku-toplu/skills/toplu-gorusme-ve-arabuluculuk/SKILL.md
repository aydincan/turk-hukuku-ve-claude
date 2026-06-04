---
name: toplu-gorusme-ve-arabuluculuk
description: "Yetki belgesinden TIS imzasina veya uyusmazlik tutanagina kadar olan toplu gorusme surecini, cagri usulunu, surelerini ve 6356 m.50 kapsaminda resmi arabuluculugu ele alir; pazarlik takvimi ve uyusmazlik tutanagi asamasinda kullanilir."
---

# Toplu Görüşme ve Resmî Arabuluculuk

## Görev
Toplu görüşmenin başlatılması, sürdürülmesi ve tıkanması halinde resmî arabuluculuğa geçişin usul-süre yönetimi. Menfaat uyuşmazlığının barışçıl çözüm hattıdır.

## Soğuk başlangıç (intake)
- Yetki belgesi tebliğ edildi mi, tarihi nedir?
- Çağrı yapıldı mı; ilk toplantı gerçekleşti mi?
- Görüşmeler kaç gündür sürüyor; uyuşmazlık tutanağı tutuldu mu?
- Hangi konularda anlaşmazlık var?

## Denetim şeması
1. **Çağrı:** 6356 m.46 — yetki belgesini alan taraf, **15 gün** içinde karşı tarafı toplu görüşmeye çağırır; çağrı tarihinden itibaren **30 gün** içinde toplanılmazsa veya görüşmeye başlanmazsa yetki düşebilir (m.46/2-3 kontrol edilir).
2. **Görüşme süresi:** 6356 m.47 — toplu görüşme süresi, ilk toplantı tarihinden itibaren **60 gün**dür.
3. **Uyuşmazlık tutanağı:** Anlaşma sağlanamaz veya taraflardan biri görüşmeye gelmezse uyuşmazlık tutanağı tutulur; bu, arabuluculuk ve grev sürecinin tetikleyicisidir.
4. **Resmî arabuluculuk:** 6356 m.50 — uyuşmazlığın görevli makama (görevli birim) bildirilmesi üzerine resmî listeden bir arabulucu görevlendirilir; arabulucu **15 gün** (gerekirse 6 işgünü uzatmayla) içinde tarafları uzlaştırmaya çalışır, sonuçta tutanak düzenler.
5. **Ara sonuç:** Arabuluculukta anlaşma olursa TİS imzalanır. Anlaşma olmazsa menfaat uyuşmazlığı grev/lokavt veya (kamu hizmeti gibi yasak hallerde) yüksek hakem yoluna açılır.

Not: Toplu menfaat uyuşmazlığında **6325 sayılı HUAK dava şartı arabuluculuk uygulanmaz**; 6356'nın kendi resmî arabuluculuk rejimi işler.

## Çıktı modülleri
- Toplu görüşme süre/aşama takvimi (15-30-60 gün eşikleri).
- Çağrı yazısı ve uyuşmazlık tutanağı iskeleti.
- Arabuluculuk sonrası yol haritası (grev / yüksek hakem / imza).

## Plugin bağlamı

Bu beceri `is-hukuku-toplu` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
