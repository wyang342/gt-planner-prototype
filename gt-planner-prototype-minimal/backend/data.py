default_curriculums = {
    'ME': {
        'CHEM 1310': {'prqs': [], 'year': 1, 'done': False, 'immediacy': 0},
        'MATH 1551': {'prqs': [], 'year': 1, 'done': False, 'immediacy': 0},
        'MATH 1553': {'prqs': [], 'year': 1, 'done': False, 'immediacy': 0},
        'Legislative': {'prqs': [], 'year': None, 'done': False, 'immediacy': 0},
        'ENGL 1101': {'prqs': [], 'year': 1, 'done': False, 'immediacy': 0},
        'Wellness': {'prqs': [], 'year': None, 'done': False, 'immediacy': 0},
        'PHYS 2211': {'prqs': ['MATH 1552*'], 'year': 2, 'done': False, 'immediacy': 2},
        'MATH 1552': {'prqs': ['MATH 1551'], 'year': 1, 'done': False, 'immediacy': 1}, 'CS 1371': {'prqs': [], 'year': 1, 'done': False, 'immediacy': 0},
        'ME 1670': {'prqs': [], 'year': 1, 'done': False, 'immediacy': 0},
        'ENGL 1102': {'prqs': ['ENGL 1101'], 'year': 1, 'done': False, 'immediacy': 1},
        'PHYS 2212': {'prqs': ['PHYS 2211'], 'year': 2, 'done': False, 'immediacy': 3},
        'MATH 2551': {'prqs': ['MATH 1552', 'MATH 1553'], 'year': 2, 'done': False, 'immediacy': 2},
        'ME 2110': {'prqs': ['ME 1670', 'COE 2001'], 'year': 2, 'done': False, 'immediacy': 4},
        'MSE 2001': {'prqs': ['CHEM 1310'], 'year': 2, 'done': False, 'immediacy': 1},
        'COE 2001': {'prqs': ['MATH 1552', 'PHYS 2211'], 'year': 2, 'done': False, 'immediacy': 3}, 
        'ECE 3710': {'prqs': ['PHYS 2212'], 'year': 3, 'done': False, 'immediacy': 4},
        'MATH 2552': {'prqs': ['MATH 1552', 'MATH 1553'], 'year': 2, 'done': False, 'immediacy': 2},
        'ME 2016': {'prqs': ['MATH 1553', 'MATH 2552*', 'CS 1371'], 'year': 2, 'done': False, 'immediacy': 3},
        'ME 2202': {'prqs': ['COE 2001', 'MATH 1553*'], 'year': 2, 'done': False, 'immediacy': 4},
        'Social Science': {'prqs': [], 'year': None, 'done': False, 'immediacy': 0},
        'ECE 3741': {'prqs': ['ECE 3710'], 'year': 3, 'done': False, 'immediacy': 5},
        'COE 3001': {'prqs': ['COE 2001', 'MATH 2552*'], 'year': 3, 'done': False, 'immediacy': 4},
        'ME 3322': {'prqs': ['PHYS 2211', 'MATH 2552'], 'year': 3, 'done': False, 'immediacy': 3},
        'ME 3340': {'prqs': ['ME 2202', 'MATH 2551', 'ME 3322*'], 'year': 3, 'done': False, 'immediacy': 5},
        'ECON 2001': {'prqs': [], 'year': 2, 'done': False, 'immediacy': 0},
        'Humanities': {'prqs': [], 'year': None, 'done': False, 'immediacy': 0},
        'ME 3017': {'prqs': ['ME 2202', 'ME 2016', 'MATH 2552', 'ECE 3710'],'year': 3,'done': False,'immediacy': 5},
        'ME 3345': {'prqs': ['ME 3322', 'ME 3340'],'year': 3,'done': False,'immediacy': 6},
        'ME 3057': {'prqs': ['COE 3001', 'ME 3017*', 'ME 3345*', 'MATH 3670*'],'year': 3,'done': False,'immediacy': 7},
        'ISYE 3025': {'prqs': ['ECON 2001'],'year': 3,'done': False,'immediacy': 1},
        'MATH 3670': {'prqs': ['MATH 2551'],'year': 3,'done': False,'immediacy': 3},
        'ME 3180': {'prqs': ['ME 2110', 'ME 3345'],'year': 3,'done': False,'immediacy': 7},
        'ME 3210': {'prqs': ['MSE 2001', 'ME 2110', 'COE 3001'],'year': 3,'done': False,'immediacy': 5},
        'ME 4056': {'prqs': ['ME 3057', 'ME 3345', 'ME 3017', 'MATH 3670'],'year': 4,'done': False,'immediacy': 8},
        'Free Elective': {'prqs': [], 'year': None, 'done': False, 'immediacy': 0},
        'ME 4182': {'prqs': ['ME 3210', 'ME 3180', 'ME 3017', 'MATH 3670', 'ME 2110'],'year': 4,'done': False,'immediacy': 8},
        'ME Elective': {'prqs': [], 'year': None, 'done': False, 'immediacy': 0},
        'Humanities Elective': {'prqs': [],'year': None,'done': False,'immediacy': 0},
        'Ethics Overlay': {'prqs': [], 'year': None, 'done': False, 'immediacy': 0}
    }
}