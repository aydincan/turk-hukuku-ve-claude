---
name: hukuka-aykirilik-ve-uygunluk-sebepleri
description: "Fiilin hukuka aykırı sayılıp sayılmayacağı tartışmalıysa veya karşı taraf meşru savunma, rıza, zorda kalma ya da hakkın kullanılması savunması ileri sürdüğünde; aykırılık ve uygunluk dengesini denetlemek için kullanılır."
---

# Hukuka Aykırılık ve Hukuka Uygunluk Sebepleri

## Görev
Fiilin hukuka aykırılığını (mutlak hak ihlali / koruma normu ihlali / ahlaka aykırı kasıtlı zarar) tespit etmek ve TBK m.63'teki hukuka uygunluk sebeplerinden birinin aykırılığı ortadan kaldırıp kaldırmadığını denetlemek. Uygunluk sebebi varsa sorumluluk doğmaz; sınırı aşılırsa kısmî sorumluluk gündeme gelir.

## Soğuk başlangıç (intake)
- Hangi hak/menfaat zarar gördü (mutlak hak mı, salt malvarlığı mı)?
- Salt malvarlığı zararıysa ihlal edilen bir koruma normu var mı?
- Karşı taraf hangi haklılık sebebine dayanıyor (rıza, savunma, iztırar, hakkın kullanımı, kamu gücü)?
- Savunma/zorunluluk hâlinde ölçü aşıldı mı?

## Denetim şeması
1. **Aykırılık tipini belirle.** Mutlak hak (yaşam, beden, sağlık, kişilik, mülkiyet) ihlali kural olarak doğrudan hukuka aykırıdır. Salt malvarlığı zararında ihlal edilen davranış/koruma normu ya da m.49/2 (ahlaka aykırı + kast) aranır.
2. **Rıza (m.63/1).** Zarar görenin geçerli, aydınlatılmış ve hukuken korunan rızası aykırılığı kaldırır; kişilik haklarından kesin/sürekli vazgeçme geçersizdir (TMK m.23).
3. **Üstün özel/kamu yararı (m.63/1).** Korunan menfaat ihlal edilen menfaatten üstünse aykırılık kalkar; orantılılık aranır.
4. **Meşru savunma ve iztırar (m.63/2 ve m.64).** Saldırıya karşı orantılı savunma hukuka uygundur. Zorda kalan, başkasının malına verdiği zararda hâkimin takdiriyle tazminata hükmedilebilir (m.64).
5. **Hakkın kullanılması ve kamu gücü (m.63/1).** Yetkili merciin hukuka uygun emrini/yetkisini kullanma aykırılığı kaldırır; sınır aşılırsa kalan kısım için sorumluluk sürer.
6. **Ara sonuç ve ispat.** Aykırılığı (ve hak ihlalini) zarar gören; hukuka uygunluk sebebini ileri süren ve ölçüye uyduğunu ispatlar (TMK m.6). Sebebin sınırı aşılmışsa indirim (m.52) ya da kısmî sorumluluk değerlendirilir.

## Çıktı modülleri
- Aykırılık nitelendirme notu (hak tipi + dayanak).
- Uygunluk sebebi kontrol listesi (sebep + şart + ölçü).
- Sınır aşımı/kısmî sorumluluk değerlendirmesi.

## Plugin bağlamı

Bu beceri `haksiz-fiil-tazminat` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
