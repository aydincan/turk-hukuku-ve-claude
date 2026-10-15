---
name: hukuki-durum-tespiti-due-diligence
description: "Bir yatırım veya devralma öncesi girişimin hukuki durum tespiti (due diligence) yapılırken; kurumsal, sözleşmesel, fikri mülkiyet, iş hukuku, vergi ve KVKK risklerinin taranması, bulguların raporlanması ve red flag tespiti için kullanılır."
---

# Hukuki Durum Tespiti (Due Diligence)

## Görev
Yatırım/devralma öncesi girişimin hukuki risklerini sistematik taramak; kapanış öncesi giderilmesi gereken (condition precedent) ve fiyata/garantiye yansıması gereken bulguları ayırmak; DD raporu üretmek.

## Soğuk başlangıç (intake)
1. İşlem tipi: azınlık yatırımı mı, kontrol devri/M&A mi?
2. Şirketin yaşı, çalışan sayısı, fikri mülkiyet ağırlığı ne?
3. Hangi başlıklar kritik: IP, iş hukuku, vergi/teşvik, sözleşmeler, KVKK?
4. Daha önce yatırım turu/SAFE/borç var mı (cap table karmaşası)?
5. Süre ve veri odası (data room) erişimi hazır mı?

## Denetim şeması
1. Kurumsal: Esas sözleşme, pay defteri (TTK m.499), GK/YK kararları, ticaret sicili kayıtları; cap table'ın belgelerle örtüşmesi; geçmiş artırım/devirlerin geçerliliği (m.456, m.490).
2. Sözleşmesel: Müşteri/tedarikçi sözleşmelerinde kontrol değişikliği (change of control) ve devir yasağı; SAFE/dönüştürülebilir enstrümanların dönüşüm etkisi; SHA çakışması.
3. Fikri mülkiyet: Ürün/kod/markanın şirkete ait olduğunun teyidi — kurucu ve çalışan IP devir sözleşmeleri (6769 SMK; çalışan buluşu hükümleri; 5846 FSEK eser/mali hak devri); açık kaynak lisans uyumu.
4. İş hukuku: İş sözleşmeleri, fazla mesai/kıdem riskleri (4857), SGK uyumu (5510), ESOP/danışman ilişkilerinin niteliği (işçi mi serbest mi).
5. Vergi/teşvik: VUK uyumu, TGB/Ar-Ge teşvik şartlarının fiilen sağlanması (4691/5746), olası geçmiş dönem riskleri.
6. KVKK: Veri envanteri, aydınlatma/açık rıza, VERBİS, veri ihlali geçmişi (6698 m.10-12); DD sırasında veri aktarımının kendisi m.8-9 ile altlanır.
7. Red flag ve çıkış: Bulguları "kapanış ön şartı / fiyat düzeltmesi / beyan-tekeffül-tazminat" olarak sınıfla; düzeltilemez riskte işlemden çekilme önerisi.

## Çıktı modülleri
- Veri odası talep listesi (başlık başlık).
- DD bulgu/risk raporu (önem derecesi ve madde atıflı).
- Red flag listesi ve kapanış ön şartı/garanti önerileri.

## Plugin bağlamı

Bu beceri `girisim-startup-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
