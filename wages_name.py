from sys import argv

wages_name, rate_param, production_param, prize_param = argv
rate_param = int(rate_param)
production_param = int(production_param)
prize_param = int(prize_param)

print(production_param * rate_param + prize_param)
