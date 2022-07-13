# p0, percent, aug (inhabitants coming or leaving each year), p (population to surpass)
#
# the function nb_year should return n number of entire years needed to get a population greater or equal to p.
#
# aug is an integer, percent a positive or null floating number, p0 and p are positive integers (> 0)
def nb_year(p0, percent, aug, p):
    count = 1
    result = p0 + p0 * (percent / 100) + aug
    while result < p:
        count += 1
        result = round(result) + result * (percent / 100) + aug
    return count


print(nb_year(1000, 2.0, 50, 1214))
