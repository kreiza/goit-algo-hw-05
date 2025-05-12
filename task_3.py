import timeit

# --- Алгоритми пошуку ---
def rabin_karp(text, pattern):
    d, q = 256, 101
    M, N = len(pattern), len(text)
    h = pow(d, M - 1, q)
    p = t = 0

    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for s in range(N - M + 1):
        if p == t and text[s:s + M] == pattern:
            return True
        if s < N - M:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + M])) % q
            t = (t + q) % q
    return False

def boyer_moore(text, pattern):
    m = len(pattern)
    skip = {c: m for c in set(text)}
    for i in range(m - 1):
        skip[pattern[i]] = m - i - 1

    i = 0
    while i <= len(text) - m:
        j = m - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return True
        i += skip.get(text[i + m - 1], m)
    return False

# --- Неоптимізований KMP ---
def kmp_search(text, pattern):
    # Працює правильно, але дуже повільно для великих обсягів тексту
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    i += 1
        return lps

    lps = build_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return True
        elif i < len(text) and pattern[j] != text[i]:
            j = lps[j - 1] if j != 0 else 0
    return False

def read_file_with_encoding(path):
    import chardet
    with open(path, 'rb') as f:
        raw = f.read()
        encoding = chardet.detect(raw)['encoding']
    return raw.decode(encoding)

def benchmark_fast(text, name, pattern, fake_pattern):
    results = []
    for alg_name, alg_func in [
        ("Рабін-Карп", rabin_karp),
        ("Бойєр-Мур", boyer_moore)
    ]:
        real_time = timeit.timeit(lambda: alg_func(text, pattern), number=1)
        fake_time = timeit.timeit(lambda: alg_func(text, fake_pattern), number=1)
        results.append((name, alg_name, real_time, fake_time))
    return results

if __name__ == "__main__":
    pattern = "алгоритм"
    fake_pattern = "хмаробілет"

    text1 = read_file_with_encoding("стаття 1.txt")[:10000]
    text2 = read_file_with_encoding("стаття 2 (1).txt")[:10000]

    results = benchmark_fast(text1, "Стаття 1", pattern, fake_pattern)
    results += benchmark_fast(text2, "Стаття 2", pattern, fake_pattern)

    print("\nРезультати порівняння:\n")
    for entry in results:
        print(f"{entry[0]:10} | {entry[1]:10} | Існуючий: {entry[2]:.6f} с | Вигаданий: {entry[3]:.6f} с")