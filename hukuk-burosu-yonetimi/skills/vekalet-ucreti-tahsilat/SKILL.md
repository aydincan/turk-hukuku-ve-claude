---
name: vekalet-ucreti-tahsilat
description: "Vekâlet ücreti ve masrafların faturalanması, tahsil edilmesi, gecikmiş alacakların takibi ve avukatın hapis hakkı ile güvence stratejisi gerektiğinde kullanılır."
---

# Vekâlet Ücreti Faturalama ve Tahsilat

## Görev
Hak edilen vekâlet ücreti ve masrafları doğru hesaplayıp faturalamak; tahsilatı yönetmek; gecikme halinde uygun hukuki yola (icra/dava) ve güvenceye karar vermek.

## Soğuk başlangıç (intake)
1. Sözleşmede ücret tipi (maktu/nispi/saatlik) ve ödeme planı ne; yazılı sözleşme var mı?
2. İş hangi aşamada bitti/kesildi; hak edilen tutar nedir, kısmi tahsilat oldu mu?
3. Karşı taraf vekâlet ücreti hükmedildi mi, tahsil edildi mi?
4. Müvekkil ödemede mi temerrütte; elde dosya/evrak (hapis hakkı) var mı?

## Denetim şeması
1. **Hak edilen ücretin tespiti (1136 m.163-164)**: Sözleşmedeki tutar; sözleşme yoksa Avukatlık Asgari Ücret Tarifesi. İşin tamamlanma derecesine göre hak ediş belirlenir.
2. **Karşı taraf vekâlet ücreti (1136 m.164/son)**: Yargılama gideri olarak hükmedilen tutar aksi kararlaştırılmadıkça avukata aittir; müvekkil bunu kendine mal edemez.
3. **Faturalama**: Serbest meslek makbuzu/fatura düzeni; KDV ve stopaj boyutu (mali müşavirle teyit). Masraflar ayrı kalemlenir.
4. **Temerrüt ve faiz (TBK m.117, 120)**: Muacceliyet/ihtar ile temerrüt; ticari/adi faiz ayrımı, sözleşmesel faiz şartı.
5. **Güvence — hapis hakkı (1136 m.166)**: Avukat, müvekkile ait olup elinde bulunan evrak ve değerler üzerinde ücret ve masraf alacağı için hapis hakkına sahiptir; sınırları gözetilerek kullanılır.
6. **Takip yolu**: Yazılı sözleşme/makbuz varsa ilamsız icra (İİK m.42 vd.) veya alacak davası; itiraz halinde itirazın iptali (İİK m.67, 1 yıl) değerlendirilir.
7. **Ara sonuç**: Hak ediş netse fatura kesilir, ödenmezse ihtar + uygun takip yolu seçilir.

## Çıktı modülleri
- Ücret/masraf hesap dökümü ve fatura kalemleri.
- İhtarname taslağı ([doldurulacak] tutar, vade, faiz).
- Takip yolu önerisi (icra/dava) ve hapis hakkı değerlendirmesi.

## Plugin bağlamı

Bu beceri `hukuk-burosu-yonetimi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
