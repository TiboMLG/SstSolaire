from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


ms = 1.988*10**30    #masse du soleil en kg
mt = 5.972*10**24    #masse de la terre
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

t = 0

# initialisation des listes pour stocker les positions précédentes des astres
xt_list_prev, yt_list_prev, zt_list_prev = [], [], []
xs_list_prev, ys_list_prev, zs_list_prev = [], [], []

# Fonction pour mettre à jour la figure à chaque pas de temps
def update_graph(i):
    global xt_list_prev, yt_list_prev, zt_list_prev, xs_list_prev, ys_list_prev, zs_list_prev

    # mise à jour de la position de la terre
    rx, ry, rz = xt - xs, yt - ys, zt - zs
    r3 = (rx**2+ry**2+rz**2)**1.5
    Fx_t, Fy_t, Fz_t = -(G*ms*mt)*rx/r3, -(G*ms*mt)*ry/r3, -(G*ms*mt)*rz/r3

    vxt += Fx_t * dt/mt
    vyt += Fy_t * dt / mt
    vzt += Fz_t * dt / mt

    xt += vxt*dt
    yt += vyt*dt
    zt += vzt*dt

    xt_list_prev.append(xt)
    yt_list_prev.append(yt)
    zt_list_prev.append(zt)

    # mise à jour de la position du soleil
    vxs += -Fx_t * dt / ms
    vys += -Fy_t * dt / ms
    vzs += -Fz_t * dt / ms

    xs += vxs * dt
    ys += vys * dt
    zs += vzs * dt
    xs_list_prev.append(xs)
    ys_list_prev.append(ys)
    zs_list_prev.append(zs)

    # mise à jour des positions précédentes des astres
    xt_list_prev = xt_list_prev[-500:]
    yt_list_prev = yt_list_prev[-500:]
    zt_list_prev = zt_list_prev[-500:]
    xs_list_prev = xs_list_prev[-500:]
    ys_list_prev = ys_list_prev[-500:]
    zs_list_prev = zs_list_prev[-500:]

    # tracer les positions des astres
    ax.clear()
    ax.scatter(xs, ys, zs, c='yellow', s=1000)
    ax.plot(xs_list_prev, ys_list_prev, zs_list_prev, c='yellow', alpha=0.5)
    ax.scatter(xt, yt, zt, c='blue', s=100)
    ax.plot(xt_list_prev, yt_list_prev, zt_list_prev, c='blue', alpha=0.5)

    # ajouter des informations sur la figure
    ax.set_title(f"Temps écoulé: {i*dt/(jour_secondes*365):.2f} ans")
    ax.set_xlim(-1.5*UA, 1.5*UA)
    ax.set_ylim(-1.5*UA, 1.5*UA)
    ax.set_zlim(-1.5*UA, 1.5*UA)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(-2*UA, 2*UA)
ax.set_ylim(-2*UA, 2*UA)
ax.set_zlim(-2*UA, 2*UA)

# tracer la position initiale des astres
ax.scatter(xs, ys, zs, c='yellow', s=1000)
ax.scatter(xt, yt, zt, c='blue', s=100)

# Trajectoire de la terre
earth_traj, = ax.plot(xt_list[:1], yt_list[:1], zt_list[:1], color='blue', label='Earth Trajectory')
# Position de la terre
earth_pos, = ax.plot([xt_list[0]], [yt_list[0]], [zt_list[0]], marker='o', color='blue', markersize=8, label='Earth')

# Trajectoire du soleil
sun_traj, = ax.plot(xs_list[:1], ys_list[:1], zs_list[:1], color='orange', label='Sun Trajectory')
# Position du soleil
sun_pos, = ax.plot([xs_list[0]], [ys_list[0]], [zs_list[0]], marker='o', color='orange', markersize=16, label='Sun')

def update(frame):
    earth_traj.set_data_3d(xt_list[:frame], yt_list[:frame], zt_list[:frame])
    earth_traj.set_color('blue')
    earth_pos.set_data_3d([xt_list[frame]], [yt_list[frame]], [zt_list[frame]])

    sun_traj.set_data_3d(xs_list[:frame], ys_list[:frame], zs_list[:frame])
    sun_traj.set_color('orange')
    sun_pos.set_data_3d([xs_list[frame]], [ys_list[frame]], [zs_list[frame]])

    return earth_traj, earth_pos, sun_traj, sun_pos,

ani = animation.FuncAnimation(fig, update, frames=len(xt_list), blit=True)

plt.legend()
plt.show()
