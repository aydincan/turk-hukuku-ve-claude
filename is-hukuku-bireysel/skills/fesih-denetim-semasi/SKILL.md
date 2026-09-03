---
name: fesih-denetim-semasi
description: "İş sözleşmesinin feshinin haklı, geçerli ya da usulsüz olup olmadığını adım adım ayırmak gerektiğinde; fesheden tarafa, sebebe, bildirime ve usule göre feshi nitelendirip doğacak tazminat ve davaları belirlemek için kullan."
---

# Fesih Denetim Şeması (Haklı / Geçerli / Usulsüz)

## Görev
Feshi türüne göre ayırmak: süreli (önelli) fesih mi, geçerli sebebe dayalı fesih mi, haklı (derhal) fesih mi; usule uygunluk ve sonuçlarını (tazminat, işe iade) belirlemek.

## Soğuk başlangıç (intake)
1. Sözleşmeyi kim feshetti, hangi tarihte, hangi gerekçeyle?
2. Fesih yazılı mı, sebep açıkça gösterildi mi (İş K. m.19)?
3. İşçi savunması alındı mı (davranış/verimsizlik halinde)?
4. İşyeri 30+ işçi çalıştırıyor mu, işçinin kıdemi 6 ayı aştı mı?

## Denetim şeması
1. **Fesheden tarafı belirle.**
2. **Haklı fesih kontrolü:**
   - İşçi yönünden: İş K. m.24 (sağlık, ahlak ve iyiniyete aykırılık — örn. ödenmeyen ücret, mobbing, zorlayıcı sebep).
   - İşveren yönünden: İş K. m.25 (özellikle m.25/II ahlak ve iyiniyete aykırılık).
   - **Hak düşürücü süre:** m.26 — öğrenmeden itibaren altı işgünü ve her halde bir yıl. Süre geçmişse haklı fesih hakkı düşer.
3. **Geçerli fesih kontrolü (m.18):** Haklı sebep yoksa, işçinin yetersizliği, davranışı veya işletme gereklerine dayalı geçerli sebep var mı? İşletme gereğinde feshin son çare (ultima ratio) olması aranır. İspat yükü işverende (m.20/2).
4. **Usul (m.19):** Fesih yazılı yapılmalı ve sebep açık-kesin gösterilmeli; m.25/II hariç davranış/verimsizlik feshinde işçinin savunması alınmalı. Usulsüzlük geçerli sebebi dahi etkisiz kılabilir.
5. **Ara sonuç ve sonuçlar:**
   - Haklı fesih (işveren m.25/II): Kıdem ve ihbar doğmaz (m.25/II ise kıdem de yok); işçinin haklı feshinde (m.24) kıdem doğar, ihbar doğmaz.
   - Usulsüz (önelsiz) fesih: İhbar tazminatı doğar (m.17).
   - Geçersiz fesih + güvence kapsamı: İşe iade davası (m.20-21) yolu açılır.

## Çıktı modülleri
- Fesih nitelendirmesi tablosu (taraf / sebep / usul / sonuç).
- Hangi tazminat kalemlerinin doğduğu.
- İşe iade yolu açık mı değerlendirmesi.
- Risk ve eksik delil notu.

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
