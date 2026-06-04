---
name: dilekce-basvuru-taslagi
description: "Sigortacıya ön başvuru, Sigorta Tahkim Komisyonu başvurusu, dava veya cevap dilekçesi gibi sigorta uyuşmazlığına özgü belgelerin taslaklanması istendiğinde kullanılır; doğru hukuki sebep ve talep mimarisiyle metin üretir."
---

# Başvuru ve Dilekçe Taslakları (Sigortacıya Başvuru, Tahkim, Dava)

## Görev
Sigorta uyuşmazlığına özgü belgeleri usulüne uygun taslaklamak: sigortacıya zorunlu ön başvuru, Sigorta Tahkim Komisyonu başvurusu, dava dilekçesi veya cevap dilekçesi; vakıa-hukuki sebep-talep mimarisini kurmak.

## Soğuk başlangıç (intake)
1. Hangi belge isteniyor (ön başvuru / tahkim / dava / cevap)?
2. Taraflar, poliçe bilgileri, riziko ve talep tutarı belli mi?
3. Forum seçildi mi (tahkim/ticaret/tüketici) ve başvuru şartı tamam mı?
4. Hangi deliller mevcut (poliçe, eksper raporu, kaza tutanağı, ödeme kanıtı)?

## Denetim şeması
1. **Belge türü ve dayanak.** Ön başvuru için KTK m.97 / 5684 m.30 başvuru şartı; tahkim için 5684 m.30; dava için HMK m.119 zorunlu unsurları. Ara sonuç: hangi format ve zorunlu unsurlar?
2. **Vakıa ve hukuki sebep.** Riziko, teminat ve ihlal vakıaları kronolojik; hukuki sebepler madde atıflı (örn. TTK m.1409/1421 teminat, m.1459 tazminat, m.1472 halefiyet, KTK m.91/97 doğrudan hak).
3. **Talep sonucu.** Net, miktar belirten talep; alacak likitse kesin, değilse belirsiz alacak/kısmi dava tercihi (HMK m.107-109); faiz başlangıcı ve türü (temerrüt/avans faizi).
4. **Delil bağlama.** Her vakıayı bir delile bağla; bilirkişi ve eksper raporu talebi; eksik belgeler için `[doldurulacak]` yer tutucu.
5. **Usul kontrolü.** Görev-yetki, harç/gider, zamanaşımı/hak düşürücü süre, başvuru şartı tamamlığı son kez doğrulanır.

## Çıktı modülleri
- İstenen belgenin tam taslağı (başlık, taraflar, açıklamalar, hukuki sebepler, deliller, talep sonucu).
- Madde atıflı hukuki sebep listesi.
- Delil dizini ve `[doldurulacak]` eksik belge listesi.
- Süre/usul uyarı notu.

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
