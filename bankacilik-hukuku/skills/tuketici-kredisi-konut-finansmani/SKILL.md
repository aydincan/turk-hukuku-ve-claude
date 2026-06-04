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
