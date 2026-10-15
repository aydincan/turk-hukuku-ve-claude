---
name: tuketici-kredisi-konut-finansmani
description: "Tüketici kredisi, konut finansmanı, kredili mevduat veya kredi kartı sözleşmesinde tüketici lehine emredici hükümlerin (cayma, erken ödeme, haksız ücret, faiz tavanı) uygulanıp uygulanmadığını denetlemek ve iade/iptal taleplerini kurmak gerektiğinde kullanılır."
---

# Tüketici Kredisi, Konut Finansmanı ve Kart Sözleşmeleri

## Görev
Tüketici nitelikli kredi ve kart ilişkilerinde TKHK ve 5464 sayılı Kanun'un emredici koruma hükümlerini uygulamak; haksız ücret/komisyon iadesi, cayma, erken ödeme ve haksız şart taleplerini hukuki dayanağıyla kurmak.

## Soğuk başlangıç (intake)
- Ürün: belirli süreli tüketici kredisi, konut finansmanı, kredili mevduat hesabı (KMH), kredi kartı mı?
- Müşteri gerçek kişi ve ticari/mesleki amaç dışı mı (tüketici tanımı, TKHK m.3)?
- Talep konusu: dosya masrafı/komisyon iadesi, faiz/asgari ödeme itirazı, cayma, erken kapatma indirimi, haksız şart iptali?
- Uyuşmazlık tutarı tüketici hakem heyeti parasal sınırı içinde mi?

## Denetim şeması
1. **Tüketici sıfatı ve kapsam**: TKHK m.3 tüketici tanımı doğrulanır. Tüketici kredisi TKHK m.22-31, konut finansmanı m.32-39, kart ilişkisi 5464 ve TKHK genel hükümlerine tabidir.
2. **Sözleşme şekli ve ön bilgilendirme**: Yazılı/kalıcı veri saklayıcısıyla düzenlenme, sözleşme örneğinin verilmesi, ön bilgilendirme formu yükümlülüğü kontrol edilir; eksiklik tüketici lehine sonuç doğurur.
3. **Cayma ve erken ödeme**: Tüketici kredisinde 14 gün cayma hakkı (TKHK m.24); erken ödemede faiz ve maliyet indirimi (TKHK m.27); konut finansmanında erken ödeme tazminatı sınırları (TKHK m.37).
4. **Ücret/komisyon ve haksız şart**: Yalnızca ürün/hizmetin zorunlu maliyetini yansıtan, tüketiciden açık onay alınan ücretler tahsil edilebilir; dayanaksız dosya masrafı, komisyon ve hesap işletim ücretleri TKHK m.5 ve ilgili tebliğ uyarınca haksız şart olup iadeye tabidir. Bu yöndeki Yargıtay/HGK uygulaması istikrarlıdır [doğrulanacak — karararama.yargitay.gov.tr].
5. **Faiz ve asgari ödeme**: Kredi kartında akdi/gecikme faizi TCMB azami oranlarıyla, asgari ödeme oranı ilgili düzenlemeyle sınırlıdır; aşan tahsilatlar fazlaya ilişkin talep oluşturur. Ara sonuç olarak iade/iptal edilebilir kalemleri ve dayanağını yaz.

## Çıktı modülleri
- İade edilebilir ücret/komisyon kalemleri ve hesap tablosu.
- Tüketici hakem heyeti / tüketici mahkemesi yol seçimi notu.
- Başvuru/dava dilekçesi iskeleti ([doldurulacak] yer tutucularıyla).

## Plugin bağlamı

Bu beceri `bankacilik-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
