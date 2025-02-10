makanan = ["Baso", "Lomie", "Cilung", "Ramen", "Cilok", "Ayam Geprek", "Gacoan", "Pizza"]
print(makanan)
last_index_makanan = len(makanan) - 1
print(f"{makanan[last_index_makanan]} adalah data terakhir dari index makanan ")

tmp_makanan = makanan
tmp_makanan[0] = "Dimsum"

print(f"{tmp_makanan} Dimsum adalah makanan sementara yang sebelumnya adalah baso")