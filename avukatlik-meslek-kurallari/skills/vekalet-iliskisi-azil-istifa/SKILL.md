---
name: vekalet-iliskisi-azil-istifa
description: "Vekâletnamenin kapsamı, avukatın özen ve sadakat borcu, müvekkilin azil hakkı ile avukatın istifası ve bunların ücret-sorumluluk sonuçları söz konusu olduğunda kullanılır."
---

# Vekâlet İlişkisinin Kurulması, Azil ve İstifa

## Görev
Avukat-müvekkil vekâlet ilişkisinin kurulması, kapsamı ve sona ermesini; azil/istifanın
haklılığını ve ücret-sorumluluk sonuçlarını belirlemek.

## Soğuk başlangıç (intake)
1. Vekâletname var mı; özel yetki gerektiren işlemler (sulh, feragat, kabul) kapsamda mı?
2. İlişki nasıl sona erdi (azil, istifa, işin bitmesi)?
3. Azil/istifanın somut sebebi haklı mı?
4. Devam eden süre/duruşma riski ve dosya teslimi durumu ne?

## Denetim şeması
1. **Kuruluş ve kapsam.** Vekâlet ilişkisi avukatlık sözleşmesiyle kurulur; temsil yetkisinin
   sınırı vekâletnamedir. Sulh, feragat, kabul, davadan vazgeçme, ibra gibi tasarruflar için
   vekâletnamede özel yetki şarttır (HMK m.74; TBK m.504/3). Ara sonuç: yapılan işlem yetki
   kapsamında mı?
2. **Özen ve sadakat.** Avukat işi özenle ve müvekkil yararına yürütür, talimatlara uyar,
   gelişmelerden bilgilendirir, hesap verir (Av. K. m.34; TBK m.506-508). Süre kaçırma,
   bildirim yapmama özen ihlali ve tazminat sebebidir (TBK m.502 vd., m.49).
3. **Azil.** Müvekkil avukatı her zaman azledebilir; ancak azil haksızsa ücretin tamamı
   muaccel olur, haklıysa indirim/iade gündeme gelir (Av. K. m.174/1; TBK m.512). Uygun
   olmayan zamanda azil tazminat doğurabilir.
4. **İstifa.** Avukat haklı sebeple istifa edebilir; istifa, müvekkilin zarar görmemesi için
   uygun zamanda yapılmalı, istifadan sonra da on beş gün süreyle (Av. K. m.41 anlamında
   işten çekilmenin sonuçları) gerekli önlemleri alma yükümü gözetilmelidir. Haksız/uygunsuz
   zamanda istifa ücret hakkını ve tazminat sorumluluğunu etkiler.
5. **Sona ermenin sonuçları.** Dosya ve belgelerin iadesi, hesap verme, hapis hakkı (Av. K.
   m.166), karşı tarafa yüklenen vekâlet ücretinin akıbeti ve zamanaşımı (TBK m.147/5)
   değerlendirilir.

## Çıktı modülleri
- Azil/istifanın haklılık ve ücret sonucu değerlendirmesi.
- Vekâletname kapsam denetimi (özel yetki kontrolü).
- İstifa/azil bildirimi ve dosya teslim tutanağı taslağı.

## Plugin bağlamı

Bu beceri `avukatlik-meslek-kurallari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
