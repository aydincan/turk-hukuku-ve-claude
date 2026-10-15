---
name: roma-hukuku-sistematigi
description: "Roma hukukunun kendi iç sistematiğini (personae-res-actiones, ius civile/gentium/honorarium, ayni-şahsi hak, contractus-delictum) açıklamak ve bir kavramın Roma kökenini çözmek gerektiğinde kullanılır; akademik temel ve kavram soykütüğü içindir."
---

# Roma Hukuku Sistematiği ve Temel Kavramlar

## Görev
Roma hukukunun iç mimarisini doğru biçimde ortaya koymak ve bir hukuki kavramın Roma kökenini, yürürlükteki Türk hukuku ile karıştırmadan, akademik düzeyde açıklamak.

## Soğuk başlangıç (intake)
- Soru akademik/eğitsel mi, yoksa yürürlükteki bir maddenin yorumuna mı bağlanacak?
- Hangi kurum sorgulanıyor (kişi-ehliyet, mülkiyet-zilyetlik, sözleşme, haksız fiil, miras)?
- Klasik dönem mi (Gaius/klasik hukukçular) yoksa Iustinianus dönemi mi referans alınacak?
- Latince maxim/kaynak metni gerekiyor mu?

## Denetim şeması
1. Tasnif katmanını belirle: Gaius Institutiones'in personae (kişiler) – res (mallar/haklar) – actiones (davalar) üçlüsü çerçevesinde kurumun yerini sapta. Bu tasnif, bugünkü Pandekt sistemli TMK/TBK ayrımının atasıdır.
2. Norm kaynağını ayrıştır: ius civile (Roma vatandaşlarına özgü), ius gentium (kavimler arası ortak), ius honorarium (praetor hukuku) ve ius naturale ayrımını kur; kurumun hangi tabakadan geldiğini göster.
3. Hak tipini belirle: ayni hak (ius in rem, herkese karşı, actio in rem) ile şahsi hak (ius in personam, belirli kişiye karşı, actio in personam) ayrımını uygula. Bu ayrım, TMK eşya hukuku ile TBK borç ilişkisi ayrımının köküdür.
4. Borç kaynağını sınıfla: contractus (re/verbis/litteris/consensu doğan), delictum, quasi contractus, quasi delictum. Consensu doğan rıza sözleşmeleri (emptio venditio, locatio conductio, societas, mandatum) bugünkü TBK isimli sözleşmelerinin atasıdır.
5. Usul mantığını ekle: Roma hukuku actio (dava kalıbı) temellidir; hak değil dava merkezlidir. Bu, modern maddi hak-dava ayrımının tarihî zıttıdır ve farkı vurgulanmalıdır.
6. Ara sonuç: Kurumu Roma sistematiğinde konumla; sonra bir sonraki adımda (resepsiyon becerisi) yürürlükteki Türk normuna bağla. Roma kuralını yürürlükteki hüküm yerine koyma.

İspat/dayanak: birincil kaynak Corpus Iuris Civilis fragmanlarıyla (D./Inst./Gai./C.) gösterilir; doktrin yazar-eser-sayfa ile, tam künye [doğrulanacak].

## Çıktı modülleri
- Kavram kartı: Roma adı + tanım + tasnifteki yeri.
- Kaynak atıfları (Digesta/Institutiones fragmanları, varsa Latince maxim).
- Yürürlükteki Türk hukukuna köprü notu (ilgili TMK/TBK maddesi, ayrıntı resepsiyon becerisinde).
- Sınır uyarısı: tarihî bilgi yürürlükteki normun yerine geçmez.

## Plugin bağlamı

Bu beceri `roma-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
