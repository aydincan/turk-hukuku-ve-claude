---
name: gmp-gdp-uretim-dagitim
description: "İlaç üretim ve dağıtım denetimleri, GMP/GDP uygunsuzlukları, soğuk zincir, ecza deposu ve geri çekme süreçlerinde TİTCK denetim ve yaptırımlarına karşı kullanılır."
---

# İyi Üretim ve Dağıtım Uygulamaları (GMP/GDP)

## Görev
Üretim yerinin GMP, ecza deposu/dağıtımın GDP uygunluğunu denetim raporu üzerinden değerlendirmek; uygunsuzluk yaptırımına ve geri çekme kararlarına karşı strateji kurmak.

## Soğuk başlangıç (intake)
- İhlal üretimde mi (GMP) dağıtımda mı (GDP, ecza deposu)?
- Denetim sonucu: kritik/major/minor bulgu sınıflandırması nedir; CAPA verildi mi?
- Soğuk zincir/sahte ilaç/karekod (İTS) ihlali var mı?
- TİTCK kararı: sertifika askısı, üretim/satış durdurma, geri çekme, idari para cezası mı?

## Denetim şeması
1. **Dayanak.** İlaçların GMP ve GDP kılavuzları (TİTCK), 1262 sayılı Kanun ve Ecza Depoları Yönetmeliği; İlaç Takip Sistemi (İTS/karekod) mevzuatı.
2. **Bulgu sınıflandırma.** Kritik bulgu (hasta güvenliği riski) → ağır yaptırım; major/minor → CAPA ile giderim. Ara sonuç: bulgunun sınıfı yaptırımla orantılı mı (ölçülülük)?
3. **İşlem denetimi.** Sertifika askısı/üretim durdurma/geri çekme birel idari işlemdir; yetki-sebep-konu yönünden incelenir. İspat: idare bulguyu denetim raporu ve numune analiziyle; firma CAPA ve düzeltici kanıtla karşılar.
4. **Geri çekme.** Sınıf 1/2/3 geri çekme; bildirim ve toplama yükümlülüğü; eksik geri çekme ek yaptırım ve TCK m.187 (bozulmuş/sahte ilaç) ceza riski doğurur.
5. **Yargı yolu.** İdari yaptırıma karşı iptal + yürütmeyi durdurma (İYUK m.7, m.27); telafisi güç zarar (tesis kapanması) somutlaştırılır. Sözleşmesel zarar (fason üretim, tedarik) adli yargıda TBK çerçevesinde ele alınır.

## Çıktı modülleri
- Denetim bulgusu-yaptırım orantılılık analizi.
- CAPA ve düzeltici kanıt dosyası planı.
- İptal + yürütmeyi durdurma dilekçe iskeleti [doldurulacak].

## Plugin bağlamı

Bu beceri `eczacilik-ilac` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
