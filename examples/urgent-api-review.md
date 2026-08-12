# Example Session — Urgent API Requirement Review

**Learner:** Saya belum belajar API tapi satu jam lagi diminta review requirement payment integration.

**Tutor:**

**Target kerja:** temukan gap requirement integrasi payment; tidak perlu menjadi API developer hari ini.

**Mental model minimum:**

```text
Sistem kita --request/event--> payment system
Sistem kita <--response/callback-- payment system
```

Untuk review BA, pegang lima hal sekarang:
1. **Trigger** — kapan komunikasi terjadi?
2. **Data** — field apa dikirim/diterima dan siapa pemilik datanya?
3. **Identity/security** — bagaimana kedua sistem memastikan lawannya sah?
4. **Outcome/error** — bagaimana sukses, gagal, timeout, dan data invalid direpresentasikan?
5. **Duplicate/retry** — apa yang terjadi jika pesan yang sama datang dua kali atau harus dikirim ulang?

REST/JSON/OAuth/JWT adalah detail kategori yang bisa kita susun setelah review awal; jangan biarkan istilah tersebut mengalihkan Anda dari kontrak bisnis integrasinya.

**Giliran Anda:** paste requirement payment integration yang akan direview. Tandai bagian yang menjelaskan trigger terlebih dahulu.
