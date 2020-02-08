from math import pi

try:

	print(''''The program shows the duration of the year on the planets
			It is a 0.1 version''')

	#Initialize block
	r = input('Insert the Radius of current planet is million km. (integer) ')
	v = input('Insert the orbital\'s speed (km/s) of current planet is ')

	#processing block
	r = float(r)
	v = float(v)

	r *= 1000000

	year = (2 * pi * r) / v / (60 * 60 * 24)

	#print block
	print("It is a current days: ", round(year, 2), "of planet\'s year")

except ValueError:
    print('We have some mistakes of userinput current value!')
except TypeError:
    print('We have some mistakes of userinput current type!')
except SystemError:
	print('The system mistakes are found in this program')
