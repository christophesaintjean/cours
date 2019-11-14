"""Module qui l'est le meilleur du monde !!"""


def monpow(a, b):
    """Calcul de a à la puissance b

      Ici une explication longue de la puissance
      d'un nombre :math:`a^b = aa..a` b fois

      :param a: la valeur
      :param b: l'exposant
      :type a: int, float,...
      :type b: int, float,...
      :returns: a**b
      :rtype: int, float
      :Exemples:
    >> > nompow(2, 3)
    8
    >> > nompow(2., 2)
    4.0

    .. note:: c'est une version accélérée de la puissance par multiplication successives
    .. seealso:: pow
    .. warning:: a et b sont des nombres
    """
    return a ** b

"""
import CM5_documentation
help(CM5_documentation)
help(CM5_documentation.monpow)
"""
print(monpow.__doc__)
