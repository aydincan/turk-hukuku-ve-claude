---
name: vekalet-sozlesmesi-ucret
description: "Avukatlık ücret sözleşmesinin kurulması, ücret türleri ve sınırları, asgari ücret tarifesi, karşı tarafa yüklenen vekâlet ücreti ve ücret alacağının takibi söz konusu olduğunda kullanılır."
---

# Avukatlık Sözleşmesi ve Vekâlet Ücreti

## Görev
Avukatlık ücret sözleşmesini geçerlilik ve sınırlar yönünden kurmak/denetlemek; akdi ve
yargısal (karşı tarafa yüklenen) vekâlet ücretini ayırt etmek; ücret alacağını yapılandırmak.

## Soğuk başlangıç (intake)
1. Ücret nasıl kararlaştırıldı (maktu, nispi, yüzde, başarı koşullu)?
2. Yazılı sözleşme var mı; iş değeri/dava değeri ne?
3. İş tamamlandı mı; haksız azil/istifa var mı?
4. Tartışma akdi ücret mi, yoksa karşı tarafa yüklenecek yargılama gideri vekâlet ücreti mi?

## Denetim şeması
1. **Sözleşmenin kurulması.** Avukatlık sözleşmesi serbestçe düzenlenir, yazılı yapılmaması
   geçersizlik sebebi değildir ama yazılılık ispat ve ücret için önemlidir (Av. K. m.163,
   TBK m.502 vd.). Belirlenmemişse ücret, tarife esas alınarak ve emeğe göre takdir edilir.
2. **Ücretin sınırları (emredici).** Ücret, dava konusu para veya değerin %25'ini aşamaz;
   yüzde belirlenen işlerde sınır bu orandır (Av. K. m.164/2). Dava konusu şeyin aynının
   ücret olarak kararlaştırılması (sonuca ortaklık) yasaktır. Ara sonuç: sözleşme bu sınırı
   aşıyor mu? Aşan kısım geçersizdir.
3. **Asgari tarife tabanı.** Kararlaştırılan ücret, yürürlükteki TBB Avukatlık Asgari Ücret
   Tarifesi'nin altında olamaz (m.164/4). Tarife her yıl Resmî Gazete'de yayımlanır; yıl/tarih
   belirt.
4. **Karşı tarafa yüklenen vekâlet ücreti.** Dava sonunda haksız çıkan tarafa yüklenen
   vekâlet ücreti yargılama giderindendir (HMK m.323/1-ğ) ve tarifeye göre hesaplanır; bu
   ücret kural olarak avukata aittir (Av. K. m.164/son), akdi ücretten ayrıdır.
5. **Azil/istifa ve müteselsil sorumluluk.** Haksız azilde ücretin tamamı muaccel olur; haklı
   sebeple azilde indirim gündeme gelir (Av. K. m.174). Karşı yan vekille sulh/feragat halinde
   ücret koruması ve müteselsil sorumluluk (m.165) gözetilir; avukatın hapis hakkı (m.166)
   ve örnek üzerinde alıkoyma değerlendirilir.
6. **Takip ve zamanaşımı.** Ücret alacağı vekâlet ilişkisinden doğar; zamanaşımı TBK m.147/5
   uyarınca beş yıldır. İlamsız icra/dava yolu seçilir; ispat yükü ücreti talep edendedir
   (TMK m.6).

## Çıktı modülleri
- Sözleşmenin geçerlilik/sınır denetimi (aşan/geçersiz şart tespiti).
- Akdi ve yargısal vekâlet ücreti ayrım tablosu.
- Ücret sözleşmesi ve ücret alacağı ihtar/talep taslağı ([doldurulacak] yer tutucularla).

## Plugin bağlamı

Bu beceri `avukatlik-meslek-kurallari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
