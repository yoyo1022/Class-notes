{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "week4-A107260009-鄭右琳.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMOY/MupHqYGMjXZCwsTDtC",
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
        "<a href=\"https://colab.research.google.com/github/yoyo1022/Class-notes/blob/master/IDS_week4_A107260009_%E9%84%AD%E5%8F%B3%E7%90%B3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "trjPpT5JOR1_",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "60c60f5d-377e-4232-ed3c-7b0a859a38f6"
      },
      "source": [
        "current_Celsius = 25\n",
        "Fahrenheit = current_Celsius*9/5+32\n",
        "print(Fahrenheit)"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "77.0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "j2Fnw2HvQKie",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "1e5e6e38-e5f2-4261-9f51-6a48c53a6f54"
      },
      "source": [
        "current_Fahrenheit = 77\n",
        "Celsius = (Fahrenheit-32)*5/9\n",
        "print(Celsius)"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "25.0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DvyDgrEASTRJ",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "e20034a3-9cb4-408d-d2a1-518e77a37138"
      },
      "source": [
        "shaq_weight = 147\n",
        "shaq_height = 216\n",
        "shaq_bmi = shaq_weight/(shaq_height/100)**2\n",
        "print(shaq_bmi)"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "31.507201646090532\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1E-zqgjITBYf",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "46920273-cc88-4e01-8bc6-46be3ba65ab9"
      },
      "source": [
        "ross_said = \"\"\"Let's put aside the fact that you \"accidentally\" pick up my grandmother's ring.\"\"\"\n",
        "print(ross_said)"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Let's put aside the fact that you \"accidentally\" pick up my grandmother's ring.\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "l4-aRrSyWn4e",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 69
        },
        "outputId": "7ffd481b-5e74-44ba-8a90-fe85ca76f62f"
      },
      "source": [
        "city = input(\"請輸入城市: \" )\n",
        "weather = input(\"請輸入天氣: \" )\n",
        "print(\"我在{}，天氣{}\".format(city, weather))"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入城市: 台北\n",
            "請輸入天氣: 晴\n",
            "我在台北，天氣晴\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "orITGt4dcLO_",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 104
        },
        "outputId": "4ba1efae-9e33-411b-e04c-9656ef8d8b82"
      },
      "source": [
        "name = input(\"請輸入姓名: \")\n",
        "shaq_height = eval(input(\"請輸入身高: \"))\n",
        "shaq_weight = eval(input(\"請輸入體重: \"))\n",
        "shaq_bmi = shaq_weight/(shaq_height/100)**2\n",
        "print(\"{}的身體質量指數為：{:.2f}\".format(name,shaq_bmi)) \n",
        "print(\"{}是否過重：{}\".format(name,shaq_bmi > 30))"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入姓名: 俠客歐尼爾 \n",
            "請輸入身高: 216\n",
            "請輸入體重: 147\n",
            "俠客歐尼爾 的身體質量指數為：31.51\n",
            "俠客歐尼爾 是否過重：True\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}