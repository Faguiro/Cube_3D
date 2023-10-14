#!/usr/bin/env python
# Versão em python 3 parao desenho do cubo e rotação com controles deslizantes.
import tkinter as tk
from math import radians, sin, cos

class Cube(object):
    def __init__(self, alpha=0, beta=0, gamma=0):
        self._alpha = alpha
        self._beta = beta
        self._gamma = gamma
        
        self.sin = [sin(alpha), sin(beta), sin(gamma)]
        self.cos = [cos(alpha), cos(beta), cos(gamma)]
        self.points = [[-1, -1, -1], [-1, -1, +1], [-1, +1, -1], [-1, +1, +1],
                       [+1, -1, -1], [+1, -1, +1], [+1, +1, -1], [+1, +1, +1]]

    def __iter__(self):
        lines = [(0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3),
                 (2, 6), (3, 7), (4, 5), (4, 6), (5, 7), (6, 7)]

        coords = ([self.points[i], self.points[j]] for i, j in lines)
        return coords

    coords = property(fget=__iter__)

    def rotate(self, alpha=None, beta=None, gamma=None):
        changed = False
        
        if alpha is not None and alpha != self._alpha:
            self.sin[0], self.cos[0] = sin(alpha), cos(alpha)
            changed = True
            
        if beta is not None and beta != self._beta:
            self.sin[1], self.cos[1] = sin(beta), cos(beta)
            changed = True

        if gamma is not None and gamma != self._gamma:
            self.sin[2], self.cos[2] = sin(gamma), cos(gamma)
            changed = True

        if changed:
            points = [[-1, -1, -1], [-1, -1, +1], [-1, +1, -1], [-1, +1, +1],
                      [+1, -1, -1], [+1, -1, +1], [+1, +1, -1], [+1, +1, +1]]

            self.points = list(map(self._rotate_point, points))

    def _rotate_point(self, point):
        x, y, z = point

        sa, sb, sg = self.sin
        ca, cb, cg = self.cos
        
        x1 = z*sa + x*ca
        y1 = y
        z1 = z*ca - x*sa
        
        x2 = x1
        y2 = y1*cb - z1*sb
        z2 = y1*sb + z1*cb
        
        x3 = y2*sg + x2*cg
        y3 = y2*cg - x2*sg
        z3 = z2
        
        return x3, y3, z3

    def _set_alpha(self, alpha):
        self.rotate(alpha=alpha)

    alpha = property(fset=_set_alpha)

    def _set_beta(self, beta):
        self.rotate(beta=beta)

    beta = property(fset=_set_beta)

    def _set_gamma(self, gamma):
        self.rotate(gamma=gamma)

    gamma = property(fset=_set_gamma)

class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        width = 400
        height = 400
        
        self.canvas = tk.Canvas(self, width=width, height=height, bg='white')
        self.canvas.grid(row=0, column=1)

        self.XOFF = XOFF = width/2
        self.YOFF = YOFF = height/2
        self.SCALE = 100.0
        
        tk.Scale(self, label='beta', from_=-180, to=180, resolution=1, orient=tk.VERTICAL, command=self._set_beta).grid(row=0, column=0, sticky=tk.N+tk.S)
        tk.Scale(self, label='alpha', from_=-180, to=180, resolution=1, orient=tk.HORIZONTAL, command=self._set_alpha).grid(row=1, column=1, sticky=tk.W+tk.E)
        tk.Scale(self, label='gamma', from_=-180, to=180, resolution=1, orient=tk.HORIZONTAL, command=self._set_gamma).grid(row=2, column=1, sticky=tk.W+tk.E)

        self.cube = Cube()

        self.draw()

    def draw(self):
        S, X, Y = self.SCALE, self.XOFF, self.YOFF
        self.lines = []
        for line in self.cube:
            line = [(point[0] * S + X, point[1] * S + Y) for point in line]
            self.lines.append(self.canvas.create_line(line))

    def _set_alpha(self, alpha):
        alpha = radians(int(alpha))
        self.cube.alpha = alpha
        self.update_cube()

    def _set_beta(self, beta):
        beta = radians(int(beta))
        self.cube.beta = beta
        self.update_cube()

    def _set_gamma(self, gamma):
        gamma = radians(int(gamma))
        self.cube.gamma = gamma
        self.update_cube()

    def update_cube(self):
        S, X, Y = self.SCALE, self.XOFF, self.YOFF
        for i, line in enumerate(self.cube):
            line = [(point[0] * S + X, point[1] * S + Y) for point in line]
            coords = []
            [coords.extend(point) for point in line]
            self.canvas.coords(self.lines[i], *coords)

if __name__ == "__main__":
    root = MainWindow()
    try:
        root.mainloop()
    except KeyboardInterrupt:
        root.destroy()
