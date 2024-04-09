import paths
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

import seaborn as sns
plt.rcParams['figure.figsize'] = (15, 10)

sns.set_style('ticks')
#sns.set_style('darkgrid')
sns.set_context("talk",font_scale=2,rc={"lines.linewidth": 4,"axes.linewidth": 5})

plt.rc('axes', linewidth=3)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['xtick.top'] = True
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['ytick.right'] = True
plt.rcParams['xtick.major.size'] = 10
plt.rcParams['xtick.major.width'] = 3
plt.rcParams['xtick.minor.size'] = 5
plt.rcParams['xtick.minor.width'] = 1.5
plt.rcParams['ytick.major.size'] = 10
plt.rcParams['ytick.major.width'] = 3
plt.rcParams['ytick.minor.size'] = 5
plt.rcParams['ytick.minor.width'] = 1.5
plt.rcParams['axes.edgecolor'] = 'k'#'gray'
#plt.rcParams['axes.grid'] = True
#plt.rcParams['grid.color'] = 'lightgray'
#plt.rcParams['grid.linestyle'] = 'dashed' #dashes=(5, 1)
plt.rcParams['lines.dashed_pattern'] = 10, 3
plt.rcParams['grid.linewidth'] = 1.5
#plt.rcParams['axes.facecolor'] = 'whitesmoke'
plt.rcParams['axes.axisbelow'] = True
plt.rcParams['legend.fancybox'] = True
plt.rcParams['legend.frameon'] = True
plt.rcParams['legend.shadow'] = False
plt.rcParams['legend.edgecolor'] = 'lightgray'
plt.rcParams['patch.linewidth'] = 3

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': 'cmr10',
    'mathtext.fontset': 'cm',
    'axes.formatter.use_mathtext': True # needed when using cm=cmr10 for normal text
})

plt.switch_backend('agg') 

Mach_range = [0.1, 1.0, 10.0, 100.0]
#label_list = ['Federrath & Klessen (2012) with Mach number = ' + str(Mach), 'Padoan et al. (2012)',  'Semenov et al. (2016)', 'Evans et al. (2022)']
color_list = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

def Evans(alpha):
    return 0.3*np.exp(-2.02*alpha**(1/2))

def Semenov(alpha):
    return 0.9*np.exp(-1.6*alpha**(1/2))

def Padoan(alpha):
    return 0.5*np.exp(-1.6*alpha**(1/2))

def Hopkins(alpha):
    return np.where(alpha < 1, 1, 0)

def Federrath(alpha):
    Mach = np.sqrt(alpha)
    print(Mach.max())
    return 0.09/(2*0.49)*np.exp(3/8*np.log(1+0.4**2*Mach**2))*(1+erf((np.log(1+0.4**2*Mach**2)-np.log(np.pi**2/5*0.19**2*alpha*Mach**2))/np.sqrt(2*np.log(1+0.4**2*Mach**2))))

# Federrath in dependence of Mach
def Federrath_mach(alpha, Mach):
    return 0.09/(2*0.49)*np.exp(3/8*np.log(1+0.4**2*Mach**2))*(1+erf((np.log(1+0.4**2*Mach**2)-np.log(np.pi**2/5*0.19**2*alpha*Mach**2))/np.sqrt(2*np.log(1+0.4**2*Mach**2))))

fig = plt.figure(figsize = (10,8))
alpha = np.logspace(-3, 4, 100)
plt.xscale('log')
plt.ylim(-0.05, 1.05)
for Mach in Mach_range:
    plt.plot(alpha, Federrath_mach(alpha, Mach), label='Federrath & Klessen (2012)' + '\n' + 'with Mach number = ' + str(Mach))    
plt.plot(alpha, Federrath(alpha), label='Federrath & Klessen (2012)')
#plt.title('Star Formation Efficiency Comparison in different models', fontsize = 14)
plt.plot(alpha, Padoan(alpha), label='Padoan et al. (2012)')
plt.plot(alpha, Hopkins(alpha), label='Hopkins et al. (2013)')
plt.plot(alpha, Semenov(alpha), label='Semenov et al. (2016)')
plt.plot(alpha, Evans(alpha), label='Evans et al. (2022)')
plt.xlabel(r'Virial Parameter $\alpha$')
#fig.tight_layout()
plt.ylabel(r'Star Formation Efficiency $\epsilon_{\rm ff}$')
plt.legend(fontsize = 20)
plt.savefig(paths.figures / 'efficiency_comparison.pdf', bbox_inches='tight')

