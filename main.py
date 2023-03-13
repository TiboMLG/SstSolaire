import ffmpeg
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import animation
from matplotlib.animation import FuncAnimation

ms = 1.988*10**30    #masse du soleil en kg
mt = 5.972*10**24    #masse de la terre
ml = 7.342*10**22
mm = 3.285*10**23    #masse de mercure
mms = 6.417*10**23   #masse de mars
mv = 4.8675*10**24   #masse de vénus
mc = 9.46*10**20
mo = 4.0e9
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

#Mars
xms, yms, zms = 1.666*UA, 0, 0
vxms, vyms, vzms = 0, 21959, -709

#Vénus
xv, yv, zv = 0.7263*UA, 0, 0
vxv, vyv, vzv = 0, 34609, -2053

#Objet 1
xo, yo, zo = 1.5*UA, 0, 0
vxo, vyo, vzo = 0, 15000, 0

t = 0

#Listes des positions des astres
xt_list, yt_list, zt_list = [], [], []
xs_list, ys_list, zs_list = [], [], []
xm_list, ym_list, zm_list = [], [], []
xc_list, yc_list, zc_list =[], [], []
xms_list, yms_list, zms_list = [], [], []
xv_list, yv_list, zv_list = [], [], []
xo_list, yo_list, zo_list = [], [], []

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

    ##  MARS   ##
    # Calcul des forces
    rxms, ryms, rzms = xms - xs, yms - ys, zms - zs
    r3_ms = (rxms ** 2 + ryms ** 2 + rzms ** 2) ** 1.5
    Fx_ms, Fy_ms, Fz_ms = -(G * ms * mms) * rxms / r3_ms, -(G * ms * mms) * ryms / r3_ms, -(G * ms * mms) * rzms / r3_ms

    vxms += Fx_ms * dt / mms
    vyms += Fy_ms * dt / mms
    vzms += Fz_ms * dt / mms

    # Màj de la position

    xms += vxms * dt
    yms += vyms * dt
    zms += vzms * dt
    xms_list.append(xms)
    yms_list.append(yms)
    zms_list.append(zms)

    ##  VENUS   ##
    # Calcul des forces
    rxv, ryv, rzv = xv - xs, yv - ys, zv - zs
    r3_v = (rxv**2+ryv**2+rzv**2)**1.5
    Fx_v, Fy_v, Fz_v = -(G*ms*mv)*rxv/r3_v, -(G*ms*mv)*ryv/r3_v, -(G*ms*mt)*rzv/r3_v


    vxv += Fx_v * dt/mv
    vyv += Fy_v * dt / mv
    vzv += Fz_v * dt / mv

    # Màj de la position

    xv += vxv*dt
    yv += vyv*dt
    zv += vzv*dt
    xv_list.append(xv)
    yv_list.append(yv)
    zv_list.append(zv)

    ##  O   ##
    # Calcul des forces
    rxo, ryo, rzo = xo - xs, yo - ys, zo - zs
    r3_o = (rxo**2+ryo**2+rzo**2)**1.5
    Fx_o, Fy_o, Fz_o = -(G*ms*mo)*rxo/r3_o, -(G*ms*mo)*ryo/r3_o, -(G*ms*mo)*rzo/r3_o


    vxo += Fx_o * dt/mo
    vyo += Fy_o * dt / mo
    vzo += Fz_o * dt / mo

    # Màj de la position

    xo += vxo*dt
    yo += vyo*dt
    zo += vzo*dt
    xo_list.append(xo)
    yo_list.append(yo)
    zo_list.append(zo)

    ## SOLEIL

    vxs += -(Fx_t+Fx_m+Fx_c+Fx_ms+Fx_v+Fx_o)*dt/ms
    vys += -(Fy_t+Fy_m+Fy_c+Fy_ms+Fy_v+Fy_o)*dt/ms
    vzs += -(Fz_t+Fz_m+Fz_c+Fz_ms+Fz_v+Fz_o)*dt/ms

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
dataset_ms = [xms_list,yms_list,zms_list]
dataset_v = [xv_list,yv_list,zv_list]
dataset_o = [xo_list,yo_list,zo_list]
datadict['s'] = dataset_s
datadict['t'] = dataset_t
datadict['m'] = dataset_m
datadict['c'] = dataset_c
datadict['ms'] = dataset_ms
datadict['v'] = dataset_v
datadict['o'] = dataset_o
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

# Mars
line_ms,     = ax.plot([0],[0],[0],'-g',lw=1)
point_ms,    = ax.plot([UA],[0],[0], marker="o", markersize=2, markeredgecolor="black", markerfacecolor="black")
text_ms      = ax.text(UA,0,0,'Mars')
vis_dict['ms'] = [line_ms,point_ms,text_ms]

# Vénus
line_v,     = ax.plot([0],[0],[0],'-g',lw=1)
point_v,    = ax.plot([UA],[0],[0], marker="o", markersize=3, markeredgecolor="gold", markerfacecolor="gold")
text_v      = ax.text(UA,0,0,'Vénus')
vis_dict['v'] = [line_v,point_v,text_v]

# O
line_o,     = ax.plot([0],[0],[0],'-g',lw=1)
point_o,    = ax.plot([UA],[0],[0], marker="o", markersize=1, markeredgecolor="grey", markerfacecolor="grey")
text_o      = ax.text(UA,0,0,'Objet O')
vis_dict['o'] = [line_o,point_o,text_o]


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

    # Mars
    dataset_ms = data_dict['ms']
    line_ms, point_ms, text_ms = vis_dict['ms'][0], vis_dict['ms'][1], vis_dict['ms'][2]
    line_ms.set_data_3d(dataset_ms[0][:num], dataset_ms[1][:num], dataset_ms[2][:num])
    point_ms.set_data_3d(dataset_ms[0][num], dataset_ms[1][num], dataset_ms[2][num])
    text_ms.set_position((dataset_ms[0][num], dataset_ms[1][num], dataset_ms[2][num]))

    # Vénus
    dataset_v = data_dict['v']
    line_v, point_v, text_v = vis_dict['v'][0], vis_dict['v'][1], vis_dict['v'][2]
    line_v.set_data_3d(dataset_v[0][:num], dataset_v[1][:num], dataset_v[2][:num])
    point_v.set_data_3d(dataset_v[0][num], dataset_v[1][num], dataset_v[2][num])
    text_v.set_position((dataset_v[0][num], dataset_v[1][num], dataset_v[2][num]))

    # O
    dataset_o = data_dict['o']
    line_o, point_o, text_o = vis_dict['o'][0], vis_dict['o'][1], vis_dict['o'][2]
    line_o.set_data_3d(dataset_o[0][:num], dataset_o[1][:num], dataset_o[2][:num])
    point_o.set_data_3d(dataset_o[0][num], dataset_o[1][num], dataset_o[2][num])
    text_o.set_position((dataset_o[0][num], dataset_o[1][num], dataset_o[2][num]))

ani = animation.FuncAnimation(
    fig
    , update
    , len(xt_list)
    , fargs=(datadict, vis_dict)
    , interval=1
)

plt.show()

#ani.save('rendu.mp4', writer='ffmpeg')

