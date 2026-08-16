#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# HEM v3.0 + V1.6.1-Auto 融合架构爬虫 v1.0

import csv
import time

# ========== 队名映射 ==========
TEAM_MAP = {
    "Almería": "阿尔维卡", "Amadora": "阿马多拉",
    "Alavés": "阿拉维斯", "Getafe": "赫塔费",
    "Willem II": "威廉二世", "Nijmegen": "奈梅亨",
    "Norwich": "诺维奇", "West Brom": "西布罗姆",
    "Mjällby": "米亚尔比", "Sirius": "天狼星",
    "Bolton": "博尔顿", "Preston": "普雷斯顿",
    "Fortuna": "福图纳", "Cambuur": "坎布尔",
    "Sevilla": "塞维利亚", "Rayo Vallecano": "巴列卡诺",
    "Arouca": "阿罗卡", "Moreirense": "摩雷伦斯",
    "Braga": "布拉加", "Gil Vicente": "吉维森特",
    "Famalicão": "法马利康", "Marítimo": "马里迪莫",
    "Portimonense": "葡国民", "Estoril": "埃斯托里",
    "Casa Pia": "卡萨皮亚", "Benfica": "本菲卡",
    "Racing Santander": "桑坦德", "Villarreal": "比利亚雷",
    "Espanyol": "西班牙人", "Levante": "莱万特",
    "Deportivo": "拉科", "Elche": "埃尔切",
    "Brann": "布兰", "HamKam": "汉坎",
    "Molde": "莫尔德", "Tromsø": "特罗姆瑟",
    "Sarpsborg": "萨普斯堡", "Sandefjord": "桑纳菲",
    "Fredrikstad": "腓特烈", "Kristiansund": "克里斯蒂",
    "Brommapojkarna": "布鲁马波", "Örgryte": "厄格里特",
    "Degerfors": "代格福什", "Göteborg": "哥德堡",
    "Djurgården": "佐加顿斯", "AIK": "索尔纳",
    "Kalmar": "卡尔马", "Hammarby": "哈马比",
    "GAIS": "盖斯", "Malmö": "马尔默",
    "Häcken": "赫根", "Halmstad": "哈尔姆斯",
    "AC Oulu": "AC奥卢", "Inter Turku": "国际图尔",
    "Heerenveen": "海伦芬", "Ajax": "阿贾克斯",
    "Feyenoord": "费耶诺德", "Go Ahead Eagles": "前进之鹰",
    "Twente": "特温特", "PEC Zwolle": "兹沃勒",
    "ADO Den Haag": "海牙", "Groningen": "格罗宁根",
    "Burnley": "伯恩利", "West Ham": "西汉姆联",
    "Cardiff": "加的夫城", "Wrexham": "雷克斯",
}

def fetch_odds(match_id):
    time.sleep(1)
    mock = {
        "周日002": [15.00, 5.80, 3.80, 3.70, 5.00, 8.40, 15.00, 22.00],
        "周日009": [28.00, 8.20, 4.80, 3.85, 4.50, 6.25, 9.50, 11.00],
        "周日016": [25.00, 7.75, 4.60, 3.85, 4.50, 6.25, 10.50, 12.50],
        "周日020": [25.00, 7.75, 4.60, 3.70, 4.50, 6.50, 10.50, 13.00],
        "周日021": [22.00, 7.20, 4.50, 3.60, 4.60, 6.70, 11.50, 15.00],
        "周日014": [17.00, 6.20, 4.00, 3.60, 4.90, 8.00, 13.50, 19.00],
    }
    return mock.get(match_id, [0.0]*8)

def fetch_schedule():
    return [
        {"match_id": "周日002", "league": "荷甲", "home_team": "海牙", "away_team": "格罗宁根", "match_time": "2026-08-16 18:15"},
        {"match_id": "周日009", "league": "荷甲", "home_team": "费耶诺德", "away_team": "前进之鹰", "match_time": "2026-08-16 20:30"},
        {"match_id": "周日014", "league": "瑞超", "home_team": "卡尔马", "away_team": "哈马比", "match_time": "2026-08-16 22:30"},
        {"match_id": "周日016", "league": "荷甲", "home_team": "阿贾克斯", "away_team": "海伦芬", "match_time": "2026-08-16 22:45"},
        {"match_id": "周日020", "league": "挪超", "home_team": "布兰", "away_team": "汉坎", "match_time": "2026-08-16 23:00"},
        {"match_id": "周日021", "league": "挪超", "home_team": "萨普斯堡", "away_team": "桑纳菲", "match_time": "2026-08-16 23:00"},
    ]

def generate_csv():
    schedule = fetch_schedule()
    rows = []
    for match in schedule:
        odds = fetch_odds(match["match_id"])
        if not odds or odds == [0.0]*8:
            continue
        min_goal = odds.index(min(odds))
        min_odds = min(odds)
        rows.append({
            "match_id": match["match_id"],
            "league": match["league"],
            "home_team": match["home_team"],
            "away_team": match["away_team"],
            "match_time": match["match_time"],
            "min_goal": min_goal,
            "min_odds": min_odds,
            "model_tag": "",
            "track_note": "",
            "track_status": "",
            "transfer_modify": "",
            "lambda_exp": "",
            "xg_weight": 1.25,
            "spi_score": 75.2,
            "odds_change_rate": 0.0,
            "multi_source_resonance": "",
            "mae_history": "",
            "odds_open_min_goal": min_odds * 1.05,
            "fatigue_index": 0,
        })
    with open("v1.6.1_crawler_output.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "match_id","league","home_team","away_team","match_time",
            "min_goal","min_odds","model_tag","track_note","track_status",
            "transfer_modify","lambda_exp","xg_weight","spi_score",
            "odds_change_rate","multi_source_resonance","mae_history",
            "odds_open_min_goal","fatigue_index"
        ])
        writer.writeheader()
        writer.writerows(rows)
    print("✅ 爬虫完成！输出文件：v1.6.1_crawler_output.csv")

if __name__ == "__main__":
    generate_csv()
fix syntax error and indentation
