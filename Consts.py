URL_ORG = "https://www.ryanair.com/api/locate/v1/autocomplete/airports?" \
             "&phrase=" \
             "&market=en-gb"

URL_DST = "https://www.ryanair.com/api/locate/v1/autocomplete/routes?" \
                  "&arrivalPhrase=" \
                  "&departurePhrase=#ORG" \
                  "&market=en-gb"

URL_DATE = "https://www.ryanair.com/api/farfnd/3/oneWayFares/#ORG/#DST/availabilities"

# API from task was not available to used other one :
# https://gist.github.com/vool/bbd64eeee313d27a82ab
URL_PRICE = "https://services-api.ryanair.com/farfnd/3/oneWayFares?" \
            "&departureAirportIataCode=#ORG" \
            "&arrivalAirportIataCode=#DST" \
            "&language=en" \
            "&limit=" \
            "&market=en-gb" \
            "&offset=0" \
            "&outboundDepartureDateFrom=#DATE" \
            "&outboundDepartureDateTo=#DATE" \
            "&priceValueTo="

KW_ORG = "#ORG"
KW_DST = "#DST"
KW_DATE = "#DATE"
