---
name: sureler-ve-zamanasimi-denetimi
description: "Mütalaa konusu talebin zamanaşımı, hak düşürücü süre veya dava/başvuru süresi yönünden hâlâ kullanılabilir olup olmadığını denetlemek gerektiğinde kullanılır; her mütalaada zorunlu bir kontrol noktasıdır."
---

# Süreler ve Zamanaşımı Denetimi

## Görev
Mütalaa edilen hakkın veya talebin süre yönünden hâlâ ileri sürülebilir olup olmadığını saptamak; zamanaşımı, hak düşürücü süre ve dava/başvuru sürelerini ayırt etmek. Esasen haklı bir talep, süre geçmişse pratikte değersizdir; bu denetim atlanamaz.

## Soğuk başlangıç (intake)
- Talebin hukuki niteliği ne? (Sözleşme, haksız fiil, sebepsiz zenginleşme, idari işlem iptali, ceza şikâyeti)
- Sürenin başladığı an hangi olay? (Muacceliyet, zarar/failin öğrenilmesi, tebliğ, ifa)
- Süreyi kesen/durduran bir işlem yapıldı mı? (Dava, takip, ihtar, kısmi ödeme)
- Karşı taraf zamanaşımı def'ini ileri sürer mi?

## Denetim şeması
1. Süre türü tayini: Zamanaşımı def'i olarak ileri sürülmeli ve hakkı sona erdirmez (borç eksik borca döner); hak düşürücü süre re'sen gözetilir ve hakkı sona erdirir. Bu ayrım sonucu kökten değiştirir.
2. Genel zamanaşımı süreleri: TBK m.146 genel on yıl; TBK m.147 beş yıllık istisnalar (kira, ücret, vekâlet vb.); haksız fiilde TBK m.72 — fiil ve failin öğrenilmesinden iki yıl ve her hâlde on yıl; sebepsiz zenginleşmede TBK m.82 — iki/on yıl. Ticari ve özel kanun süreleri (TTK, İş K., 6502, SMK) ayrıca kontrol edilir.
3. Başlangıç anı: Süre muacceliyet/öğrenme/tebliğ anından işler; her talep için bu an ayrı belirlenir.
4. Kesilme/durma: TBK m.154 (dava, takip, ihtar, borç ikrarı zamanaşımını keser) ve m.153 (durma sebepleri) uygulanır; kesilmeyle süre yeniden işler.
5. Dava/başvuru süreleri (hak düşürücü nitelikte): İdari davada İYUK m.7 (genel altmış gün); işe iade başvurusu İş K. m.20/m.21 (fesih tebliğinden bir ay); AYM bireysel başvuru otuz gün; bunlar re'sen gözetilir.
6. Ara sonuç: Süre türü + dolup dolmadığı + kesen/durduran işlem etkisi + "geçmişse hangi alternatif kalır" notu.

## Çıktı modülleri
- Süre hesap tablosu (talep | süre türü | başlangıç | bitiş | durum)
- Kesilme/durma değerlendirmesi
- Re'sen gözetilen süreler uyarısı
- Süre dolmuşsa kalan hukuki imkânlar

## Plugin bağlamı

Bu beceri `hukuki-mutalaa` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
