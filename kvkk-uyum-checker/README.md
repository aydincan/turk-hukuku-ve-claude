# KVKK Uyum Denetleyicisi

KVKK uyum tarayıcısı: veri işleme envanteri, aydınlatma ve açık rıza metinleri, saklama-imha politikası, aktarım ve VERBİS kontrolü; uyum boşluğu raporu ve eylem planı çıktısı.

**Başat mevzuat:** 6698 KVKK

**Alan sayfası:** [turk-hukuku.com/beceriler/kvkk-uyum-checker](https://turk-hukuku.com/beceriler/kvkk-uyum-checker/) ·
Terminal kullanmıyorsanız aynı beceriler [masaüstü uygulamasında](https://turk-hukuku.com/uygulama/) da var.

## Beceriler

- `genel-bakis` — Giriş, triyaj ve yönlendirme (önce bunu çalıştırın).
- `denetim-kapsami-ve-yontem` — Bir KVKK uyum taraması başlatılırken kapsamın, denetlenecek birim ve sistemlerin, rol tespitinin ve denetim yönteminin sabitlenmesi gerektiğinde kullanılır.
- `veri-envanteri-cikarma` — Kuruluşun hangi veriyi hangi amaç ve hukuki sebeple işlediğinin haritalanması, mevcut envanterin doğrulanması veya sıfırdan envanter oluşturulması gerektiğinde kullanılır.
- `aydinlatma-acik-riza-denetimi` — Mevcut aydınlatma metinlerinin ve açık rıza beyanlarının m.10, Aydınlatma Tebliği ve Rıza Tebliği'ne uygunluğu denetlenirken ya da bu metinler taslaklanırken kullanılır.
- `saklama-imha-denetimi` — Saklama sürelerinin mevzuat dayanağına uygunluğu, imha yöntemleri ve periyodik imha düzeni denetlenirken ya da saklama-imha politikası ve süre matrisi kurulurken kullanılır.
- `aktarim-ve-verbis-denetimi` — Yurt içi/yurt dışı veri aktarım mekanizmalarının (7499 sonrası m.9) ve VERBİS kayıt yükümlülüğü ile kayıt içeriğinin doğruluğu denetlenirken kullanılır.
- `veri-guvenligi-tedbir-denetimi` — KVKK m.12 kapsamında teknik ve idari güvenlik tedbirlerinin Kurul rehberine göre denetlenmesi veya tedbir boşluklarının tespiti gerektiğinde kullanılır.
- `veri-ihlali-mudahale-hazirligi` — Kuruluşun veri ihlali müdahale planının varlığı ve yeterliliği denetlenirken, 72 saatlik Kurul bildirim ve ilgili kişi bilgilendirme süreçleri test edilirken kullanılır.
- `ilgili-kisi-basvuru-sureci-denetimi` — Kuruluşun ilgili kişi başvurularını karşılama prosedürünün m.13 ve Başvuru Tebliği'ne uygunluğu, 30 günlük yanıt süresine riayet ve şikâyete geçiş riski denetlenirken kullanılır.
- `cerez-pazarlama-uyumu` — Web sitesi çerezleri, çerez aydınlatması ve ticari elektronik ileti (İYS) süreçlerinin KVKK ve ilgili mevzuata uygunluğu denetlenirken kullanılır.
- `uyum-boslugu-raporu-eylem-plani` — Tüm denetim bulgularının tek raporda birleştirilmesi, risk önceliklendirmesi ve sorumlu-termin atanmış düzeltici eylem planı çıkarılması gerektiğinde kullanılır.

## Kullanım

```
/plugin install kvkk-uyum-checker@turk-hukuku-skills
```

Eklenti kurulduktan sonra Claude'a olayınızı anlatın ya da belgeyi yükleyin; `genel-bakis`
becerisi sizi uygun uzman beceriye yönlendirir.

---

> ⚠️ **Sorumluluk reddi:** Bu eklenti deneyseldir ve **hukuki danışmanlık değildir**.
> Çıktılar yürürlükteki mevzuat ve doğrulanmış içtihatla teyit edilmelidir. Nihai
> sorumluluk yetkili hukukçudadır. Ayrıntı için kökteki `SORUMLULUK-REDDI.md`.
