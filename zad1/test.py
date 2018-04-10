from fuzzy import Fuzzy

a=Fuzzy(0.7)
b=Fuzzy(0.4)

if not a:
    print('ERROR : in line 7 a should be true')

if b:
    print('ERROR : in line 10 b should be false')

Fuzzy.set_truth_threshold(3)
if Fuzzy.TRUTH_TRESHOLD>1.0:
    print('ERROR : thrut treshold set above 1')
Fuzzy.set_truth_threshold(0.3)
if not b:
    print('ERROR : in line 10 b should be true')

c=Fuzzy(23)
if c>1.0:
    print('ERROR : thrut value set above 1')

if -a!=0.3:
    print('ERROR: negation is incorrect ({})'.format(-a))

if (a|b)!=0.7:
    print('ERROR: alternative is incorrect ({})'.format(a|b))

if a&b!=0.4:
    print('ERROR: conjunction is incorrect ({})'.format(a&b))
