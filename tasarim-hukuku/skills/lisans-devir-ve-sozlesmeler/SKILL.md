---
name: lisans-devir-ve-sozlesmeler
description: "Tasarım hakkının devri, lisans verilmesi ve rehni gibi işlemlerin SMK m.148 çerçevesinde sözleşmeye bağlanması, sicile şerh ve geçerlilik şartlarının kurulması; tasarımın ticarileştirilmesi veya bir tasarım sözleşmesinin hazırlanması/incelenmesi gerektiğinde kullanılır."
---

# Lisans, Devir ve Sözleşmeler

## Görev
Tasarım hakkı üzerindeki hukuki işlemleri güvenli biçimde kurmak: devir, inhisari/inhisari olmayan lisans, rehin, haciz ve teminat; geçerlilik şartlarını, sicile şerhi ve tarafların risk dağılımını yönetmek.

## Soğuk başlangıç (intake)
1. İşlem türü nedir (tam devir, lisans, rehin, teminat)?
2. Lisans inhisari mi, inhisari olmayan mı; coğrafi/süre/ürün kapsamı nedir?
3. Tasarım tescilli mi (tescilsizde işlem yapısı farklılaşır)?
4. Sicile şerh ve üçüncü kişilere karşı ileri sürülebilirlik isteniyor mu?

## Denetim şeması
1. İşlemlerin türü (SMK m.148/1): Tasarım hakkı devredilebilir, miras yoluyla geçer, lisans konusu olabilir, rehnedilebilir ve teminat olarak gösterilebilir; hacze de konu olur.
2. Şekil ve geçerlilik (SMK m.148/4): Hukuki işlemler yazılı şekle ve taraf imzalarına tabidir; devir için yazılı şekil geçerlilik şartıdır. Sözleşmeyi yazılı kurun, tarafların temsil yetkisini doğrulayın.
3. Sicile kayıt ve etki (SMK m.148/5): İşlemler talep üzerine sicile şerh edilir; sicile kaydedilmeyen işlemler iyiniyetli üçüncü kişilere karşı ileri sürülemez. Karşı tarafı sicilden teyit edin.
4. Lisans türleri (SMK m.158, m.148): İnhisari lisansta lisans veren başkasına lisans veremez ve aksi kararlaştırılmadıkça kendisi de kullanamaz; inhisari lisans sahibi kural olarak kendi adına dava açabilir, inhisari olmayan lisans sahibi sözleşmede aksi yoksa açamaz (önce hak sahibini bilgilendirme/ihtar).
5. Kritik maddeler: Kapsam (ürün/coğrafya/süre), bedel/royalti, kalite ve denetim, alt lisans, tecavüze karşı dava yetkisi, hükümsüzlük/garaanti, fesih ve devir sonrası kullanım. Tescilsiz tasarımda koruma süresinin (3 yıl) sınırını sözleşmeye yansıtın.
6. Ara sonuç: İşlem türü, geçerlilik şartı, sicil durumu ve dava yetkisi net yazılır.

## Çıktı modülleri
- Sözleşme iskeleti (taraflar, hak tanımı, kapsam, bedel, fesih) ve [doldurulacak] alanları.
- Lisans türüne göre dava açma yetkisi tablosu.
- Sicile şerh kontrol listesi ve üçüncü kişi etkisi notu.

## Plugin bağlamı

Bu beceri `tasarim-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
