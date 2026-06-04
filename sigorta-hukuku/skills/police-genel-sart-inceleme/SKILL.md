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
