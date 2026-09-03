---
name: hukuki-due-diligence
description: "Hedef şirkette kurumsal, sözleşmesel, dava, iş, fikri mülkiyet, gayrimenkul, vergi ve uyum başlıklarını taramak, kırmızı bayrakları tespit etmek ve bedel-teminat etkili bulguları raporlamak için kullanılır."
---

# Hukuki Durum Tespiti (Due Diligence)

## Görev
Hedef şirketin hukuki durumunu sistematik tarayarak deal-breaker, bedel düzeltici ve indemnity/teminat gerektiren bulguları ayıklamak ve raporlamak.

## Soğuk başlangıç (intake)
- DD kapsamı tam mı, sınırlı (red-flag) mı; eşik (materiality threshold) nedir?
- Veri odası (data room) açıldı mı, hangi başlıklar eksik?
- Müvekkil alıcı tarafında mı (savunmacı tarama) yoksa satıcı vendor DD mi?
- İşlem takvimi ve kritik kapanış tarihi var mı?

## Denetim şeması
1. **Kurumsal**: Kuruluş, esas sözleşme, pay defteri ve gerçek pay sahipliği (TTK m.499), genel kurul/yönetim kurulu kararlarının usulüne uygunluğu, sermaye kaybı/borca batıklık (TTK m.376) kontrolü.
2. **Sözleşmesel**: Önemli sözleşmelerde change-of-control, münhasırlık, fesih ve teminat klozları; devir kısıtları.
3. **Dava ve icra**: Derdest dava/icra dosyaları, muhtemel husumetler; UYAP/dosya bazlı risk skoru.
4. **İş hukuku**: İşçilik alacakları, kıdem/ihbar yükü, sendikal durum, alt işveren riskleri (4857), SGK borçları (5510).
5. **Fikri mülkiyet ve gayrimenkul**: Marka/patent tescil ve devir engelleri (6769), tapu ve ipotek kayıtları.
6. **Vergi ve uyum**: Vergi incelemesi/tarhiyat riski, KVKK uyumu (6698), sektörel izinler, rekabet ihlali geçmişi.
7. **İspat yükü**: DD bulgusunun varlığını alıcı; satıcının beyanının doğruluğunu ise beyanda bulunan taraf taşır → bulgular disclosure letter'a bağlanır.
8. **Ara sonuç**: Her bulgu deal-breaker / bedel düzeltici / indemnity / teminat (escrow) / closing condition olarak etiketlenir.

## Çıktı modülleri
- DD bulgu matrisi (başlık, bulgu, risk düzeyi, etki, öneri)
- Kırmızı bayrak özeti (yönetici özeti)
- SPA'ya yansıtılacak özel indemnity ve CP listesi
- Eksik belge / ek soru listesi (Q&A)

## Plugin bağlamı

Bu beceri `birlesme-devralma-ma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
