import pandas as pd
import os


def process_files(in_file, out_file):
    try:
        # Перевірка чи файл взагалі існує перед відкриттям
        if not os.path.exists(in_file):
            raise FileNotFoundError(f"Файл {in_file} не знайдено у директорії.")

        # Читання CSV файлу
        data = pd.read_csv(in_file, na_values='..')

        # --- НАЛАШТУВАННЯ ВІДОБРАЖЕННЯ ---
        pd.set_option('display.max_rows', None)
        # Встановлюємо максимальну кількість стовпців
        pd.set_option('display.max_columns', None)
        # Налаштовуємо ширину екрана, щоб рядки не переносилися
        pd.set_option('display.width', 1000)
        # --------------------------------

        # 1. Виведення ВСЬОГО вмісту вхідного файлу на екран
        print("--- ПОВНИЙ вміст вхідного файлу ---")
        print(data.to_string())
        print("\n" + "=" * 60 + "\n")

        # 2. Логіка обробки: запит країн від користувача
        user_input = input("Введіть назви країн для пошуку через кому (наприклад: Ukraine, Poland): ")
        countries_to_search = [name.strip() for name in user_input.split(',')]

        # 3. Пошук даних
        filtered_data = data[data['Country Name'].isin(countries_to_search)].copy()
        columns_to_keep = ['Country Name', 'Country Code', '2018 [YR2018]', '2019 [YR2019]']

        available_columns = [col for col in columns_to_keep if col in filtered_data.columns]
        result_df = filtered_data[available_columns]

        # 4. Виведення результату пошуку
        if not result_df.empty:
            print("\n--- Результати пошуку ---")
            print(result_df.to_string())

            # 5. Збереження
            result_df.to_csv(out_file, index=False, encoding='utf-8-sig')
            print(f"\n[УСПІХ] Дані збережено у {out_file}")
        else:
            print("\n[УВАГА] Нічого не знайдено.")

    except Exception as e:
        print(f"Помилка: {e}")


# Виклик програми
input_filename = "d6871d0d-5b97-4b4e-8f28-027ceb906dda_Data.csv"
output_filename = "Звіт_країн.csv"

process_files(input_filename, output_filename)