---
name: yorum-yontemleri
description: "Bir kanun hükmünün ne anlama geldiği tartışmalı olduğunda; lafzı belirsiz, çok anlamlı ya da amacıyla çatışır göründüğünde dört yorum yöntemini sırayla uygulamak için kullanılır."
---

# Yorum Yöntemleri (Lafzî, Sistematik, Tarihsel, Amaçsal)

## Görev
Bir normun anlamını TMK m.1 çerçevesinde, kabul gören dört yorum yöntemini birlikte kullanarak ortaya koymak; lafız ile amaç çatıştığında gerekçeli bir tercih yapmak.

## Soğuk başlangıç (intake)
- Hangi kanunun hangi madde/fıkra/bendi tartışmalı? Tam metni elimizde mi?
- Tereddüt nereden doğuyor: kelimenin çok anlamlılığı mı, sessizlik mi, başka hükümle çelişki mi?
- Bu bir özel hukuk normu mu, ceza/idare gibi yorum yasaklarının sıkı olduğu bir alan mı?
- Tarafların savunduğu iki rakip okuma nedir?

## Denetim şeması
1. **Lafzî (sözel) yorum** — TMK m.1: önce metnin olağan dil anlamı ve hukuk dilindeki teknik anlamı. Hükmün "açık" görünmesi yorumu bitirmez; lafız sadece başlangıç ve dış sınırdır.
2. **Sistematik yorum** — Hükmü bulunduğu kanun içindeki yerine, başlık/kenar başlığına, yollamalara (örn. TMK m.5 ile genel hükümlerin yayılması) ve üst normlara göre oku. Çelişkide *lex specialis*, *lex superior*, *lex posterior* kurallarını uygula.
3. **Tarihsel yorum** — Madde gerekçesi, kanunun hazırlık çalışmaları, İsviçre/Alman kaynak hükümle karşılaştırma ve önceki düzenlemeyle fark. Kaynak kanun yorumu yol gösterir ama bağlamaz.
4. **Amaçsal (gai/teleolojik) yorum** — Normun koruduğu menfaat ve güttüğü amaç (ratio legis). Menfaatler içtihadı ile çatışan menfaatleri tart. Anayasaya ve AİHS'e uygun yorum (Anayasa m.11, m.90/5) tercih edilir.
5. **Sentez ve sınır** — Yöntemler çatışırsa amaçsal sonuç genellikle üstün tutulur; ancak lafzın olası anlamı aşılırsa bu artık yorum değil hukuk yaratma/kıyas olur (ayrı beceri). Ceza ve vergi gibi kanunilik ağır basan alanlarda lafzın dışına çıkan genişletici yorumdan kaçın (TCK m.2).

## Çıktı modülleri
- Tartışılan hüküm ve iki rakip okumanın tablosu.
- Dört yöntemin her birinin sonucu ve ağırlığı.
- Gerekçeli tercih + karşı argümana cevap.
- Atıf taslağı: ilke + `[doğrulanacak]` künye yeri (karararama.yargitay.gov.tr).

## Plugin bağlamı

Bu beceri `hukuk-metodolojisi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
