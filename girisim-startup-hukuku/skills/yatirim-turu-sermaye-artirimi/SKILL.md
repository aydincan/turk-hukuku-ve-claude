---
name: yatirim-turu-sermaye-artirimi
description: "Bir yatırım turunda yeni yatırımcıya doğrudan pay verilirken (equity round); bedelli sermaye artırımı, rüçhan hakkının yönetimi, pay ihracı, kapanış ön şartları ve fonun şirkete girişi adım adım kurgulanırken kullanılır."
---

# Yatırım Turu ve Bedelli Sermaye Artırımı

## Görev
Equity yatırım turunu hukuken icra etmek: yeni payların ihracı için sermaye artırımını, rüçhan yönetimini, kapanış ön şartlarını ve fonun şirkete girişini doğru sıralamak.

## Soğuk başlangıç (intake)
1. Tur büyüklüğü, değerleme ve yatırımcıya verilecek pay oranı nedir?
2. Şirket kayıtlı sermaye sisteminde mi (YK ile artırım) yoksa esas sermaye sisteminde mi (GK)?
3. Mevcut pay sahiplerinin rüçhan hakkı kullandırılacak mı, sınırlanacak mı?
4. Yatırımcıya imtiyazlı pay mı veriliyor (tasfiye tercihi, oy, veto)?
5. Kapanış için hangi ön şartlar (DD, onaylar, rekabet izni) var?

## Denetim şeması
1. Artırım türü: Esas sermaye artırımı GK kararı + esas sözleşme değişikliği (TTK m.456-458); kayıtlı sermayede tavan içinde YK kararı (m.460). Önceki sermayenin tamamen ödenmiş olması kural (m.456/1).
2. Rüçhan hakkı: m.461 — mevcut pay sahiplerine oranları kadar; yatırımcı girişi için bu hak sınırlanır (m.461/2: haklı sebep + nitelikli nisap + eşit işlem). Sınırlama gerekçesi GK kararında belgelenmeli.
3. İmtiyazlı pay ihracı: Yatırımcı payı imtiyazlıysa (m.478-479) esas sözleşmede pay grubu/imtiyaz tanımlanmalı; imtiyazlı pay sahipleri özel kurulu (m.454) ilerideki değişikliklerde devreye girer.
4. Bedel ve ödeme: Nominal üstü çıkış primli ihraçta emisyon primi; nakdî sermaye ödeme kuralı m.344; primli payda bedelin tescilden önce ödenmesi.
5. Kapanış ön şartları: DD'nin tamamlanması, kurumsal kararlar (GK/YK), gerekiyorsa rekabet izni (4054 m.7) ve üçüncü kişi onayları; eş zamanlı SHA imzası.
6. Tescil ve hüküm: Artırım tescille hüküm ifade eder (m.456 vd.); pay defterine kayıt (m.499).
7. İspat/şekil: Nisap ve ödeme belgeleri şirkette; rüçhan sınırlamasının haklı sebebi şirketçe ortaya konur.

## Çıktı modülleri
- Tur kapanış adım planı (DD → karar → ödeme → tescil).
- GK/YK karar taslakları (rüçhan sınırlama gerekçeli).
- Pay alım/iştirak (SSA) sözleşmesi iskeleti ve kapanış checklist'i.

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
