import ffmpeg
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import animation
from matplotlib.animation import FuncAnimation

ms = 1.988*10**30    #masse du soleil en kg
mt = 5.972*10**24    #masse de la terre
mm = 3.285*10**23    #masse de mercure
mc = 9.46*10**20
G = 6.6743*10**-11   #cste de gravitation universelle
UA = 149597870700    #unite astronomique
jour_secondes = 86400
dt = 1*jour_secondes

#conditions initiale
#Soleil au centre du repère
xs, ys, zs = 0, 0, 0
vxs, vys, vzs = 0, 0, 0

#Terre
xt, yt, zt = 1*UA, 0 , 0
vxt, vyt, vzt = 0, 29290, 0

#Mercure
xm, ym, zm = 0.4*UA, 0, 0
vxm, vym, vzm = 0, 38700, 0

#Cérès
xc, yc, zc = 2.987*UA, 0, 0
vxc, vyc, vzc = 0, 16262, -2867

t = 0

#Listes des positions des astres
xt_list, yt_list, zt_list = [], [], []
xs_list, ys_list, zs_list = [], [], []
xm_list, ym_list, zm_list = [], [], []
xc_list, yc_list, zc_list =[], [], []

while t<5*365*jour_secondes:

    ##  TERRE   ##
    # Calcul des forces
    rxt, ryt, rzt = xt - xs, yt - ys, zt - zs
    r3_t = (rxt**2+ryt**2+rzt**2)**1.5
    Fx_t, Fy_t, Fz_t = -(G*ms*mt)*rxt/r3_t, -(G*ms*mt)*ryt/r3_t, -(G*ms*mt)*rzt/r3_t


    vxt += Fx_t * dt/mt
    vyt += Fy_t * dt / mt
    vzt += Fz_t * dt / mt

    # Màj de la position

    xt += vxt*dt
    yt += vyt*dt
    zt += vzt*dt
    xt_list.append(xt)
    yt_list.append(yt)
    zt_list.append(zt)

    ## MERCURE
    rxm, rym, rzm = xm - xs, ym - ys, zm - zs
    r3_m = (rxm**2+rym**2+rzm**2)**1.5
    Fx_m, Fy_m, Fz_m = -(G*ms*mm)*rxm/r3_m, -(G*ms*mm)*rym/r3_m, -(G*ms*mm)*rzm/r3_m

    vxm += Fx_m * dt/mm
    vym += Fy_m * dt / mm
    vzm += Fz_m * dt / mm

    # Màj de la position

    xm += vxm*dt
    ym += vym*dt
    zm += vzm*dt
    xm_list.append(xm)
    ym_list.append(ym)
    zm_list.append(zm)

    ##  CERES   ##
    # Calcul des forces
    rxc, ryc, rzc = xc - xs, yc - ys, zc - zs
    r3_c = (rxc ** 2 + ryc ** 2 + rzc ** 2) ** 1.5
    Fx_c, Fy_c, Fz_c = -(G*ms*mc)*rxc/r3_c, -(G*ms*mc)*ryc/r3_c, -(G*ms*mc)*rzc/r3_c

    vxc += Fx_c * dt / mc
    vyc += Fy_c * dt / mc
    vzc += Fz_c * dt / mc

    # Màj de la position

    xc += vxc * dt
    yc += vyc * dt
    zc += vzc * dt
    xc_list.append(xc)
    yc_list.append(yc)
    zc_list.append(zc)

    ## SOLEIL

    vxs += -(Fx_t+Fx_m+Fx_c)*dt/ms
    vys += -(Fy_t+Fy_m+Fy_c)*dt/ms
    vzs += -(Fz_t+Fz_m+Fz_c)*dt/ms

    # Màj de la position

    xs += vxs * dt
    ys += vys * dt
    zs += vzs * dt
    xs_list.append(xs)
    ys_list.append(ys)
    zs_list.append(zs)
    t += dt

fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.axis('auto')

axis_size = 2.5
ax.set_xlim(-axis_size*UA,axis_size*UA)
ax.set_ylim(-axis_size*UA,axis_size*UA)
ax.set_zlim(-axis_size*UA,axis_size*UA)

# ax.set_aspect('auto')
# ax.grid()
datadict = {}
dataset_s = [xs_list,ys_list,zs_list]
dataset_t = [xt_list,yt_list,zt_list]
dataset_m = [xm_list,ym_list,zm_list]
dataset_c = [xc_list,yc_list,zc_list]
datadict['s'] = dataset_s
datadict['t'] = dataset_t
datadict['m'] = dataset_m
datadict['c'] = dataset_c
vis_dict = {}

# Soleil
line_s,     = ax.plot([0],[0],[0],'-g',lw=1)
point_s,    = ax.plot([UA],[0],[0], marker="o", markersize=7, markeredgecolor="yellow", markerfacecolor="yellow")
text_s      = ax.text(UA,0,0,'Soleil')
vis_dict['s'] = [line_s,point_s,text_s]

# Terre
line_t,     = ax.plot([0],[0],[0],'-g',lw=1)
point_t,    = ax.plot([UA],[0],[0], marker="o", markersize=4, markeredgecolor="blue", markerfacecolor="blue")
text_t      = ax.text(UA,0,0,'Terre')
vis_dict['t'] = [line_t,point_t,text_t]

# Mercure
line_m, = ax.plot([0], [0], [0], '-g', lw=1)
point_m, = ax.plot([UA], [0], [0], marker="o", markersize=2, markeredgecolor="brown", markerfacecolor="brown")
text_m = ax.text(UA, 0, 0, 'Mercure')
vis_dict['m'] = [line_m, point_m, text_m]

# Cérès
line_c,     = ax.plot([0],[0],[0],'-g',lw=1)
point_c,    = ax.plot([UA],[0],[0], marker="o", markersize=1, markeredgecolor="black", markerfacecolor="black")
text_c      = ax.text(UA,0,0,'Cérès')
vis_dict['c'] = [line_c,point_c,text_c]


def update(num, data_dict, vis_dict):
    # Soleil
    dataset_s = data_dict['s']
    line_s, point_s, text_s = vis_dict['s'][0], vis_dict['s'][1], vis_dict['s'][2]
    line_s.set_data_3d(dataset_s[0][:num], dataset_s[1][:num], dataset_s[2][:num])
    point_s.set_data_3d(dataset_s[0][num], dataset_s[1][num], dataset_s[2][num])
    text_s.set_position((dataset_s[0][num], dataset_s[1][num], dataset_s[2][num]))

    # Cérès
    dataset_c = data_dict['c']
    line_c, point_c, text_c = vis_dict['c'][0], vis_dict['c'][1], vis_dict['c'][2]
    line_c.set_data_3d(dataset_c[0][:num], dataset_c[1][:num], dataset_c[2][:num])
    point_c.set_data_3d(dataset_c[0][num], dataset_c[1][num], dataset_c[2][num])
    text_c.set_position((dataset_c[0][num], dataset_c[1][num], dataset_c[2][num]))

    # Terre
    dataset_t = data_dict['t']
    line_t, point_t, text_t = vis_dict['t'][0], vis_dict['t'][1], vis_dict['t'][2]
    line_t.set_data_3d(dataset_t[0][:num], dataset_t[1][:num], dataset_t[2][:num])
    point_t.set_data_3d(dataset_t[0][num], dataset_t[1][num], dataset_t[2][num])
    text_t.set_position((dataset_t[0][num], dataset_t[1][num], dataset_t[2][num]))

    # Mercure
    dataset_m = data_dict['m']
    line_m, point_m, text_m = vis_dict['m'][0], vis_dict['m'][1], vis_dict['m'][2]
    line_m.set_data_3d(dataset_m[0][:num], dataset_m[1][:num], dataset_m[2][:num])
    point_m.set_data_3d(dataset_m[0][num], dataset_m[1][num], dataset_m[2][num])
    text_m.set_position((dataset_m[0][num], dataset_m[1][num], dataset_m[2][num]))

ani = animation.FuncAnimation(
    fig
    , update
    , len(xt_list)
    , fargs=(datadict, vis_dict)
    , interval=1
)

plt.show()

#ani.save('rendu.mp4', writer='ffmpeg')

