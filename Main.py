meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "Tanggapan terhadap lelucon"
            "SHEESH": "Sedikit ketidaksetujuan"
            "CREEPY": "Menakutkan, tidak menyenangkan"
            "AGGRO": "Untuk menjadi agresif/marah"
            }
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
if word in meme_dict.keys():
    print("Right")# Apa yang harus kita lakukan jika kata itu ditemukan?
else:
    print("Nope") # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
