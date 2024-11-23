import threading
import time
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name, power):
        # вызываем конструктор потока
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)

    def run(self):
        print(f'{self.name}, на нас напали!')
        counter = 100
        days = 0
        while counter:
            counter -= self.power
            days += 1
            print(f'{self.name} сражается {days} день(дня), осталось {counter} воинов. ')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {days} дней(дня).')

#создаем потоки
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
first_knight.join()

second_knight.start()
second_knight.join()

print("Все битвы закончены!")



