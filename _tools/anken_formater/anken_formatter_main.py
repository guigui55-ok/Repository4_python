# anken_formatter_main.py
# Python 3.10+
from __future__ import annotations
import os
import re
import sys
import json
import subprocess
import platform
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Callable

# =========
# データモデル（固定）
# =========
@dataclass
class AnkenRecord:
    title: Optional[str] = None
    start_period: Optional[str] = None     # 参画時期
    work_style: Optional[str] = None       # 勤務形態
    work_time: Optional[str] = None        # ★ 勤務時間（追加）
    reward_gross: Optional[str] = None     # 報酬額(税込)
    skills_must: List[str] = field(default_factory=list)  # スキル必須
    skills_nice: List[str] = field(default_factory=list)  # スキル尚可
    tasks: List[str] = field(default_factory=list)        # 業務内容
    seisan_low: Optional[int] = None       # 清算幅下限
    seisan_high: Optional[int] = None      # 清算幅上限
    contract_end: Optional[str] = None     # 契約期間


# =========
# 共通ユーティリティ
# =========# 旧:
# SECTION_HEADER_RE = re.compile(r"^【(.+?)】\s*$", re.MULTILINE)

# 新: 見出しと同一行の本文（例: 【期間】2025年11月〜）も拾う
SECTION_HEADER_RE = re.compile(r"^【([^】]+)】(.*)$", re.MULTILINE)


def read_text(path: str, encoding: str = "utf-8") -> str:
    with open(path, "r", encoding=encoding) as f:
        return f.read()

def split_sections(text: str) -> Dict[str, str]:
    """
    行頭の【見出し】でセクション分割し、{見出し: 本文} を返す。
    見出しと同一行の本文（例: 『【期間】2025年11月〜』）にも対応。
    """
    sections: Dict[str, str] = {}
    matches = list(SECTION_HEADER_RE.finditer(text))
    if not matches:
        return sections

    for i, m in enumerate(matches):
        header = m.group(1).strip()
        inline = m.group(2).strip()  # 同一行の本文（なければ空）
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        following = text[m.end():end].strip()
        body = (inline + ("\n" + following if following else "")).strip()
        sections[header] = body
    return sections

def normalize_zenhan(s: str) -> str:
    # 必要になったら全角→半角などを実装。ひとまずは素通し。
    return s

def extract_first_date_like(s: str) -> Optional[str]:
    """
    期間テキストから最初に見つかった年月を"YYYY/MM"で返す
    対応: 2025年11月 / 2025/11 / 2025.11 / 11月（年は不明のためNoneにする）
    """
    s = s.replace(" ", "")
    # YYYY年M月 / YYYY/M / YYYY.M
    m = re.search(r"(\d{4})[./年](\d{1,2})月?", s)
    if m:
        y, mon = m.group(1), m.group(2).zfill(2)
        return f"{y}/{mon}"

    # M月（年なし）
    m2 = re.search(r"(\d{1,2})月", s)
    if m2:
        mon = m2.group(1).zfill(2)
        return f"?/{mon}"  # 年不明は"?"表記（運用で決めてOK）
    return None

def extract_contract_end(s: str) -> Optional[str]:
    """
    期間テキストの右側（〜 の後）にある終端候補を拾う
    例: "2025年11月〜2026年2月末" -> "2026/02末"
    """
    # 〜, -, ～, 〜 を許容
    sp = re.split(r"[〜～\-~]", s, maxsplit=1)
    if len(sp) < 2:
        return None
    right = sp[1]

    # "YYYY年M月末" / "YYYY年M月" / "YYYY/M" / "M月末" / "M月"
    right = right.strip()
    # 末が付くか判定
    has_matsu = "末" in right

    m = re.search(r"(\d{4})[./年](\d{1,2})月?", right)
    if m:
        y, mon = m.group(1), m.group(2).zfill(2)
        return f"{y}/{mon}{('末' if has_matsu else '')}"

    m2 = re.search(r"(\d{1,2})月", right)
    if m2:
        mon = m2.group(1).zfill(2)
        return f"?/{mon}{('末' if has_matsu else '')}"

    return None

def extract_seisan(s: str) -> tuple[Optional[int], Optional[int]]:
    """
    清算幅（140～180 など）を抽出。確認中などは (None, None)
    """
    if "確認中" in s or "未定" in s:
        return (None, None)
    m = re.search(r"(\d{2,3})\s*[〜～\-]\s*(\d{2,3})", s)
    if m:
        low, high = int(m.group(1)), int(m.group(2))
        if low > high:
            low, high = high, low
        return (low, high)
    return (None, None)

def extract_reward(s: str) -> Optional[str]:
    """
    金額欄の自由記述をそのまま返す（スキル見合い等）
    将来ここで税込/税別、万円/円換算など正規化。
    """
    s = s.strip()
    if not s:
        return None
    return s

def extract_work_style(s: str) -> Optional[str]:
    """
    場所欄から勤務形態を抽出
    """
    s = s.strip()
    if "フルリモート" in s:
        return "フルリモート"
    if "常駐" in s:
        return s  # 例: "常駐(○○)" をそのまま
    # 単に地名だけ書かれているケースも将来対応可
    return s or None

def extract_work_time(s: str) -> Optional[str]:
    """
    時間欄から勤務時間を抽出（最小実装：そのまま返す）
    例: '確認中', '9:00-18:00', '10:00～19:00（休憩1h）' など
    """
    s = s.strip()
    if not s:
        return None
    return s

def bullets_to_list(s: str) -> List[str]:
    """
    行頭「・」の箇条書きを配列化。無ければ非空行を返す。
    """
    lines = [ln.strip(" \t・") for ln in s.splitlines()]
    items = [ln for ln in lines if ln]
    return items

def extract_skills(section: str) -> tuple[List[str], List[str]]:
    """
    【スキル】本文から『（尚可）』だけの行を境に、前=必須、後=尚可。
    箇条書きの「・」は取り除いて配列化。
    """
    lines = [ln.strip() for ln in section.splitlines()]
    must_lines: List[str] = []
    nice_lines: List[str] = []
    is_nice = False

    for ln in lines:
        if not ln:
            continue
        # 「（尚可）」or "(尚可)" だけの行を区切りとする
        if re.fullmatch(r"[（(]\s*尚可\s*[）)]", ln):
            is_nice = True
            continue
        # 箇条書きマークの除去
        ln = ln.lstrip("・ \t")
        if not ln:
            continue
        (nice_lines if is_nice else must_lines).append(ln)

    return must_lines, nice_lines


def list_to_field(items: List[str]) -> str:
    """
    タブ区切り1セル内に収めるため、箇条書きは ' / ' で結合
    """
    return " / ".join(items)

def record_to_tsv(rec: AnkenRecord) -> str:
    def join(items: List[str]) -> str:
        return " / ".join(items)

    fields = [
        rec.start_period or "",
        rec.work_style or "",
        rec.work_time or "",          # ★ 追加（勤務形態の直後）
        rec.reward_gross or "",
        join(rec.skills_must),
        join(rec.skills_nice),
        join(rec.tasks),
        "" if rec.seisan_low is None else str(rec.seisan_low),
        "" if rec.seisan_high is None else str(rec.seisan_high),
        rec.contract_end or "",
    ]
    return "\t".join(fields)

def copy_to_windows_clipboard(text: str) -> None:
    """
    Windows の 'clip' へパイプ。Windows以外は何もしない（将来拡張可）
    """
    if platform.system().lower().startswith("windows"):
        try:
            subprocess.run(["clip"], input=text, text=True, check=True)
        except Exception as e:
            print(f"[WARN] クリップボードコピーに失敗: {e}", file=sys.stderr)
    else:
        print("[INFO] 非Windows環境のためクリップボードコピーはスキップしました。", file=sys.stderr)


# =========
# パーサ（モード別）——同じデータモデルを返す
# =========
def parse_mode_jp_basic_v1(text: str) -> AnkenRecord:
    """
    今回のサンプル（日本語・【内容】【スキル】【金額】…見出し）向けの基本パーサ
    """
    sections = split_sections(text)

    # デバッグ用
    print("[debug] SECTIONS:", list(sections.keys()))
    
    rec = AnkenRecord()

    # タイトルは任意（先頭行に【案件】があれば）
    m_title = re.search(r"^【案件.+?】\s*(.+)$", text, re.MULTILINE)
    rec.title = m_title.group(0).strip() if m_title else None

    s_content = sections.get("内容", "")
    s_skill = sections.get("スキル", "")
    s_price = sections.get("金額", "")
    s_period = sections.get("期間", "")
    s_place = sections.get("場所", "")
    s_time    = sections.get("時間", "")     # ★ 追加
    s_seisan = sections.get("精算", "")

    # 参画時期（開始）
    # 勤務形態
    # 報酬額(税込)
    # スキル（必須/尚可）
    # 業務内容（箇条書き）
    # 清算幅
    # 契約期間（終了）
    rec.start_period = extract_first_date_like(s_period)
    rec.work_style = extract_work_style(s_place)
    rec.work_time    = extract_work_time(s_time)    # ★ 追加
    rec.reward_gross = extract_reward(s_price)
    rec.skills_must, rec.skills_nice = extract_skills(s_skill)
    rec.tasks = bullets_to_list(s_content)
    rec.seisan_low, rec.seisan_high = extract_seisan(s_seisan)
    rec.contract_end = extract_contract_end(s_period)

    return rec


# 将来: parse_mode_xxx を追加していく
PARSER_REGISTRY: dict[str, Callable[[str], AnkenRecord]] = {
    "jp_basic_v1": parse_mode_jp_basic_v1,
    # "jp_variant_v2": parse_mode_jp_variant_v2, など追加
}


def print_human_readable(rec: AnkenRecord) -> None:
    def join(items: List[str]) -> str:
        return " / ".join(items)

    print("参画時期：", rec.start_period or "")
    print("勤務形態：", rec.work_style or "")
    print("勤務時間：", rec.work_time or "")       # ★ 追加（勤務形態の直後）
    print("報酬額(税込)：", rec.reward_gross or "")
    print("スキル必須：", join(rec.skills_must))
    print("スキル尚可：", join(rec.skills_nice))
    print("業務内容：", join(rec.tasks))
    print("清算幅下限：", "" if rec.seisan_low is None else rec.seisan_low)
    print("清算幅上限：", "" if rec.seisan_high is None else rec.seisan_high)
    print("契約期間：", rec.contract_end or "")


# =========
# エントリポイント
# =========
def parse_anken(text: str, mode: str = "jp_basic_v1") -> AnkenRecord:
    if mode not in PARSER_REGISTRY:
        raise ValueError(f"未知のモードです: {mode}")
    return PARSER_REGISTRY[mode](text)

def main():
    path = "./sample/anken1.txt"
    mode = "jp_basic_v1"

    text = read_text(path)
    rec = parse_anken(text, mode=mode)

    # 1) 人間可読（テストがこの出力を検証）
    print_human_readable(rec)

    # 2) TSV（Excel 貼り付け用）
    tsv = record_to_tsv(rec)
    print("\nTSV：")
    print(tsv)

    # 3) クリップボード（Windowsのみ／テスト時は無効化可能）
    if os.environ.get("ANKEN_NO_CLIP") != "1":
        copy_to_windows_clipboard(tsv)


if __name__ == "__main__":
    main()
