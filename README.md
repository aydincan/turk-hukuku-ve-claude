# Claude ve Türk Hukuku

> **Claude ve Türk Hukuku** — Türk hukuku için deneysel bir Claude Code beceri (skill)
> koleksiyonu. Avukat, hukuk müşaviri, hâkim/savcı adayı, akademisyen ve hukuk öğrencisi
> için metodoloji, atıf hijyeni, sözleşme, dava ve mütalaa iş akışları.

Claude ve Türk Hukuku — Türk hukuku için deneysel skill (beceri) koleksiyonu. Avukat, hukuk müşaviri, hâkim/savcı adayı ve hukuk öğrencisi için metodoloji, atıf hijyeni, sözleşme, dava ve mütalaa iş akışları. Katı kaynak hijyeni: içtihat yalnızca mahkeme + daire + esas/karar no + tarih + doğrulanabilir kaynakla; uydurma karar numarası yok.

**81 eklenti · 1002 beceri · Apache-2.0 OR MIT**

**Yazar:** Aydın Can Polatkan

> *Bu çalışma, ömrünü Türk yargısına adamış babam Hâkim Vahit Polatkan'ın ebedi anısına ithaf edilmiştir.*

> **Terminal kullanmıyor musunuz?** Aynı beceriler ve resmî kaynak bağlantısı, Mac ve Windows
> için bir [masaüstü uygulamasında](https://turk-hukuku.com/uygulama/) da var: indirin, yapay
> zekâ anahtarınızı ekleyin, sorun. Tüm hukuk alanları ve rehberler: [turk-hukuku.com](https://turk-hukuku.com/).

---

## ⚠️ Önce bunu okuyun

Bu proje **hukuki danışmanlık değildir** ve **denenmiş bir ürün değildir** — denemek için
teknik bir oyun alanıdır. Çıktılar **yürürlükteki mevzuat ve doğrulanmış güncel içtihatla**
teyit edilmelidir. Avukat-müvekkil sırrı (TCK m.285-286, 1136 s.K.), KVKK (6698),
yurt dışı veri aktarımı ve mesleki yükümlülükler bakımından dağıtımın kendi durumunuza
uygunluğunu **bağımsız olarak** denetleyin. Ayrıntı: [`SORUMLULUK-REDDI.md`](./SORUMLULUK-REDDI.md).

## Kurulum

### Claude Code (terminal)

```bash
/plugin marketplace add https://github.com/aydincan/turk-hukuku-ve-claude
/plugin install <eklenti-adı>@turk-hukuku-skills
```

Örnek:

```bash
/plugin install hukuk-metodolojisi@turk-hukuku-skills
/plugin install borclar-hukuku-genel@turk-hukuku-skills
```

Ayrıntılı kurulum (Claude Desktop dâhil) için [`KURULUM.md`](./KURULUM.md).

## Nasıl çalışır?

1. **Önce temel eklentileri yükleyin:** [`hukuk-metodolojisi`](./hukuk-metodolojisi) ve
   [`atif-turk-hukuku`](./atif-turk-hukuku) — yöntem ve kaynak hijyeni tüm alanların
   zeminidir.
2. **Çalışma alanınıza uyan uzmanlık eklentilerini** etkinleştirin.
3. **Olayı anlatın veya dosyayı yükleyin** (sessiz yükleme desteklenir).
4. Her eklentinin `genel-bakis` becerisi sizi triyajdan geçirir ve uygun uzman beceriye
   yönlendirir.
5. **Çıktı**: gerekçeli mütalaa, dilekçe/sözleşme taslağı, kontrol listesi veya yapılandırılmış analiz.

## Kaynak hijyeni (projenin omurgası)

Her beceri katı bir kaynak kuralına uyar:

- **İçtihat asla model hafızasından zikredilmez.** Her karar mahkeme + daire +
  **esas/karar no** + tarih + doğrulanabilir kaynakla verilir; emin olunmayan künye
  `[doğrulanacak]` işaretlenir.
- **Mevzuat** madde/fıkra/bent ile; **doktrin** yalnızca kullanıcı kaynağıyla.

## Örnek dosyalar

[`ornek-dosyalar/`](./ornek-dosyalar) altında, eklentileri gerçekçi bir olayla denemek için
hazırlanmış **kurgusal ve anonim** örnek dava dosyaları bulunur — iş alacağı, kira/tahliye,
ayıplı mal, **vergi davaları** (re'sen tarhiyat), ceza soruşturması, boşanma, karşılıksız çek
ve KVKK veri ihlali. Hepsi yalnızca eğitim/deneme amaçlıdır.

## Eklenti kataloğu

### Temel — Metodoloji, Atıf ve Genel Teori

| Eklenti | Başlık | Açıklama |
|---|---|---|
| `hukuk-metodolojisi` | [Hukuk Metodolojisi ve Yorum](https://turk-hukuku.com/beceriler/hukuk-metodolojisi/) | Türk hukukunda yöntem ve hukuk uygulaması: TMK m.1 çerçevesinde lafzî/amaçsal/sistematik/tarihsel yorum, kıyas ve evleviyet, hâkimin hukuk yaratması, kanun boşluğu, içtihat çalışması ve gerekçeli (mütalaa) üslubu. |
| `atif-turk-hukuku` | [Türk Hukukunda Atıf ve Kaynak Hijyeni](https://turk-hukuku.com/beceriler/atif-turk-hukuku/) | Türk hukukçusunun ev içi atıf düzeni: içtihat yalnızca mahkeme, daire, esas/karar numarası, tarih ve doğrulanabilir kaynakla; mevzuat madde/fıkra/bent ile; doktrin yazar-eser-sayfa ile. Model hafızasından karar zikretme yok. |
| `hukuk-felsefesi-genel-teori` | [Hukuk Felsefesi ve Genel Hukuk Teorisi](https://turk-hukuku.com/beceriler/hukuk-felsefesi-genel-teori/) | Hukuk teorisi ve felsefesi katmanı: hukuki pozitivizm, doğal hukuk, norm geçerliliği, hukuk sosyolojisi, hukuki realizm ve eleştirel yaklaşımlar; hukuk öğrencisi ve akademik tartışma için metodolojik derinlik. |
| `roma-hukuku` | [Roma Hukuku ve Tarihî Temeller](https://turk-hukuku.com/beceriler/roma-hukuku/) | Türk medeni hukukunun tarihî kökenleri: Roma hukuku kavramları, pandekt sistemi, İsviçre Medeni Kanunu ve Borçlar Kanunu resepsiyonu; modern TMK/TBK kavramlarının soykütüğü ve akademik temel. |

### Özel Hukuk — Medeni Hukuk

| Eklenti | Başlık | Açıklama |
|---|---|---|
| `medeni-hukuk-baslangic` | [Medeni Hukuk Başlangıç Hükümleri](https://turk-hukuku.com/beceriler/medeni-hukuk-baslangic/) | TMK başlangıç hükümleri ve genel ilkeler: dürüstlük kuralı (m.2), iyiniyetin korunması (m.3), hâkimin takdir yetkisi (m.4), ispat yükü (m.6), hakkın kötüye kullanılması yasağı; tüm medeni hukuk için temel süzgeç. |
| `kisiler-hukuku` | [Kişiler Hukuku](https://turk-hukuku.com/beceriler/kisiler-hukuku/) | Gerçek ve tüzel kişiler hukuku: hak ve fiil ehliyeti, kişilik haklarının korunması (m.23-25), ad, yerleşim yeri, dernek ve vakıf; kişilik hakkı ihlali ve manevi tazminat denetim şeması. |
| `aile-hukuku` | [Aile Hukuku](https://turk-hukuku.com/beceriler/aile-hukuku/) | Aile hukuku uygulaması: evlenme, boşanma sebepleri (TMK m.161-166), nafaka türleri, velayet ve kişisel ilişki, mal rejimleri ve tasfiye, soybağı; 6284 sayılı Kanun kapsamında koruma tedbirleri. |
| `miras-hukuku` | [Miras Hukuku](https://turk-hukuku.com/beceriler/miras-hukuku/) | Miras hukuku: yasal ve atanmış mirasçılık, saklı paylı mirasçılar (m.505-506), ölüme bağlı tasarruflar, tenkis ve denkleştirme davaları, mirasın reddi, tereke tespiti ve paylaşma. |
| `esya-hukuku` | [Eşya Hukuku](https://turk-hukuku.com/beceriler/esya-hukuku/) | Eşya hukuku: zilyetlik ve tapu sicili, taşınır/taşınmaz mülkiyeti, sınırlı ayni haklar (irtifak, rehin, intifa), istihkak ve el atmanın önlenmesi (müdahalenin meni) davaları. |
| `tapu-kadastro` | [Tapu ve Kadastro Uygulaması](https://turk-hukuku.com/beceriler/tapu-kadastro/) | Tapu ve kadastro uygulaması: tapu sicili ilkeleri, kadastro tespitine itiraz, tapu iptali ve tescil davaları, kazandırıcı zamanaşımı, şerh-beyan-rehin işlemleri ve yolsuz tescilin düzeltilmesi. |
| `kat-mulkiyeti` | [Kat Mülkiyeti ve Site Yönetimi](https://turk-hukuku.com/beceriler/kat-mulkiyeti/) | Kat Mülkiyeti Kanunu uygulaması: kat irtifakı/kat mülkiyeti kurulması, yönetim planı, kat malikleri kurulu kararları, aidat ve ortak gider, ortak alan kullanımı ve projeye aykırılığın giderilmesi. |

### Özel Hukuk — Borçlar Hukuku

| Eklenti | Başlık | Açıklama |
|---|---|---|
| `borclar-hukuku-genel` | [Borçlar Hukuku Genel Hükümler](https://turk-hukuku.com/beceriler/borclar-hukuku-genel/) | TBK genel hükümler: sözleşmenin kurulması ve geçerliliği, irade sakatlıkları (hata-hile-korkutma), temsil, hükümsüzlük, ifa ve ifa engelleri, borçlu temerrüdü, zamanaşımı; borç ilişkisinin kaynak piramidi. |
| `borclar-hukuku-ozel` | [Borçlar Hukuku Özel Hükümler](https://turk-hukuku.com/beceriler/borclar-hukuku-ozel/) | İsimli sözleşmeler: satış (ayıptan/zapttan sorumluluk), kira, eser, vekâlet, kefalet, bağışlama, ödünç ve hizmet sözleşmeleri; her sözleşme tipi için kuruluş, ifa ve sorumluluk denetim şeması. |
| `haksiz-fiil-tazminat` | [Haksız Fiil ve Tazminat Hukuku](https://turk-hukuku.com/beceriler/haksiz-fiil-tazminat/) | Haksız fiil sorumluluğu: TBK m.49 vd. unsurları (fiil, hukuka aykırılık, kusur, zarar, illiyet), kusursuz sorumluluk halleri, maddi/manevi tazminatın hesabı, destekten yoksun kalma ve tazminattan indirim sebepleri. |
| `sebepsiz-zenginlesme` | [Sebepsiz Zenginleşme](https://turk-hukuku.com/beceriler/sebepsiz-zenginlesme/) | Sebepsiz zenginleşmeden doğan borç ilişkisi: TBK m.77 vd. — haklı sebep olmaksızın malvarlığı kayması, iade kapsamı, iyiniyetli/kötüniyetli zenginleşen ayrımı ve diğer taleplerle yarışma. |
| `tuketici-hukuku` | [Tüketici Hukuku](https://turk-hukuku.com/beceriler/tuketici-hukuku/) | Tüketicinin Korunması Hakkında Kanun uygulaması: ayıplı mal/hizmet, cayma hakkı, mesafeli ve kapıdan satış, haksız sözleşme şartları, tüketici kredisi; tüketici hakem heyeti ve tüketici mahkemesi yolu. |
| `kira-hukuku` | [Kira Hukuku](https://turk-hukuku.com/beceriler/kira-hukuku/) | Konut ve çatılı işyeri kiraları: kira sözleşmesi, kira bedelinin belirlenmesi ve tespit davası, tahliye sebepleri (ihtiyaç, yeniden inşa, tahliye taahhüdü, iki haklı ihtar, temerrüt) ve ilamsız tahliye icrası. |
| `gayrimenkul-hukuku` | [Gayrimenkul Hukuku Uygulaması](https://turk-hukuku.com/beceriler/gayrimenkul-hukuku/) | Gayrimenkul işlem ve uyuşmazlıkları: taşınmaz satış vaadi, kat karşılığı inşaat sözleşmesi, arsa payı düzeltimi, ön ödemeli konut satışı; tapu, sözleşme ve dava boyutlarının birlikte ele alındığı uygulama eklentisi. |

### Özel Hukuk — Ticaret ve Şirketler Hukuku

| Eklenti | Başlık | Açıklama |
|---|---|---|
| `ticari-isletme-hukuku` | [Ticari İşletme ve Tacir Hukuku](https://turk-hukuku.com/beceriler/ticari-isletme-hukuku/) | TTK genel hükümler ve ticari işletme: tacir sıfatı ve sonuçları, ticari iş ve hükümler, ticaret unvanı ve sicil, cari hesap, ticari işlerde faiz ve TTK kapsamında haksız rekabet. |
| `sirketler-hukuku` | [Şirketler Hukuku (AŞ ve Ltd.)](https://turk-hukuku.com/beceriler/sirketler-hukuku/) | Sermaye şirketleri: anonim ve limited şirket kuruluşu, organlar, pay ve pay sahipliği, sermaye artırımı/azaltımı, yönetici sorumluluğu (TTK m.553 vd.), sermaye kaybı ve borca batıklık (TTK m.376). |
| `anonim-sirket-genel-kurul` | [Anonim Şirket Genel Kurulu](https://turk-hukuku.com/beceriler/anonim-sirket-genel-kurul/) | AŞ genel kurulu hazırlık ve icrası: çağrı usulü, gündem, toplantı ve karar nisapları, vekâleten temsil, tutanak, genel kurul kararlarının iptali (TTK m.445 vd.) ve azlık haklarının kullanımı. |
| `kiymetli-evrak` | [Kıymetli Evrak Hukuku](https://turk-hukuku.com/beceriler/kiymetli-evrak/) | Kıymetli evrak ve kambiyo senetleri: çek, bono ve poliçenin unsurları, ciro ve devir, aval, müracaat hakkı, kambiyo senetlerine özgü takip; karşılıksız çek ve çek düzenleme yasağı. |
| `sigorta-hukuku` | [Sigorta Hukuku](https://turk-hukuku.com/beceriler/sigorta-hukuku/) | Sigorta hukuku: sigorta sözleşmesi, beyan yükümlülüğü, prim ve riziko, tazminat ve rücu; zorunlu/ihtiyari sigortalar, trafik sigortası ve Sigorta Tahkim Komisyonu yolu. |
| `deniz-ticareti-hukuku` | [Deniz Ticareti Hukuku](https://turk-hukuku.com/beceriler/deniz-ticareti-hukuku/) | Deniz ticareti: gemi ve donatan, navlun sözleşmeleri ve konişmento, deniz alacakları ve gemi ipoteği, müşterek avarya, çatma ve kurtarma; TTK Beşinci Kitap uygulaması. |
| `tasima-hukuku` | [Taşıma ve Lojistik Hukuku](https://turk-hukuku.com/beceriler/tasima-hukuku/) | Kara taşıması ve lojistik: TTK taşıma hükümleri ve CMR Konvansiyonu, taşıyıcının ziya/hasar/gecikme sorumluluğu, taşıma senedi, sorumluluk sınırları ve taşıma işleri komisyonculuğu. |
| `bankacilik-hukuku` | [Bankacılık Hukuku](https://turk-hukuku.com/beceriler/bankacilik-hukuku/) | Bankacılık hukuku: 5411 sayılı Kanun çerçevesinde bankacılık faaliyeti ve BDDK denetimi, kredi ve teminat sözleşmeleri, mevduat, banka sırrı; banka-müşteri uyuşmazlıkları ve hukuk müşavirliği. |
| `sermaye-piyasasi-hukuku` | [Sermaye Piyasası Hukuku](https://turk-hukuku.com/beceriler/sermaye-piyasasi-hukuku/) | Sermaye piyasası: 6362 sayılı Kanun kapsamında halka arz ve izahname, kamuyu aydınlatma, piyasa dolandırıcılığı ve içeriden öğrenenlerin ticareti, yatırım kuruluşları ve SPK idari yaptırımları. |
| `rekabet-hukuku` | [Rekabet Hukuku](https://turk-hukuku.com/beceriler/rekabet-hukuku/) | Rekabet hukuku: 4054 sayılı Kanun — rekabeti sınırlayıcı anlaşmalar (m.4), hâkim durumun kötüye kullanılması (m.6), birleşme/devralma denetimi (m.7), pazar tanımı, muafiyet ve Rekabet Kurulu süreçleri. |
| `birlesme-devralma-ma` | [Birleşme ve Devralma (M&A)](https://turk-hukuku.com/beceriler/birlesme-devralma-ma/) | Birleşme-devralma işlemleri: hukuki durum tespiti (due diligence), pay/varlık devri yapıları, pay alım satım sözleşmesi (SPA), beyan ve tekeffüller, kapanış şartları ve işlem sonrası entegrasyon; ihtiyaç halinde rekabet izni. |
| `girisim-startup-hukuku` | [Girişim ve Startup Hukuku](https://turk-hukuku.com/beceriler/girisim-startup-hukuku/) | Girişim hukuku: kuruluş ve ortaklık yapısı, yatırım turları, term sheet, pay sahipleri sözleşmesi, kurucu vesting ve çalışan hisse opsiyonu, tasfiye tercihi ve sulandırma; yatırımcı-girişimci dengeleri. |

### Özel Hukuk — Fikri ve Sınai Mülkiyet

| Eklenti | Başlık | Açıklama |
|---|---|---|
| `marka-hukuku` | [Marka Hukuku](https://turk-hukuku.com/beceriler/marka-hukuku/) | Marka hukuku: 6769 sayılı SMK kapsamında marka tescili ve mutlak/nispi ret sebepleri, karıştırılma ihtimali, tanınmış marka koruması, hükümsüzlük ve iptal, marka hakkına tecavüz ve tazminat. |
| `patent-faydali-model` | [Patent ve Faydalı Model](https://turk-hukuku.com/beceriler/patent-faydali-model/) | Patent ve faydalı model: patentlenebilirlik şartları (yenilik, buluş basamağı, sanayiye uygulanabilirlik), istem yorumu, hükümsüzlük, çalışan buluşları ve patent hakkına tecavüz; SMK uygulaması. |
| `tasarim-hukuku` | [Tasarım Hukuku](https://turk-hukuku.com/beceriler/tasarim-hukuku/) | Tasarım hukuku: tescilli ve tescilsiz tasarım koruması, yenilik ve ayırt edici nitelik, bilgilenmiş kullanıcı ölçütü, hükümsüzlük ve tasarım hakkına tecavüz; SMK kapsamında uygulama. |
| `telif-haklari` | [Telif Hakları (FSEK)](https://turk-hukuku.com/beceriler/telif-haklari/) | Fikir ve Sanat Eserleri Kanunu: eser türleri ve sahipliği, mali ve manevi haklar, işleme ve umuma iletim, bağlantılı haklar, lisans ve devir sözleşmeleri, tecavüzün ref'i/men'i ve tazminat. |
| `fikri-mulkiyet-dava` | [Fikri ve Sınai Haklar Dava Uygulaması](https://turk-hukuku.com/beceriler/fikri-mulkiyet-dava/) | Fikri ve sınai haklarda dava: Fikri ve Sınai Haklar Hukuk/Ceza Mahkemeleri, ihtiyati tedbir ve delil tespiti, tecavüzün tespiti ve durdurulması, tazminat hesabı ve gümrükte el koyma süreçleri. |

### Özel Hukuk — İş ve Sosyal Güvenlik Hukuku

| Eklenti | Başlık | Açıklama |
|---|---|---|
| `is-hukuku-bireysel` | [Bireysel İş Hukuku](https://turk-hukuku.com/beceriler/is-hukuku-bireysel/) | Bireysel iş hukuku: iş sözleşmesi türleri, feshin geçerli/haklı sebebi, iş güvencesi ve işe iade (m.18-21), kıdem ve ihbar tazminatı, fazla çalışma, yıllık izin; işçilik alacakları denetim şeması. |
| `is-hukuku-toplu` | [Toplu İş Hukuku](https://turk-hukuku.com/beceriler/is-hukuku-toplu/) | Toplu iş hukuku: 6356 sayılı Kanun — sendika özgürlüğü ve güvenceler, toplu iş sözleşmesi yetkisi ve bağıtlanması, toplu hak/menfaat uyuşmazlıkları, grev ve lokavt; barışçıl çözüm yolları. |
| `sosyal-guvenlik` | [Sosyal Güvenlik Hukuku](https://turk-hukuku.com/beceriler/sosyal-guvenlik/) | Sosyal güvenlik: 5510 sayılı Kanun — sigortalılık türleri, hizmet tespiti davası, prim ve borçlanma, iş kazası/meslek hastalığı, gelir-aylık bağlanması ve SGK rücu davaları. |
| `is-sagligi-guvenligi` | [İş Sağlığı ve Güvenliği](https://turk-hukuku.com/beceriler/is-sagligi-guvenligi/) | İş sağlığı ve güvenliği: 6331 sayılı Kanun — işverenin önleme yükümlülükleri, risk değerlendirmesi, İSG profesyonelleri, iş kazası bildirimi ve sorumluluk, idari yaptırımlar ve işverenin tazminat sorumluluğu. |
| `ik-insan-kaynaklari` | [İnsan Kaynakları ve İşveren Uyumu](https://turk-hukuku.com/beceriler/ik-insan-kaynaklari/) | İşveren/İK perspektifi: işe alım ve sözleşme şablonları, disiplin ve savunma süreçleri, performans ve fesih yönetimi, işyeri yönetmelikleri, çalışan kişisel verilerinin KVKK uyumu; risk azaltıcı süreç tasarımı. |

### Kamu Hukuku — Ceza Hukuku

| Eklenti | Başlık | Açıklama |
|---|---|---|
| `ceza-hukuku-genel` | [Ceza Hukuku Genel Hükümler](https://turk-hukuku.com/beceriler/ceza-hukuku-genel/) | TCK genel hükümler ve suç genel teorisi: tipiklik, hukuka aykırılık ve kusurluluk katmanları, kast/taksir, hukuka uygunluk sebepleri, teşebbüs, iştirak, içtima ve yaptırım teorisi; suç denetim şeması. |
| `ceza-hukuku-ozel` | [Ceza Hukuku Özel Hükümler](https://turk-hukuku.com/beceriler/ceza-hukuku-ozel/) | TCK özel hükümler: kişilere karşı (yaralama, tehdit, hakaret), malvarlığına karşı (hırsızlık, dolandırıcılık, güveni kötüye kullanma), kamu idaresine ve güvene karşı suçların unsurları ve nitelikli halleri. |
| `ceza-muhakemesi` | [Ceza Muhakemesi (CMK)](https://turk-hukuku.com/beceriler/ceza-muhakemesi/) | Ceza muhakemesi: soruşturma ve kovuşturma, koruma tedbirleri (yakalama, gözaltı, tutuklama, arama-el koyma), delil yasakları, savunma hakları, iddianame, hüküm ve istinaf/temyiz kanun yolları. |
| `ekonomik-ceza` | [Ekonomik ve Mali Suçlar](https://turk-hukuku.com/beceriler/ekonomik-ceza/) | Ekonomik ceza hukuku: aklama (5549/MASAK), vergi kaçakçılığı (VUK m.359), nitelikli dolandırıcılık, zimmet/rüşvet, sermaye piyasası suçları; şirketler ve yöneticiler için ceza riski yönetimi. |
| `infaz-hukuku` | [İnfaz Hukuku](https://turk-hukuku.com/beceriler/infaz-hukuku/) | Ceza ve güvenlik tedbirlerinin infazı: 5275 sayılı Kanun — infaz rejimi ve hesabı, koşullu salıverilme ve denetimli serbestlik, açık kuruma ayrılma, disiplin ve infaz hâkimliği başvuruları. |
| `kabahatler-hukuku` | [Kabahatler Hukuku](https://turk-hukuku.com/beceriler/kabahatler-hukuku/) | Kabahatler hukuku: 5326 sayılı Kanun — idari para cezalarının genel rejimi, kabahat-suç ayrımı, idari yaptırım kararına karşı başvuru (sulh ceza hâkimliği), zamanaşımı ve iptal denetimi. |

### Kamu Hukuku — Anayasa, İdare ve Vergi

| Eklenti | Başlık | Açıklama |
|---|---|---|
| `anayasa-hukuku` | [Anayasa Hukuku](https://turk-hukuku.com/beceriler/anayasa-hukuku/) | Anayasa hukuku: temel hak ve hürriyetlerin sınırlanması rejimi (m.13), ölçülülük ve kanunilik, eşitlik ilkesi, devletin temel organları ve yetki ilişkileri; norm denetimi mantığı. |
| `anayasa-mahkemesi-bireysel-basvuru` | [AYM Bireysel Başvuru](https://turk-hukuku.com/beceriler/anayasa-mahkemesi-bireysel-basvuru/) | Anayasa Mahkemesi'ne bireysel başvuru: konu ve kişi bakımından yetki, başvuru yollarının tüketilmesi ve süre, kabul edilebilirlik kriterleri, ihlal kararı ve sonuçları; AİHM ile ilişki. |
| `idare-hukuku-genel` | [İdare Hukuku Genel](https://turk-hukuku.com/beceriler/idare-hukuku-genel/) | İdare hukuku: idari işlemin unsurları ve sakatlık halleri (yetki-şekil-sebep-konu-maksat), idari sözleşmeler, kamu hizmeti, kamulaştırma ve idarenin kusurlu/kusursuz sorumluluğu. |
| `idari-yargilama` | [İdari Yargılama Usulü (İYUK)](https://turk-hukuku.com/beceriler/idari-yargilama/) | İdari yargılama: 2577 sayılı İYUK — iptal ve tam yargı davaları, dava açma süreleri ve dava şartları (ehliyet/menfaat), yürütmenin durdurulması, idari merci tecavüzü ve istinaf/temyiz. |
| `imar-hukuku` | [İmar ve Planlama Hukuku](https://turk-hukuku.com/beceriler/imar-hukuku/) | İmar hukuku: 3194 sayılı Kanun — imar planları ve plan değişikliklerine karşı dava, yapı ruhsatı ve yapı kullanma izni, kaçak yapı ve yıkım kararları, imar para cezaları ve planlama hiyerarşisi. |
| `cevre-hukuku` | [Çevre Hukuku](https://turk-hukuku.com/beceriler/cevre-hukuku/) | Çevre hukuku: 2872 sayılı Kanun — ÇED süreci ve iptali, çevre izin ve lisansları, kirletenin sorumluluğu, idari yaptırımlar; çevresel uyuşmazlıklarda idari ve adli yargı yolları. |
| `kamu-ihale-hukuku` | [Kamu İhale Hukuku](https://turk-hukuku.com/beceriler/kamu-ihale-hukuku/) | Kamu ihale hukuku: 4734/4735 sayılı Kanunlar — ihale usulleri, yeterlik ve teklif değerlendirme, aşırı düşük teklif, şikâyet ve itirazen şikâyet (KİK), ihale sözleşmesi ve yasaklama. |
| `vergi-hukuku` | [Vergi Hukuku](https://turk-hukuku.com/beceriler/vergi-hukuku/) | Vergi hukuku: VUK genel esasları, vergiyi doğuran olay ve tarhiyat, vergi ziyaı ve usulsüzlük cezaları, uzlaşma ve düzeltme, gelir/kurumlar/KDV temel kavramları; mükellef hakları. |
| `vergi-davalari` | [Vergi Davaları](https://turk-hukuku.com/beceriler/vergi-davalari/) | Vergi yargısı: vergi/ceza ihbarnamesine ve ödeme emrine karşı dava, ihtirazi kayıtla beyan, dava açma süreleri, yürütmenin durdurulması, matrah/ceza denetimi; vergi mahkemesi-BİM-Danıştay yolu. |
| `gumruk-disticaret` | [Gümrük ve Dış Ticaret](https://turk-hukuku.com/beceriler/gumruk-disticaret/) | Gümrük ve dış ticaret: 4458 sayılı Gümrük Kanunu — gümrük rejimleri, kıymet ve menşe, ek tahakkuk ve ceza kararları, idari itiraz ve dava yolu; dış ticaret mevzuatı uyumu. |

### Yargılama, İcra ve Uyuşmazlık Çözümü

| Eklenti | Başlık | Açıklama |
|---|---|---|
| `hukuk-muhakemesi` | [Hukuk Muhakemesi (HMK)](https://turk-hukuku.com/beceriler/hukuk-muhakemesi/) | Medeni yargılama: 6100 sayılı HMK — dava şartları ve ilk itirazlar, görev ve yetki, dilekçeler ve ön inceleme, ispat yükü ve deliller, tahkikat ve hüküm, istinaf/temyiz; usul denetim şeması. |
| `icra-iflas-hukuku` | [İcra ve İflas Hukuku](https://turk-hukuku.com/beceriler/icra-iflas-hukuku/) | İcra ve iflas: 2004 sayılı İİK — ilamlı/ilamsız takip, ödeme emrine itiraz ve itirazın iptali/kaldırılması, kambiyo senetlerine özgü takip, haciz ve satış, sıra cetveli, iflas yolları. |
| `konkordato-yeniden-yapilandirma` | [Konkordato ve Yeniden Yapılandırma](https://turk-hukuku.com/beceriler/konkordato-yeniden-yapilandirma/) | Konkordato hukuku: geçici ve kesin mühlet, konkordato komiseri ve alacaklılar kurulu, projenin hazırlanması ve tasdiki, sözleşmesel yeniden yapılandırma; mali güçlük yönetimi. |
| `tahkim-arabuluculuk` | [Tahkim ve Arabuluculuk](https://turk-hukuku.com/beceriler/tahkim-arabuluculuk/) | Alternatif uyuşmazlık çözümü: iç ve milletlerarası tahkim (4686/HMK), tahkim sözleşmesi ve hakem kararının iptali/tenfizi; 6325 sayılı HUAK kapsamında ihtiyari ve dava şartı arabuluculuk. |
| `dava-dilekce-atolyesi` | [Dava Dilekçesi ve Layiha Atölyesi](https://turk-hukuku.com/beceriler/dava-dilekce-atolyesi/) | Layiha üretimi: HMK/İYUK/CMK'ya uygun dava, cevap, replik-düplik, istinaf ve temyiz dilekçeleri; vakıa-hukuki sebep-talep sonucu mimarisi, delil bağlama ve [doldurulacak] yer tutucu disiplini. |
| `hukuki-mutalaa` | [Hukuki Mütalaa ve Görüş Yazımı](https://turk-hukuku.com/beceriler/hukuki-mutalaa/) | Hukuki mütalaa ve görüş yazımı: olayın tespiti, hukuki sorunun çerçevelenmesi, mevzuat-içtihat-doktrin değerlendirmesi (altlama), seçeneklerin tartılması ve gerekçeli sonuç; risk haritası ve eylem önerisi. |

### Sektörel ve Düzenlenmiş Alanlar

| Eklenti | Başlık | Açıklama |
|---|---|---|
| `enerji-hukuku` | [Enerji Hukuku](https://turk-hukuku.com/beceriler/enerji-hukuku/) | Enerji hukuku: EPDK düzenlemesi altında elektrik/doğal gaz piyasaları, lisanslama, yenilenebilir enerji destekleri (YEKDEM), tarifeler ve düzenleyici uyum; enerji yatırım sözleşmeleri. |
| `saglik-hukuku` | [Sağlık Hukuku ve Hekim Sorumluluğu](https://turk-hukuku.com/beceriler/saglik-hukuku/) | Sağlık hukuku: hekimin hukuki/cezai sorumluluğu, aydınlatılmış onam, malpraktis-komplikasyon ayrımı, hasta hakları, ATK/bilirkişi raporu değerlendirmesi; tıbbi uyuşmazlık denetim şeması. |
| `eczacilik-ilac` | [Eczacılık ve İlaç Hukuku](https://turk-hukuku.com/beceriler/eczacilik-ilac/) | İlaç ve eczacılık hukuku: eczane açılışı ve nakli, beşeri tıbbi ürün ruhsatı, fiyatlandırma ve geri ödeme, tanıtım kuralları ve TİTCK düzenlemeleri; sektörel uyum ve uyuşmazlık. |
| `telekomunikasyon-bilisim` | [Telekomünikasyon ve Bilişim Düzenlemesi](https://turk-hukuku.com/beceriler/telekomunikasyon-bilisim/) | Telekom ve internet düzenlemesi: 5809 sayılı Kanun ve BTK yetkilendirme, 5651 kapsamında içerik/yer/erişim sağlayıcı sorumluluğu, erişim engelleme ve içerik kaldırma; düzenleyici uyum. |
| `kvkk-veri-koruma` | [Kişisel Verilerin Korunması (KVKK)](https://turk-hukuku.com/beceriler/kvkk-veri-koruma/) | KVKK uyumu: veri işleme şartları ve açık rıza, aydınlatma yükümlülüğü, VERBİS, yurt içi/yurt dışı aktarım, veri ihlali bildirimi, ilgili kişi başvurusu ve Kurul yaptırımları; uyum programı. |
| `bilisim-hukuku-siber` | [Bilişim Hukuku ve Siber Güvenlik](https://turk-hukuku.com/beceriler/bilisim-hukuku-siber/) | Bilişim hukuku: bilişim suçları (TCK m.243-245), veri ihlali ve siber olay müdahalesi, dijital delilin elde edilmesi ve değerlendirilmesi, kurumsal siber güvenlik yükümlülükleri ve hukuki sorumluluk. |
| `e-ticaret-hukuku` | [E-Ticaret Hukuku](https://turk-hukuku.com/beceriler/e-ticaret-hukuku/) | Elektronik ticaret: 6563 sayılı Kanun — hizmet/aracı hizmet sağlayıcı yükümlülükleri, ticari elektronik ileti ve İYS, mesafeli sözleşmeler ve tüketici hakları, platform düzenlemesi ve uyum. |
| `yapay-zeka-hukuku` | [Yapay Zekâ ve Veri Hukuku](https://turk-hukuku.com/beceriler/yapay-zeka-hukuku/) | Yapay zekâ hukuku: otomatik karar ve profilleme (KVKK), algoritmik şeffaflık ve sorumluluk, veri yönetişimi, AB Yapay Zekâ Tüzüğü ile karşılaştırmalı yaklaşım ve sözleşmesel risk dağıtımı. |
| `spor-hukuku` | [Spor Hukuku](https://turk-hukuku.com/beceriler/spor-hukuku/) | Spor hukuku: federasyon ve TFF düzenlemeleri, disiplin ve tahkim (Tahkim Kurulu/CAS), sporcu ve menajer sözleşmeleri, transfer ve doping; spor kulüpleri için uyuşmazlık yönetimi. |
| `basin-medya-hukuku` | [Basın ve Medya Hukuku](https://turk-hukuku.com/beceriler/basin-medya-hukuku/) | Basın ve medya hukuku: basın özgürlüğü ile kişilik hakkı dengesi, cevap ve düzeltme (tekzip), basın yoluyla kişilik hakkı ihlali ve tazminat, RTÜK düzenlemesi ve sorumluluk rejimi. |
| `goc-yabancilar-hukuku` | [Göç ve Yabancılar Hukuku](https://turk-hukuku.com/beceriler/goc-yabancilar-hukuku/) | Yabancılar ve uluslararası koruma: 6458 sayılı Kanun — ikamet izinleri, sınır dışı etme ve idari gözetim, uluslararası koruma başvurusu, çalışma izni ve vatandaşlık; idari dava yolları. |

### Büro Yönetimi ve Uygulama Araçları

| Eklenti | Başlık | Açıklama |
|---|---|---|
| `avukatlik-meslek-kurallari` | [Avukatlık Hukuku ve Meslek Kuralları](https://turk-hukuku.com/beceriler/avukatlik-meslek-kurallari/) | Avukatlık hukuku: 1136 sayılı Kanun ve meslek kuralları — sır saklama, çıkar çatışması, vekâlet sözleşmesi ve ücret, reklam yasağı, disiplin sorumluluğu; büroda uyum ve etik denetim. |
| `hukuk-burosu-yonetimi` | [Hukuk Bürosu Yönetimi](https://turk-hukuku.com/beceriler/hukuk-burosu-yonetimi/) | Hukuk bürosu işletmesi: müvekkil kabulü ve çıkar çatışması taraması, dosya ve süre yönetimi, vekâlet ücreti ve tahsilat, büro KVKK uyumu, iş akışı ve kalite kontrol panoları. |
| `dava-dosya-takip` | [Dava ve Dosya Takip Yardımcısı](https://turk-hukuku.com/beceriler/dava-dosya-takip/) | Dava dosyası işleme: yapılandırılmış dosya özeti, taraf-vekil ve süre takvimi, vakıa kronolojisi, delil dizini ve eksik/çelişki listesi; dosyaya hızlı hâkim olmayı sağlayan Excel'lenebilir çıktılar. |
| `sozlesme-inceleme-redline` | [Sözleşme İnceleme ve Redline](https://turk-hukuku.com/beceriler/sozlesme-inceleme-redline/) | Sözleşme inceleme: madde madde risk analizi, eksik/asimetrik/geçersiz şart tespiti, redline önerileri ve alternatif lafızlar, müzakere notu ve risk skoru; TBK ve emredici hükümler süzgeci. |
| `kvkk-uyum-checker` | [KVKK Uyum Denetleyicisi](https://turk-hukuku.com/beceriler/kvkk-uyum-checker/) | KVKK uyum tarayıcısı: veri işleme envanteri, aydınlatma ve açık rıza metinleri, saklama-imha politikası, aktarım ve VERBİS kontrolü; uyum boşluğu raporu ve eylem planı çıktısı. |
| `kendini-temsil-asliye` | [Kendini Temsil — Hukuk Mahkemeleri](https://turk-hukuku.com/beceriler/kendini-temsil-asliye/) | Vekille temsil edilmeyen tarafa rehber: küçük alacak ve sulh hukuk uyuşmazlıkları, tüketici hakem heyeti başvurusu, dilekçe ve delil hazırlığı, duruşma hazırlığı; hukuki danışmanlık yerine geçmez. |
| `bilirkisi-rapor-inceleme` | [Bilirkişi Raporu İnceleme](https://turk-hukuku.com/beceriler/bilirkisi-rapor-inceleme/) | Bilirkişi raporu analizi: görevlendirme kapsamına uygunluk, metodoloji ve dayanak denetimi, hesap ve maddi hata kontrolü, çelişki tespiti; gerekçeli itiraz ve ek rapor/yeni bilirkişi talebi taslağı. |
| `sade-hukuk-dili` | [Sade Hukuk Dili Çevirmeni](https://turk-hukuku.com/beceriler/sade-hukuk-dili/) | Sade hukuk dili: karmaşık dilekçe, karar ve sözleşmeleri müvekkilin anlayacağı yalın Türkçeye çevirme; hukuki doğruluğu koruyarak özetleme, terim açıklama ve bilgilendirme metni üretimi. |


## Yazar ve lisans

**Yazar / telif sahibi:** Aydın Can Polatkan

Bu proje **Apache-2.0 OR MIT** koşullarıyla sunulur. Telif © 2026 Aydın Can Polatkan.
Bkz. [`LICENSE-APACHE`](./LICENSE-APACHE), [`LICENSE-MIT`](./LICENSE-MIT), [`NOTICE`](./NOTICE).

> "Claude" Anthropic'in markasıdır; bu proje Anthropic ile resmî olarak ilişkili değildir.
