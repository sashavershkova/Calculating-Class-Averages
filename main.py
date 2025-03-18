def calculate_class_averages(classrooms):
    ave_dict = {}

    for subject in classrooms:        
        all_grades = []
        if not classrooms[subject]:
            ave_dict[subject] = 0
        else:
            for student_grades in classrooms[subject].values():
                all_grades += student_grades   
        
            sum_subj_grades = sum(all_grades)
            count = len(all_grades)

            ave_dict[subject] = sum_subj_grades/count

    return ave_dict






    