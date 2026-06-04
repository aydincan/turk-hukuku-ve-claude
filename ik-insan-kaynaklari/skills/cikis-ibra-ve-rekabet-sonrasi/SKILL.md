---
name: cikis-ibra-ve-rekabet-sonrasi
description: "İş ilişkisi sona ererken ibraname, çalışma belgesi, SGK çıkış, gizlilik/rekabet yasağının devamı ve çıkış görüşmesi belgelerinin hazırlanması gerektiğinde kullanılır."
---

# Çıkış İşlemleri, İbraname ve Rekabet Sonrası

## Görev
İş ilişkisinin sonlanmasında tüm çıkış belgelerini hukuka uygun ve geçerli biçimde üretmek; özellikle ibranamenin geçerlilik şartlarını ve fesih sonrası rekabet/gizlilik yükümlülüklerini güvence altına almak.

## Soğuk başlangıç (intake)
1. Fesih kim ve hangi sebeple yapıldı, çıkış tarihi nedir?
2. Ödenecek alacaklar net mi, banka üzerinden mi ödenecek?
3. Sözleşmede rekabet yasağı/gizlilik kaydı var mı, devam edecek mi?
4. Çalışma belgesi, SGK çıkış bildirimi ve referans talebi var mı?

## Denetim şeması
1. **İbraname geçerlilik şartları (TBK m.420)**: İbra sözleşmesi **yazılı**, fesihten **en az 1 ay sonra** tarihli, alacak türü-tutarı açıkça belirtilmiş ve ödemenin **banka aracılığıyla** yapılmış olması gerekir. Bu şartları taşımayan ibra **kesin hükümsüz**; tam ödeme içermeyen belge makbuz hükmündedir.
2. **Çalışma belgesi (4857 m.28)**: İşveren, istek halinde işin türü ve süresini gösteren belgeyi vermek zorunda; gerçeğe aykırı belge sorumluluk doğurur.
3. **SGK çıkış (5510)**: İşten ayrılış bildirgesi süresinde verilmeli; gecikme idari para cezası doğurur.
4. **Rekabet yasağının devamı (TBK m.444-447)**: Yasağın fesihten sonra işlemesi için geçerlilik şartları (yer-zaman-konu sınırı, korunmaya değer menfaat) sürmeli; işveren haklı sebep olmadan feshederse veya işçi işverenin kusuruyla haklı feshederse **rekabet yasağı sona erer (m.447/2)**.
5. **Gizlilik**: Sözleşmesel gizlilik ve sır saklama borcu iş ilişkisi sonrası da sürebilir; süre ve kapsam makul olmalı.
6. **Ara sonuç**: Erken tarihli/elden ödemeli ibra geçersiz → dava riski; rekabet yasağının ayakta olup olmadığı fesih şekline bağlı.

## Çıktı modülleri
- Geçerli ibraname taslağı (1 ay + banka ödemesi notlu).
- Çalışma belgesi ve çıkış görüşmesi tutanağı taslağı.
- Rekabet/gizlilik yükümlülüğü hatırlatma yazısı.

## Plugin bağlamı

Bu beceri `ik-insan-kaynaklari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
