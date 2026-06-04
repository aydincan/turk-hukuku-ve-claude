---
name: kamu-gorevlileri-disiplin
description: "Memur ve diğer kamu görevlilerine ilişkin atama, nakil, disiplin cezası, görevden uzaklaştırma gibi işlemleri ve bunların iptalini değerlendirmek için kullanılır; personel hukuku uyuşmazlıklarında başvurulur."
---

# Kamu Görevlileri ve Disiplin İşlemleri

## Görev
Kamu görevlisine yönelik personel işlemlerini (özellikle disiplin cezalarını) usul ve esas yönünden denetlemek ve iptal stratejisini kurmak. Dayanak: Anayasa m.128/m.129, 657 sayılı DMK ve özel personel mevzuatı.

## Soğuk başlangıç (intake)
1. İşlem türü nedir (uyarı/kınama/aylıktan kesme/kademe ilerlemesinin durdurulması/memurluktan çıkarma; atama/nakil/görevden uzaklaştırma)?
2. Soruşturma açıldı mı, savunma hakkı tanındı mı?
3. Ceza zamanaşımı süreleri korunmuş mu?
4. İşlem tebliğ edildi mi; başvuru yolları gösterildi mi?

## Denetim şeması
1. **Yetki.** Cezayı veren makam/kurul yetkili mi; ağır cezalarda disiplin kurulu kararı şart mı (657 sayılı DMK m.126 vd.)?
2. **Şekil/usul.** Disiplin soruşturması açılması, **savunma hakkının tanınması** (savunma alınmadan ceza verilemez), muhakkik raporu, gerekçe. Savunma alınmaması esaslı şekil sakatlığıdır ve tek başına iptal sebebi olabilir.
3. **Sebep.** İsnat edilen fiil sabit mi; fiilin karşılığı olan disiplin hükmü doğru nitelendirilmiş mi? Maddi olayın gerçekliği re'sen araştırılır (İYUK m.20).
4. **Konu/ölçülülük.** Verilen ceza fiille orantılı mı; alt ceza uygulaması (657 sayılı DMK m.125 indirim) değerlendirildi mi? Eşitlik ve ölçülülük (Anayasa m.13) denetimi.
5. **Maksat.** İşlem kamu hizmeti yararı yerine kişisel saikle mi tesis edilmiş (yetki saptırması)?
6. **Zamanaşımı.** Disiplin soruşturmasına başlama ve ceza verme süreleri (657 sayılı DMK m.127); süre geçmişse ceza verilemez.
7. **Yargı yolu ve süre.** İdare mahkemesinde iptal davası; İYUK m.7 (60 gün) ve gerekiyorsa parasal/özlük kayıpları için tam yargı talebi. **Ara sonuç:** usul ve esas aykırılıkları + iptal sebepleri.

## Çıktı modülleri
- Disiplin sürecinin usul kontrol listesi (soruşturma/savunma/kurul/zamanaşımı).
- Ceza-fiil orantılılık ve alt ceza değerlendirmesi.
- İptal sebepleri + özlük kaybı tazmin notu.
- Dava dilekçesi için talep sonucu önerisi.

## Plugin bağlamı

Bu beceri `idare-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
