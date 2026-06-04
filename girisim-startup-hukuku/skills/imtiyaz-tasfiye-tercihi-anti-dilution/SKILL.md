---
name: imtiyaz-tasfiye-tercihi-anti-dilution
description: "Yatırımcıya verilen ekonomik ve yönetsel koruma hükümleri (tasfiye tercihi, oy/veto imtiyazı, anti-dilution, kâr payı imtiyazı) kurgulanır veya denetlenirken; bunların TTK imtiyaz rejimiyle ve esas sözleşmeyle uyumunu sağlamak için kullanılır."
---

# İmtiyazlar, Tasfiye Tercihi ve Anti-Dilution

## Görev
Yatırımcı koruma hükümlerini TTK imtiyaz sınırları içinde geçerli biçimde kurmak: tasfiye tercihi, oy/veto imtiyazı, kâr payı imtiyazı ve sulandırmaya karşı koruma (anti-dilution).

## Soğuk başlangıç (intake)
1. Hangi koruma isteniyor: tasfiye tercihi, oyda imtiyaz, kâr payı imtiyazı, anti-dilution?
2. Tasfiye tercihi katı (non-participating) mı, katılımlı (participating) mı; çarpan kaç (1x, 2x)?
3. Anti-dilution tam koruma (full ratchet) mı, ağırlıklı ortalama mı?
4. İmtiyazlar esas sözleşmeye işlendi mi, yalnız SHA'da mı?
5. Pay grupları (A/B) tanımlı mı; imtiyazlı pay sahipleri kurulu öngörüldü mü?

## Denetim şeması
1. İmtiyazın kaynağı: İmtiyaz ancak esas sözleşmeyle ve pay grubu tanımıyla kurulur (TTK m.478); salt SHA'daki "imtiyaz" şirkete/üçüncü kişilere karşı imtiyaz doğurmaz, taraflar arası borçtur.
2. Oyda imtiyaz: m.479 — bir paya en çok 15 oy; istisnalar (kurumsal yönetim, haklı sebep). Bazı kararlarda oyda imtiyaz kullanılamaz (m.479/3: esas sözleşme değişikliği, ibra, sorumluluk davası).
3. Tasfiye/kâr payı imtiyazı: Kâr payı ve tasfiye payında imtiyaz (m.478-479; tasfiye payı dağıtımı m.543). Tasfiye tercihi pratikte tasfiye payı imtiyazı + SHA çıkış şelalesi (waterfall) ile kurulur; çarpan ve katılımlı/katılımsız ayrımı sözleşmesel.
4. Anti-dilution: Sonraki turun daha düşük değerlemeli (down round) olması halinde yatırımcının pay oranını koruma. Full ratchet veya ağırlıklı ortalama (broad/narrow) formülü SHA'da; uygulanışı yeni artırımda yatırımcıya ek/bonus pay (genellikle rüçhan + bedelsiz pay mekaniğiyle) gerektirir — TTK m.461 ve sermaye kuralları süzgeci.
5. İmtiyazlı pay sahipleri kurulu: m.454 — imtiyazı zedeleyen GK kararları bu özel kurulun onayına bağlı.
6. Eşit işlem: m.357 (eşit işlem ilkesi) ve dürüstlük sınırı imtiyazların üst çerçevesi.
7. İspat/şekil: İmtiyaz esas sözleşme + tescil; SHA ekonomik şelale yazılı. Çarpan/oranları [doldurulacak] bırak.

## Çıktı modülleri
- İmtiyaz/koruma matrisi (esas sözleşme mi SHA mı, madde atıflı).
- Tasfiye/çıkış şelalesi (waterfall) modeli iskeleti.
- Anti-dilution formülü ve down-round senaryo notu.

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
