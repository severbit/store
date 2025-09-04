import json
from typing import Literal, List, Dict, Any

def find(input_str: str, method: Literal["name", "code"]) -> List[Dict[str, Any]]:
    try:
        print(f"🔍 Поиск: '{input_str}' методом: '{method}'")
        
        # Чтение файла
        with open("./app/data.json", "r", encoding="utf-8") as file:
            products = json.load(file)
        
        print(f"📊 Загружено продуктов: {len(products)}")
        if products:
            print(f"📋 Первый продукт: {products[0]}")
        
        res = []
        search_term = input_str.lower().strip()
        print(f"🔎 Ищем: '{search_term}'")
        
        for i, product in enumerate(products):
            try:
                if not isinstance(product, dict):
                    print(f"❌ Продукт #{i} не словарь: {product}")
                    continue
                
                if method == "name":
                    if "name" not in product:
                        print(f"⚠️ Продукт #{i} нет ключа 'name'")
                        continue
                    
                    product_name = product["name"]
                    if not isinstance(product_name, str):
                        product_name = str(product_name)
                        print(f"ℹ️ Продукт #{i} имя преобразовано в строку")
                    
                    if search_term in product_name.lower():
                        print(f"✅ Найдено совпадение в продукте #{i}: {product_name}")
                        res.append(product)
                
                elif method == "code":
                    # Проверяем все возможные ключи для кода
                    code_keys = ["pin_code", "code", "product_code", "sku", "id"]
                    found_code = None
                    
                    for key in code_keys:
                        if key in product:
                            code_value = product[key]
                            if isinstance(code_value, str) and code_value.strip():
                                found_code = code_value.lower()
                                break
                            elif isinstance(code_value, (int, float)):
                                found_code = str(code_value).lower()
                                break
                    
                    if not found_code:
                        print(f"⚠️ Продукт #{i} не содержит код")
                        continue
                    
                    if search_term in found_code:
                        print(f"✅ Найдено совпадение кода в продукте #{i}: {found_code}")
                        res.append(product)
                        
            except Exception as e:
                print(f"❌ Ошибка в продукте #{i}: {e}")
                continue
        
        print(f"🎯 Итоговый результат: {len(res)} товаров")
        return res

    except FileNotFoundError:
        print("❌ Файл data.json не найден!")
        return []
    except json.JSONDecodeError:
        print("❌ Ошибка формата JSON!")
        return []
    except Exception as e:
        print(f"❌ Неизвестная ошибка: {e}")
        return []

# Тестируем
print("=" * 50)
results = find("На", "name")
print("=" * 50)
print(f"Финальный результат: {results}")