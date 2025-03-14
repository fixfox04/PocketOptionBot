git add market_analysis.py
git commit -m "Добавлен анализ рынка с уровнями Smart Money"
git push origin main

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf

# Загрузка данных (пример, заменить на реальные данные)
def load_data(filename="eurusd_data.json"):
    df = pd.read_json(filename)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df.set_index('timestamp', inplace=True)
    return df

# Определение уровней поддержки и сопротивления
def find_support_resistance(df, window=10):
    df['min'] = df['low'].rolling(window=window, center=True).min()
    df['max'] = df['high'].rolling(window=window, center=True).max()
    support = df['min'].dropna().unique()
    resistance = df['max'].dropna().unique()
    return support, resistance

# Визуализация уровней на графике
def plot_chart(df, support, resistance):
    fig, ax = plt.subplots(figsize=(12,6))
    mpf.plot(df, type='candle', ax=ax)
    
    for level in support:
        plt.axhline(y=level, color='green', linestyle='dashed', alpha=0.5, label='Support')
    for level in resistance:
        plt.axhline(y=level, color='red', linestyle='dashed', alpha=0.5, label='Resistance')
    
    plt.legend()
    plt.title("Smart Money - Support & Resistance")
    plt.show()

if __name__ == "__main__":
    df = load_data("eurusd_data.json")
    support, resistance = find_support_resistance(df)
    plot_chart(df, support, resistance)
