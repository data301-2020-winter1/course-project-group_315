{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_and_process(url_or_path_to_csv_file):\n",
    "    df1 = (\n",
    "        pd.read_csv(url_or_path_to_csv_file)\n",
    "      \n",
    "    )\n",
    "    \n",
    "    df2 = (\n",
    "    df1\n",
    "    .rename(columns={\"Name\": \"Game\"})\n",
    "    .loc(axis = 1)[\"Game\",\"Genre\",\"Platform\",\"Global_Sales\"]\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def genre_sales(genre_type):\n",
    "    return data.loc[data[\"Genre\"] == genre_type, \"Global_Sales\"].sum()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def platform_sales(platform_type):\n",
    "    return data.loc[data[\"Platform\"] == platform_type, \"Global_Sales\"].sum()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
