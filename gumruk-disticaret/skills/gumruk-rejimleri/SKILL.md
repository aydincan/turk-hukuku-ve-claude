---
name: gumruk-rejimleri
description: "Dahilde işleme, antrepo, geçici ithalat, transit ve hariçte işleme gibi rejimlerin şartları, kapatılması ve ihlal sonuçlarını analiz etmek gerektiğinde; rejim ihlalinden doğan yükümlülük ve cezaları değerlendirmek için kullanılır."
---

# Gümrük Rejimleri ve Şartlı Muafiyet

## Görev
Ekonomik etkili ve şartlı muafiyet rejimlerinin (dahilde işleme, antrepo, geçici ithalat, transit, hariçte işleme, gümrük kontrolü altında işleme) şartlarını, izin yükümlülüklerini, kapatma sürelerini ve ihlal sonuçlarını analiz etmek.

## Soğuk başlangıç (intake)
- Hangi rejim ve hangi izin (DİİB, antrepo izni, geçici ithalat izni) söz konusu?
- İzin süresi/kapatma süresi nedir; süre aşıldı mı, taahhütler yerine getirildi mi?
- Eşya işlendi, ihraç edildi, yeniden ihraç edildi mi; fire/zayiat oranı uygun mu?
- İdare ihlal mi tespit etti, yoksa rejim usulüne uygun mu kapatılacak?

## Denetim şeması
1. Rejim seçimi ve izin: Şartlı muafiyet rejimleri izne tabidir (4458 m.80 vd.). İznin kapsamı, süresi ve taahhütleri belirleyicidir; izinsiz veya kapsam dışı işlem ihlaldir.
2. Dahilde işleme: Eşya işlenip ihraç edilmek üzere vergileri askıya alınarak (DİİB) ithal edilir; ihracat taahhüdü süresinde gerçekleşmezse askıdaki vergiler ek tahakkukla doğar. İkincil işlem görmüş ürün, fire ve verimlilik oranları denetlenir.
3. Antrepo: Eşya antrepoda gümrük gözetiminde tutulur; antrepodan izinsiz çekme, sayım noksanlığı veya kayıt uyumsuzluğu yükümlülük ve ceza doğurur (m.236 ilgili hükümleri).
4. Geçici ithalat: Tam/kısmi muafiyetle belirli süre için ithal edilen eşya süresinde yeniden ihraç edilmeli; aksi halde serbest dolaşıma giriş vergileri ve cezası gündeme gelir.
5. Yükümlülüğün doğumu: Rejim ihlalinde yükümlülük 4458 m.182-184 çerçevesinde doğar; doğum anı oran/kur ve zamanaşımı (m.197) için saptanır.
6. İspat yükü: Rejim şartlarına uygunluğu (ihracatın gerçekleştiği, sürenin tutulduğu, fire oranının makul olduğu) izin sahibi belgelerle ispatlar; idare ihlali somut tespitle ortaya koyar.
7. Ara sonuç: Rejimin doğru kapatılıp kapatılmadığı, ihlal varsa doğan vergi ve cezanın dayanağı belirlenir; telafi edici düzeltme imkânları değerlendirilir.

## Çıktı modülleri
- Rejim-izin-taahhüt uyum kontrol listesi
- İhlal halinde yükümlülük hesabı ve savunma notu
- Rejim kapatma/düzeltme başvuru taslağı

## Plugin bağlamı

Bu beceri `gumruk-disticaret` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
