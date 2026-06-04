> ⚠️ Bu belge tamamen KURGUSAL ve anonimdir; gerçek bir kişi, olay veya dava ile ilgisi yoktur. Eğitim/deneme amaçlıdır.

# İhlal Kronolojisi — Ayrıntılı Zaman Çizelgesi

Aşağıdaki zaman çizelgesi, Demir Yapı Tic. A.Ş.'nin (Şirket) yaşadığı kurgusal veri ihlalinin
oluşum, tespit, müdahale ve bildirim aşamalarını saat/tarih ayrıntısıyla göstermektedir. Tüm
tarih ve saatler kurgusaldır ve örnektir.

## A. İhlal Öncesi (Açığın Oluşumu)

| Tarih / Saat | Aktör | Olay |
|--------------|-------|------|
| 02.03.2026 — — | Üçüncü taraf yazılım sağlayıcı | Yönetim panelinde kullanılan bileşen için kritik güvenlik yaması yayımlanır. |
| 02.03.2026 – 18.04.2026 | Şirket BT ekibi | Yama uygulanmaz; açık açık kalır (kök neden: yama yönetimi prosedürünün işletilmemesi). |

## B. İhlalin Gerçekleşmesi

| Tarih / Saat | Aktör | Olay |
|--------------|-------|------|
| 18.04.2026 ~03:40 | Kimliği belirsiz saldırgan(lar) | Açıktan yararlanılarak yönetim paneline yetkisiz erişim sağlanır (sonradan log analiziyle tespit edilmiştir). |
| 18.04.2026 ~03:55 | Saldırgan(lar) | Müşteri veritabanının dışa aktarımı (yaklaşık 48.500 kayıt). |
| 18.04.2026 – 09.05.2026 | — | İhlal fark edilmeden geçen dönem (~3 hafta). İzleme/SIEM uyarısı oluşmaz. |

## C. Tespit

| Tarih / Saat | Aktör | Olay |
|--------------|-------|------|
| 09.05.2026 09:12 | Bağımsız güvenlik araştırmacısı | Sızan verinin bir çevrimiçi forumda satışa çıktığını Şirket'e e-posta ile bildirir. |
| 09.05.2026 10:05 | Şirket BT / Bilgi Güvenliği | E-posta incelenir, örnek kayıtlar doğrulanır; ihlal teyit edilir (**T0 — öğrenme/teyit anı**). |

## D. İlk Müdahale (Olay Yönetimi)

| Tarih / Saat | Aktör | Olay |
|--------------|-------|------|
| 09.05.2026 10:30 | Şirket | Olay müdahale ekibi toplanır; ihlal kaydı açılır. |
| 09.05.2026 11:00 | Şirket BT | Etkilenen yönetim paneli devre dışı bırakılır, erişim anahtarları iptal edilir. |
| 09.05.2026 12:30 | Şirket BT | Açıklı bileşene güvenlik yaması uygulanır. |
| 09.05.2026 14:00 | Şirket | Tüm müşteriler için parola sıfırlama zorunluluğu getirilir. |
| 09.05.2026 15:00 | Şirket + BulutNet | Log analizi başlatılır; erişim ve sızdırma zaman aralığı belirlenir. |

## E. Bildirim Süreci

| Tarih / Saat | Aktör | Olay | İlgili Hüküm |
|--------------|-------|------|--------------|
| 12.05.2026 09:40 | Şirket | Kurum'a "Kişisel Veri İhlali Bildirim Formu" sunulur (**T0 + ~71 saat**). | KVKK m.12/5, 72 saat ilke kararı |
| 15.05.2026 10:00 | Şirket | Etkilenen ilgili kişilere e-posta bilgilendirmesi gönderilir; web sitesinde duyuru yayımlanır. | KVKK m.12/5 (ilgili kişiye bildirim) |
| 15.05.2026 10:00 | Şirket | Bilgilendirmeye oltalama (phishing) ve sosyal mühendislik uyarısı eklenir. | — |

> **Süre hesabı notu:** Teyit anı (T0) 09.05.2026 10:05 kabul edilirse, 72 saatlik süre
> 12.05.2026 ~10:05'te dolar. Bildirim 12.05.2026 09:40'ta yapıldığından **süre sınırı içinde**
> kalmış görünmektedir. Ancak "öğrenme" anının saldırganın forum ilanını yayımladığı veya
> araştırmacının e-postayı gönderdiği an (09.05.2026 09:12) olarak alınması hâlinde hesap değişir.
> Bu ayrım, savunma ve şikâyet açısından kritiktir.

## F. İlgili Kişi Başvurusu ve Şikâyet

| Tarih / Saat | Aktör | Olay | İlgili Hüküm |
|--------------|-------|------|--------------|
| 21.05.2026 — | İlgili kişi A. Yılmaz | Veri sorumlusuna yazılı başvuru: verilerinin silinmesi, alınan tedbirler hakkında bilgi ve zarar tazmini talebi. | KVKK m.11, m.13 |
| 04.06.2026 — | Şirket | A. Yılmaz'a cevap verir; alınan tedbirleri açıklar, tazminat talebini reddeder. | KVKK m.13/2 (30 günlük süre) |
| 18.06.2026 — | A. Yılmaz | Cevabı yetersiz bularak Kurul'a şikâyet dilekçesi sunar. | KVKK m.14 |

## G. Süre Özeti (T0 = 09.05.2026 10:05)

| Aşama | Geçen Süre |
|-------|------------|
| Açığın oluşması → İhlal | ~47 gün |
| İhlal → Tespit | ~21 gün |
| Tespit/teyit (T0) → Kurum'a bildirim | ~71 saat |
| Tespit/teyit (T0) → İlgili kişilere bildirim | ~6 gün |
| İlgili kişi başvurusu → Şirket cevabı | ~14 gün (30 gün sınırı içinde) |

---

*Tüm tarih, saat ve sürelerin yanı sıra kişi/şirket adları kurgusaldır. KVKK madde atıfları genel
niteliktedir; somut uygulamada güncel mevzuat ve Kurul ilke kararlarıyla doğrulanmalıdır.*
