from idlelib.replace import replace

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace(" .... ", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
litera_h = adwentures_of_tom_sawer.count("h")
print(litera_h)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
adwentures_of_tom_sawer_bez_krapky = adwentures_of_tom_sawer

for char in [".", ",", "!", "?", "-", ":", ";", "(", ")"]:
    adwentures_of_tom_sawer_bez_krapky = adwentures_of_tom_sawer_bez_krapky.replace(char, " ")

slova = adwentures_of_tom_sawer_bez_krapky.split()

count = 0

for word in slova:
    if word[0].isalpha() and word[0].isupper():
        count += 1

print(f"Кількість слів, що починаються з великої літери: {count}")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
tom_x1 = adwentures_of_tom_sawer.find("Tom")
tom_x2 = adwentures_of_tom_sawer.find("Tom", tom_x1 + 1)
print(tom_x2)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
for char in ["!", "?"]:
    adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace(char, ".")

adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
rechennya_4 = adwentures_of_tom_sawer_sentences[3].strip().lower()
print(rechennya_4)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip().startswith("By the time"):
        print(True)
        break
else:
    print(False)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip():
        sliv_v_ostannyomu_rechenny = sentence.strip()

words = sliv_v_ostannyomu_rechenny.split()

print(len(words))
print("зміна для пулл реквесту")