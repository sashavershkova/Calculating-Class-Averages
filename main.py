def calculate_class_averages(classrooms):
    class_averages = {}

    for classroom, students in classrooms.items():
    
        if not students:
            class_averages[classroom] = 0
            continue
        
        scores = 0
        num_grades = 0

        for grades in students.values():
            if not grades:
                continue
            
            for grade in grades:
                scores += grade
                num_grades += 1

        avg = scores / num_grades
        class_averages[classroom] = avg
    
    return class_averages