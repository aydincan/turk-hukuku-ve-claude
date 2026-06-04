---
name: temel-kavramlar-ve-sistem
description: "Enerji dosyasını piyasa (elektrik 6446, doğal gaz 4646, yenilenebilir 5346) ve katman (lisans-düzenleyici, sözleşmesel, idari yargı) ekseninde konumlandırıp doğru kanun, yönetmelik ve mercii belirlemek gerektiğinde kullanılır."
---

# Enerji Hukuku Temel Kavramlar ve Sistematik

## Görev
Enerji dosyasını doğru piyasaya ve hukuki katmana oturtmak; uygulanacak kanun (6446/4646/5346/5015/5307), ilgili ikincil mevzuat ve görevli mercii hızlıca tespit ederek sonraki uzman becerilere doğru giriş kapısını açmak.

## Soğuk başlangıç (intake)
1. Hangi enerji türü/piyasa: elektrik, doğal gaz, yenilenebilir, akaryakıt, LPG?
2. Müvekkilin sıfatı: üretici/önlisans sahibi, tedarikçi, dağıtım/iletim, OSB üreticisi, tüketici, yatırımcı, EPC yüklenicisi?
3. Uyuşmazlık türü: lisans/düzenleyici uyum, EPDK yaptırımı, tarife/uzlaştırma alacağı, sözleşmesel (PPA/EPC) mi?
4. Lisans/önlisans var mı, hangi tarihli; lisanssız üretim kapsamında mı?
5. Bir EPDK işlemi/yaptırımı tebliğ edildi mi, tebliğ tarihi nedir?

## Denetim şeması
1. **Piyasa tespiti**: Elektrik için 6446 ve Elektrik Piyasası Lisans Yönetmeliği; doğal gaz için 4646; yenilenebilir destek için 5346; akaryakıt için 5015; LPG için 5307. Faaliyet birden çok kanunu ilgilendirebilir (ör. yenilenebilir üretim hem 6446 lisansı hem 5346 desteği).
2. **Faaliyet/lisans türü**: 6446 m.5 lisans gerektiren faaliyetler (üretim, iletim, dağıtım, toptan/perakende satış, OSB, piyasa işletim); m.14 ve Lisanssız Elektrik Üretimi Yönetmeliği kapsamında lisanssız üretim eşikleri ve mahsuplaşma. Ara sonuç: lisanslı mı lisanssız mı rejim.
3. **Katman ayrımı**: (a) Düzenleyici uyum — EPDK Kurul kararı/yönetmelik; (b) Sözleşmesel — bağlantı anlaşması, sistem kullanım anlaşması, PPA, EPC, TBK 6098; (c) İdari yargı — EPDK işlemine karşı iptal/tam yargı (İYUK).
4. **Görev-yetki ve süre**: EPDK işlemleri idari işlem; idari yargıda dava (İYUK m.7, kural 60 gün). Sözleşmesel uyuşmazlıkta tahkim şartı varsa adli yargı/tahkim ayrımını netleştir.
5. **Tarih kilidi**: Olay tarihindeki yürürlük halini ve YEKDEM/tarife versiyonunu sabitlemeden değerlendirme yapma.

## Çıktı modülleri
- Dosya konumlandırma notu (piyasa + katman + uygulanacak norm seti).
- Görevli merci ve süre uyarısı.
- Hangi uzman beceriye geçileceğine dair yönlendirme.

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
