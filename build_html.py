# -*- coding: utf-8 -*-
"""
questions.py의 데이터를 읽어서 단일 HTML 파일로 조립.
GitHub Pages에 올릴 수 있는 self-contained 파일 생성.
"""
import json
from questions import QUESTIONS, CATEGORY_NAMES

# 데이터 직렬화
data_json = json.dumps(
    {"questions": QUESTIONS, "categories": CATEGORY_NAMES},
    ensure_ascii=False,
    indent=2,
)

# HTML 템플릿의 __DATA_PLACEHOLDER__를 실제 JSON으로 치환
with open("template_standalone.html", "r", encoding="utf-8") as f:
    template = f.read()

html_out = template.replace("__DATA_PLACEHOLDER__", data_json)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_out)

print(f"생성 완료: index.html ({len(html_out):,} bytes)")
print(f"  문제 수: {len(QUESTIONS)}")
print(f"  카테고리: {len(CATEGORY_NAMES)}")
