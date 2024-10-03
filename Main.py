{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMmYf40B1+5+znIFgoHy0M0",
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
        "<a href=\"https://colab.research.google.com/github/ssamuel819/AP0059-2024-3/blob/main/Main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "id": "crJB-2XvauvQ",
        "outputId": "805c3600-498f-4858-d707-5302f2017b9a"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "IndentationError",
          "evalue": "unexpected indent (<ipython-input-3-be661f8d3515>, line 13)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-3-be661f8d3515>\"\u001b[0;36m, line \u001b[0;32m13\u001b[0m\n\u001b[0;31m    while True:\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m unexpected indent\n"
          ]
        }
      ],
      "source": [
        "# Importamos las clases Suma, Resta, Multiplicacion, Division y Exponencial desde el archivo 'Calculadora'\n",
        "from calculadora import Suma\n",
        "from calculadora import Resta\n",
        "from calculadora import Multiplicacion\n",
        "from calculadora import Division\n",
        "from calculadora import Exponencial\n",
        "\n",
        "# Definimos la función principal main que contiene el bucle de la calculadora\n",
        "def main():\n",
        "  print (\"Abriendo calculadora\")\n",
        "\n",
        "\n",
        "    while True:\n",
        "\n",
        "        # Muestra las multiples opciones al usuario\n",
        "        print(\"Selecciona la operación:\")\n",
        "        print(\"1. Suma\")\n",
        "        print(\"2. Resta\")\n",
        "        print(\"3. Multiplicación\")\n",
        "        print(\"4. División\")\n",
        "        print(\"5. Exponencial\")\n",
        "        print(\"6. Salir\")\n",
        "\n",
        "        opcion = input(\"Elige una opción (1-6): \")\n",
        "\n",
        "\n",
        "        if opcion == '6':\n",
        "            print(\"Saliendo de la calculadora.\")\n",
        "            break  # Al escoger el numero 6 el bucle terminara y se saldra de la calculadora\n",
        "\n",
        "\n",
        "        num1 = float(input(\"Introduce el primer número: \"))\n",
        "\n",
        "\n",
        "        if opcion == '5':\n",
        "            num2 = float(input(\"Introduce el exponente: \"))\n",
        "        else:\n",
        "            num2 = float(input(\"Introduce el segundo número: \"))\n",
        "\n",
        "\n",
        "        if opcion == '1':\n",
        "            operacion = Suma()\n",
        "        elif opcion == '2':\n",
        "            operacion = Resta()\n",
        "        elif opcion == '3':\n",
        "            operacion = Multiplicacion()\n",
        "        elif opcion == '4':\n",
        "            operacion = Division()\n",
        "        elif opcion == '5':\n",
        "            operacion = Exponencial()\n",
        "        else:\n",
        "\n",
        "            print(\"Opción no válida\")  # Si se ingresa una opción no válida, se muestra un mensaje de error y continúa el bucle\n",
        "            continue\n",
        "\n",
        "\n",
        "        resultado = operacion.operar(num1, num2)\n",
        "\n",
        "        print(f\"El resultado es: {resultado}\")\n",
        "\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "J_j2-wKea3J3"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}