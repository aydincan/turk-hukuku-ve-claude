---
name: police-genel-sart-inceleme
description: "Eldeki poliçe, genel ve özel şartların madde madde okunup teminat kapsamı, istisnalar, muafiyet ve sigortalı aleyhine geçersiz şartların ayıklanması gerektiğinde kullanılır; uyuşmazlık öncesi belge analizi için temel beceri."
---

# Poliçe ve Genel Şart İnceleme (Teminat-İstisna-Muafiyet)

## Görev
Poliçeyi, ekli genel şartları ve özel şart/klozları sistematik okuyup teminat kapsamını, istisnaları, muafiyetleri ve sigortalı aleyhine geçersiz şartları ortaya çıkarmak; bir teminat haritası üretmek.

## Soğuk başlangıç (intake)
1. Hangi tip poliçe ve hangi tarihli genel şart yürürlükte?
2. Sigorta bedeli, teminat limitleri ve muafiyet türü (tenzili/entegral) ne?
3. Özel şart, kloz veya zeyilname (ek belge) var mı?
4. Sigortalı tüketici mi (haksız şart denetimi gerekir mi)?

## Denetim şeması
1. **Belge bütünlüğü.** Poliçe + SEDDK onaylı genel şartlar + özel şartlar + zeyilnameler birlikte değerlendirilir; çelişkide özel şart genel şarta üstündür (TTK m.1452 nispi emredicilik süzgeci).
2. **Teminat kapsamı.** Sigortalanan riziko, kıymet, riziko adresi/aracı ve teminat türleri çıkarılır. Ara sonuç: somut olay teminat tanımına giriyor mu?
3. **İstisna taraması.** Genel ve özel şarttaki teminat dışı haller listelenir (örn. kasko: alkol/uyuşturucu, ehliyetsizlik, savaş, deprem opsiyonel). İstisnayı sigortacı ispatlar; istisnalar dar yorumlanır.
4. **Muafiyet ve oranlama.** Tenzili muafiyet (her hasardan düşülen tutar), entegral muafiyet (altında ödeme yok), eksik sigorta oranlaması (TTK m.1462). Hesaba etkisi gösterilir.
5. **Geçersiz/haksız şart denetimi.** Sigortalı aleyhine TTK emredici hükümlerine aykırı şartlar geçersiz (m.1452); tüketici sigortalarında 6502 m.5 haksız şart ve dürüstlük denetimi. Açık olmayan şart sigortacı aleyhine yorumlanır.

## Çıktı modülleri
- Teminat-istisna-muafiyet haritası (madde atıflı).
- Geçersiz/haksız/tartışmalı şart listesi.
- Somut olay için kapsam değerlendirmesi.
- İspat yükü dağılımı ve müzakere/dava notu.

## Plugin bağlamı

Bu beceri `sigorta-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
