---
name: sermaye-sirketleri-temel-sistematik
description: "Bir uyuşmazlığın veya işlemin AŞ mi Ltd. mi olduğunu, hangi eksene (kuruluş, organ, pay, sermaye, sorumluluk, kriz) düştüğünü ve uygulanacak TTK hükümlerini ayırt etmek için kullanılır; sınırlı sorumluluk, tüzel kişilik ve sermayenin korunması ilkelerini netleştirir."
---

# Sermaye Şirketleri Temel Sistematiği

## Görev
Önündeki olayı doğru şirket tipi ve doğru hukuki eksen üzerine oturtmak; AŞ (TTK m.329 vd.) ile Ltd. (TTK m.573 vd.) ayrımını, sınırlı sorumluluk ve tüzel kişiliğin sonuçlarını uygulamaya bağlamak.

## Soğuk başlangıç (intake)
1. Şirket tipi nedir (AŞ / Ltd. / kollektif-komandit) ve sermayesi/ortak sayısı?
2. Sorun hangi eksende: kuruluş, organ/karar, pay/pay sahipliği, sermaye işlemi, sorumluluk, yoksa kriz (m.376)?
3. Olay tarihi nedir; o tarihte hangi TTK metni ve geçici maddeler yürürlükteydi?
4. Esas sözleşmenin/şirket sözleşmesinin ilgili maddesi ve varsa iç yönerge mevcut mu?
5. Sicil durumu nedir (tescil edilmiş mi, tescil bekliyor mu, kuruluş tamamlanmış mı)?

## Denetim şeması
1. Tip tayini: Sermaye şirketi mi? AŞ ise m.329, Ltd. ise m.573 başlangıç hükmü; ortağın sorumluluğu taahhüt ettiği sermaye ile sınırlı (m.329/2, m.573/2). İstisna: ortak/yönetici aleyhine kamu alacağı (VUK m.10, 6183 mük. m.35) veya yönetici sorumluluğu (m.553) söz konusu olabilir.
2. Tüzel kişilik anı: Tescil ile kazanılır (m.355, m.588). Tescilden önceki işlemlerde m.355/2-3 sorumluluk rejimi.
3. Eksen tayini: (a) Kuruluş → m.335-340/579; (b) Organ/karar → AŞ m.407, m.359, m.375; Ltd. m.616, m.623; (c) Pay → m.476, m.490/595; (d) Sermaye → m.456, m.473; (e) Sorumluluk → m.549-561; (f) Kriz → m.376.
4. Sözleşme serbestisi sınırı: AŞ'de tipe bağlılık ve emredici hükümler (m.340); Ltd.'de m.579. Esas sözleşme hükmü emredici kurala aykırıysa geçersiz.
5. İspat yükü: Kural olarak iddia eden ispatla yükümlü (HMK m.190; TMK m.6); ancak yönetici sorumluluğunda kusursuzluğu ispat yönetime düşebilir (özen yükümü m.369 bağlamında).
6. Ara sonuç: Tip + eksen + uygulanacak madde + ilgili özel beceri yönlendirmesi.

## Çıktı modülleri
- Tip ve eksen tespiti tablosu (madde atıflı).
- Uygulanacak hükümler listesi ve hangi alt-beceriye geçileceği.
- Sözleşme serbestisi/emredici hüküm uyarı notu.

## Plugin bağlamı

Bu beceri `sirketler-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
