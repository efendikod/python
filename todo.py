# To-Do List uygulaması

# Görevleri saklayacak liste
tasks = []

# Görev ekleme fonksiyonu
def add_task(task):
    tasks.append(task)
    print(f"'{task}' görevi eklendi.")

# Görev silme fonksiyonu
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"'{task}' görevi silindi.")
    else:
        print(f"'{task}' görevi listede bulunamadı.")

# Görevleri listeleme fonksiyonu
def list_tasks():
    if tasks:
        print("Görev Listesi:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("Görev listesi boş.")

# Ana fonksiyon
def main():
    while True:
        print("\n1. Görev Ekle")
        print("2. Görev Sil")
        print("3. Görevleri Listele")
        print("4. Çıkış")
        
        choice = input("Seçiminiz (1-4): ")
        
        if choice == '1':
            task = input("Eklemek istediğiniz görevi girin: ")
            add_task(task)
        elif choice == '2':
            task = input("Silmek istediğiniz görevi girin: ")
            remove_task(task)
        elif choice == '3':
            list_tasks()
        elif choice == '4':
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen 1-4 arasında bir değer girin.")

# Programı çalıştırma
if __name__ == "__main__":
    main()
