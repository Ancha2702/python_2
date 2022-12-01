participant_count = int(input("Количество игроков:"))
stop_interval = int(input("Номер игрока, на котором закончить счет:"))
# participant_count = 4
# stop_interval = 2
coins = [0] * participant_count
statuses = [True] * len(coins)

def print_participants_info(coins, statuses, iteration_number):
    print('\nРАУНД:', iteration_number)
    print('№  Статус  Монет')
    for j, element in enumerate(coins):
        status = 'играю' if statuses[j] else 'выбыл'
        print(j, '', status, " ", element)

def give_extra_coins(coins, statuses, stop_index, last_stop_index):
    for j, element in enumerate(coins):
        if statuses[j]:
            if last_stop_index > stop_index:
                if j <= stop_index or j > last_stop_index:
                    coins[j] += 1
                else:
                    coins[j] += 2
            else:
                if j <= last_stop_index or j > stop_index:
                    coins[j] += 2
                else:
                    coins[j] += 1

can_continue = True
enabled_count = 0
coin_buffer = 0
iteration_number = 0
last_stop_index = len(coins) - 1

while can_continue:
    can_continue = False
    for i in range(len(statuses)):
        if statuses[i]:
            enabled_count += 1  # увеличиваем счетчик посчитанных активных участников
            if coin_buffer > 0:  # если есть монетки, которые мы отобрали у предыдущего выбывшего участника...
                coins[i] += coin_buffer  # ...то мы их отдаем следующему активному после выбывшего участнику
                coin_buffer = 0  # сбрасываем буфер, т.к. монетки мы уже отдали
                iteration_number += 1
                print_participants_info(coins, statuses, iteration_number)
        if enabled_count == stop_interval:  # остановили счет на определенном участнике
            give_extra_coins(coins, statuses, i, last_stop_index)  # начисляем монетки по правилам игры
            statuses[i] = False  # делаем участника выбывшим
            coin_buffer += coins[
                i]  # сложили монетки выбывшего участника в буфер, чтобы потом их передать следующему активному участнику
            coins[i] = 0  # отобрали монетки у выбывшего участника
            enabled_count = 0  # сбросили счетчик активных участников
            last_stop_index = i  # запомнили индекс выбывшего участника для начисления монеток согласно правилам при каждой итерации

    can_continue = statuses.count(True) > 1 or coin_buffer > 0  #
    continue_index = 0
