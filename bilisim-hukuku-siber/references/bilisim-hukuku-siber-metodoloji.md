# Bilişim Hukuku ve Siber Güvenlik — Metodoloji Referansı

## Alanın sistematiği
Bilişim hukuku, tek bir kodda toplanmamış; ceza, idari (düzenleyici) ve özel hukuk katmanlarının kesiştiği melez bir alandır. Çalışırken üç eksen birlikte düşünülmelidir: (i) bilişim sistemlerine ve verilere yönelik fiillerin **cezai** boyutu (TCK), (ii) kişisel veri ve elektronik haberleşme alanındaki **idari/düzenleyici** yükümlülükler (KVKK, 5651, BTK), (iii) siber olaydan doğan **tazminat ve sözleşmesel** sorumluluk (TBK). Aynı somut olay (örneğin bir veri ihlali) çoğu zaman üç eksende de sonuç doğurur; bu nedenle olayı tek bir başlığa hapsetmeden çok yönlü tasnif şarttır.

## Başat normlar ve madde atıfları
- **Bilişim suçları:** TCK m.243 (bilişim sistemine girme), m.244 (sistemi engelleme, bozma, verileri yok etme/değiştirme), m.245 (banka/kredi kartlarının kötüye kullanılması), m.245/A (yasak cihaz veya programlar). Verilerle bağlantılı diğer suçlar: TCK m.135-140 (kişisel verilerin kaydedilmesi, hukuka aykırı verme/ele geçirme, yok etmeme), m.132-134 (haberleşmenin gizliliği, özel hayat). Bilişim yoluyla işlenen dolandırıcılığın nitelikli hali TCK m.158/1-f.
- **Kişisel veri ve ihlal:** 6698 sayılı KVKK m.12 (veri güvenliği yükümlülükleri), m.12/5 (ihlalin Kurula ve ilgili kişiye bildirimi), m.18 (idari para cezaları). Kurul kararları ve veri ihlali bildirim formu kvkk.gov.tr üzerinden takip edilir.
- **İnternet ortamı:** 5651 sayılı Kanun — içerik/yer/erişim sağlayıcı tanımları ve sorumluluğu, m.8 (erişimin engellenmesi), m.8/A (gecikmesinde sakınca bulunan hallerde tedbir), m.9 (içeriğin çıkarılması ve erişimin engellenmesi başvurusu), m.9/A (özel hayatın gizliliği). Trafik/yer sağlayıcı loglarının tutulması yükümlülükleri.
- **Dijital delil:** CMK m.134 (bilgisayarlarda, programlarda ve kütüklerde arama, kopyalama, elkoyma); CMK m.116-123 (arama-elkoyma genel rejimi). Adli Bilişim İncelemesi yönergeleri ve imaj alma/hash doğrulama uygulaması.
- **Diğer:** 5809 sayılı Elektronik Haberleşme Kanunu ve BTK düzenlemeleri; e-imza için 5070 sayılı Kanun; banka ve ödeme sistemleri için sektörel mevzuat (BDDK/6493).

## Çalışma yöntemi
1. **Olayı katmana ayır:** Fiil bir suç mu, bir idari yükümlülük ihlali mi, yoksa bir tazminat sorumluluğu mu doğuruyor? Çoğu zaman üçü birden.
2. **Yer/zaman/sistem tespiti:** Olayın işlendiği sistem, etkilenen veri, zaman damgaları ve loglar belirlenir; delil bütünlüğü en başta korunur.
3. **Norm altına yerleştirme (altlama):** Her fiil için tip unsurlarını (TCK), yükümlülük şartlarını (KVKK m.12, 5651) ve sorumluluk unsurlarını (TBK m.49 vd.) ayrı ayrı denetle.
4. **Yetki/görev haritası:** Cezada Cumhuriyet savcılığı/asliye ceza-ağır ceza; KVKK'da idare ve idari yargı; tazminatta asliye hukuk/tüketici/ticaret; 5651 tedbirlerinde sulh ceza hâkimliği.
5. **Strateji ve süre:** Bildirim süreleri (KVKK ihlal bildirimi), şikâyet süreleri, zamanaşımı ve delil kaybı riskleri en baştan takvimlenir.

## Kaynak hijyeni
Mevzuat daima madde/fıkra/bent ile verilir; KVKK Kurul kararları karar tarih ve sayısıyla, içtihat ise mahkeme + daire + esas/karar no + tarih ile doğrulanır. İçtihat doğrulaması için karararama.yargitay.gov.tr, idari uyuşmazlıklar için karararama.danistay.gov.tr, anayasal şikâyet için kararlarbilgibankasi.anayasa.gov.tr kullanılır. Karar numarası hatırdan yazılmaz; doğrulanmamış künye `[doğrulanacak]` olarak işaretlenir. Teknik standartlar (TS ISO/IEC 27001, adli bilişim kılavuzları) kaynağıyla anılır.
