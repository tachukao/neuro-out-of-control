def load():
    import matplotlib
    import matplotlib.pyplot as plt
    # Configure figure
    matplotlib.rc('font', **{'family': 'Helvetica'})
    SMALL_SIZE = 18
    MEDIUM_SIZE = 18
    BIGGER_SIZE = 18
    plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)  # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    plt.rc('xtick', direction='out')
    plt.rc('ytick', direction='out')
    plt.rc('xtick', top=False)
    plt.rc('ytick', right=False)
    plt.rc('axes', labelpad=20)
    plt.rc('axes.spines', right=False)
    plt.rc('axes.spines', top=False)
    plt.rc('patch', facecolor='None')
    plt.rc('axes', facecolor='None')
    plt.rc('axes', linewidth=2)
    plt.rc('ytick.major', size=10)
    plt.rc('xtick.major', width=1.5)
    plt.rc('xtick.major', size=10)
    plt.rc('ytick.major', width=1.5)


def adjust_spines(spines,smart_bounds=True):
    for spine in spines.values():
        spine.set_position(('outward',10))
        spine.set_smart_bounds(smart_bounds)
