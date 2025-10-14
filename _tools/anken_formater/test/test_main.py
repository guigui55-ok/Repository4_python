import os
import sys
import subprocess
from pathlib import Path
import textwrap
import re

ROOT = Path(__file__).resolve().parents[1]

def setup_sample_file():
    """サンプル案件テキストファイルを作成"""
    sample_dir = ROOT / "sample"
    sample_dir.mkdir(parents=True, exist_ok=True)
    sample_path = sample_dir / "anken_test1.txt"

    sample_text = textwrap.dedent("""\
        【案件①】Python計算処理アプリの運用保守支援
        【内容】
        ・アプリの運用保守案件です。
        ・画面と内部処理の開発ベンダーが分かれており、今回は内部処理側のベンダーとして問い合わせ対応を実施します。
        ・アプリ内部の計算処理がPythonで実装されており、開発知見を持つ人材を募集します。
        ・問い合わせ対応や切り分け(計算処理が正しいのか、バグなのか、画面入力の問題なのか等)がメイン業務です。
        ・画面側の開発は別ベンダーが対応するため、能動的に切り分け・調査できることが求められます。
        ・不具合発生時には修正の段取り(顧客とのスケジュール調整や大枠要件決定など)はしますが、修正作業は開発チーム側で実施します。
        ・既存のPMがしばらくは対応しますが、慣れてきたらPMから引継ぎを受け、顧客の窓口含めて対応依頼する想定です。
        【スキル】
        ・Pythonの読解/開発経験
        ・問い合わせ対応・切り分けの実務経験(能動的に動ける方)
        ・Javaの知見
        ・指示待ちではなく自走できる方
        （尚可）
        ・フローチャート作成、運用フローの設計経験
        ・EOL対応を考慮できる方
        ・ヘルプデスク/サービスデスク経験
        【金額】スキル見合い
        【期間】2025年11月〜
        【場所】フルリモート
        【時間】確認中
        【精算】確認中
        【面談】2回
    """)
    sample_path.write_text(sample_text, encoding="utf-8")
    return sample_path


def test_console_outputs_all_fields(capsys):
    """anken_formatter_main.py を実行して、出力内容をすべて表示・検証する"""
    setup_sample_file()

    env = os.environ.copy()
    env["ANKEN_NO_CLIP"] = "1"  # クリップボード操作を無効化
    env["PYTHONIOENCODING"] = "utf-8"

    proc = subprocess.run(
    [sys.executable, str(ROOT / "anken_formatter_main.py")],
    capture_output=True,
    text=True,
    encoding="utf-8",   # ★ 追加
    env=env,
    cwd=str(ROOT),
    timeout=30,
)

    assert proc.returncode == 0, proc.stderr
    out = proc.stdout.strip()

    print("\n===== anken_formatter_main.py 出力内容 =====")
    print(out)
    print("============================================\n")

    # --- ここから簡易検証（抽出が行われているか） ---
    # 各項目の行が出力されていることを確認
    assert re.search(r"参画時期：", out)
    assert re.search(r"勤務形態：", out)
    assert re.search(r"報酬額\(税込\)：", out)
    assert re.search(r"スキル必須：", out)
    assert re.search(r"スキル尚可：", out)
    assert re.search(r"業務内容：", out)
    assert re.search(r"清算幅下限：", out)
    assert re.search(r"清算幅上限：", out)
    assert re.search(r"契約期間：", out)
    assert re.search(r"勤務時間：", out)             # 行の存在

    # 値の存在をざっくり検証（詳細一致は不要）
    # assert "2025/11" in out
    assert "フルリモート" in out
    assert "スキル見合い" in out
    assert "Pythonの読解/開発経験" in out
    assert "フローチャート作成" in out
    assert "アプリの運用保守案件です" in out

    # 値の確認（今回のサンプル）
    assert re.search(r"^勤務時間：\s*確認中\s*$", out, re.MULTILINE)  
    assert re.search(r"^参画時期：\s*2025/11\s*$", out, re.MULTILINE)
    assert re.search(r"^勤務形態：\s*フルリモート\s*$", out, re.MULTILINE)
    assert re.search(r"^報酬額\(税込\)：\s*スキル見合い\s*$", out, re.MULTILINE)