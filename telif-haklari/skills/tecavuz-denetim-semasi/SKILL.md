---
name: tecavuz-denetim-semasi
description: "Bir eylemin eser sahibinin mali veya manevi haklarına tecavüz oluşturup oluşturmadığını adım adım denetlemek gerektiğinde; izin, istisna ve hukuka uygunluk süzgeçlerinden geçirerek ihlal sonucuna varmak için kullanılır."
---

# Hak İhlali (Tecavüz) Denetim Şeması

## Görev
İddia edilen eylemin FSEK anlamında hak ihlali (tecavüz) oluşturup oluşturmadığını sistematik biçimde belirlemek ve hukuka uygunluk savunmalarını test etmek.

## Soğuk başlangıç (intake)
- Tecavüz iddiasına konu eylem ve tarihi nedir?
- Eyleme dayanak bir izin, lisans veya devir sözleşmesi gösteriliyor mu?
- Eylem ticari mi, kişisel/eğitim/haber amaçlı mı?
- Eserin tamamı mı yoksa bir kısmı/uyarlaması mı kullanılmış?

## Denetim şeması
1. Korunan hakkın varlığı: Eser + geçerli hak + hak sahibi belirlenir (m.1/B, m.8, m.20-25). Koruma süresi dolmuşsa ihlal yoktur.
2. El atma eylemi: Eylem hangi mali/manevi hakka karşılık geliyor (çoğaltma m.22, yayma m.23, umuma iletim m.25, işleme m.21, ad belirtmeme m.15, değişiklik m.16)?
3. İzin/yetki süzgeci: Sahibin veya hak sahibinin izni var mı? İzin/lisans dar yorumlanır (m.52); sözleşmede sayılmayan hak devredilmiş sayılmaz. İzin yoksa veya kapsam aşılmışsa ihlal karinesi güçlenir.
4. İstisna ve tahditler (m.30-40): Eylem kamu düzeni/genel menfaat istisnalarına, şahsen kullanma (m.38 — kâr amacı gütmeyen, çoğaltmayı sınırlı kılan), iktibas (m.35 — kaynak gösterme ve ölçü şartı), haber/güncel olay (m.37) veya eğitim-öğretim amaçlı kullanıma giriyor mu? İstisnalar dar yorumlanır; üç aşamalı teste benzer biçimde eserin normal kullanımını engellememe ve sahibin meşru menfaatini zedelememe aranır.
5. Manevi hak özelinde: İzinli kullanımda dahi ad belirtilmemesi (m.15) veya esere zarar veren değişiklik (m.16) bağımsız ihlal oluşturabilir.
6. Ara sonuç: İhlal var/yok; varsa hangi hak(lar), kusur şartı aranmayan talepler (ref/men) ve kusura bağlı talepler (tazminat) ayrılır.

İspat yükü: ihlali davacı, izin/istisnayı davalı ispatlar (HMK m.190).

## Çıktı modülleri
- İhlal denetim raporu (eylem — hak — izin/istisna değerlendirmesi — sonuç).
- Savunma (izin/istisna) zayıflık-güçlülük notu.
- Talep yelpazesine köprü.

## Plugin bağlamı

Bu beceri `telif-haklari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
