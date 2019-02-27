"""

python 3 dependencies

# install python 3.7.2
https://www.python.org/downloads/

# Power Shell
py -m pip install -U pip
py -m pip install -U matplotlib
"""

import matplotlib
import matplotlib.pyplot as plt

participants = ['caca', 'caique', 'chico', 'kairon', 'leticia', 'nayrla']

sessions = [
    'caca_01','caca_02','caca_03',
    'caique_01','caique_02','caique_03','caique_04','caique_05',
    'chico_01','chico_02','chico_03','chico_04','chico_05',
    'kairon_01','kairon_02','kairon_03','kairon_04','kairon_05',
    'leticia_01','leticia_02','leticia_03','leticia_04','leticia_05',
    'nayrla_01','nayrla_02','nayrla_03','nayrla_04','nayrla_05'
]
begin_session = [
    [4680,1140,1110],
    [886,928,832,846,844],
    [6060,1080,1110,960,1170],
    [9080,1200,1530,1080,1080],
    [3332,962,730,638,676],
    [7296,790,684,706,676]
]
end_session = [
    [9540,2712,2428],
    [6238,2660,5208,12178,2644],
    [35016,6086,2760,3138,1972],
    [16426,8518,29188,2020,2186],
    [16528,2770,1598,1554,1546],
    [9646,6984,2426,2948,1684]
]

deltas = []
for endd, begind in zip(end_session, begin_session):
    deltas.append([(end-begin)/60 for end, begin in zip(endd, begind)])
        
def draw_line(data, name):
    x_label = 'Tentativas'
    f = plt.figure(figsize=(5,3))
    axes = plt.gca()
    plt.suptitle(name, fontsize=12)

    axes.plot(data,color="k",marker='.', lw=1)
    plt.xticks(range(0, len(data), 1),(str(x) for x in range(1, len(data)+1)))

    # remove outer frame
    axes.spines['top'].set_visible(False)
    axes.spines['bottom'].set_visible(False)
    axes.spines['left'].set_visible(False)
    axes.spines['right'].set_visible(False)

    axes.set_xlim(-0.5, len(data)+0.5)

    #remove ticks
    # axes.xaxis.set_ticks_position('none')
    # axes.yaxis.set_ticks_position('none')

    axes.set_ylabel('Tempo (s)')
    axes.set_xlabel('Tentativas')

    plt.show()

for delta, name in zip(deltas, participants):
    draw_line(delta, name)
