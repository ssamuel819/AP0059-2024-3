{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNVTqVO55Xgxa8YKIxHSZjm",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ssamuel819/AP0059-2024-3/blob/main/Calculadora.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "kuY5iHmKdrME"
      },
      "outputs": [],
      "source": [
        "class Suma:\n",
        "\n",
        "    def operar(self, num1, num2):\n",
        "        return num1 + num2  # Retorna la suma de num1 y num2\n",
        "\n",
        "\n",
        "class Resta:\n",
        "\n",
        "    def operar(self, num1, num2):\n",
        "        return num1 - num2  # Retorna la resta de num1 menos num2\n",
        "\n",
        "\n",
        "class Multiplicacion:\n",
        "\n",
        "    def operar(self, num1, num2):\n",
        "        return num1 * num2  # Retorna el producto de num1 y num2\n",
        "\n",
        "class Division:\n",
        "\n",
        "    def operar(self, num1, num2):\n",
        "        # Verifica si el divisor es 0,para no realizar esta operacion\n",
        "        if num2 == 0:\n",
        "            return \"error\"  # Si el divisor es 0, retorna un mensaje de error\n",
        "        return num1 / num2  # Si no existe un error, retorna el cociente de num1 y num2\n",
        "\n",
        "\n",
        "class Exponencial:\n",
        "\n",
        "    def operar(self, base, exponente):\n",
        "        return base ** exponente  # Retorna la base elevada al exponente"
      ]
    }
  ]
}