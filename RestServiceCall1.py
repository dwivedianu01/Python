{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Copy of RestServiceCall1.py",
      "provenance": [],
      "authorship_tag": "ABX9TyPe7Z1BfD5n2BTqmF5T9smp",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/dwivedianu01/Python/blob/main/RestServiceCall1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ui3MwhjmdH5H",
        "outputId": "30ffdb70-daa6-4051-ce85-c7a35cd6d53d",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 55
        }
      },
      "source": [
        "import requests\n",
        "response = requests.get(\"http://api.open-notify.org/astros.json\")\n",
        "print(response.json())\n",
        "\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "{'number': 6, 'message': 'success', 'people': [{'name': 'Chris Cassidy', 'craft': 'ISS'}, {'name': 'Anatoly Ivanishin', 'craft': 'ISS'}, {'name': 'Ivan Vagner', 'craft': 'ISS'}, {'name': 'Sergey Ryzhikov', 'craft': 'ISS'}, {'name': 'Kate Rubins', 'craft': 'ISS'}, {'name': 'Sergey Kud-Sverchkov', 'craft': 'ISS'}]}\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}