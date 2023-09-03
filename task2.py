# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали. 
# Превратите функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов экземпляра.Задача

# Задача про акции

class EquityBasket():
    def __init__(self, name: str, quantity: int, price: int = 0, sum: int = 0, growth: int = 0, growth_share: int = 0):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.sum = sum
        self.growth = growth
        self.growth_share = growth_share

    def equity_price_and_sum_set(self, prices: dict):
        for key, values in prices.items():
            if key == self.name:
                self.price = values
                self.sum = self.quantity * values

    def growth_in_money(self, initial_prices: dict, current_prices: dict):
        self.growth = self.quantity * \
            (current_prices[self.name] - initial_prices[self.name])
        self.growth_share = round(
            (((current_prices[self.name] - initial_prices[self.name])/initial_prices[self.name])*100), 2)

    def __str__(self) -> str:
        return f'Название акции - {self.name}, количество акций - {self.quantity}, цена одной акции - \
{self.price}, общая сумма по акции - {self.sum}, рост составил - {self.growth}, рост в % - {self.growth_share}'


def max_growth_find() -> tuple:
    max = 0
    for i in range(len(list_equites)):
        if list_equites[i].growth > max:
            max = list_equites[i].growth
            max_name = list_equites[i].name
    return (max, max_name)


def portfolio_revenue_calculation() -> int:
    result = 0
    for i in range(len(list_equites)):
        result += list_equites[i].sum
    return result


if __name__ == '__main__':

    list_equites = []
    initial_prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
    current_prices = {"AAPL": 200.25, "GOOGL": 2750.75, "MSFT": 350.50}

    e1 = EquityBasket('AAPL', 30)
    e2 = EquityBasket('GOOGL', 5)
    e3 = EquityBasket('MSFT', 8)

    list_equites.append(e1)
    list_equites.append(e2)
    list_equites.append(e3)

    for i in range(len(list_equites)):
        list_equites[i].equity_price_and_sum_set(initial_prices)
        list_equites[i].equity_price_and_sum_set(current_prices)
        list_equites[i].growth_in_money(initial_prices, current_prices)


    print(e1, e2, e3, sep="\n")
    print(f'максимальный прирост - {max_growth_find()}')
    print(f'Стоимость портфеля - {portfolio_revenue_calculation()}')
