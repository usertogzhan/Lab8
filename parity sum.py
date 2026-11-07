"""Задача 4. Просуммировать двоичные коды по правилу чётности (сложение по модулю 2).

Запуск: python parity_sum.py
"""

WORDS = [
    "010101100011",
    "111110001100",
    "000010001010",
]


def parity_sum(*words: str) -> str:
    """Поразрядная сумма по модулю 2: в разряде 1, если единиц нечётное число."""
    if len({len(w) for w in words}) != 1:
        raise ValueError("Все слова должны быть одной длины")
    return "".join(str(sum(int(w[i]) for w in words) % 2) for i in range(len(words[0])))


def main() -> None:
    for w in WORDS:
        print(f"  {w}")
    print("  " + "-" * len(WORDS[0]))
    print(f"  {parity_sum(*WORDS)}")


if __name__ == "__main__":
    main()
