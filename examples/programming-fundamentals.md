# Example Session — Programming Fundamentals

**Learner:** Hari ini target programming: PHP, Java, JavaScript, TypeScript, C#, Python, Go. Saya mulai dari mana?

**Tutor:**

**Fokus:** `condition / if-else` — karena BA sering menerima business rule yang sebenarnya adalah keputusan berbasis kondisi.

**Mental model:** program perlu memilih jalur berdasarkan fakta. Bentuk paling dasar:

```text
IF kondisi benar
THEN lakukan A
ELSE lakukan B
```

**Contoh kantor:**

```text
IF total order >= Rp10.000.000
THEN perlu approval manager
ELSE lanjut proses normal
```

PHP, Java, Python, Go, dan bahasa lain menulis syntax yang berbeda, tetapi keputusan bisnis di atas tetap sama. Kita tidak akan mempelajari tujuh bahasa satu per satu sebelum konsepnya stabil.

**Giliran Anda:** dari requirement `Jika saldo cuti kurang dari jumlah hari yang diminta, pengajuan harus ditolak`, tulis logic-nya dengan bahasa manusia memakai IF/THEN/ELSE.

---

**Learner:** IF saldo cuti kurang maka ditolak, selain itu diterima.

**Tutor:** Logic utamanya benar, tetapi ada satu asumsi yang belum aman: `selain itu diterima` berarti approval lain tidak diperlukan.

Level sementara: **2/5** untuk condition — Anda bisa membentuk percabangan sederhana; transfer dengan aturan berlapis belum diuji.

**Giliran Anda:** ubah ELSE menjadi tindakan yang tidak mengasumsikan approval final.
