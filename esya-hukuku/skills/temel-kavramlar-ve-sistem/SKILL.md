---
name: temel-kavramlar-ve-sistem
description: "Eşya hukuku uyuşmazlığını ilk kez nitelendirirken; ayni hak mı zilyetlik mi borç ilişkisi mi, taşınır mı taşınmaz mı, mülkiyet mi sınırlı ayni hak mı sorularını ayırmak ve doğru hukuki temeli kurmak için kullanılır."
---

# Temel Kavramlar ve Ayni Hak Sistematiği

## Görev
Önündeki olayı eşya hukuku sistematiğine oturtmak: hangi hakkın ihlal edildiğini, hakkın mutlak (ayni) mı yoksa nispi (alacak) mı olduğunu, taşınır/taşınmaz ayrımını ve uygulanacak normu belirlemek. Doğru nitelendirme sonraki tüm adımların (talep, süre, yetki, ispat) önkoşuludur.

## Soğuk başlangıç (intake)
- Uyuşmazlık konusu eşya taşınmaz mı (arsa, bina, bağımsız bölüm) yoksa taşınır mı (araç, makine, eşya)?
- Talep sahibi malik mi, zilyet mi, yoksa sınırlı ayni hak (intifa, ipotek, geçit) sahibi mi?
- Talep eşyanın aynına mı (geri alma, el atmanın önlenmesi) yoksa para/tazminata mı yöneliyor?
- Karşı tarafın hakkı bir tapu kaydına mı, sözleşmeye mi, fiilî zilyetliğe mi dayanıyor?

## Denetim şeması
1. **Hakkın türü**: TMK m.683 mülkiyetin kullanma-yararlanma-tasarruf yetkilerini verir; mutlak haktır, herkese karşı ileri sürülür. Ayni haklar sınırlı sayı (numerus clausus) ilkesine tabidir: taraflar yeni tür ayni hak ihdas edemez. Talep bir sözleşmeden doğuyorsa (örn. satış vaadi) henüz ayni hak değil, kişisel hak vardır.
2. **Taşınır/taşınmaz ayrımı**: Taşınmazlarda aleniyet aracı tapu sicilidir (m.997 vd.) ve kazanım kural olarak tescille olur (m.705/1). Taşınırlarda aleniyet zilyetliktir; mülkiyet teslimle geçer (m.762 vd.) ve zilyetlik karinesi (m.985) işler.
3. **Mülkiyet biçimi**: Paylı mülkiyette (m.688 vd.) her paydaş belirli pay üzerinde tasarruf edebilir; elbirliği mülkiyetinde (m.701 vd., örn. tereke) tasarruf ancak oybirliğiyle ve bütün üzerinde mümkündür. Bu ayrım dava ehliyetini ve husumeti belirler.
4. **Sınırlı ayni hak süzgeci**: İrtifaklar (m.779 vd.), taşınmaz yükü (m.839), rehin (m.850 vd., m.939 vd.) malikin yetkisini sınırlar. Bunların varlığı tapu kaydından veya teslimden okunur.
5. **Ara sonuç**: Talebin eşya hukukuna mı borçlar hukukuna mı dayandığını ve hangi davanın açılacağını tespit et. İspat yükü TMK m.6 uyarınca hakkı iddia edene aittir.

## Çıktı modülleri
- Nitelendirme notu (hak türü, eşya türü, mülkiyet biçimi).
- Olası talep türleri listesi ve dayandığı madde.
- Bir sonraki uzman beceriye yönlendirme (istihkak, el atma, tapu, zilyetlik, rehin).

## Plugin bağlamı

Bu beceri `esya-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
