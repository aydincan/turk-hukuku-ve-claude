---
name: lisanslama-onlisans-denetim
description: "Üretim, dağıtım, tedarik gibi lisanslı faaliyetlerde önlisans/lisans başvurusu, yükümlülükler, tadil, süre uzatımı veya iptal riski değerlendirildiğinde ve EPDK lisans rejimi uyumu kontrol edileceğinde kullanılır."
---

# Lisanslama ve Önlisans Denetim Şeması

## Görev
Bir enerji faaliyetinin doğru lisans rejimine tabi olup olmadığını, önlisans/lisans yükümlülüklerinin yerine getirilip getirilmediğini ve iptal/sona erme riskini denetleyerek uyum yol haritası çıkarmak.

## Soğuk başlangıç (intake)
1. Faaliyet türü ve kapasite (MWe/MWm) nedir?
2. Önlisans mı lisans mı; veriliş ve geçerlilik tarihleri?
3. Bağlantı görüşü/çağrı mektubu, ÇED, mülkiyet/irtifak durumu tamam mı?
4. Süre uzatımı veya tadil talebi var mı; gerekçesi?

## Denetim şeması
1. **Lisans gerekliliği**: 6446 m.5 — lisansa tabi faaliyetler. İstisna: m.14 ve Lisanssız Elektrik Üretimi Yönetmeliği kapsamı (çatı GES, kendi tüketimi karşılama). Ara sonuç: lisanslı/lisanssız.
2. **Önlisans aşaması**: 6446 m.7 ve Lisans Yönetmeliği — önlisans süresi içinde mülkiyet/kullanım hakkı, ÇED kararı, bağlantı anlaşmasına çağrı, ödenmiş sermaye gibi yükümlülüklerin tamamlanması. İspat yükü başvuru sahibinde; belge eksikliği reddi/iptali doğurur.
3. **Lisansa geçiş ve yükümlülükler**: İnşa ve işletmeye geçiş süreleri, tamamlanma oranı bildirimi, teminat. Yükümlülük ihlali 6446 m.16 yaptırımlarını tetikler.
4. **Tadil/süre uzatımı**: Kurul kararı ve yönetmelikteki mücbir sebep/uzatma halleri; gecikme gerekçesinin müvekkile yüklenemeyen sebeplere dayandığı ispatlanmalı.
5. **Sona erme/iptal**: Yükümlülük ihlali, teminat iradı, başvuru üzerine sona erme. İptal işlemi idari işlem olduğundan İYUK m.7 süresi içinde dava ve m.27 yürütmenin durdurulması istemi değerlendirilir.

İçtihat için lisans iptali/önlisans uyuşmazlıklarında karararama.danistay.gov.tr (13. Daire ağırlıklı) taranır; künye doğrulanmadan [doğrulanacak] işaretlenir.

## Çıktı modülleri
- Lisans uyum kontrol listesi (yükümlülük/durum/eksik).
- Süre ve teminat riski tablosu.
- Tadil/uzatma başvurusu veya iptale karşı dava stratejisi taslağı.

## Plugin bağlamı

Bu beceri `enerji-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
