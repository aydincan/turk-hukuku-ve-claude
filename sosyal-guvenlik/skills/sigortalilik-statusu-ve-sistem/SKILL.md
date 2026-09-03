---
name: sigortalilik-statusu-ve-sistem
description: "Bir kişinin 4/a, 4/b veya 4/c kapsamında olup olmadığını, sigortalılığın başlangıç-bitişini ve hangi sigorta kolunun devreye girdiğini belirlemek gerektiğinde; her sosyal güvenlik dosyasının ilk adımı olarak kullanılır."
---

# Sigortalılık Statüsü ve Sistem Haritası

## Görev
Kişinin sosyal güvenlik sistemindeki yerini (statü, dönem, sigorta kolu) doğru saptamak ve uyuşmazlığı sistematik olarak konumlandırmak. Yanlış statü tespiti, tüm emeklilik/prim/dava değerlendirmesini geçersiz kılar.

## Soğuk başlangıç (intake)
- Kişi hizmet akdiyle mi (işçi), kendi nam ve hesabına mı (esnaf/şirket ortağı), yoksa kamu görevlisi olarak mı çalışıyor/çalıştı?
- Çalışma dönemi(leri) hangi tarih aralığında; 2008 Ekim öncesi (mülga kanun) dönem var mı?
- İşe giriş bildirgesi verilmiş mi, SGK hizmet dökümünde kaydı var mı?
- Uyuşmazlık emeklilik, prim, hizmet tespiti, iş kazası mı yoksa GSS mi?

## Denetim şeması
1. Statü tayini — 5510 m.4: Hizmet akdi varsa 4/a; bağımsız çalışma (esnaf, şirket ortağı, tarım) 4/b; kamu görevlisi 4/c. Şirket ortaklığında m.4/1-b ve ortaklık türü (limited ortağı, AŞ yönetim kurulu üyesi) ayrımı yapılır.
2. Sigortalı sayılmayanlar — m.6: İstisna haller (örn. bazı aile çalışmaları) elenir.
3. Başlangıç/bitiş — m.7 ve m.9: 4/a'da fiilen işe başlama, 4/b'de tescil/kayıt belirleyicidir. Ara sonuç: sigortalılık dönemleri çıkarılır.
4. Geçiş hükümleri: 2008/Ekim öncesi için 506/1479/5434 ve 5510 geçici maddeleri uygulanır; emeklilik koşulu kademeli geçişe tâbidir.
5. Sigorta kolu ayrımı: kısa vade (m.13-18) / uzun vade (m.25-37) / GSS (m.60). İspat yükü: sigortalılık iddiasında kural olarak iddia eden tarafta; kuruma bildirilmiş kayıt aksini ispata kadar esas alınır.

## Çıktı modülleri
- Statü ve dönem tablosu (statü / tarih aralığı / dayanak madde).
- Uygulanacak mevzuat (5510 mi, mülga kanun mu) tespiti.
- Devreye giren sigorta kolu ve sonraki uzman beceriye yönlendirme.

## Plugin bağlamı

Bu beceri `sosyal-guvenlik` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
