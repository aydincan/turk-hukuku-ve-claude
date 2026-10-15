---
name: sira-cetveli-ve-paylastirma
description: "Hacze birden çok alacaklı katıldığında veya iflasta, satış bedelinin alacaklılar arasında hangi sırayla dağıtılacağını belirlemek ve sıra cetveline itiraz/şikâyet etmek gerektiğinde kullanılır."
---

# Sıra Cetveli ve Paraların Paylaştırılması

## Görev
Satıştan elde edilen bedeli alacaklılar arasında doğru sırayla paylaştırmak; rehinli, imtiyazlı ve adi alacakların sırasını belirlemek; sıra cetveline karşı sıra (icra mahkemesi) veya esas (genel mahkeme) itirazını yürütmek.

## Soğuk başlangıç (intake)
- Birden çok haciz/alacaklı var mı; iflas masası söz konusu mu?
- Rehinli alacak var mı (öncelik); kamu alacağı (6183) gündemde mi?
- Sıra cetveli tebliğ edildi mi (7 günlük itiraz süresi)?
- İtirazın konusu sıraya mı, alacağın esasına/miktarına mı yönelik?

## Denetim şeması
1. **Garameten paylaşım kuralı (m.140)**: Satış tutarı tüm alacakları karşılamıyorsa icra müdürü sıra cetveli düzenler; aynı derecedeki alacaklılar arasında garameten (oranlı) paylaşım yapılır.
2. **Öncelik sırası**: Rehinli alacaklar rehin konusu bedelden öncelikle ödenir (m.151 vd.); kamu alacaklarının önceliği 6183 s.K. çerçevesinde değerlendirilir; iflasta alacak sıraları İİK m.206-207'ye göre belirlenir (rehinli, imtiyazlı I-IV, adi).
3. **İtiraz türü (m.142)**: Sıraya itiraz icra mahkemesine; alacağın esasına/miktarına itiraz genel mahkemede ayrı davayla ileri sürülür. Süre tebliğden 7 gündür.
4. **İspat yükü**: İtiraz eden, cetveldeki tertibin/alacağın hatalı olduğunu ispatlar; muvazaa/sıra önceliği iddiaları belgeyle desteklenir.
5. **Hacze iştirak etkisi**: m.100/101 iştiraki cetveldeki payları değiştirir; ilk haciz tarihi belirleyicidir.
6. **Ara sonuç**: Düzeltilmiş dağıtım tablosu ve itiraz stratejisi oluşturulur.

## Çıktı modülleri
- Sıra/dağıtım tablosu (alacaklı × sıra × pay).
- Sıra cetveline itiraz dilekçesi (sıra/esas ayrımıyla).
- Öncelik analizi (rehinli/imtiyazlı/kamu/adi).

## Plugin bağlamı

Bu beceri `icra-iflas-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
