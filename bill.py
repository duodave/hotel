# Number of nights of the stay.
#nights = 4
nights = int(input('Number of nights for your hotel stay: '))

# Nightly hotel rate for this room.
#rate = 108
rate = float(input('Nightly hotel rate: '))

# Indianapolis hotel tax rate of %17:
taxes = 0.17

# Incidentals are things like room service or buying movies, charged in advance as a hold.
# Any remainder is refunded a few days after the stay.
incid = 25

# Calculate what the taxes are, per night
totaltaxes = rate * taxes

# The bill before the incidentals, including taxes
nightlybill = rate + totaltaxes



print("Your room rate is: $%.2f." % (rate))
print("The taxes on your room will be %%%s, or $%.2f" % (int(taxes*100), totaltaxes))

print("The up front bill will be: $%.2f." % (nightlybill * nights + incid * nights))
print("You will be refunded $%s for a total bill of %.2f." % (incid * nights, nightlybill * nights))