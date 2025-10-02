import csv
import os

library = {
            "Война и мир": {
            "author": "Л. Толстой", 
            "year": 1869, 
            "ratings": [5, 4, 5]
        },
            "Преступление и наказание": {
            "author": "Ф. Достоевский", 
            "year": 1866, 
            "ratings": [5, 5, 4]
        }
}
def menu():
    print("\n" + "="*50)
    print("БИБЛИОТЕЧНАЯ СИСТЕМА")
    print("="*50)
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Найти книгу по названию")
    print("4. Удалить книгу")
    print("5. Добавить новую оценку книге")
    print("6. Книги выпущенные после определённого года")
    print("7. Книги с рейтингом выше порога")
    print("8. Экспортировать книги в CSV")
    print("9. Импортировать книги из CSV")
    print("10. Выход")
    print("="*50)

def add_book():
    try:
        title = input("Введите название книги: ").strip()
        if not title:
            print("Ошибка: название книги не может быть пустым!")
            return
        
        if title in library:
            print("Ошибка: книга с таким названием уже существует!")
            return
        
        author = input("Введите автора книги: ").strip()
        if not author:
            print("Ошибка: поле автор не может быть пустым!")
            return
        
        year = int(input("Введите год издания: "))
        if year < 0 or year > 2025:
            print("Ошибка: некорректный год!")
            return
        
        ratings_input = input("Введите оценки через запятую (макс. 5): ").strip()
        if ratings_input:
            ratings = [int(r.strip()) for r in ratings_input.split(",")]
            for rating in ratings:
                if rating < 1 or rating > 5:
                    print("Ошибка: оценки должны быть от 1 до 5!")
                    return
        else:
            ratings = []
        
        library[title] = {
            "author": author,
            "year": year,
            "ratings": ratings
        }
        print(f"Книга '{title}' успешно добавлена!")
        
    except ValueError:
        print("Ошибка: некорректный формат данных!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def show_all_books():
    if not library:
        print("Библиотека пуста!")
        return
    print("\nСПИСОК ВСЕХ КНИГ:")
    print("-" * 80)
    print(f"{'Название':<30} {'Автор':<20} {'Год':<6} {'Рейтинг':<8} {'Оценок':<6}")
    print("-" * 80)
    
    for title, info in sorted(library.items(), key=lambda x: x[0]):
        ratings = info["ratings"]
        avg_rating = sum(ratings) / len(ratings) if ratings else 0
        rating_count = len(ratings)
        print(f"{title:<30} {info['author']:<20} {info['year']:<6} {avg_rating:<8.2f} {rating_count:<6}")
    
    print("-" * 80)
    print(f"Всего книг: {len(library)}")

def find_book():
    search_title = input("Введите название книги для поиска: ").strip()
    
    for title, info in library.items():
        if search_title.lower() in title.lower():
            ratings = info["ratings"]
            avg_rating = sum(ratings) / len(ratings) if ratings else "Нет оценок"
            rating_count = len(ratings)
            
            print(f"\nНайдена книга:")
            print(f"Название: {title}")
            print(f"Автор: {info['author']}")
            print(f"Год: {info['year']}")
            print(f"Количество оценок: {rating_count}")
            print(f"Средний рейтинг: {avg_rating}")
            if ratings:
                print(f"Все оценки: {', '.join(map(str, ratings))}")
            break
    else:
        print("Книга не найдена")

def delete_book():
    title = input("Введите название книги для удаления: ").strip()
    
    for book_title in library.keys():
        if title.lower() == book_title.lower():
            del library[book_title]
            print(f"Книга '{book_title}' успешно удалена!")
            break
    else:
        print("Книга не найдена")

def add_rating():
    title = input("Введите название книги: ").strip()
    
    for book_title, info in library.items():
        if title.lower() == book_title.lower():
            try:
                rating = int(input("Введите оценку (1-5): "))
                if rating < 1 or rating > 5:
                    print("Ошибка: оценка должна быть от 1 до 5!")
                    return
                
                info["ratings"].append(rating)
                print(f"Оценка {rating} добавлена к книге '{book_title}'!")
                break
            except ValueError:
                print("Ошибка: введите число!")
                return
    else:
        print("Книга не найдена")

def books_after_year():
    try:
        year = int(input("Введите год: "))
        found_books = []
        
        for title, info in library.items():
            if info["year"] > year:
                found_books.append((title, info))
        
        if found_books:
            print(f"\nКниги выпущенные после {year} года:")
            print("-" * 60)
            for title, info in sorted(found_books, key=lambda x: x[1]["year"]):
                print(f"{title} - {info['author']} ({info['year']})")
            print(f"Найдено книг: {len(found_books)}")
        else:
            print(f"Книг выпущенных после {year} года не найдено")
            
    except ValueError:
        print("Ошибка: введите корректный год!")

def books_above_rating():
    try:
        threshold = float(input("Введите минимальный рейтинг (0-5): "))
        if threshold < 0 or threshold > 5:
            print("Ошибка: рейтинг должен быть от 0 до 5!")
            return
        
        found_books = []
        
        for title, info in library.items():
            ratings = info["ratings"]
            if ratings:
                avg_rating = sum(ratings) / len(ratings)
                if avg_rating >= threshold:
                    found_books.append((title, info, avg_rating))
        
        if found_books:
            print(f"\nКниги с рейтингом выше {threshold}:")
            print("-" * 70)
            for title, info, rating in sorted(found_books, key=lambda x: x[2], reverse=True):
                print(f"{title} - {info['author']} (Рейтинг: {rating:.2f})")
            print(f"Найдено книг: {len(found_books)}")
        else:
            print(f"Книг с рейтингом выше {threshold} не найдено")
            
    except ValueError:
        print("Ошибка: введите число!")

def export_to_csv():
    try:
        filename = input("Введите имя файла для экспорта (без расширения): ").strip()
        if not filename:
            filename = "library"
        
        filename = f"{filename}.csv"
        
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['название', 'автор', 'год', 'оценки'])
            
            for title, info in library.items():
                ratings_str = ','.join(map(str, info['ratings']))
                writer.writerow([title, info['author'], info['year'], ratings_str])
        
        print(f"Данные успешно экспортированы в файл '{filename}'")
        
    except Exception as e:
        print(f"Ошибка при экспорте: {e}")

def import_from_csv():
    try:
        filename = input("Введите имя файла для импорта: ").strip()
        if not filename.endswith('.csv'):
            filename += '.csv'
        
        if not os.path.exists(filename):
            print("Файл не найден!")
            return
        
        imported_count = 0
        skipped_count = 0
        
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)  # Пропускаем заголовок
            
            for row in reader:
                if len(row) != 4:
                    continue
                
                title, author, year, ratings_str = row
                
                if title in library:
                    skipped_count += 1
                    continue
                
                try:
                    year = int(year)
                    ratings = [int(r) for r in ratings_str.split(',')] if ratings_str else []
                    
                    # Проверка оценок
                    for rating in ratings:
                        if rating < 1 or rating > 5:
                            ratings = []
                            break
                    
                    library[title] = {
                        "author": author,
                        "year": year,
                        "ratings": ratings
                    }
                    imported_count += 1
                    
                except ValueError:
                    skipped_count += 1
        
        print(f"Импорт завершен!")
        print(f"Добавлено книг: {imported_count}")
        print(f"Пропущено книг: {skipped_count}")
        
    except FileNotFoundError:
        print("Файл не найден!")
    except Exception as e:
        print(f"Ошибка при импорте: {e}")

def save_data():
    try:
        with open('library_backup.txt', 'w', encoding='utf-8') as file:
            for title, info in library.items():
                ratings_str = ','.join(map(str, info['ratings']))
                file.write(f"{title};{info['author']};{info['year']};{ratings_str}\n")
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")
    else:
        print("Данные успешно сохранены!")
    finally:
        print("Завершение работы программы...")

def main():
    print("Добро пожаловать в библиотечную систему!")
    
    while True:
        menu()
        
        try:
            choice = input("Выберите действие (1-10): ").strip()
            
            if choice == '10':
                save_data()
                break
            elif choice == '1':
                add_book()
            elif choice == '2':
                show_all_books()
            elif choice == '3':
                find_book()
            elif choice == '4':
                delete_book()
            elif choice == '5':
                add_rating()
            elif choice == '6':
                books_after_year()
            elif choice == '7':
                books_above_rating()
            elif choice == '8':
                export_to_csv()
            elif choice == '9':
                import_from_csv()
            else:
                print("Неверный выбор! Попробуйте снова.")
        
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем")
            save_data()
            break
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":

    main()
