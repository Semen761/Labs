words = ["python", "Java", "c++", "Rust", "go"]
# Делаем слова большими буквами и берем только длиннее 3 букв
big_words = [word.upper() for word in words if len(word) > 3]
print(big_words)