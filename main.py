class Acceptor:
    # инициализация
    def __init__(self, alphabet, states, initialState, endState):
        # алфавит
        self.alphabet = set(alphabet)
        # состояния
        self.states = states
        # начальное состояние
        self.initialState = initialState
        # конечное состояние
        self.endState = set(endState)

    # проверка корректного ввода
    def accept(self, u):
        cs = self.startState
        for sym in u:
            if (sym in self.alph) == False:
                return False
            cs = self.transition[cs][sym]
        return cs in self.finState

    # Удаление лишних состояний
    def removeExcess(self):
        # Преобразование алфавита
        symbols = set(self.states[1].keys())
        self.alphabet -= self.alphabet.difference(symbols)

        # Преобразование состояний
        diff = list(symbols.difference(self.alphabet))
        # Удаление элементов из состояний
        if (len(diff) > 0):
            for st in range(len(self.states)):
                for sym in diff:
                    self.states[st].pop(sym)

        # Невозможно перейти

        checked = set()  # проверянные
        unchecked = set({self.initialState})  # непроверянные

        # Множество возможных состояний
        while (True):
            if (len(unchecked) == 0):
                break;
            # до проверки проверянные
            temp = list(unchecked)
            # проверили 1 элемент
            checked.add(temp[0])
            # проверянный удаляем из непроверянного
            unchecked.remove(temp[0])
            # обновляем непроверянные состояния, не учитывая уже пройденные
            unchecked.update(set(states[temp[0]].values()).difference(checked))

        # Удаление лишних состояний
        if (len(checked) != len(self.states)):
            for key in list(states.keys()):
                # состояния нет в проверянных
                if (key in checked) == False:
                    states.pop(key)


alphabit = {'a', 'b', 'c', 'd'}

states = {1: {'a': 1, 'b': 2, 'c': 4},
          2: {'a': 1, 'b': 2, 'd': 5},
          3: {'a': 2, 'd': 4, 'c': 3},
          4: {'b': 1, 'd': 1, 'c': 1},
          5: {'a': 1, 'b': 2, 'd': 3},
          6: {'d': 3, 'b': 2, 'c': 1}}
initialState = 1

endState = {3}

print("Before")

print("States: ")
print(states)
print("Alphabet: ")
print(alphabit)

Acc = Acceptor(alphabit, states, initialState, endState)

Acc.removeExcess()

print("After")

print("States: ")
print(Acc.states)
print("Alphabet: ")
print(Acc.alphabet)

alphabit2 = {'a', 'b', '3'}

states2 = {1: {'a': 1, 'b': 2, '3': 4},
           2: {'a': 1, 'b': 2, '3': 3},
           3: {'a': 2, 'b': 4, '3': 3},
           4: {'a': 1, 'b': 1, '3': 1}}

initialState2 = 2

endState2 = {4}

print("Before2")
print("States2: ")
print(states2)
print("Alphabit2: ")
print(alphabit2)

Acc2 = Acceptor(alphabit2, states2, initialState2, endState2)

Acc2.removeExcess()

print("After2")

print("States2: ")
print(Acc2.states)
print("Alphabit2: ")
print(Acc2.alphabet)