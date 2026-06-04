# Yapay Zekâ ve Veri Hukuku

Yapay zekâ hukuku: otomatik karar ve profilleme (KVKK), algoritmik şeffaflık ve sorumluluk, veri yönetişimi, AB Yapay Zekâ Tüzüğü ile karşılaştırmalı yaklaşım ve sözleşmesel risk dağıtımı.

**Başat mevzuat:** 6698 KVKK, TBK 6098

## Beceriler

- `genel-bakis` — Giriş, triyaj ve yönlendirme (önce bunu çalıştırın).
- `temel-kavramlar-ve-sistem` — Yapay zekâ içeren bir dosyayı katman (veri-KVKK, sözleşme, sorumluluk, fikri mülkiyet, sektörel), sistemin rolü (karar destek, tam otomatik karar, üretken model, profilleme) ve tarafların sıfatı eksenlerinde konumlandırıp doğru normu ve görevli mercii belirlemek gerektiğinde kullanılır.
- `otomatik-karar-profilleme` — Bireyi etkileyen kredi skoru, işe alım eleme, sigorta fiyatlama, içerik moderasyonu gibi münhasıran otomatik kararlar ve profilleme söz konusu olduğunda KVKK m.11/1-g itiraz hakkı, hukuki dayanak ve insan denetimi gerekliliği değerlendirildiğinde kullanılır.
- `veri-yonetisim-egitim-verisi` — Bir yapay zekâ modelinin eğitiminde veya çalıştırılmasında kullanılan veri kümelerinin hukuka uygunluğu, kişisel veri içerip içermediği, kaynağı ve amaç sınırı değerlendirildiğinde ve web kazıma (scraping) ile veri toplama riski incelendiğinde kullanılır.
- `algoritmik-seffaflik-aciklanabilirlik` — İlgili kişinin veya denetçinin bir yapay zekâ kararının mantığına, kullanılan verilere ve karara dair açıklama talep etmesi durumunda aydınlatma ve bilgi verme yükümlülüğünün kapsamı ile ticari sır sınırı dengelendiğinde kullanılır.
- `yapay-zeka-sorumluluk` — Bir yapay zekâ sistemi (otonom karar, üretken çıktı, gömülü ürün) bir kişiye zarar verdiğinde geliştirici, kullanan ve veri sağlayıcı arasında sorumluluğun haksız fiil, kusursuz sorumluluk ve sözleşme temelinde dağıtılması gerektiğinde kullanılır.
- `ab-yz-tuzugu-risk-siniflandirma` — Müvekkilin yapay zekâ sistemi AB pazarına ürün veya hizmet sunduğunda ya da karşılaştırmalı uyum hedeflendiğinde AB Yapay Zekâ Tüzüğü kapsamında yasak/yüksek riskli/sınırlı risk sınıflandırması ve yükümlülükler değerlendirildiğinde kullanılır.
- `yz-sozlesmeleri-risk-dagitimi` — Yapay zekâ modeli geliştirme, lisanslama, API kullanımı, SaaS veya entegrasyon sözleşmeleri hazırlanırken ya da incelenirken sorumluluk, veri kullanımı, fikri mülkiyet, performans garantisi ve tazminat maddeleri tasarlandığında kullanılır.
- `telif-fikri-mulkiyet-yz` — Üretken yapay zekânın eğitiminde eser kullanımı, ürettiği içeriğin eser/tasarım/marka sahipliği, telif ihlali iddiası veya açık kaynak lisans uyumu gündeme geldiğinde FSEK ve SMK çerçevesinde değerlendirme yapıldığında kullanılır.
- `yz-yonetisim-uyum-programi` — Bir kurumda yapay zekâ sistemlerinin geliştirilmesi veya kullanılması için iç politika, etki değerlendirmesi, envanter, insan gözetimi ve sorumluluk yapısı kurulması istendiğinde proaktif uyum programı tasarlandığında kullanılır.
- `sektorel-yz-uygulama` — Sağlıkta klinik karar destek, bankacılıkta kredi skorlama, istihdamda işe alım eleme, sigortada fiyatlama veya kamuda otomatik işlem gibi yüksek etkili yapay zekâ kullanımlarında sektörel mevzuat ile KVKK birlikte değerlendirildiğinde kullanılır.
- `dava-usul-gorev-yetki` — Yapay zekâ kaynaklı bir uyuşmazlık yargıya veya Kurula taşınırken görevli merci, yetkili mahkeme, başvuru yolu, dava türü, ihtiyati tedbir ve süreler belirlendiğinde ve usul yol haritası çıkarıldığında kullanılır.
- `musteri-iletisim-risk-bilgilendirme` — Teknik bir yapay zekâ konusunun hukuki risklerini müvekkile yalın ve doğru biçimde anlatmak, beklenti yönetimi yapmak ve mevzuat belirsizliğini şeffafça aktarmak gerektiğinde bilgilendirme ve risk haritası üretildiğinde kullanılır.

## Kullanım

```
/plugin install yapay-zeka-hukuku@turk-hukuku-skills
```

Eklenti kurulduktan sonra Claude'a olayınızı anlatın ya da belgeyi yükleyin; `genel-bakis`
becerisi sizi uygun uzman beceriye yönlendirir.

---

> ⚠️ **Sorumluluk reddi:** Bu eklenti deneyseldir ve **hukuki danışmanlık değildir**.
> Çıktılar yürürlükteki mevzuat ve doğrulanmış içtihatla teyit edilmelidir. Nihai
> sorumluluk yetkili hukukçudadır. Ayrıntı için kökteki `SORUMLULUK-REDDI.md`.
