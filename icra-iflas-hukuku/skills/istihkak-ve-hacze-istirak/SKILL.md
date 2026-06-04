---
name: istihkak-ve-hacze-istirak
description: "Hacizli malın borçluya değil üçüncü kişiye ait olduğu iddiası (istihkak) ya da başka alacaklının hacze iştiraki gündeme geldiğinde; istihkak prosedürü, ispat yükü, mülkiyet karinesi ve sıraya katılma için kullanılır."
---

# İstihkak ve Hacze İştirak

## Görev
Haczedilen mal üzerinde üçüncü kişinin mülkiyet/rehin iddiasını (istihkak, m.96-99) çözmek; takibe sonradan katılan alacaklının hacze iştirakini (m.100, m.101) ve sıraya etkisini yönetmek.

## Soğuk başlangıç (intake)
- İstihkak iddiasında bulunan kim; mal kimin elinde haczedildi (zilyetlik)?
- Mal borçlu ile aynı çatı/işyerinde mi (karine yönü)?
- İddia haciz sırasında mı, sonra mı ileri sürüldü (3 günlük bildirim)?
- İştirak eden alacaklının ilk haciz tarihiyle ilişkisi nedir?

## Denetim şeması
1. **Zilyetlik karinesi (m.97/a)**: Haciz sırasında malı elinde bulunduran lehine mülkiyet karinesi vardır. Mal borçlunun elinde haczedilmişse istihkak iddia eden üçüncü kişi mülkiyetini ispatla yükümlüdür; üçüncü kişinin elinde haczedilmişse ispat yükü alacaklıdadır.
2. **Usul (m.96-99)**: İstihkak iddiası icra dairesine bildirilir; icra müdürü dosyayı icra mahkemesine gönderir. Takibin devamı/talikine mahkeme karar verir (m.97). İstihkak davası süresinde açılmazsa iddiadan vazgeçilmiş sayılır.
3. **Hacze iştirak (m.100)**: Borçluya karşı önce takip yapan alacaklının haczine, belirli belgelere dayanan diğer alacaklılar adi olarak iştirak edebilir; iştirak sırayı ve paylaşımı etkiler.
4. **İmtiyazlı iştirak (m.101)**: Eş, çocuk, vasi/kayyım gibi kişilerin belirli alacakları için özel iştirak imkânı denetlenir.
5. **İspat ve karine çatışması**: Muvazaa iddiası (özellikle aile/şirket içi devirler) ayrıca incelenir; gerektiğinde tasarrufun iptali becerisine geçilir.
6. **Ara sonuç**: İstihkakın akıbeti ve iştirakle oluşacak yeni sıra/dağıtım belirlenir.

## Çıktı modülleri
- İstihkak davası/itiraz dilekçesi iskeleti.
- İspat yükü ve karine yönü analizi.
- Hacze iştirak talebi ve sıraya etki notu.

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
