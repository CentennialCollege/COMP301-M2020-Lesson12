import pandas as pd
import random


def main():
    pd.set_option('precision', 2)

    mikes_grades = []
    janes_grades = []
    thiagos_grades = []
    steves_grades = []
    josephs_grades=[]
    nushigs_grades=[]

    random.seed(46)

    for num in range(8):
        mikes_grades.append(random.randrange(50, 100))
        janes_grades.append(random.randrange(50, 100))
        thiagos_grades.append(random.randrange(50, 100))
        steves_grades.append(random.randrange(50, 100))
        josephs_grades.append(random.randrange(50, 100))
        nushigs_grades.append(random.randrange(50, 100))


    grades_dict = {"Mike": mikes_grades, "Jane": janes_grades, "Thiago":thiagos_grades, "Steve":steves_grades, 
                "Joseph":josephs_grades, "Nushig":nushigs_grades}

    grades = pd.DataFrame(grades_dict, index=['COMP391', 'COMP397', 'COMP392','COMP308', 'COMP123', 'COMP125','COMP229', 'COMP228'])

    print(grades.T)
    print('==================================================')

    COMP391 = grades.iloc[1]

    #print(COMP391)

    game_courses = grades.loc['COMP391':'COMP392']

    #print(game_courses)

    descr = grades.T.describe()

    print(descr)





if __name__ == "__main__":
    main()