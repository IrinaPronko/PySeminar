# -*- coding: utf-8 -*-
# Реализовать дескрипторы для любых двух классов

class DescriptorRun:
    def __init__(self):
        self.__run_cap = 0

    def __get__(self, instance, owner):
        return self.__run_cap

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Величина пробега должна быть целочисленной')
        if value >= 0:
            self.__run_cap = value
            return
        raise ValueError('Показатель пробега не может быть меньше нуля')

    def __delete__(self, instance):
        del self.__run_cap


class DescriptorWork:
    def __init__(self):
        self.__worker = ' '

    def __get__(self, instance, owner):
        return self.__worker

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Некорректная фамилия водителя')
        else:
            self.__worker = value

    def __delete__(self, instance):
        del self.__worker


class Car:
    run_cap = DescriptorRun()

    def __init__(self, run_cap):
        self.run_cap = run_cap

    def __str__(self):
        return 'имеет пробег {0} км.'.format(self.run_cap)


class Worker:
    worker = DescriptorWork()

    def __init__(self, worker):
        self.worker = worker

    def __str__(self):
        return 'Автомобиль управляемый водителем {0}'.format(self.worker)


print(Worker('Громыко А.А.'), Car(40500))
print(Worker('Осауленко А.А.'), Car(30600))
exit()