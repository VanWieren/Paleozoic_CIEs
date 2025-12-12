def facies(max_depth):
    """
    
    """
    # old one
    # facies_data = [{'name':'Terrestrial','type': 'land','width':1,'min':1,'max':2}, # terrestrial is always everyting <0 (above water)
    #                {'name':'Grainstone','type': 'uniform', 'min': -0.01, 'max': max_depth/20,'width':.8}, # need this slightly modified min and the threshold below to make it work well
    #                {'name':'Packstone','type': 'uniform', 'min': max_depth/20, 'max': max_depth/15,'width':.6},
    #                {'name':'Wackestone','type': 'uniform', 'min': max_depth/15, 'max': max_depth/12,'width':.4},
    #                {'name':'Mudstone','type': 'uniform', 'min': max_depth/12, 'max': max_depth/10,'width':.3},
    #                {'name':'Shallow Marine','type': 'uniform', 'min': max_depth/10, 'max': max_depth/8,'width':.3},
    #                {'name':'Intermediate Marine','type': 'uniform', 'min': max_depth/8, 'max': max_depth/5,'width':.2},
    #                {'name':'Deep Marine','type': 'uniform', 'min': max_depth/5, 'max': max_depth,'width':.2}]

    # made wider ranges
    facies_data = [{'name':'Terrestrial','type': 'land','width':1,'min':1,'max':2},  # terrestrial remains unchanged
               {'name':'Grainstone','type': 'uniform', 'min': -0.01, 'max': max_depth/25, 'width': 0.8},  # reduced depth range
               {'name':'Packstone','type': 'uniform', 'min': max_depth/25, 'max': max_depth/12, 'width': 0.6},  # adjusted for continuity
               {'name':'Wackestone','type': 'uniform', 'min': max_depth/12, 'max': max_depth/9, 'width': 0.4},  # extended
               {'name':'Mudstone','type': 'uniform', 'min': max_depth/9, 'max': max_depth/7, 'width': 0.3},  # extended
               {'name':'Shallow Marine','type': 'uniform', 'min': max_depth/7, 'max': max_depth/6, 'width': 0.3},  # minor shift
               {'name':'Intermediate Marine','type': 'uniform', 'min': max_depth/6, 'max': max_depth/4, 'width': 0.2},  # slightly adjusted
               {'name':'Deep Marine','type': 'uniform', 'min': max_depth/4, 'max': max_depth, 'width': 0.2}]  # unchanged

    return facies_data
