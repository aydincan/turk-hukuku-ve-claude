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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
