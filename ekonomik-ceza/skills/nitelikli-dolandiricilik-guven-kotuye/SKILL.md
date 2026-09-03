---
name: nitelikli-dolandiricilik-guven-kotuye
description: "Hileyle menfaat temini (TCK m.157-158) veya devralınan malvarlığının amacı dışında kullanılması (TCK m.155) iddiaları; bilişim, bankacılık, ticari faaliyet kapsamındaki nitelikli haller ve sözleşmeden doğan ihtilafın suç boyutu söz konusu olduğunda kullanılır."
---

# Nitelikli Dolandırıcılık ve Güveni Kötüye Kullanma

## Görev
TCK m.157-158 dolandırıcılık ve m.155 güveni kötüye kullanma suçlarını unsurlarına göre denetlemek; özellikle ticari/sözleşmesel ihtilafın gerçekten suç oluşturup oluşturmadığını ayırmak.

## Soğuk başlangıç (intake)
- Mağdur nasıl bir işleme/ödemeye yöneltildi; hile fiili somut olarak ne?
- İlişki sözleşmeye mi dayanıyor (alacak/borç ihtilafı mı, hile mi)?
- Nitelikli hal var mı? (banka/kredi kurumu, bilişim sistemi, kamu kurumu, tacir/şirket)
- Güveni kötüye kullanmada: mal kime, hangi amaçla tevdi edildi?

## Denetim şeması
1. **Dolandırıcılığın unsurları (TCK m.157)**: Hileli davranış + mağdurun aldatılması + bu sayede kendi/başkası lehine haksız menfaat + mağdur veya başkasının zararı. Hile, mağdurun denetim imkânını ortadan kaldıracak yoğunlukta olmalı; salt yalan/ödememe yetmez.
2. **Hukuki ihtilaf-suç ayrımı**: Sözleşmenin kurulduğu anda hile yoksa, sonradan ödememe kural olarak hukuki uyuşmazlıktır (alacak davası). Baştan var olan aldatma kastı aranır.
3. **Nitelikli haller (TCK m.158)**: Bilişim sistemlerinin/banka-kredi kurumlarının araç kılınması, ticari faaliyet kapsamında, serbest meslek, kamu kurumlarının zararına vb. Hangi bent uyuyorsa cezayı belirler.
4. **Güveni kötüye kullanma (TCK m.155)**: Zilyetliği devredilen malın, devir amacı dışında veya iade yükümlülüğüne aykırı kullanılması/temellük edilmesi. Hizmet/meslek/sanat/ticaret ilişkisiyle işlenmesi nitelikli haldir (m.155/2). Dolandırıcılıktan farkı: malın hileyle değil, güvene dayalı olarak elde edilmesidir.
5. **Manevi unsur**: Kast (TCK m.21); haksız menfaat/temellük kastı.
6. **Etkin pişmanlık ve içtima**: TCK m.168 malvarlığı suçlarında etkin pişmanlık (kısmi/tam iade ile indirim); zincirleme suç (m.43) ve diğer suçlarla içtima değerlendirilir.
7. **Ara sonuç**: Hile fiilinin yoğunluğu, suç-hukuki ihtilaf sınırı, doğru suç tipi ve nitelikli hal netleşir.

## Çıktı modülleri
- Hile fiili somutlaştırma notu
- Suç/hukuki ihtilaf sınır analizi
- Nitelikli hal bent eşleştirmesi
- m.155 vs m.157 ayrım değerlendirmesi
- Etkin pişmanlık/savunma stratejisi

## Plugin bağlamı

Bu beceri `ekonomik-ceza` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
