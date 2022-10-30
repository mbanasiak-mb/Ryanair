import matplotlib.pyplot as plt
import numpy as np

from Functions import *

# --------------------------------------------------------------------------------


def get_dates_prices(org: str, dst: str):
    dates = get_dates(org, dst)

    # TODO: Collect separate data for min. / max. / avg.
    px = []
    py = []
    currency = ''

    print(">    Collecting data ...")
    for date in dates:
        x = str(date)

        fares = get_prices(org, dst, x)
        for fare in fares['fares']:
            value = int(fare['summary']['price']['value'])

            # TODO: The currency should be taken in other way ...
            currency = fare['summary']['price']['currencyCode']
            # print(f"$ : {value} {currency}")

            px.append(x)
            py.append(value)
    print(">    Data collected.")
    return px, py, currency


def get_airport_num(min: int, max: int):
    while True:
        c = input(">    Enter input:\n")
        try:
            v = int(c)
            if min <= v < max:
                return v
            else:
                raise ValueError
        except:
            print(">    Incorrect input.")

# --------------------------------------------------------------------------------


airports_org = get_airports_org()
airports_org_count = len(airports_org)


def REPL():
    while True:

        # ---------- Print origin

        print(">    ")
        for i, airport in enumerate(airports_org):
            print(f"{i} : {airport['name']}")

        print(">    Choose airport origin (#ORG) number :")

        # ---------- Get origin num / code

        numOrg = get_airport_num(0, airports_org_count)
        codeOrg = airports_org[numOrg]['code']

        airports_dst = get_airports_dst(codeOrg)
        airports_dst_count = len(airports_dst)

        # ---------- Print destination

        if airports_dst_count < 1:
            print(">    Airport destination is not available, choose other origin airport.")

        # ---------- Print destination

        print(">    ")
        for i, airport in enumerate(airports_dst):
            print(f"{i} : {airport['arrivalAirport']['name']}")

        print(">    Choose airport destination (#DST) number :")

        # ---------- Get destination num / code

        numDst = get_airport_num(0, airports_dst_count)
        codeDst = airports_dst[numDst]['arrivalAirport']['code']

        # ---------- Get and plot data

        px, py, currency = get_dates_prices(codeOrg, codeDst)

        px = np.array(px, dtype='datetime64')
        py = np.array(py, dtype='int')
        px = np.sort(px)
        py = np.sort(py)

        # TODO: Data can be plotted as dots or as line --> '.k' / '-k'
        plt.plot(px, py, '.k')
        plt.ylabel(f"Currency : {currency}")
        plt.xlabel("Datetime")
        plt.grid(True)
        plt.show()


if __name__ == '__main__':
    REPL()
