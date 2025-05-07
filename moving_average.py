closing_price_sum = 0

with open('data/spy.csv') as f:
    next(f)

    content = f.readlines()
    for line in content:
        print(line)
        tokens = line.split(",")
        close = tokens[4]

        closing_price_sum += float(close)
# 200 day MA
print(closing_price_sum / 200)
# 50 day MA
print(closing_price_sum / 50)