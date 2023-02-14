from collections import deque


food_portions = list(map(int, input().split(", ")))
stamina = deque(map(int, input().split(", ")))

#  Mountain names and the difficulty level for each.
mountain_peaks = {
"Vihren": 80,
"Kutelo": 90,
"Banski Suhodol": 100,
"Polezhan": 60,
"Kamenitza": 70,
}

#  If he manage to conquer a peak, we add it to the list below.
conquered_peaks = []

for mountain_name, difficulty in mountain_peaks.items():
    while food_portions:
        daily_food = food_portions.pop()
        daily_stamina = stamina.popleft()

        if daily_stamina + daily_food >= difficulty:
            conquered_peaks.append(mountain_name)
            break

if len(conquered_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    print('\n'.join(conquered_peaks))