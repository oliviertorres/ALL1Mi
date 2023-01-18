#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy as sp #calcul numérique
import numpy as np #calcul numérique

import sympy as sy #calcul symbolique


# **Exercice 1**

# In[2]:


# déclaration des symboles utilisés
# inconnues et paramètres

x,y,z,m = sy.symbols('x,y,z,m')


# $$\newcommand{\pp}{\:+\:}\newcommand{\mm}{\:-\:}\newcommand{\ee}{\:=\:}
# 1)\qquad \left\{\begin{alignat*}{4}
# && x &&\mm &&2y  &&\ee && 2\\
# && x &&\mm  &&my &&\ee && m
# \end{alignat*}
# \right.
# $$

# In[3]:


# 2. linsolve
S1=sy.linsolve((x-2*y-2,x-m*y-m),(x,y))
print('Solution du système : {}'.format(S1))


# **Exercice 2**

# $$\newcommand{\pp}{\:+\:}\newcommand{\mm}{\:-\:}\newcommand{\ee}{\:=\:}
# 1)\qquad \left\{\begin{alignat*}{5}
# && x &&\pp 2y \pp &&3z&&\ee&&14\\
# && 4x &&\pp 5y\pp &&6z&&\ee&&32\\
# && 7x &&\pp 8 y\pp &&10z&&\ee&&53
# \end{alignat*}
# \right.
# $$

# In[4]:


Sa=sy.linsolve((x+2*y+3*z-14,4*x+5*y+6*z-32,7*x+8*y+10*z-53),(x,y,z))
print('Solution du système : {}'.format(Sa))


# $$%\newcommand{\pp}{\:+\:}\newcommand{\mm}{\:-\:}\newcommand{\ee}{\:=\:}
# 2) \qquad \left\{\begin{alignat*}{6}
# && 2x &&\pp 3y \mm && z &&\ee&& -1&&\\
# && x &&\pp 2y \pp && 3z &&\ee&& 2&&\\
# && 3x &&\pp 4y \mm && 5z &&\ee&& -4&& 
# \end{alignat*}
# \right.
# $$

# In[5]:


Sb=sy.linsolve((2*x+3*y-z+1,x+2*y+3*z-2,3*x+4*y-5*z+4),(x,y,z))
print('Solution du système : {}'.format(Sb))


# In[6]:


Sc=sy.linsolve((x-2*y + 3*z - 5,2*x - 4*y + z - 5,3*x - 5*y + 2*z - 8),(x,y,z))
print('Solution du système : {}'.format(Sc))


# In[7]:


Sd=sy.linsolve((2*x + y - z - 3,x-y+z - 2,x + y + 2*z),(x,y,z))
print('Solution du système Sd : {}'.format(Sd))

