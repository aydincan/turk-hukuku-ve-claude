---
name: yonetici-secimi-gorev-sorumluluk
description: "Yöneticinin (veya yönetim kurulunun) seçilmesi, görev ve yetkilerinin sınırlanması, hesap vermemesi, azli ya da mahkemece atanması ve yönetici aleyhine açılacak hesap/sorumluluk davası gündeme geldiğinde kullanılır."
---

# Yönetici/Denetçi — Atama, Görevler ve Sorumluluk

## Görev
Anagayrimenkul yöneticisinin (veya yönetim kurulunun) seçimini, görev ve yetkilerini, hesap verme yükümlülüğünü ve sorumluluğunu belirlemek; yöneticinin atanmasına/azline ilişkin uyuşmazlıkları ve hesap/sorumluluk davalarını kurmak.

## Soğuk başlangıç (intake)
- Mevcut yönetici nasıl belirlendi: kurul kararıyla mı, yönetim planıyla mı, yoksa mahkemece mi atandı?
- Uyuşmazlık atama/azil mi, hesap vermeme mi, yetkisini aşma mı, yoksa zarar/sorumluluk mu?
- Kat malikleri yönetici seçemiyor/anlaşamıyor mu (mahkemeden atama gereği)?
- İşletme defteri, makbuz ve hesap belgeleri ibraz edildi mi?

## Denetim şeması
1. **Yöneticinin belirlenmesi (KMK m.34)**: Kat malikleri, kendi aralarından veya dışarıdan bir yöneticiyi ya da yönetim kurulunu **kat maliklerinin sayı ve arsa payı çoğunluğuyla** atar. Sekiz ve daha fazla bağımsız bölümü olan anagayrimenkulde yönetici atanması **zorunludur** (m.34/2).
2. **Mahkemece atama (m.34/son)**: Yönetici atanamaz veya kurul anlaşamazsa, kat maliklerinden birinin istemiyle sulh hukuk mahkemesi yönetici atar; bu yönetici altı ay geçmeden ancak haklı sebeple değiştirilebilir.
3. **Görevler (m.35)**: Kurul kararlarını yerine getirme, anagayrimenkulü amacına uygun yönetme, ortak yerlerin bakım-onarım-temizliği, giderlerin toplanması ve avans tahsili, defter tutma, kat maliklerini temsil, sigorta yaptırma vb. Yönetici, yönetim planı ve kurul kararlarıyla bağlıdır.
4. **Hesap verme ve defter (m.36, m.39)**: Yönetici, **işletme defteri** tutar ve gelir-gider belgelerini saklar; her takvim yılı sonunda kesin hesap verir ve kurulca **ibra** edilir. İbra etmeyen malik hesap davası açabilir.
5. **Sorumluluk (m.38, m.40)**: Yönetici, kat maliklerine karşı **vekil gibi** sorumludur (TBK vekâlet hükümleri); kusuruyla verdiği zararı tazmin eder. Aynı zamanda haklı sebeple her zaman azledilebilir.
6. **Denetim (m.41)**: Kurul, yöneticinin yönetimini ve hesaplarını denetler; bu amaçla denetçi veya denetim kurulu seçebilir.
7. **Ara sonuç**: Atama/azil için kurul kararı veya mahkeme; hesap için ibra/hesap davası; zarar için vekilin sorumluluğu (m.38).

## Çıktı modülleri
- Yönetici atama/azil kurul kararı taslağı (nisap kontrolüyle).
- Mahkemeden yönetici atanması başvuru iskeleti (m.34/son).
- Hesap/ibra ve sorumluluk (m.38) davası dilekçe çatısı.

## Plugin bağlamı

Bu beceri `kat-mulkiyeti` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
