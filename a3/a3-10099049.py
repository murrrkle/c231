# CPSC 231 ASSIGNMENT THREE: Histogram for Grade Distribution                                                               Coded by 10099049; Michael Hung

######################################################################## functions ########################################################################


#  The following two functions are shortcuts for instructing the QuickDraw program on what to draw.

def draw_line(xA, yA, xB, yB):
    print('line', xA, yA, xB, yB)
    

def text(string, x, y):
    print('text', string, x, y)
    

# 'stats' calculates the test score averages, the maximum and minimum grades achieved by the students, the median, and the standard deviation of the grades.

def stats(grades):

    mean, max_grade, min_grade, median = float('%.3f' % (sum(grades) / len(grades))), max(grades), min(grades), sorted(grades)[len(grades) // 2]

    dev = []
    for grade in grades:
        dev += [(grade - mean) ** 2]
    st_dev = float('%.3f' % (sum(dev) / (len(dev))) ** 0.5)
    
    return (mean, max_grade, min_grade, median, st_dev)



# 'A1_extract' takes all grades under the 'A1' category in the file 'grades.txt' and appends them into a separate list as floating-point numbers.

def A1_extract(file):

    A1_grd = []
    
    for i in file:
        if i != 'EOF':
            A1_grd += [float(i.split(', ')[5])]

    return A1_grd



# 'percentiles' is meant to be used in conjunction with 'A1_extract'. It takes the extracted grades and sorts them into a list
#  describing how many students fall under specific grade parameters: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10.

def percentiles(grades):

    A1_0, A1_1, A1_2, A1_3, A1_4, A1_5, A1_6, A1_7, A1_8, A1_9, A1_10 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    for i in grades:
            
        if i >= 0 and i < 1:
            A1_0 += 1
        
        elif i >= 1 and i < 2:
            A1_1 += 1
        
        elif i >= 2 and i < 3:
            A1_2 += 1

        elif i >= 3 and i < 4:
            A1_3 += 1

        elif i >= 4 and i < 5:
            A1_4 += 1

        elif i >= 5 and i < 6:
            A1_5 += 1

        elif i >= 6 and i < 7:
            A1_6 += 1

        elif i >= 7 and i < 8:
            A1_7 += 1

        elif i >= 8 and i < 9:
            A1_8 += 1

        elif i >= 9 and i < 10:
            A1_9 += 1

        elif i == 10:
            A1_10 += 1

    return [A1_0, A1_1, A1_2, A1_3, A1_4, A1_5, A1_6, A1_7, A1_8, A1_9, A1_10]



# 'histogram' uses 'A1_extract' and 'percentiles' for the calculations necessary to represent the A1 grades in histogram format.
# 'stats' is also incorporated for putting the statistics information directly onto the histogram. The values chosen for drawing
#  and labelling were chosen to optimize the histogram for an 800 x 600 window.

def histogram(grades):
    
    A1_distr = percentiles(grades)
    
    max_l = max(A1_distr)
    ratio = 300 / max_l
    base = 400
    origin = 100

    mean, max_grd, min_grd, median, st_dev = stats(grades)

    draw_line(origin - 50, 34, origin - 50, base)                                       # Drawing and labelling the x- and y-axes.
    draw_line(origin - 50, base, 700, base)
    text('number', origin - 89, 20)
    text('grade', 710, base + 4)
    
    for i in range(len(A1_distr)):                                                      # Drawing the data bars.
        
        draw_line(origin + i * 50, base, origin + i * 50, base - A1_distr[i] * ratio)
        draw_line(origin + i * 50 + 20, base, origin + i * 50 + 20, base - A1_distr[i] * ratio)
        draw_line(origin + i * 50, base - A1_distr[i] * ratio, origin + i * 50 + 20, base - A1_distr[i] * ratio)
        
        for j in range(10, 70, 10):                                                     # Drawing and labelling x-increments.
            draw_line(origin - 55, base - j * ratio, origin - 50, base - j * ratio)
            text(j, origin - 75, base - j * ratio + 5)

        for j in range(100, 650, 50):                                                   # Drawing y-increments.
            draw_line(j + 10, base + 5, j + 10, base)

        for j in range(1, 12):                                                          # Labelling y-increments.
            text(j - 1 , j * 49.6 + 58, base + 25)

    text('mean=' + str(mean), 50, 470)                                                  # These last five lines superimpose the
    text('min=' + str(min_grd), 50, 490)                                                # statistics information onto the histogram.
    text('max=' + str(max_grd), 50, 510)
    text('median=' + str(median), 50, 530)
    text('standard_deviation=' + str(st_dev), 50, 550)


###########################################################################################################################################################

file = open('grades.txt', 'r')
s = file.readline()

histogram((A1_extract(file)))
