---
name: navlun-sozlesmesi-carter-konismento
description: "Deniz yoluyla yük taşıma sözleşmeleri (yolculuk çarteri, zaman çarteri, kırkambar) ve konişmento düzenlendiğinde; sözleşme tipini, tarafların borçlarını, starya/sürastarya ve konişmentonun ispat işlevini analiz etmek için kullan."
---

# Navlun Sözleşmesi, Çarter Parti ve Konişmento

## Görev
Deniz yoluyla eşya taşıma ilişkisini sözleşme tipine göre çözümlemek; taşıyan ve taşıtanın borçlarını, navlun ve sürastarya alacaklarını belirlemek; konişmentonun düzenlenmesi, içeriği ve ispat gücünü denetlemek.

## Soğuk başlangıç (intake)
- Sözleşme yolculuk çarteri mi, zaman çarteri mi, yoksa kırkambar (parça yük) mü?
- Konişmento düzenlendi mi; nama, emre veya hamiline mi; "temiz" mi yoksa rezerv kayıtlı mı?
- Yükleme/boşaltma süreleri (starya) ve sürastarya kayıtları nasıl belirlenmiş?
- Navlun peşin mi (freight prepaid) yoksa varışta mı ödenecek; FIOST gibi kayıtlar var mı?

## Denetim şeması
1. **Sözleşme tipi**: Yolculuk çarteri/kırkambar ayrımını TTK m.1138 vd. çerçevesinde yap; zaman çarterinde geminin tahsisi ve işletme yükünün dağılımı farklıdır. Tip, riziko ve masraf dağılımını belirler.
2. **Tarafların borçları**: Taşıyanın gemiyi denize, yola ve yüke elverişli hale getirme borcu (TTK m.1141) ve yükü özenle yükleme/istif/boşaltma borcu; taşıtanın navlun ve doğru beyan borcu. İhlalleri tespit et.
3. **Starya/sürastarya**: Yükleme-boşaltma süresinin başlangıcı, hesabı ve sürastarya (demuraj) alacağını sözleşme kayıtlarına göre hesapla; "once on demurrage always on demurrage" gibi kayıtların etkisini değerlendir.
4. **Konişmento işlevi**: Konişmentonun düzenlenmesi, zorunlu içeriği ve üç işlevi — makbuz, taşıma sözleşmesinin ispatı, kıymetli evrak/temsil (TTK m.1228 vd.). Konişmentodaki rezervlerin (clausing) ispat değerine etkisini belirle; konişmento ile çarter parti arasındaki çatışmada hangisinin geçerli olacağını analiz et.
5. **İspat yükü ve ara sonuç**: Temiz konişmento, yükün iyi durumda teslim alındığına dair karine doğurur; aksini taşıyan ispatlar. Çıktıda kimin neyi ispatlayacağını ve sözleşmenin zayıf kayıtlarını işaretle.

## Çıktı modülleri
- Sözleşme tipi ve borç dağılımı tablosu
- Starya/sürastarya hesap taslağı
- Konişmento denetim notu (rezervler, çatışma, ispat değeri)

## Plugin bağlamı

Bu beceri `deniz-ticareti-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
