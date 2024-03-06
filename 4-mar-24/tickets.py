def readFile(fname: str):
    with open(fname, "r") as f:
        return f.readlines()


def main():
    fileData = readFile("input.txt")
    ticketPrices = {}
    for entry in fileData:
        data = entry.split()
        airliner = data[0].rstrip(":")
        reason = data[1].lower()
        amount = int(data[2])

        if airliner in ticketPrices:
            if reason in ["discount", "rebate"]:
                ticketPrices[airliner] -= amount
            else:
                ticketPrices[airliner] += amount
        else:
            ticketPrices[airliner] = 0
            if reason in ["discount", "rebate"]:
                ticketPrices[airliner] -= amount
            else:
                ticketPrices[airliner] += amount

    ticketPrices = {v: k for k, v in ticketPrices.items()}
    # for k, v in ticketPrices.items():
    #     print(f"{k} {v}")
    prices = ticketPrices.keys()
    sortedPrices = sorted(prices)
    print(
        f"Cheapest airline is {ticketPrices[sortedPrices[0]]} offering a price of {sortedPrices[0]} "
    )


if __name__ == "__main__":
    main()
