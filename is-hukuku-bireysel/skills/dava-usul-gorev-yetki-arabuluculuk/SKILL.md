---
name: dava-usul-gorev-yetki-arabuluculuk
description: "İş uyuşmazlığında dava şartı arabuluculuk, görevli ve yetkili mahkeme, harç-yargılama usulü ve dava açma adımları gerektiğinde; işçilik alacağı veya işe iade davasının usul iskeletini kurmak için kullan."
---

# Dava, Usul, Görev-Yetki ve Zorunlu Arabuluculuk

## Görev
İş uyuşmazlığını doğru usul rejimine oturtmak: zorunlu arabuluculuk, görev-yetki, yargılama usulü ve dava açılış adımlarını belirlemek.

## Soğuk başlangıç (intake)
1. Talep konusu nedir (işçilik alacağı, işe iade, hizmet tespiti, tazminat)?
2. İşyeri ve işverenin adresi nerede; işçi işi nerede gördü?
3. Fesih/dava açma tarihleri ve süre durumu nedir?
4. Daha önce arabuluculuğa başvuruldu mu?

## Denetim şeması
1. **Dava şartı arabuluculuk (7036 m.3):** İşçi-işveren arasındaki kıdem, ihbar, fazla çalışma, ücret, yıllık izin gibi alacak ve tazminat talepleri ile işe iade davaları için arabuluculuk **dava şartıdır**. İş kazası/meslek hastalığından kaynaklı maddi-manevi tazminat ve bunlara ilişkin rücu davaları kapsam dışı (bunlar için ihtiyaridir). Başvuru olmadan açılan dava, dava şartı yokluğundan usulden reddedilir.
2. **Görev (7036 m.5):** İş mahkemeleri görevlidir; iş mahkemesi yoksa o yer asliye hukuk mahkemesi iş mahkemesi sıfatıyla bakar.
3. **Yetki (7036 m.6):** Davalı gerçek/tüzel kişinin davanın açıldığı tarihteki yerleşim yeri ile işin/işlemin yapıldığı yer mahkemesi yetkilidir; bu yetki kesindir (aksine sözleşme yapılamaz).
4. **Usul:** İş mahkemelerinde kural olarak **basit yargılama usulü** uygulanır (HMK m.316 vd.); dilekçeler dilekçe-cevap ile sınırlıdır, ön inceleme ve tahkikat hızlandırılmıştır.
5. **Ara sonuç:** Önce arabuluculuk → son tutanak → süresinde dava (işe iadede 2 hafta). Dava dilekçesine son tutanağın aslı/onaylı örneği eklenmezse bir haftalık kesin süre verilir; eklenmezse dava usulden reddedilir.
6. **Faiz ve talep:** Alacak türüne göre faiz türü (mevduat/yasal) ve başlangıcı talep sonucunda doğru gösterilir; belirsiz alacak/kısmi dava tercihi değerlendirilir.

## Çıktı modülleri
- Arabuluculuk kapsam kontrolü (zorunlu/ihtiyari).
- Görevli ve yetkili mahkeme tespiti.
- Süre takvimi ve dava açılış kontrol listesi.
- Faiz/talep türü ve dava türü (belirsiz alacak vb.) önerisi.

## Plugin bağlamı

Bu beceri `is-hukuku-bireysel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
